
from zope.interface import alsoProvides
from Products.CMFPlone.interfaces import IHideFromBreadcrumbs
from cirb.novac.browser.novacview import INovacView
import os
from Products.CAS4PAS.CASAuthHelper import addCASAuthHelper 

def get_package_path():
    from cirb.novac import config
    return os.path.dirname(config.__file__)

def setupNovac(context):

    site = context.getSite()
    portal_workflow = site.portal_workflow
    if context.readDataFile('cirb.novac_various.txt') is None:
        return
    
    #NOVAC="permis-d-urbanisme"
    #NOVACNL="stedenbouwkundige-vergunning"
    NOVAC="novac"
    NOVACNL="novac-nl"
    add_cas(context)
    
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
                                      title="Stedenbouwkundige vergunning",
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
        news.reindexObject()
        
        events = site.events
        events.setExcludeFromNav(True)
        events.reindexObject()
        
        Members = site.Members
        Members.setExcludeFromNav(True)
        Members.reindexObject()
        
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


def add_cas(context):
    site = context.getSite()
    name = "CASAuthHelper"
    if not name in site.acl_users.keys():
        addCASAuthHelper(site.acl_users,name)
        
        cah = site.acl_users.CASAuthHelper
        #cah.manage_changeProperties(login_url='https://sso.irisnetlab.be/cas/login',
        #            logout_url='https://sso.irisnetlab.be/cas/logout',
        #            validate_url='https://sso.irisnetlab.be/cas/validate')
        #validate_url = 'https://sso.irisnetlab.be/cas/validate'
        #domain = 'https://192.168.13.71:443/'
        domain = 'https://sso.irisnetlab.be/'
        validate_url = '%scas/serviceValidate' % domain
        cah.manage_changeProperties(login_url='%scas/login' % domain,
                    logout_url='%scas/logout' % domain,
                    validate_url=validate_url)
    
        cah.manage_activateInterfaces(['IAuthenticationPlugin', 
                                       'IChallengePlugin', 
                                       'ICredentialsResetPlugin',
                                       'IExtractionPlugin',
                                       'IPropertiesPlugin'])
        #'IPropertiesPlugin'
        #cah.plugins.movePluginsUp(cah.plugins._getInterfaceFromName('IAuthenticationPlugin'),['CASAuthHelper'])
        movePluginsTop(cah, 'IAuthenticationPlugin','CASAuthHelper')
        movePluginsTop(cah, 'IChallengePlugin','CASAuthHelper')
        movePluginsTop(cah, 'ICredentialsResetPlugin','CASAuthHelper')
        movePluginsTop(cah, 'IExtractionPlugin','CASAuthHelper')
        
        
        logger = context.getLogger("CASAuthHelper")
        logger.info('end install CASAuthHelper')

def movePluginsTop(acl, plugins_name, id_to_move):
    plugin_type = acl.plugins._getInterfaceFromName(plugins_name)
    while acl.plugins.listPlugins(plugin_type)[0][0] != id_to_move:
        #acl.plugins.movePluginsUp(plugin_type, [ids_to_move,])
        acl.plugins.movePluginsUp(plugin_type,[id_to_move])