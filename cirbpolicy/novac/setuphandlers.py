
from zope.interface import alsoProvides
from Products.CMFPlone.interfaces import IHideFromBreadcrumbs
from cirb.novac.browser.novacview import INovacView
import os

def get_package_path():
    from cirb.novac import config
    return os.path.dirname(config.__file__)

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
        
        site.invokeFactory(type_name='Folder', 
                                      id=NOVACNL,
                                      title="NL Permis d'urbanisme",
                                      description="",
                                      language="nl")
        novac_nl = getattr(site, NOVACNL)
        alsoProvides(novac_nl, INovacView)
        portal_workflow.doActionFor(novac_nl,'publish')
        novac_nl.addTranslationReference(novac)
        
        novac.invokeFactory(type_name='Folder', id='img', title='img',description="", excludeFromNav=True)
        img = novac.img
        portal_workflow.doActionFor(img,'publish')
        #alsoProvides(img, IHideFromBreadcrumbs)
        
        from OFS.Image import File
        path = os.sep.join([get_package_path(),"img"])
        dir_list = os.listdir(path)
        for filename in dir_list:
            imgfile = File("dummy", "dummy", open('%s/%s' % (path,filename),"rb"))
            img.invokeFactory(type_name='Image', id=filename)
            my_img = getattr(img,filename)
            my_img.setImage(imgfile)
        
        logger = context.getLogger("Novac")
        logger.info('end install Novac')
