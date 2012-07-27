#!/usr/bin/env python
# coding: utf-8

from setuptools import setup


setup(
    name='localtodo',
    url='https://github.com/miracle2k/localtodo',
    version='1.0',
    license='BSD',
    author=u'Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    description=
        '.gitignore local todo files, but sync them through Dropbox.',
    py_modules=['localtodo'],
    install_requires=['docopt==0.4.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points="""[console_scripts]\nlocaltodo = localtodo:run\n""",
)