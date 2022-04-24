from subprocess import PIPE, Popen

class Piped:
    def __init__(self, cmd):
        self.exe_args = cmd
        self.proc = None

    def start(self):
        self.proc = Popen(self.exe_args, stdin=PIPE, stdout=PIPE)

    def stop(self):
        if self.proc:
            self.proc.kill ()
            self.proc = None

    def communicate (self, input):
        self.proc.stdin.write (input)
        self.proc.stdin.flush ()
        return self.proc.stdout.readline ()
