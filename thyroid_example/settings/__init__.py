from base import *
from secret import *

PRODUCTION = False

if PRODUCTION:
    from production import *
else:
    from development import *
