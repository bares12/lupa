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
    def queryBeaconActions(self, hwid, secureMessage, applicationType, applicationVersion, lang):
        """
        Parameters:
         - hwid
         - secureMessage
         - applicationType
         - applicationVersion
         - lang
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def queryBeaconActions(self, hwid, secureMessage, applicationType, applicationVersion, lang):
        """
        Parameters:
         - hwid
         - secureMessage
         - applicationType
         - applicationVersion
         - lang
        """
        self.send_queryBeaconActions(hwid, secureMessage, applicationType, applicationVersion, lang)
        return self.recv_queryBeaconActions()

    def send_queryBeaconActions(self, hwid, secureMessage, applicationType, applicationVersion, lang):
        self._oprot.writeMessageBegin('queryBeaconActions', TMessageType.CALL, self._seqid)
        args = queryBeaconActions_args()
        args.hwid = hwid
        args.secureMessage = secureMessage
        args.applicationType = applicationType
        args.applicationVersion = applicationVersion
        args.lang = lang
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_queryBeaconActions(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = queryBeaconActions_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "queryBeaconActions failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["queryBeaconActions"] = Processor.process_queryBeaconActions

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

    def process_queryBeaconActions(self, seqid, iprot, oprot):
        args = queryBeaconActions_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = queryBeaconActions_result()
        try:
            result.success = self._handler.queryBeaconActions(args.hwid, args.secureMessage, args.applicationType, args.applicationVersion, args.lang)
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
        oprot.writeMessageBegin("queryBeaconActions", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class queryBeaconActions_args(object):
    """
    Attributes:
     - hwid
     - secureMessage
     - applicationType
     - applicationVersion
     - lang
    """


    def __init__(self, hwid=None, secureMessage=None, applicationType=None, applicationVersion=None, lang=None,):
        self.hwid = hwid
        self.secureMessage = secureMessage
        self.applicationType = applicationType
        self.applicationVersion = applicationVersion
        self.lang = lang

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
                    self.applicationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.applicationVersion = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.lang = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('queryBeaconActions_args')
        if self.hwid is not None:
            oprot.writeFieldBegin('hwid', TType.STRING, 1)
            oprot.writeBinary(self.hwid)
            oprot.writeFieldEnd()
        if self.secureMessage is not None:
            oprot.writeFieldBegin('secureMessage', TType.STRING, 2)
            oprot.writeBinary(self.secureMessage)
            oprot.writeFieldEnd()
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.I32, 3)
            oprot.writeI32(self.applicationType)
            oprot.writeFieldEnd()
        if self.applicationVersion is not None:
            oprot.writeFieldBegin('applicationVersion', TType.STRING, 4)
            oprot.writeString(self.applicationVersion.encode('utf-8') if sys.version_info[0] == 2 else self.applicationVersion)
            oprot.writeFieldEnd()
        if self.lang is not None:
            oprot.writeFieldBegin('lang', TType.STRING, 5)
            oprot.writeString(self.lang.encode('utf-8') if sys.version_info[0] == 2 else self.lang)
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
all_structs.append(queryBeaconActions_args)
queryBeaconActions_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'hwid', 'BINARY', None, ),  # 1
    (2, TType.STRING, 'secureMessage', 'BINARY', None, ),  # 2
    (3, TType.I32, 'applicationType', None, None, ),  # 3
    (4, TType.STRING, 'applicationVersion', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'lang', 'UTF8', None, ),  # 5
)


class queryBeaconActions_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
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
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = BeaconQueryResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
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
        oprot.writeStructBegin('queryBeaconActions_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
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
all_structs.append(queryBeaconActions_result)
queryBeaconActions_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BeaconQueryResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

