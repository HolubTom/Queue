# -*- coding: utf-8 -*-

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


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