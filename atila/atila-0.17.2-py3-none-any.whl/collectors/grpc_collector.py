from .stream_collector import StreamCollector
from skitai.handlers.collectors import FormCollector
from skitai import counter
from rs4.protocols.sock.impl.grpc.message import decode_message
import struct
import time

class GRPCCollector (FormCollector):
    stream_id = counter.counter ()
    def __init__ (self, handler, request, *args):
        super ().__init__ (handler, request, *args)
        self.ch = request.channel
        self.stream_id.inc ()
        self._compressed = None
        self._msg_length = 0
        self.buffer = b""
        self.msgs = []

    def close (self):
        self.handler.continue_request (self.request, self.msgs)

    def start_collect (self):
        self.ch.set_terminator (1)

    def collect_incoming_data (self, data):
        self.buffer += data

    def handle_message (self, msg):
        self.msgs.append (msg)

    def found_terminator (self):
        if not self.buffer:
            self.close ()
            return

        buf, self.buffer = self.buffer, b""
        # print (buf, self.ch.get_terminator ())
        if self._compressed is None:
            self._compressed = struct.unpack ("!B", buf)[0]
            self.ch.set_terminator (4)

        elif self._msg_length == 0:
            self._msg_length = struct.unpack ("!I", buf)[0]
            if self._msg_length:
                self.ch.set_terminator (self._msg_length)
            else:
                self.ch.set_terminator (1)
                self._compressed = None

        else:
            msg = decode_message (buf, self._compressed)
            self._compressed = None
            self._msg_length = 0
            self.handle_message (msg)
            self.ch.set_terminator (1)


class GRPCStreamCollector (GRPCCollector, StreamCollector):
    DEFAULT_BUFFER_SIZE = 1
    END_DATA = None
    stream_id = counter.counter ()

    def __init__ (self, handler, request, *args):
        GRPCCollector.__init__ (self, handler, request, *args)
        self.initialize_stream_variables ()
        self.input_type = None

    def set_input_type (self, input_type):
        self.input_type = input_type

    def flush (self):
        self.first_data and self.continue_request ()
        if not self.proxy:
            return
        while self.msgs:
            msg = self.msgs.pop (0)
            f = self.input_type [0]()
            f.ParseFromString (msg)
            self.queue.append (f)
            self.callback ()
        if self.end_of_data:
            self.callback ()

    def close (self):
        self.end_of_data = True
        StreamCollector.close (self)

    def handle_message (self, msg):
        super ().handle_message (msg)
        self.flush ()
