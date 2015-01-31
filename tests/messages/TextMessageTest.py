# -*- coding: utf-8 -*-
from pCore.module.queue.messages.TextMessage import TextMessage
from tests.messages.MessageTest import MessageTest

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class TextMessageTest(MessageTest):

    def getInstance(self):
        return TextMessage(pText=u"test message")

    def testShouldHavePropertyText(self):
        self.assertEqual(u"test message", self.instance.text)

    def testShouldImplementUnicodeAndStringInterpretation(self):
        self.assertEqual(u"test message", unicode(self.instance))
        self.assertEqual("test message", str(self.instance))