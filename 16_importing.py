import config as conf
print(locals())
print(dir(conf))
print(conf.token)

from config import token
print(locals())

from config import *
print(locals())

