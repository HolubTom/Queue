# -*- coding: utf-8 -*-
from pCore.module.queue.messages.Message import Message

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class Queue(object):
    u""" Class implementing FIFO principle """

    def __init__(self, pDriver):
        u""" Class constructor """
        self.__aDriver = pDriver

    def put(self, lMessage):
        u"""
        Puts message at the end of the queue

        :param lMessage: Message object
        :type lMessage: pCore.module.queue.messages.Message.Message
        """
        assert isinstance(lMessage, Message)

        lMessage.setQueued()
        self.__aDriver.put(lMessage)

    def get(self):
        u"""
        Returns and removes message from the beginning of the queue

        :rtype : pCore.module.queue.messages.Message.Message
        """
        lItem = self.__aDriver.get()
        lItem.setDequeued()
        return lItem

    @property
    def count(self):
        u"""
        Returns count of messages waiting in the line
        :rtype : int
        """
        return self.__aDriver.count