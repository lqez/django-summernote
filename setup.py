from setuptools import setup, find_packages
from django_summernote import version, PROJECT


MODULE_NAME = 'django_summernote'
PACKAGE_DATA = list()
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]


setup(
    name=PROJECT,
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='django-summernote maintainers',
    url='http://github.com/summernote/django-summernote',

    description='Summernote plugin for Django',
    classifiers=CLASSIFIERS,

    install_requires=['django', ],
    test_suite='runtests.runtests',
    tests_require=['django-dummy-plug', ],
)
