# Calls the dependencies and modules that are needed to operate the Main Function
from serv_func import *
from time import sleep


# The purpose of this script is to help automate some day to day functions of running a valheim dedicated server. It
# also helps automate the process of creating a server. This script is windows based and is hard coded into the script.
# I was still in the process of learning python. The code does stretch a little over on line length is some areas.

def main():
    steamcmd_dir_check()
    directory_check()
    sleep(1)
    serverchk()
    sleep(1)
    resetchk()
    sleep(1)
    user_start_server()
    while True:
        reset_clock()
        continue


if __name__ == "__main__":
    main()
