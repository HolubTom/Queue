# -*- coding: utf-8 -*-
from pCore.module.queue.messages.Message import Message
from pCore.module.queue.Queue import Queue
from pCore.module.queue.drivers.MemoryDriver import MemoryDriver

from tests.BaseTest import BaseTest

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class QueueTest(BaseTest):

    def setUp(self):
        super(QueueTest, self).setUp()

        self.driverMock = self.mox.CreateMock(MemoryDriver)
        self.instance = Queue(pDriver=self.driverMock)

    def testShouldReturnZeroCountOfMessagesInQueue(self):
        self.driverMock.count = 0

        self.mox.ReplayAll()

        self.assertEqual(0, self.instance.count)

        self.mox.VerifyAll()

    def testShouldPutNewMessageToTheQueue(self):
        lMessageMock = self.mox.CreateMock(Message)
        lMessageMock.setQueued()
        self.driverMock.put(lMessageMock)

        self.driverMock.count = 1

        self.mox.ReplayAll()

        self.instance.put(lMessageMock)

        self.assertEqual(1, self.instance.count)

        self.mox.VerifyAll()

    def testShouldPopFromTheQueue(self):
        lMessageMock1 = self.mox.CreateMock(Message)
        lMessageMock2 = self.mox.CreateMock(Message)

        self.driverMock.put(lMessageMock1)
        lMessageMock1.setQueued()

        self.driverMock.put(lMessageMock2)
        lMessageMock2.setQueued()

        self.driverMock.get().AndReturn(lMessageMock1)
        lMessageMock1.setDequeued()
        self.driverMock.count = 1

        self.mox.ReplayAll()

        self.instance.put(lMessageMock1)
        self.instance.put(lMessageMock2)

        self.assertEqual(lMessageMock1, self.instance.get())
        self.assertEqual(1, self.instance.count)

        self.mox.VerifyAll()