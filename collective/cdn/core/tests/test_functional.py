# -*- coding:utf-8 -*-

import unittest2 as unittest
import doctest

from plone.testing import layered

from collective.cdn.core.testing import FUNCTIONAL_TESTING

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('browser.txt',
                                     package='collective.cdn.core.docs',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
    ])
    return suite
