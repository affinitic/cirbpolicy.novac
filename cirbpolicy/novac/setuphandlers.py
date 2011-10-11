
from zope.interface import alsoProvides
from Products.CMFPlone.interfaces import IHideFromBreadcrumbs

def setupNovac(context):

    site = context.getSite()
    portal_workflow = site.portal_workflow
    if context.readDataFile('cirb.novac_various.txt') is None:
        return
    if not site.objectIds('Nova Citoyen'):
        site.invokeFactory(type_name='Nova Citoyen', id='novac')
        novac = site.novac
        novac.setTitle("Permis d'urbanisme")
        novac.setDescription("")
        novac.setLanguage("fr")
        #alsoProvides(novac, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(novac,'publish')
        
        site.invokeFactory(type_name='Nova Citoyen', id='novac_nl')
        novac_nl = site.novac_nl
        novac_nl.setTitle("Page novac_nl")
        novac_nl.setDescription("")
        novac_nl.setLanguage("nl")
        #alsoProvides(novac_nl, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(novac_nl,'publish')
        novac_nl.addTranslationReference(novac)        
        
        
        novac.invokeFactory(type_name='Urbis Map', id='urbismap')
        urbismap = novac.urbismap
        urbismap.setTitle("urbismap")
        urbismap.setDescription("")
        urbismap.setLanguage("fr")
        urbismap.setWs_urbis("http://192.168.13.45:8080/geoserver/gwc/service/wms")
        #alsoProvides(urbismap, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(urbismap,'publish')
        
        novac_nl.invokeFactory(type_name='Urbis Map', id='urbismap_nl')
        urbismap_nl = novac_nl.urbismap_nl
        urbismap_nl.setTitle("urbismap_nl")
        urbismap_nl.setDescription("")
        urbismap_nl.setLanguage("nl")
        urbismap_nl.setWs_urbis("http://192.168.13.45:8080/geoserver/gwc/service/wms")
        #alsoProvides(urbismap_nl, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(urbismap_nl,'publish')
        urbismap_nl.addTranslationReference(urbismap)
        
        
        novac.invokeFactory(type_name='Public Folder', id='public')
        public = novac.public
        public.setTitle("public")
        public.setDescription("")
        public.setLanguage("fr")
        public.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(public, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(public,'publish')
        
        novac_nl.invokeFactory(type_name='Public Folder', id='publiek')
        publiek = novac_nl.publiek
        publiek.setTitle("publiek")
        publiek.setDescription("")
        publiek.setLanguage("nl")
        publiek.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(publiek, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(publiek,'publish')
        publiek.addTranslationReference(public)
        
        
        novac.invokeFactory(type_name='List Private Folder', id='privatefolder')
        privatefolder = novac.privatefolder
        privatefolder.setTitle("privatefolder")
        privatefolder.setDescription("")
        privatefolder.setLanguage("fr")
        privatefolder.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(privatefolder, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(privatefolder,'publish')
        
        novac_nl.invokeFactory(type_name='List Private Folder', id='privatefolder_nl')
        privatefolder_nl = novac_nl.privatefolder_nl
        privatefolder_nl.setTitle("privatefolder_nl")
        privatefolder_nl.setDescription("")
        privatefolder_nl.setLanguage("nl")
        privatefolder_nl.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(privatefolder_nl, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(privatefolder_nl,'publish')
        privatefolder_nl.addTranslationReference(privatefolder)
        
        
        privatefolder.invokeFactory(type_name='Private Folder', id='private')
        private = privatefolder.private
        private.setTitle("private")
        private.setDescription("")
        private.setLanguage("fr")
        private.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(private, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(private,'publish')
        
        privatefolder_nl.invokeFactory(type_name='Private Folder', id='private_nl')
        private_nl = privatefolder_nl.private_nl
        private_nl.setTitle("private_nl")
        private_nl.setDescription("")
        private_nl.setLanguage("nl")
        private_nl.setWs_url("http://ws.irisnet.be/waws/nova")
        #alsoProvides(private_nl, IHideFromBreadcrumbs)
        portal_workflow.doActionFor(private_nl,'publish')
        private_nl.addTranslationReference(private)
        
        
        logger = context.getLogger("Novac")
        logger.info('end install Novac')
