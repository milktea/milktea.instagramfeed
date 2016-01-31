from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import invariant, Invalid
from milktea.instagramfeed import MessageFactory as _
import urllib2
import json

grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):

    portlet_title = schema.TextLine(
        title=u'Portlet Title',
        default=u"Latest Instagram Posts",
        required=False)

    instagram_username = schema.TextLine(
        title=u'Instagram Username or Hashtags',
        required=False,
        description=u"Override default instagram username or hashtags of the entire site (Config at http://localhost:8080/Plone/@@twitter-controlpanel). "
                    u'Please specify hashtags in a comma-separated list, e.g. #shoes, #tea. '
                    u'If you type @milktea here, user feed would be displayed instead of '
                    u'hashtags.'
                    u"If you plan to use the default, leave blank. "
    )

    no_posts = schema.Int(
        title=u'Number of posts to be shown',
        default=10)

    portlet_height=schema.TextLine(
        title=u"Height of Portlet",
        description=u"e.g. '500px'",
        default=u'500px')

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self, instagram_username=None, no_posts=None, portlet_title=None, portlet_height=None):
        self.instagram_username = instagram_username
        self.no_posts = no_posts
        self.portlet_title = portlet_title
        self.portlet_height = portlet_height
       
    @property
    def title(self):
        return "Milktea Instagram Feed Portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/instagramfeedportlet.pt')
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
    def data(self):
        return self.data

    def insta_contents(self):
        portlet_username = self.data.instagram_username
        if portlet_username:
            return portlet_username
        else:
            return self.instagram_default()

    def instagram_default(self):
        registry = getUtility(IRegistry)
        field = 'milktea.instagramfeed.controlpanel.IInstagramSettings.instagram_username'
        instagram_username = ''
        if registry.get(field):
            instagram_username = registry.get(field).encode()
        return instagram_username

    def instagram_hashtags_joined(self):
        hashtag = self.insta_contents()
        if not hashtag or '@' in hashtag:
            return u''
        return u','.join(map(
            lambda x: x.strip(),
            hashtag.replace('#', '').split(',')
        ))

        if not hashtag or '@' in hashtag:
            return u''
        if ',' in hashtag:
            return u','.join(map(lambda x: x.strip(),hashtag.replace('#', '').split(',')))
        if ',' not in hashtag:
            return u','.join(map(lambda x: x.strip(),hashtag.replace('#', '').split(' ')))

    def instagram_user_feed(self):
        hashtag = self.insta_contents()
        if not hashtag or '#' in hashtag:
            return u''
        return hashtag.replace('@', '').strip()

    def instagram(self, username= None):
        url = "https://api.instagram.com/v1/users/search?q='"+str(username)+"'&client_id=81b42938f3dd4e48b77846755069ce56&count=1"
        response = urllib2.urlopen(url)
        html = response.read()
        data = ''
        json_data = json.loads(html)
        if json_data.has_key('data'):
            if json_data['data']:
                data = json_data['data'][0]['id']
        return data

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Add Milktea Instagram Feed Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Milktea Instagram Feed Portlet"
    description = ''
