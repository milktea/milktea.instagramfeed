from collective.grok import gs
from milktea.instagramfeed import MessageFactory as _

@gs.importstep(
    name=u'milktea.instagramfeed', 
    title=_('milktea.instagramfeed import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('milktea.instagramfeed.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
