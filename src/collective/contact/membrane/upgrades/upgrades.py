# -*- coding: utf-8 -*-
"""Upgrades for collective.contact.membrane
"""
from ecreall.helpers.upgrade.interfaces import IUpgradeTool


def v2(context):
    tool = IUpgradeTool(context)
    tool.runImportStep('webpro.ged', 'typeinfo')  #pylint: disable=E1121
