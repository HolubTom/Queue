# -*- coding: utf-8 -*-

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class IDriver(object):

    def put(self, lMessage):
        u""" Puts message to the end of the queue """
        pass

    def get(self):
        u""" Returns and removes message from the beginning of the queue """
        pass

    @property
    def count(self):
        u""" Returns count of messages waiting in the line """
        pass