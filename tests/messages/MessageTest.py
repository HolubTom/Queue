# -*- coding: utf-8 -*-
from pCore.module.queue.messages.Message import Message
from tests.BaseTest import BaseTest
from datetime import datetime

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class MessageTest(BaseTest):

    def setUp(self):
        super(MessageTest, self).setUp()

        self.instance = Message()

    def testShouldMarkMessageAsQueued(self):
        self.instance.setQueued()

        self.assertEqual(Message.STATUS_QUEUED, self.instance.status)
        self.assertIsInstance(self.instance.queuedDate, datetime)

    def testShouldMarkMessageAsDequeued(self):
        self.instance.setDequeued()

        self.assertEqual(Message.STATUS_DEQUEUED, self.instance.status)
        self.assertIsInstance(self.instance.dequeuedDate, datetime)

    def testShouldHaveMessageType(self):
        self.assertIsInstance(Message.MESSAGE_TYPE, unicode)
