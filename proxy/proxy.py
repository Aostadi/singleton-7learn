"""
	Proxy
	- a structural design pattern that lets you provide a substitute or placeholder
	for another object. A proxy controls access to the original object, allowing you
	to perform something either before or after the request gets through to the original object.
"""

import datetime
import time
from abc import ABC, abstractmethod


class ServerBase(ABC):
    @abstractmethod
    def receive(self):
        pass


class Server(ServerBase):
    def receive(self):
        print('Processing your request...')
        time.sleep(1)
        print('Done...')


class LogProxy(ServerBase):
    def __init__(self, server):
        self._server = server

    def receive(self):
        self.logging()
        self._server.receive()
        
    @staticmethod
    def logging():
        with open('log.log', 'a') as log:
            log.write(f'Request {datetime.datetime.now()} \n')


s = Server()
p = LogProxy(s)
p.receive()