import os, sys
import vdf
from util import prefix


user = os.environ("USER")
steamdir = os.path.join("/home", user, ".steam/steam/steamapps")
gameprefix = prefix.searchprefix(steamdir)
gameid = 1175140



