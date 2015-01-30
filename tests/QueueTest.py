# -*- coding: utf-8 -*-
from pCore.module.queue.Message import Message
from pCore.module.queue.Queue import Queue
from pCore.module.queue.drivers.MemoryDriver import MemoryDriver

from tests.BaseTest import BaseTest

__author__ = u"Tomas Holub (tomas.holub@olc.cz)"
__credits__ = u"""\
Author: Tomas Holub
Create date: 2014-09-01 13:14
Modification date:  
Description: """


class QueueTest(BaseTest):

    def setUp(self):
        super(QueueTest, self).setUp()

        self.driverMock = self.mox.CreateMock(MemoryDriver)
        self.instance = Queue()

    def testShouldReturnZeroCountOfMessagesInQueue(self):
        self.assertEqual(0, self.instance.count)

    def testShouldPutNewMessageToTheQueue(self):
        lMessageMock = self.mox.CreateMock(Message)

        self.instance.put(lMessageMock)
        self.instance.put(lMessageMock)

        self.assertEqual(2, self.instance.count)

    def testShouldPopFromTheQueue(self):
        lMessageMock1 = self.mox.CreateMock(Message)
        lMessageMock2 = self.mox.CreateMock(Message)

        self.instance.put(lMessageMock1)
        self.instance.put(lMessageMock2)

        self.assertEqual(lMessageMock1, self.instance.get())
        self.assertEqual(1, self.instance.count)