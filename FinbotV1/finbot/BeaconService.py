from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
from FinbotServer.TRecursive import fix_spec
import sys
import logging
from .ttypes import *
from FinbotServer.Thrift import TProcessor
from FinbotServer.transport import TTransport
all_structs = []

class Iface(object):
    def notifyBeaconDetected(self, hwid, secureMessage, notificationType):
        """
        Parameters:
         - hwid
         - secureMessage
         - notificationType
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def notifyBeaconDetected(self, hwid, secureMessage, notificationType):
        """
        Parameters:
         - hwid
         - secureMessage
         - notificationType
        """
        self.send_notifyBeaconDetected(hwid, secureMessage, notificationType)
        self.recv_notifyBeaconDetected()

    def send_notifyBeaconDetected(self, hwid, secureMessage, notificationType):
        self._oprot.writeMessageBegin('notifyBeaconDetected', TMessageType.CALL, self._seqid)
        args = notifyBeaconDetected_args()
        args.hwid = hwid
        args.secureMessage = secureMessage
        args.notificationType = notificationType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyBeaconDetected(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyBeaconDetected_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["notifyBeaconDetected"] = Processor.process_notifyBeaconDetected

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_notifyBeaconDetected(self, seqid, iprot, oprot):
        args = notifyBeaconDetected_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyBeaconDetected_result()
        try:
            self._handler.notifyBeaconDetected(args.hwid, args.secureMessage, args.notificationType)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("notifyBeaconDetected", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class notifyBeaconDetected_args(object):
    """
    Attributes:
     - hwid
     - secureMessage
     - notificationType
    """


    def __init__(self, hwid=None, secureMessage=None, notificationType=None,):
        self.hwid = hwid
        self.secureMessage = secureMessage
        self.notificationType = notificationType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.hwid = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.secureMessage = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.notificationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyBeaconDetected_args')
        if self.hwid is not None:
            oprot.writeFieldBegin('hwid', TType.STRING, 1)
            oprot.writeBinary(self.hwid)
            oprot.writeFieldEnd()
        if self.secureMessage is not None:
            oprot.writeFieldBegin('secureMessage', TType.STRING, 2)
            oprot.writeBinary(self.secureMessage)
            oprot.writeFieldEnd()
        if self.notificationType is not None:
            oprot.writeFieldBegin('notificationType', TType.I32, 3)
            oprot.writeI32(self.notificationType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyBeaconDetected_args)
notifyBeaconDetected_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'hwid', 'BINARY', None, ),  # 1
    (2, TType.STRING, 'secureMessage', 'BINARY', None, ),  # 2
    (3, TType.I32, 'notificationType', None, None, ),  # 3
)


class notifyBeaconDetected_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyBeaconDetected_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyBeaconDetected_result)
notifyBeaconDetected_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

