# -*- coding: utf-8 -*-
from pCore.module.queue.messages.Message import Message

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class TextMessage(Message):
    u""" Basic implementation of Message with simple text information """

    def __init__(self, pText):
        u"""
        Class constructor

        :param pText: Text information for the message
        :type pText: __builtin__.unicode
        """
        assert isinstance(pText, unicode)

        super(TextMessage, self).__init__()

        self.__aText = pText

    @property
    def text(self):
        u"""
        Getter for text information

        :rtype : __builtin__.unicode
        """
        return self.__aText

    def __unicode__(self):
        u"""
        Unicode interpretation

        :rtype : unicode
        """
        return unicode(self.__aText)

    def __str__(self):
        u"""
        Basestring interpretation

        :rtype : basestring
        """
        return str(self.__aText)