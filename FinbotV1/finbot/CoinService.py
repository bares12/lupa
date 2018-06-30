from FinbotServer.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from FinbotServer.protocol.TProtocol import TProtocolException
from Thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from FinbotServer.Thrift import TProcessor
from FinbotServer.transport import TTransport
all_structs = []

class Iface(object):
    def getCoinUseAndRefundHistory(self, request):
        """
        Parameters:
         - request
        """
        pass

    def getTotalCoinBalance(self, request):
        """
        Parameters:
         - request
        """
        pass

    def getCoinProducts(self, request):
        """
        Parameters:
         - request
        """
        pass

    def getCoinPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        pass

    def reserveCoinPurchase(self, request):
        """
        Parameters:
         - request
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getCoinUseAndRefundHistory(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCoinUseAndRefundHistory(request)
        return self.recv_getCoinUseAndRefundHistory()

    def send_getCoinUseAndRefundHistory(self, request):
        self._oprot.writeMessageBegin('getCoinUseAndRefundHistory', TMessageType.CALL, self._seqid)
        args = getCoinUseAndRefundHistory_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinUseAndRefundHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinUseAndRefundHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinUseAndRefundHistory failed: unknown result")

    def getTotalCoinBalance(self, request):
        """
        Parameters:
         - request
        """
        self.send_getTotalCoinBalance(request)
        return self.recv_getTotalCoinBalance()

    def send_getTotalCoinBalance(self, request):
        self._oprot.writeMessageBegin('getTotalCoinBalance', TMessageType.CALL, self._seqid)
        args = getTotalCoinBalance_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getTotalCoinBalance(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getTotalCoinBalance_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getTotalCoinBalance failed: unknown result")

    def getCoinProducts(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCoinProducts(request)
        return self.recv_getCoinProducts()

    def send_getCoinProducts(self, request):
        self._oprot.writeMessageBegin('getCoinProducts', TMessageType.CALL, self._seqid)
        args = getCoinProducts_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinProducts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinProducts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinProducts failed: unknown result")

    def getCoinPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCoinPurchaseHistory(request)
        return self.recv_getCoinPurchaseHistory()

    def send_getCoinPurchaseHistory(self, request):
        self._oprot.writeMessageBegin('getCoinPurchaseHistory', TMessageType.CALL, self._seqid)
        args = getCoinPurchaseHistory_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCoinPurchaseHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCoinPurchaseHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCoinPurchaseHistory failed: unknown result")

    def reserveCoinPurchase(self, request):
        """
        Parameters:
         - request
        """
        self.send_reserveCoinPurchase(request)
        return self.recv_reserveCoinPurchase()

    def send_reserveCoinPurchase(self, request):
        self._oprot.writeMessageBegin('reserveCoinPurchase', TMessageType.CALL, self._seqid)
        args = reserveCoinPurchase_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reserveCoinPurchase(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reserveCoinPurchase_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reserveCoinPurchase failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getCoinUseAndRefundHistory"] = Processor.process_getCoinUseAndRefundHistory
        self._processMap["getTotalCoinBalance"] = Processor.process_getTotalCoinBalance
        self._processMap["getCoinProducts"] = Processor.process_getCoinProducts
        self._processMap["getCoinPurchaseHistory"] = Processor.process_getCoinPurchaseHistory
        self._processMap["reserveCoinPurchase"] = Processor.process_reserveCoinPurchase

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

    def process_getCoinUseAndRefundHistory(self, seqid, iprot, oprot):
        args = getCoinUseAndRefundHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinUseAndRefundHistory_result()
        try:
            result.success = self._handler.getCoinUseAndRefundHistory(args.request)
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
        oprot.writeMessageBegin("getCoinUseAndRefundHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getTotalCoinBalance(self, seqid, iprot, oprot):
        args = getTotalCoinBalance_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getTotalCoinBalance_result()
        try:
            result.success = self._handler.getTotalCoinBalance(args.request)
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
        oprot.writeMessageBegin("getTotalCoinBalance", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinProducts(self, seqid, iprot, oprot):
        args = getCoinProducts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinProducts_result()
        try:
            result.success = self._handler.getCoinProducts(args.request)
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
        oprot.writeMessageBegin("getCoinProducts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCoinPurchaseHistory(self, seqid, iprot, oprot):
        args = getCoinPurchaseHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCoinPurchaseHistory_result()
        try:
            result.success = self._handler.getCoinPurchaseHistory(args.request)
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
        oprot.writeMessageBegin("getCoinPurchaseHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reserveCoinPurchase(self, seqid, iprot, oprot):
        args = reserveCoinPurchase_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reserveCoinPurchase_result()
        try:
            result.success = self._handler.reserveCoinPurchase(args.request)
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
        oprot.writeMessageBegin("reserveCoinPurchase", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getCoinUseAndRefundHistory_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = GetCoinHistoryRequest()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getCoinUseAndRefundHistory_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
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
all_structs.append(getCoinUseAndRefundHistory_args)
getCoinUseAndRefundHistory_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'request', [GetCoinHistoryRequest, None], None, ),  # 1
)


class getCoinUseAndRefundHistory_result(object):
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
                    self.success = GetCoinHistoryResponse()
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
        oprot.writeStructBegin('getCoinUseAndRefundHistory_result')
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
all_structs.append(getCoinUseAndRefundHistory_result)
getCoinUseAndRefundHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GetCoinHistoryResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getTotalCoinBalance_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = GetTotalCoinBalanceRequest()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getTotalCoinBalance_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
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
all_structs.append(getTotalCoinBalance_args)
getTotalCoinBalance_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'request', [GetTotalCoinBalanceRequest, None], None, ),  # 1
)


class getTotalCoinBalance_result(object):
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
                    self.success = GetTotalCoinBalanceResponse()
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
        oprot.writeStructBegin('getTotalCoinBalance_result')
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
all_structs.append(getTotalCoinBalance_result)
getTotalCoinBalance_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GetTotalCoinBalanceResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinProducts_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = GetCoinProductsRequest()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getCoinProducts_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
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
all_structs.append(getCoinProducts_args)
getCoinProducts_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'request', [GetCoinProductsRequest, None], None, ),  # 1
)


class getCoinProducts_result(object):
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
                    self.success = GetCoinProductsResponse()
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
        oprot.writeStructBegin('getCoinProducts_result')
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
all_structs.append(getCoinProducts_result)
getCoinProducts_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GetCoinProductsResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCoinPurchaseHistory_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = GetCoinHistoryRequest()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('getCoinPurchaseHistory_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
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
all_structs.append(getCoinPurchaseHistory_args)
getCoinPurchaseHistory_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'request', [GetCoinHistoryRequest, None], None, ),  # 1
)


class getCoinPurchaseHistory_result(object):
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
                    self.success = GetCoinHistoryResponse()
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
        oprot.writeStructBegin('getCoinPurchaseHistory_result')
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
all_structs.append(getCoinPurchaseHistory_result)
getCoinPurchaseHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GetCoinHistoryResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class reserveCoinPurchase_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

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
                    self.request = CoinPurchaseReservation()
                    self.request.read(iprot)
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
        oprot.writeStructBegin('reserveCoinPurchase_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 1)
            self.request.write(oprot)
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
all_structs.append(reserveCoinPurchase_args)
reserveCoinPurchase_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'request', [CoinPurchaseReservation, None], None, ),  # 1
)


class reserveCoinPurchase_result(object):
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
                    self.success = PaymentReservationResult()
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
        oprot.writeStructBegin('reserveCoinPurchase_result')
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
all_structs.append(reserveCoinPurchase_result)
reserveCoinPurchase_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaymentReservationResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

