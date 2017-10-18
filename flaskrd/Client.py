#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from thrift.Thrift import TException
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from genpy.calc.ICalc import Client

if __name__ == '__main__':
    try:
        TRANSPORT = TSocket.TSocket('localhost', 9090)
        TRANSPORT = TTransport.TBufferedTransport(TRANSPORT)
        PROTOCOL = TBinaryProtocol.TBinaryProtocol(TRANSPORT)
        CLIENT = Client(PROTOCOL)

        TRANSPORT.open()
        num1, num2 = sys.argv[1], sys.argv[2]

        print CLIENT.add(int(num1), int(num2))

        TRANSPORT.close()
    except TException as e:
        print e.message



