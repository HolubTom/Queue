# -*- coding: utf-8 -*-


class Queue(object):

    def __init__(self, pDriver):
        self.__aDriver = pDriver

    def put(self, lMessage):
        self.__aDriver.put(lMessage)

    def get(self):
        return self.__aDriver.get()

    @property
    def count(self):
        return self.__aDriver.count