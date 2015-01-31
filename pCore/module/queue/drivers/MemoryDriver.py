# -*- coding: utf-8 -*-

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class MemoryDriver(object):

    def __init__(self):
        u""" Class Constructor """
        self.__activeQueue = []

    def put(self, lMessage):
        u"""
        Puts message to the end of the queue

        :param lMessage: Message object
        :type lMessage: pCore.module.queue.messages.Message.Message
        """
        self.__activeQueue.append(lMessage)

    def get(self):
        u"""
        Returns and removes message from the beginning of the queue

        :rtype : pCore.module.queue.messages.Message.Message
        """
        return self.__activeQueue.pop(0)

    @property
    def count(self):
        u"""
        Returns count of messages waiting in the line
        :rtype : int
        """
        return len(self.__activeQueue)