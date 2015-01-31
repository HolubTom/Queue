# -*- coding: utf-8 -*-

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class Queue(object):

    def __init__(self, pDriver):
        self.__aDriver = pDriver

    def put(self, lMessage):
        lMessage.setQueued()
        self.__aDriver.put(lMessage)

    def get(self):
        lItem = self.__aDriver.get()
        lItem.setDequeued()
        return lItem

    @property
    def count(self):
        return self.__aDriver.count