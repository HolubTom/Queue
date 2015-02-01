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

    def testShouldStoreAndReturnHistoryOfMessages(self):
        lMessageMock1 = self.mox.CreateMock(Message)
        lMessageMock2 = self.mox.CreateMock(Message)
        lMessageMock3 = self.mox.CreateMock(Message)
        lMessageMock4 = self.mox.CreateMock(Message)
        lMessageMock5 = self.mox.CreateMock(Message)

        self.driverMock.put(lMessageMock1)
        lMessageMock1.setQueued()

        self.driverMock.put(lMessageMock2)
        lMessageMock2.setQueued()

        self.driverMock.put(lMessageMock3)
        lMessageMock3.setQueued()

        self.driverMock.put(lMessageMock4)
        lMessageMock4.setQueued()

        self.driverMock.put(lMessageMock5)
        lMessageMock5.setQueued()

        self.driverMock.get().AndReturn(lMessageMock1)
        lMessageMock1.setDequeued()

        self.driverMock.get().AndReturn(lMessageMock2)
        lMessageMock2.setDequeued()

        self.driverMock.count = 3

        self.driverMock.getHistory().AndReturn([
            lMessageMock1,
            lMessageMock2
        ])

        self.mox.ReplayAll()

        self.instance.put(lMessageMock1)
        self.instance.put(lMessageMock2)
        self.instance.put(lMessageMock3)
        self.instance.put(lMessageMock4)
        self.instance.put(lMessageMock5)

        self.assertEqual(lMessageMock1, self.instance.get())
        self.assertEqual(lMessageMock2, self.instance.get())

        self.assertEqual(3, self.instance.count)

        self.assertEqual([
            lMessageMock1,
            lMessageMock2
        ], self.instance.getHistory())

        self.mox.VerifyAll()