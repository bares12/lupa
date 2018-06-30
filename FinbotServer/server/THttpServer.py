from six.moves import BaseHTTPServer

from Thrift.server import TServer
from Thrift.transport import TTransport


class ResponseException(Exception):
    """Allows handlers to override the HTTP response

    Normally, THttpServer always sends a 200 response.  If a handler wants
    to override this behavior (e.g., to simulate a misconfigured or
    overloaded web server during testing), it can raise a ResponseException.
    The function passed to the constructor will be called with the
    RequestHandler as its only argument.
    """
    def __init__(self, handler):
        self.handler = handler


class THttpServer(TServer.TServer):
    """A simple HTTP-based Thrift server

    This class is not very performant, but it is useful (for example) for
    acting as a mock version of an Apache-based PHP Thrift endpoint.
    """
    def __init__(self,
                 processor,
                 server_address,
                 inputProtocolFactory,
                 outputProtocolFactory=None,
                 server_class=BaseHTTPServer.HTTPServer):
        """Set up protocol factories and HTTP server.

        See BaseHTTPServer for server_address.
        See TServer for protocol factories.
        """
        if outputProtocolFactory is None:
            outputProtocolFactory = inputProtocolFactory

        TServer.TServer.__init__(self, processor, None, None, None,
                                 inputProtocolFactory, outputProtocolFactory)

        thttpserver = self

        class RequestHander(BaseHTTPServer.BaseHTTPRequestHandler):
            def do_POST(self):
                # Don't care about the request path.
                itrans = TTransport.TFileObjectTransport(self.rfile)
                otrans = TTransport.TFileObjectTransport(self.wfile)
                itrans = TTransport.TBufferedTransport(
                    itrans, int(self.headers['Content-Length']))
                otrans = TTransport.TMemoryBuffer()
                iprot = thttpserver.inputProtocolFactory.getProtocol(itrans)
                oprot = thttpserver.outputProtocolFactory.getProtocol(otrans)
                try:
                    thttpserver.processor.process(iprot, oprot)
                except ResponseException as exn:
                    exn.handler(self)
                else:
                    self.send_response(200)
                    self.send_header("content-type", "application/x-thrift")
                    self.end_headers()
                    self.wfile.write(otrans.getvalue())

        self.httpd = server_class(server_address, RequestHander)

    def serve(self):
        self.httpd.serve_forever()
