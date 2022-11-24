from setuptools import setup

APP = ['application.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True, 'iconfile': 'elearner.icns'}

setup(
    app=APP,
    name="Elearner",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)