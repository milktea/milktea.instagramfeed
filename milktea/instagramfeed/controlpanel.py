from zope import schema
from zope.interface import Interface
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from z3c.form import form
from zope.interface import invariant, Invalid

from milktea.instagramfeed import MessageFactory as _

class IInstagramSettings(Interface):
    instagram_username = schema.TextLine(
        title=u'Instagram hashtags',
        required=True,
        description=u'Instagram username or hashtags for the entire site. '
        			u'Please specify hashtags in a comma-separated list, e.g. #shoes, #tea. '
                    u'If you type @milktea here, user feed would be displayed instead of '
                    u'hashtags.'
    )
   
class InstagramControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IInstagramSettings

InstagramControlPanelView = layout.wrap_form(InstagramControlPanelForm, ControlPanelFormWrapper)
InstagramControlPanelView.label = _(u"Milktea Instagram Feed Portlet Settings")





