from logging import debug
from modules.createQR import createQR
from modules.server import setupServer, startServer

setupServer()
if __name__ == '__main__':
    startServer()