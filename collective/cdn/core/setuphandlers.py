# -*- coding: utf-8 -*-
import logging
from Products.CMFCore.utils import getToolByName

from Products.GenericSetup.upgrade import listUpgradeSteps


_PROJECT = 'collective.cdn.core'
_PROFILE_ID = 'collective.cdn.core:default'


def doUpgrades(context):
    ''' If exists, run migrations
    '''
    if context.readDataFile('collective.cdn.core.txt') is None:
        return

    logger = logging.getLogger(_PROJECT)
    site = context.getSite()
    setup_tool = getToolByName(site, 'portal_setup')
    cache = getToolByName(context, 'portal_cache_settings', None)
    enable_cache = False
    version = setup_tool.getLastVersionForProfile(_PROFILE_ID)
    upgradeSteps = listUpgradeSteps(setup_tool, _PROFILE_ID, version)
    sorted(upgradeSteps, key=lambda step: int(step['sortkey']))

    if cache and cache.getEnabled():
        # In case we have a cache fu, disable it to avoid a
        # tsunami of purges
        cache.setEnabled(False)
        enable_cache = True

    for step in upgradeSteps:
        oStep = step.get('step')
        if oStep is not None:
            oStep.doStep(setup_tool)
            msg = "Ran upgrade step %s for profile %s" % (oStep.title,
                                                          _PROFILE_ID)
            setup_tool.setLastVersionForProfile(_PROFILE_ID, oStep.dest)
            logger.info(msg)

    if cache and enable_cache:
        # Now, turn cachefu back to normal
        cache.setEnabled(True)
