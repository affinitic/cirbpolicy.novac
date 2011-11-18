import logging
from Products.CMFCore.utils import getToolByName

def upToFourOneTwo(context):
    """ upgrade steps to plone 4.1.2 """
    log = logging.getLogger("cirbpolicy.novac upgrade step")
    portal_migration = getToolByName(context, 'portal_migration')
   
    portal_migration.upgrade()
    log.info("Ran Plone Upgrade")
    
    # migrate blob ?