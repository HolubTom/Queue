# -*- coding: utf-8 -*-


class MemoryDriver(object):

    def __init__(self):
        self.__activeQueue = []

    def put(self, lMessage):
        self.__activeQueue.append(lMessage)

    def get(self):
        return self.__activeQueue.pop(0)

    @property
    def count(self):
        return len(self.__activeQueue)