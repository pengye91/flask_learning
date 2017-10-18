from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer
from genpy.calc.ICalc import Processor
import time


class CalcHandler(object):
    def add(self, num1, num2):
        print "starting...\n"
        time.sleep(20)
        return num1 + num2


if __name__ == '__main__':
    HANDLER = CalcHandler()
    PROCESSOR = Processor(HANDLER)
    TRANSPORT = TSocket.TServerSocket('localhost', 9090)
    TFACTORY = TTransport.TBufferedTransportFactory()
    PFACTORY = TBinaryProtocol.TBinaryProtocolFactory()
    SERVER = TServer.TThreadPoolServer(PROCESSOR, TRANSPORT, TFACTORY, PFACTORY)

    print 'starting server...'
    SERVER.serve()
    print 'Done.'
