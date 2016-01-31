from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='milktea.instagramfeed',
      version=version,
      description="A Plone product that displays Instagram photos from any non-private Instagram account or from hashtags in a portlet",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      author='Millkea',
      author_email='sescatalan@gmail.com',
      url = 'https://github.com/milktea/milktea.instagramfeed', # URL to the github repo
      download_url = 'https://github.com/milktea/milktea.instagramfeed/tarball/1.0', # Version tag
      keywords = ['plone', 'portlet', 'instagram', 'feed', 'product'], # arbitrary keywords

      license='gpl',
      packages=find_packages(),
      namespace_packages=['milktea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'collective.grok',
          'plone.app.referenceablebehavior',
          'collective.dexteritytextindexer',
          # 'plone.app.multilingual',
          # 'plone.multilingualbehavior',
          'plone.app.versioningbehavior',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],

      )
