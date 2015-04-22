#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-16

import time
import socket
from twisted.internet import protocol, reactor

# ��װtwisted��ֱ��ִ�У�easy_install twisted
# see :http://blog.csdn.net/jonahzheng/article/details/8987333

HOST = "localhost"
PORT = 8888

class TcpServerProtocol(protocol.Protocol):
    def connectionMade(self):  # �пͻ������ӹ�����ʱ�򱻵���
        clnt = self.clnt = self.transport.getPeer().host
        print("... connected from %s", clnt)
    def dataReceived(self, data):  # �ڿͻ���ͨ�����緢�����ݹ���ʱ������
        self.transport.write("[%s] %s" % (ctime(), data))

def runTwistedReactorServer():
    factory = protocol.Factory()
    factory.protocol = TcpServerProtocol
    print("waiting for connection...")

    #ÿ�������ӽ�����ʱ�����ᡰ������һ�� protocol ����
    #Ȼ���� reactor �а�װһ�� TCP�������Եȴ���������
    #�����������ʱ������һ�� TSServProtocol ʵ���������Ǹ��ͻ��� 
    reactor.listenTCP(PORT, factory)
    reactor.run()  

class TcpClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print("recv from server: %s" % data)
        self.sendData()
    def sendData(self):
        data = raw_input("please input some msg>>>")
        if data:
            print("send to server : %s" % data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()  # �ر��׽��֣����������clientConnectionLost����
class TcpClientFactory(protocol.ClientFactory):
    protocol = TcpClientProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason : reactor.stop()
    
def runTwistedReactorClient():
    reactor.connectTCP(HOST, PORT, TcpClientFactory())
    reactor.run()


if __name__ == "__main__":
    funcs = {'s' : runTwistedReactorServer, 'c' : runTwistedReactorClient}
    choice = raw_input("run server(s) or client(c)? enter >>>").strip().lower()[0]
    funcs[choice]()
