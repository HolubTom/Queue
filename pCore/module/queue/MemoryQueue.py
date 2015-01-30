# -*- coding: utf-8 -*-
from classes.Queue.IQueue import IQueue
from pCore.base.CoreObject import CoreObject

__author__ = u"Tomas Holub (tomas.holub@olc.cz)"
__credits__ = u"""\
Author: Tomas Holub
Create date: 2014-09-01 13:14
Modification date:  
Description: """


class MemoryQueue(IQueue):

    def __init__(self):
        self.__activeQueue = []

    def put(self, lMessage):
        self.__activeQueue.append(lMessage)

    def get(self):
        return self.__activeQueue.pop(0)

    @property
    def count(self):
        return len(self.__activeQueue)