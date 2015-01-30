# -*- coding: utf-8 -*-

import mox
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()

    def tearDown(self):
        if hasattr(self, u"mox"):
            self.mox.UnsetStubs()