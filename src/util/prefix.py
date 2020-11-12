import os,sys
import vdf

def searchprefix(steamdir) -> str:
    with open(os.path.join(steamdir, "libraryfolders.vdf")) as libfile:
        vdf.load(libfile)
        
def editprefix(gameprefix:str) -> None:
    pass