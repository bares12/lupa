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
    def getPlaceSearchInfo(self, provider, keyword, clientLocale, latitude, longitude, radius):
        """
        Parameters:
         - provider
         - keyword
         - clientLocale
         - latitude
         - longitude
         - radius
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getPlaceSearchInfo(self, provider, keyword, clientLocale, latitude, longitude, radius):
        """
        Parameters:
         - provider
         - keyword
         - clientLocale
         - latitude
         - longitude
         - radius
        """
        self.send_getPlaceSearchInfo(provider, keyword, clientLocale, latitude, longitude, radius)
        return self.recv_getPlaceSearchInfo()

    def send_getPlaceSearchInfo(self, provider, keyword, clientLocale, latitude, longitude, radius):
        self._oprot.writeMessageBegin('getPlaceSearchInfo', TMessageType.CALL, self._seqid)
        args = getPlaceSearchInfo_args()
        args.provider = provider
        args.keyword = keyword
        args.clientLocale = clientLocale
        args.latitude = latitude
        args.longitude = longitude
        args.radius = radius
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPlaceSearchInfo(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPlaceSearchInfo_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPlaceSearchInfo failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getPlaceSearchInfo"] = Processor.process_getPlaceSearchInfo

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

    def process_getPlaceSearchInfo(self, seqid, iprot, oprot):
        args = getPlaceSearchInfo_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPlaceSearchInfo_result()
        try:
            result.success = self._handler.getPlaceSearchInfo(args.provider, args.keyword, args.clientLocale, args.latitude, args.longitude, args.radius)
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
        oprot.writeMessageBegin("getPlaceSearchInfo", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getPlaceSearchInfo_args(object):
    """
    Attributes:
     - provider
     - keyword
     - clientLocale
     - latitude
     - longitude
     - radius
    """


    def __init__(self, provider=None, keyword=None, clientLocale=None, latitude=None, longitude=None, radius=None,):
        self.provider = provider
        self.keyword = keyword
        self.clientLocale = clientLocale
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.provider = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.keyword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.clientLocale = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.DOUBLE:
                    self.latitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.DOUBLE:
                    self.longitude = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.radius = iprot.readI32()
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
        oprot.writeStructBegin('getPlaceSearchInfo_args')
        if self.provider is not None:
            oprot.writeFieldBegin('provider', TType.I32, 2)
            oprot.writeI32(self.provider)
            oprot.writeFieldEnd()
        if self.keyword is not None:
            oprot.writeFieldBegin('keyword', TType.STRING, 3)
            oprot.writeString(self.keyword.encode('utf-8') if sys.version_info[0] == 2 else self.keyword)
            oprot.writeFieldEnd()
        if self.clientLocale is not None:
            oprot.writeFieldBegin('clientLocale', TType.STRING, 4)
            oprot.writeString(self.clientLocale.encode('utf-8') if sys.version_info[0] == 2 else self.clientLocale)
            oprot.writeFieldEnd()
        if self.latitude is not None:
            oprot.writeFieldBegin('latitude', TType.DOUBLE, 5)
            oprot.writeDouble(self.latitude)
            oprot.writeFieldEnd()
        if self.longitude is not None:
            oprot.writeFieldBegin('longitude', TType.DOUBLE, 6)
            oprot.writeDouble(self.longitude)
            oprot.writeFieldEnd()
        if self.radius is not None:
            oprot.writeFieldBegin('radius', TType.I32, 7)
            oprot.writeI32(self.radius)
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
all_structs.append(getPlaceSearchInfo_args)
getPlaceSearchInfo_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'provider', None, None, ),  # 2
    (3, TType.STRING, 'keyword', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'clientLocale', 'UTF8', None, ),  # 4
    (5, TType.DOUBLE, 'latitude', None, None, ),  # 5
    (6, TType.DOUBLE, 'longitude', None, None, ),  # 6
    (7, TType.I32, 'radius', None, None, ),  # 7
)


class getPlaceSearchInfo_result(object):
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
                if ftype == TType.LIST:
                    self.success = []
                    (_etype774, _size771) = iprot.readListBegin()
                    for _i775 in range(_size771):
                        _elem776 = PlaceSearchInfo()
                        _elem776.read(iprot)
                        self.success.append(_elem776)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('getPlaceSearchInfo_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter777 in self.success:
                iter777.write(oprot)
            oprot.writeListEnd()
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
all_structs.append(getPlaceSearchInfo_result)
getPlaceSearchInfo_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [PlaceSearchInfo, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

