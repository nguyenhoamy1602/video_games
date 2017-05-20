import os
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
DATABASE = os.path.join(_basedir, 'videogame.db')
SECRET_KEY = 'many random bytes'
del os
