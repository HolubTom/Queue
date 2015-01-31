# -*- coding: utf-8 -*-

from datetime import datetime

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class Message(object):
    u"""Basic class for Messages that goes into the Queue"""

    MESSAGE_TYPE = u"basic"

    STATUS_NEW = u"new"
    STATUS_QUEUED = u"queued"
    STATUS_DEQUEUED = u"dequeued"

    def __init__(self):
        u""" Class constructor """

        self.__status = self.STATUS_NEW
        self.__queuedDate = None
        self.__dequeuedDate = None

    def setQueued(self):
        u""" Mark message as queued """
        self.__status = self.STATUS_QUEUED
        self.__queuedDate = datetime.now()

    def setDequeued(self):
        u""" Mark message that it was removed from the queue """
        self.__status = self.STATUS_DEQUEUED
        self.__dequeuedDate = datetime.now()

    @property
    def status(self):
        u"""
        Returns message status
        :rtype : unicode
        """
        return self.__status

    @property
    def queuedDate(self):
        u"""
        Returns date when was message put in the queue
        :rtype : datetime
        """
        return self.__queuedDate

    @property
    def dequeuedDate(self):
        u"""
        Returns date when message was removed from the queue
        :rtype : datetime
        """
        return self.__dequeuedDate