
from zope.interface import alsoProvides
from Products.CMFPlone.interfaces import IHideFromBreadcrumbs
from cirb.novac.browser.novacview import INovacView

def setupNovac(context):

    site = context.getSite()
    portal_workflow = site.portal_workflow
    if context.readDataFile('cirb.novac_various.txt') is None:
        return
    
    NOVAC="novac"
    NOVACNL="novac_nl"
    if not site.hasObject(NOVAC):
        site.invokeFactory(type_name='Folder', 
                                   id=NOVAC,
                                   title="Permis d'urbanisme",
                                   description="",
                                   language="fr")
        novac = getattr(site, NOVAC)
        alsoProvides(novac, INovacView)
        portal_workflow.doActionFor(novac,'publish')
        
        novac_nl = site.invokeFactory(type_name='Folder', id=NOVACNL)
        novac_nl = getattr(site, NOVACNL)
        novac_nl.setTitle("Page novac_nl")
        novac_nl.setDescription("")
        novac_nl.setLanguage("nl")
        alsoProvides(novac_nl, INovacView)
        portal_workflow.doActionFor(novac_nl,'publish')
        novac_nl.addTranslationReference(novac)
        
        logger = context.getLogger("Novac")
        logger.info('end install Novac')
