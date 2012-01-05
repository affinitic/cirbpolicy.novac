import logging
from Products.CMFCore.utils import getToolByName

def upToFourOneTwo(context):
    """ upgrade steps to plone 4.1.3 """
    log = logging.getLogger("cirbpolicy.novac upgrade step")
    portal_migration = getToolByName(context, 'portal_migration')
   
    portal_migration.upgrade()
    log.info("Ran Plone Upgrade")
    
    # clean danny's changes
    
    # clean AROffice
    
    # make splash page