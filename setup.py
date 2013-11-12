import os
from setuptools import setup, find_packages
from django_summernote import version, PROJECT


MODULE_NAME = 'django_summernote'
PACKAGE_DATA = list()
CLASSIFIERS = [
    'Topic :: Utilities',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
]

for directory in ['static', 'templates']:
    for root, dirs, files in os.walk(os.path.join(MODULE_NAME, directory)):
        for filename in files:
            PACKAGE_DATA.append("%s/%s" % (root[len(MODULE_NAME) + 1:],
                                           filename))


setup(
    name=PROJECT,
    version=version,
    packages=find_packages(),
    package_data={'': PACKAGE_DATA, },
    zip_safe=False,

    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/django-summernote',

    description='Summernote plugin for Django',
    classifiers=CLASSIFIERS,

    install_requires=['django'],
    tests_require=['argparse', 'django-setuptest'],
    test_suite='setuptest.setuptest.SetupTestSuite',
)
