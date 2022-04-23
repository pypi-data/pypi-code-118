# Adafruit MicroPython Tool - File Operations
# Author: Tony DiCola
# Copyright (c) 2016 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import ast
import json
import textwrap
import binascii
from .pyboard import PyboardError


BUFFER_SIZE = 1024  # Amount of data to read or write to the serial port at a time.
# This is kept small because small chips and USB to serial
# bridges usually have very small buffers.


class DirectoryExistsError(Exception):
    pass


class Files(object):
    """Class to interact with a MicroPython board files over a serial connection.
    Provides functions for listing, uploading, and downloading files from the
    board's filesystem.
    """

    def __init__(self, pyboard):
        """Initialize the MicroPython board files class using the provided pyboard
        instance.  In most cases you should create a Pyboard instance (from
        pyboard.py) which connects to a board over a serial connection and pass
        it in, but you can pass in other objects for testing, etc.
        """
        self._pyboard = pyboard

    def get(self, filename):
        """Retrieve the contents of the specified file and return its contents
        as a byte string.
        """
        # Open the file and read it a few bytes at a time and print out the
        # raw bytes.  Be careful not to overload the UART buffer so only write
        # a few bytes at a time, and don't use print since it adds newlines and
        # expects string data.
        command = """
            import sys
            import ubinascii
            with open('{0}', 'rb') as infile:
                while True:
                    result = infile.read({1})
                    if result == b'':
                        break
                    len = sys.stdout.write(ubinascii.hexlify(result))
        """.format(
            filename, BUFFER_SIZE
        )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            # Check if this is an OSError #2, i.e. file doesn't exist and
            # rethrow it as something more descriptive.
            try:
                
                #if ex.args[2].decode("utf-8").find("OSError: [Errno 2] ENOENT") != -1:
                if len(ex.args) > 2 and ex.args[2].decode("utf-8").find("OSError: [Errno 2] ENOENT") != -1:
                    raise RuntimeError("No such file: {0}".format(filename))
                else:
                    raise ex
            except UnicodeDecodeError:
                raise ex
        self._pyboard.exit_raw_repl()
        return binascii.unhexlify(out)

    def ls(self, directory=None, long_format=True, bundle_format=False, recursive=False):
        """List the contents of the specified directory (or root if none is
        specified).  Returns a list of strings with the names of files in the
        specified directory.  If long_format is True then a list of 2-tuples
        with the name and size (in bytes) of the item is returned.  Note that
        it appears the size of directories is not supported by MicroPython and
        will always return 0 (i.e. no recursive size computation).
        """

        # Disabling for now, see https://github.com/adafruit/ampy/issues/55.
        # # Make sure directory ends in a slash.
        # if not directory.endswith("/"):
        #     directory += "/"

        # Make sure directory starts with slash, for consistency.
        if not directory:
            directory = "os.getcwd()"
        else:
            if not directory.startswith("/"):
                directory = "/" + directory
            directory = "'{}'".format(directory)

        command = """\
                try:        
                    import os
                except ImportError:
                    import uos as os\n"""

        if recursive:
            command += """\
                def listdir(directory):
                    result = set()
                    def _listdir(dir_or_file):
                        try:
                            # if its a directory, then it should provide some children.
                            children = os.listdir(dir_or_file)
                        except OSError:                        
                            # probably a file. run stat() to confirm.
                            os.stat(dir_or_file)
                            result.add(dir_or_file) 
                        else:
                            # probably a directory, add to result if empty.
                            if children:
                                # queue the children to be dealt with in next iteration.
                                for child in children:
                                    # create the full path.
                                    if dir_or_file == '/':
                                        next = dir_or_file + child
                                    else:
                                        next = dir_or_file + '/' + child
                                    
                                    _listdir(next)
                            else:
                                result.add(dir_or_file)                     
                    _listdir(directory)
                    return sorted(result)\n"""
        else:
            command += """\
                def listdir(directory):
                    if directory == '/':                
                        return sorted([directory + f for f in os.listdir(directory)])
                    else:
                        return sorted([directory + '/' + f for f in os.listdir(directory)])\n"""

        # Execute os.listdir() command on the board.
        if bundle_format:
            command += """
                r = []
                for f in listdir({0}):
                    size = os.stat(f)[6]                    
                    r.append((f, size))
                print(r)
            """.format(
                directory
            )
        elif long_format:
            command += """
                r = []
                for f in listdir({0}):
                    size = os.stat(f)[6]                    
                    r.append('{{0}} - {{1}} bytes'.format(f, size))
                print(r)
            """.format(
                directory
            ) 
        else:
            command += """
                print(listdir({0}))
            """.format(
                directory
            )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            import traceback
            traceback.print_exc()
            print("PyboardError", ex)
            # Check if this is an OSError #2, i.e. directory doesn't exist and
            # rethrow it as something more descriptive.
            if ex.args[2].decode("utf-8").find("OSError: [Errno 2] ENOENT") != -1:
                raise RuntimeError("No such directory: {0}".format(directory))
            else:
                raise ex
        self._pyboard.exit_raw_repl()
        # Parse the result list and return it.
        return ast.literal_eval(out.decode("utf-8"))

    def fsmngls(self):
        # only list user file
        command = """
            import fsmng
            print(fsmng.list())
        """
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()
        info = ast.literal_eval(out.decode("utf-8"))
        return info

    def mkdir(self, directory, exists_okay=False):
        """Create the specified directory.  Note this cannot create a recursive
        hierarchy of directories, instead each one should be created separately.
        """
        # Execute os.mkdir command on the board.
        command = """
            try:
                import os
            except ImportError:
                import uos as os
            os.mkdir('{0}')
        """.format(
            directory
        )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            # Check if this is an OSError #17, i.e. directory already exists.
            if ex.args[2].decode("utf-8").find("OSError: [Errno 17] EEXIST") != -1:
                if not exists_okay:
                    raise DirectoryExistsError(
                        "Directory already exists: {0}".format(directory)
                    )
            else:
                raise ex
        self._pyboard.exit_raw_repl()

    def put(self, filename, data, callback=None):
        """Create or update the specified file with the provided data.
        """
        # Open the file for writing on the board and write chunks of data.
        self._pyboard.enter_raw_repl()
        self._pyboard.exec_("f = open('{0}', 'wb')".format(filename))
        size = len(data)
        # Loop through and write a buffer size chunk of data at a time.
        for i in range(0, size, BUFFER_SIZE):
            chunk_size = min(BUFFER_SIZE, size - i)
            chunk = repr(data[i : i + chunk_size])
            # Make sure to send explicit byte strings (handles python 2 compatibility).
            if not chunk.startswith("b"):
                chunk = "b" + chunk
            self._pyboard.exec_("f.write({0})".format(chunk))
            if callback:
                callback(i, size)
        self._pyboard.exec_("f.close()")
        self._pyboard.exit_raw_repl()

    def putasync(self, filename, data, callback=None, delete=False):
        # Open the file for writing on the board and write chunks of data.
        self._pyboard.enter_raw_repl()
        size = len(data)
        if delete:
            cmd = '''
            try:
                os.remove("{}")
            except:
                pass
            '''.format(filename)
            self._pyboard.exec_(textwrap.dedent(cmd))
        # Loop through and write a buffer size chunk of data at a time.
        for i in range(0, size, BUFFER_SIZE):
            chunk_size = min(BUFFER_SIZE, size - i)
            chunk = repr(data[i : i + chunk_size])
            # Make sure to send explicit byte strings (handles python 2 compatibility).
            if not chunk.startswith("b"):
                chunk = "b" + chunk
            if chunk_size + i == size:
                timeout = 5000
            else:
                timeout = 500
            self._pyboard.exec_("import fsmng\nfsmng.putasync('{}',{},{},{})".format(filename,chunk,i,size), timeout=timeout)
            if callback:
                callback(i, size)
        self._pyboard.exit_raw_repl()

    def showmsg(self, msg, title, type='err'):
        # Open the file for writing on the board and write chunks of data.
        self._pyboard.enter_raw_repl()
        self._pyboard.exec_("screen.showmsg('{}','{}', '{}')".format(msg, title, type))
        self._pyboard.exit_raw_repl()

    def uname(self):
        command = """
            try:
                import os
            except ImportError:
                import uos as os
            print(list(os.uname()))
        """
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()
        info = ast.literal_eval(out.decode("utf-8"))
        if len(info) == 6: # meow32
            model = info[0] 
            date = info[4]
            ver = info[4][3] + '.' +info[4][5:7] + info[4][8:10]
            intro = info[5]
            mac = info[1]
            ret = (model, model, ver, ver, date, intro, mac)
            return ret    
        else:
            return info

    def fsinfo(self, prompt='/'):
        """Get filesystem info"""
        command = """
            import fsmng
            print(fsmng.diskinfo())
        """.format(
            prompt
        )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()
        info = ast.literal_eval(out.decode("utf-8"))
        return {'total': info[0], 'used': info[1], 'free': info[2]}

    def rm(self, filename):
        """Remove the specified file or directory."""
        command = """
            try:
                import os
            except ImportError:
                import uos as os
            os.remove('{0}')
        """.format(
            filename
        )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            message = ex.args[2].decode("utf-8")
            # Check if this is an OSError #2, i.e. file/directory doesn't exist
            # and rethrow it as something more descriptive.
            if message.find("OSError: [Errno 2] ENOENT") != -1:
                raise RuntimeError("No such file/directory: {0}".format(filename))
            # Check for OSError #13, the directory isn't empty.
            if message.find("OSError: [Errno 13] EACCES") != -1:
                raise RuntimeError("Directory is not empty: {0}".format(filename))
            else:
                raise ex
        self._pyboard.exit_raw_repl()

    def resetfs(self):
        """Reset user disk"""
        command = """
            try:
                fp = open("main.py")
                mainpy = fp.read()
                fp.close()
            except:
                mainpy = None
                pass
            import inisetup
            inisetup.resetfs(mainpy)
        """
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()

    def syncCheck(self, d, reset=False):
        if type(d) != str:
            d = json.dumps(d)
        command = """
        import fsmng
        print(fsmng.syncFileCheck('{}',reset={}))
        """.format(d, reset)
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command), timeout=10000)
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()
        return ast.literal_eval(out.decode("utf-8"))

    def rmdir(self, directory, missing_okay=False):
        """Forcefully remove the specified directory and all its children."""
        # Build a script to walk an entire directory structure and delete every
        # file and subfolder.  This is tricky because MicroPython has no os.walk
        # or similar function to walk folders, so this code does it manually
        # with recursion and changing directories.  For each directory it lists
        # the files and deletes everything it can, i.e. all the files.  Then
        # it lists the files again and assumes they are directories (since they
        # couldn't be deleted in the first pass) and recursively clears those
        # subdirectories.  Finally when finished clearing all the children the
        # parent directory is deleted.
        command = """
            try:
                import os
            except ImportError:
                import uos as os
            def rmdir(directory):
                os.chdir(directory)
                for f in os.listdir():
                    try:
                        os.remove(f)
                    except OSError:
                        pass
                for f in os.listdir():
                    rmdir(f)
                os.chdir('..')
                os.rmdir(directory)
            rmdir('{0}')
        """.format(
            directory
        )
        self._pyboard.enter_raw_repl()
        try:
            out = self._pyboard.exec_(textwrap.dedent(command))
        except PyboardError as ex:
            message = ex.args[2].decode("utf-8")
            # Check if this is an OSError #2, i.e. directory doesn't exist
            # and rethrow it as something more descriptive.
            if message.find("OSError: [Errno 2] ENOENT") != -1:
                if not missing_okay:
                    raise RuntimeError("No such directory: {0}".format(directory))
            else:
                raise ex
        self._pyboard.exit_raw_repl()

    def run(self, filename, wait_output=True, stream_output=True):
        """Run the provided script and return its output.  If wait_output is True
        (default) then wait for the script to finish and then return its output,
        otherwise just run the script and don't wait for any output.
        If stream_output is True(default) then return None and print outputs to
        stdout without buffering.
        """
        self._pyboard.enter_raw_repl()
        out = None
        if stream_output:
            self._pyboard.execfile(filename, stream_output=True)
        elif wait_output:
            # Run the file and wait for output to return.
            out = self._pyboard.execfile(filename)
        else:
            # Read the file and run it using lower level pyboard functions that
            # won't wait for it to finish or return output.
            with open(filename, "rb") as infile:
                self._pyboard.exec_raw_no_follow(infile.read())
        self._pyboard.exit_raw_repl()
        return out

    def run_code(self, code):
        self._pyboard.enter_raw_repl()
        try:
            code = textwrap.dedent(code)
            out = self._pyboard.exec_(code, timeout=10000)
        except PyboardError as ex:
            raise ex
        self._pyboard.exit_raw_repl()
        return ast.literal_eval(out.decode("utf-8"))

if __name__ == "__main__":
    import pyboard
    import SerialCom as SC
    com = SC.serialList()[0]['peripheralId']
    def testrx(msg, dt):
        print(">>>>>>>>", msg, dt)

    s = SC.serialCom(testrx)
    s.connect(com, baud=115200)

    # setattr(ser, 'pybMutex', False)
    s.setPybMutex(True)
    pyb = pyboard.Pyboard(s.ser)
    fp = Files(pyb)
    ls = fp.ls()
    s.setPybMutex(False)
    print(ls)
