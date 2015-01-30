# -*- coding: utf-8 -*-

from datetime import datetime


class Message(object):

    STATUS_NEW = u"new"
    STATUS_QUEUED = u"queued"
    STATUS_DEQUEUED = u"dequeued"

    def __init__(self):
        self.__status = self.STATUS_NEW
        self.__queuedDate = None
        self.__dequeuedDate = None

    def setQueued(self):
        self.__status = self.STATUS_QUEUED
        self.__queuedDate = datetime.now()

    def setDequeued(self):
        self.__status = self.STATUS_DEQUEUED
        self.__dequeuedDate = datetime.now()

    @property
    def status(self):
        return self.__status

    @property
    def queuedDate(self):
        return self.__queuedDate

    @property
    def dequeuedDate(self):
        return self.__dequeuedDate