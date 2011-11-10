
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
        """
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
        """
        folders = [{'fr':{'id':'lesreglesdujeu','name':'Les regles du jeu'},'nl':{'id':'spelregels','name':'Spelregels'}},
                   {'fr':{'id':'quisommesnous','name':'Qui sommes-nous ?'},'nl':{'id':'wiezijnwij','name':'Wie zijn wij?'}},
                   {'fr':{'id':'cartographie','name':'Cartographie'},'nl':{'id':'cartografie','name':'Cartografie'}},
                   {'fr':{'id':'publications','name':'Etudes et Publications'},'nl':{'id':'publicaties','name':'Studies en publicaties'}}
                ]

        news = site.news
        news.setExcludeFromNav(True)
        
        events = site.events
        events.setExcludeFromNav(True)
        
        Members = site.Members
        Members.setExcludeFromNav(True)
        
        for folder in folders:            
            site.invokeFactory(type_name='Folder', 
                                       id=folder['fr']['id'],
                                       title=folder['fr']['name'],
                                       description="",
                                       language="fr")
            f_fr = getattr(site, folder['fr']['id'])
            portal_workflow.doActionFor(f_fr,'publish')
        
            site.invokeFactory(type_name='Folder', 
                                          id=folder['nl']['id'],
                                          title=folder['nl']['name'],
                                          description="",
                                          language="nl")
            f_nl = getattr(site, folder['nl']['id'])
            portal_workflow.doActionFor(f_nl,'publish')
            f_nl.addTranslationReference(f_fr)
            
        logger = context.getLogger("Novac")
        logger.info('end install Novac')
