import os
import os.path
import subprocess
from subprocess import Popen
from time import sleep
import datetime
from time import strftime

import json
import psutil
import pygetwindow as gw

from serv_class import *


def makefile():
    target = input(clrs.OKBLUE + 'Please input the directory path for steamcmd.exe: ' + clrs.ENDC)
    path = {
        "directory": target
    }
    with open("directory.json", "w") as outfile:
        json.dump(path, outfile)


def getdir():
    with open('directory.json', 'r') as openfile:
        json_object = json.load(openfile)
        return json_object


def add_dir():
    target = requested_time()
    answer = {
        'time': target
    }
    with open('directory.json', 'r+') as f:
        data = json.load(f)
        data.update(answer)
        f.seek(0)
        json.dump(data, f)
    return


def steamcmd_dir_check():
    print(clrs.WARNING + ' The program will check to ensure both the "SteamCMD" and "Valheim dedicated'
                         ' server"\n directories exist.\n'
                         ' When entering the directory please use the following format:\n'
                         ' "C:\\SteamCMD" or "Drive:\\Directory" where steamcmd.exe is installed.\n' + clrs.ENDC)
    checkjson = file_check_json()
    if checkjson is not True:
        makefile()
        instructions()
        add_dir()
    elif checkjson:
        getfile = getdir()
        steam_path = getfile.get('directory')
        print(steam_path)
        steamcmd = "steamcmd.exe"
        vds = "valheim_server.exe"
        if FileNotFoundError in os.listdir('%s' % steam_path):
            print(
                clrs.FAIL + 'SteamCMD not detected. Please install SteamCMD and rerun this program. This program will now '
                            'close.' + clrs.ENDC)
            input('Press any key to continue...')
            exit()
        if FileNotFoundError in os.listdir('%s\\steamapps\\common\\Valheim dedicated server' % steam_path):
            print(
                clrs.FAIL + 'The valheim server is not installed. Please install the valheim server before proceeding.'
                + clrs.ENDC)
            input('Press any key to continue...')
            exit()
        fnf = os.listdir(steam_path)
        vdsp = os.listdir('%s\\steamapps\\common\\Valheim dedicated server' % steam_path)
        steamtrue = any(item in steamcmd for item in fnf)
        servertrue = any(item in vds for item in vdsp)
        while steamtrue:
            print(clrs.OKGREEN + 'SteamCMD is present in the entered directory.' + clrs.ENDC)
            break
        while servertrue:
            print(clrs.OKGREEN + 'Server files already installed' + clrs.ENDC)
            break
        return steam_path


# Calls the server status function to verify the operation of the server. This function is self-contained and does
# not return a value.
def user_start_server():
    # Define the variable as the call.
    request = server_status()

    # If the server is operational it lets the user know and returns nothing.
    if request:
        print(clrs.OKGREEN + 'The server is already running.' + clrs.ENDC)
    # If the server is not running it queries the users on whether they would like to start the server and
    # asks for a response before continuing.
    else:
        print(clrs.WARNING + 'Would you like to start the server?\n' + clrs.ENDC)
        answer = input(clrs.OKCYAN + 'PLEASE ENTER Yes OR No: ' + clrs.ENDC)
        # If the response is yes it calls the server_start function and boots up the dedicated server, pauses, then
        # returns nothing.
        if answer == "y":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "Y":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "Yes":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "YEs":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "YES":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "yES":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "yeS":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "yes":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "yEs":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        elif answer == "yeS":
            print('STARTING THE SERVER')
            print('=======================\n')
            server_start()
            sleep(1)
        # If the answer is no it notifies the user that it is skipping over the operation and returns nothing.
        elif answer == "n":
            print('Skipping server start...')
            print('========================================\n')
        elif answer == "N":
            print('Skipping server start...')
            print('========================================\n')
        elif answer == "no":
            print('Skipping server start...')
            print('========================================\n')
        elif answer == "nO":
            print('Skipping server start...')
            print('========================================\n')
        elif answer == "No":
            print('Skipping server start...')
            print('========================================\n')
        elif answer == "NO":
            print('Skipping server start...')
            print('========================================\n')
        # Check to ensure that the user responds with the appropriate response and limits the answers to y or n.
        # It then recalls the function to loop.
        else:
            print('Please input yes or no')
            user_start_server()
    return


# Calls for a directory check to ensure that the needed directory is present and if not it creates one. This
# function is self-contained and does not return a value.
def directory_check():
    # Defines the bat_dir variable as the initial call for a directory check
    bat_dir = dir_check()
    # Pulls the current working directory and the assigns it a variable.
    cwd = os.getcwd()
    # If the directory is true it prints an empty line.
    if bat_dir:
        print('')
    # If the directory is not true it creates a directory named "batch_files"
    elif bat_dir is not True:
        directory = "batch_files"
        path = os.path.join(cwd, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)
    return


# Calls the file_check_server function, returns and assigns it a variable of serverbat. After running the check,
# if the result is True, it does nothing and continues. If the result is not True it flags a message to
# the user and creates a new server boot file. The function is self-contained and does not return a value.
def serverchk():
    # Assignment of the variable serverbat to be the returned value of the function file_check_server.
    serverbat = file_check_server()
    if serverbat:
        pass
    elif serverbat is not True:
        getfile = getdir()
        steam_dir = getfile.get('directory')
        # Alerts the user that it could not find the batch file.
        print(clrs.FAIL + 'COULD NOT FIND "URDediServ.bat" - Creating a new server boot file.\n' + clrs.ENDC)

        # Asks the user to input the display name of the server.
        name = input(clrs.OKGREEN + 'Please input the name would you like to have publicly displayed for your'
                                    ' server: \n' + clrs.ENDC)

        # Asks the user to input the name of the save file they would like to use.
        world = input(clrs.OKGREEN +
                      'Please input the name of the save you would like to use \n(If it is a new save do not use a '
                      'previously '
                      'used name): \n' + clrs.ENDC)

        # Asks the user to input the password they would like to use
        password = input(clrs.OKGREEN + 'Please input a password - The password must be at minimum 5 characters '
                                        'otherwise the server will not boot.: \n' + clrs.ENDC)

        # Assigns a variable to the Current Working Directory.
        cwd = os.getcwd()

        # Creates a new batch file and writes the necessary CMD Terminal to both update the server via SteamCMD and
        # start the server with the input parameters the user had input into the program earlier. Unless the file
        # is deleted this will only happen once.
        filepath = open(
            '%s/batch_files/URDediServ.bat' % cwd,
            "w")
        filepath.write('@ECHO OFF\n'
                       'title "valheimserver"'
                       '\n'
                       'color a\n'
                       '\n'
                       'ECHO UPDATING VALHEIM DEDICATED SERVER\n'
                       'ECHO ===================================================\n'
                       '\n'
                       'cd /D %s\n'
                       'steamcmd +login anonymous +app_update 896660 validate +exit\n'
                       '\n'
                       'ECHO STARTING THE SERVER...\n'
                       'ECHO ===================================================\n'
                       '\n'
                       'cd "%s\steamapps\common\Valheim dedicated server"\n'
                       '\n'
                       'set SteamAppId=892970\n'
                       '\n'
                       'echo "Starting server PRESS CTRL-C to exit"\n'
                       '\n'
                       'REM Tip: Make a local copy of this script to avoid it being overwritten by steam.\n'
                       'REM NOTE: Minimum password length is 5 characters & Password cant be in the server name.\n'
                       'REM NOTE: You need to make sure the ports 2456-2458 are being forwarded to your server '
                       'through your local router & firewall.\n '
                       'valheim_server -nographics -batchmode -name "%s" -port 2456 -world "%s" -password "%s" '
                       '-crossplay' % (
                           steam_dir, steam_dir, name, world, password))
        filepath.close()
    return


# Calls the file_check_reset function and checks if the file server_reset.bat exists. If it does, it does nothing
# and if it does not it creates the appropriate file.
def resetchk():
    # Takes the return from file_check_reset and assigns it to the variable resetbat
    resetbat = file_check_reset()
    # Gets the Current Working Directory and assigns it to the variable cwd.
    cwd = os.getcwd()
    # If resetbat is true the program does nothing and continues.
    if resetbat:
        pass
    # If reset bat is false the program notifies the user and creates the necessary batch file.
    elif resetbat is not True:
        print(clrs.FAIL + 'COULD NOT FIND "server_reset.bat" - Creating a new server reset file.\n' + clrs.ENDC)
        filepath2 = open(
            '%s/batch_files/server_reset.bat' % cwd,
            "w")
        filepath2.write('@ECHO OFF\n taskkill /IM "valheim_server.exe"')
        filepath2.close()
    return


# Prints the instructions to the user for time entry and requests the user input for a time to restart the server.
# Once the value is entered it is assigned to the variable and checks to make sure it is the proper format. If it
# is not the proper format it kicks back an error telling the user they have 3 attempts to enter the correct time
# before the program quits. After the third incorrect attempt the program exits.
def match_time():
    # Calls the function to give instructions to the user if the time value is not already present in directory.json.
    # Assignment of the variable answer to the returned value of requested time.
    # Attempts to check the format of the answer variable against the needed format.
    if file_check_json():
        getfile = getdir()
        answer = getfile.get('time')
        try:
            datetime.datetime.strptime(answer, "%H:%M")
        # Raises an error if the format does not match and gives the user 3 attempts to input a time in the correct
        # format.
        except ValueError as err:
            # First error raised and requests input a second time. The new returned value is assigned to the variable
            # again.
            if err:
                print(clrs.FAIL + 'ERROR: INVALID TIME FORMAT' + clrs.ENDC)
                print('You have 3 attempts to enter the correct time. Attempt: 1/3')
                input('Press any key to continue...')
                instructions()
                answer = requested_time()
                # Attempts to check the format of the answer variable against the needed format.
                try:
                    datetime.datetime.strptime(answer, "%H:%M")
                # Second error raised and requests input a third time. The new returned value is assigned to the
                # variable again.
                except ValueError as err:
                    if err:
                        print(clrs.FAIL + 'ERROR: INVALID TIME FORMAT' + clrs.ENDC)
                        print('You have 3 attempts to enter the correct time. Attempt: 2/3')
                        input('Press any key to continue...')
                        instructions()
                        answer = requested_time()
                    # Attempts to check the format of the answer variable against the needed format.
                    try:
                        datetime.datetime.strptime(answer, "%H:%M")
                    # Third error raised and notifies the user of program termination.
                    except ValueError as err:
                        if err:
                            print(clrs.FAIL + 'ERROR: INVALID TIME FORMAT' + clrs.ENDC)
                            print('You have 3 attempts to enter the correct time. Attempt: 3/3')
                            print('You have failed to enter a valid time - exiting the program.')
                            input('PRESS ANY KEY TO EXIT...')
                            exit()
        return answer
    elif file_check_json() is not True:
        print(clrs.FAIL + 'ERROR: dictionary.json does not exist! Exiting the program...' + clrs.ENDC)
        exit()


def reset_clock():
    output = match_time()
    servercondition = "valheim_server.exe" in (i.name() for i in psutil.process_iter())
    if servercondition:
        while output != strftime('%H:%M'):
            print(clrs.OKGREEN + "Time is presented in 24hr format.\n" + clrs.ENDC)
            print(clrs.WARNING + "Checking the time..." + clrs.ENDC)
            print(strftime('%H:%M'))
            print(clrs.OKCYAN + "NOT TIME TO RESTART THE SERVER. SERVER RESTART TIME:", output)
            print(clrs.UNDERLINE + "To end this program press CTRL + C" + clrs.ENDC)
            sleep(5)
            os.system('cls')
            if output == strftime('%H:%M'):
                print("RESTARTING THE SERVER...")
                restart()
                sleep(1)
            break
    elif servercondition is not True:
        print('THE SERVER SHUT DOWN UNEXPECTEDLY')
        print('RESTARTING THE SERVER...TO CANCEL THIS OPERATION PRESS CTRL + C')
        sleep(30)
        server_start()


def restart():
    server_kill()
    sleep(30)
    server_start()
    sleep(1)


def instructions():
    print(clrs.OKGREEN + "All times must be input in 24hr format - TO END THIS PROGRAM PRESS CTRL + C\n" + clrs.ENDC
          )
    print(
        clrs.WARNING + "TIME MUST BE ENTERED AS 'XX:XX' OTHERWISE THE PROGRAM WILL NOT WORK!!!\n" + clrs.ENDC)
    print(
        clrs.OKBLUE + "Please enter the time in hours and minutes (eg. 13:00 = 1:00 PM) \nyou would like to have"
                      " the server restart.\n" + clrs.ENDC)
    return


def server_status():
    print(clrs.WARNING + 'CHECKING THE STATUS OF THE SERVER...' + clrs.ENDC)
    print('========================================\n')
    server_up_down = "valheim_server.exe" in (i.name() for i in psutil.process_iter())
    print('THE SERVER IS CURRENTLY RUNNING:', server_up_down, '\n')
    return server_up_down


def server_kill():
    cwd = os.getcwd()
    Popen(["%s/batch_files/server_reset.bat" % cwd])


def server_start():
    cwd = os.getcwd()
    Popen(["%s/batch_files/URDediServ.bat" % cwd],
          creationflags=subprocess.CREATE_NEW_CONSOLE)
    print('STANDING BY FOR SERVER UPDATE, BOOT, AND MINIMIZING THE WINDOW')
    print('======================================\n')
    sleep(2)
    win = gw.getWindowsWithTitle('valheimserver')[0]
    win.minimize()
    activity_status_steam = "SteamCMD.exe"
    valheim_server_status = "valheim_server.exe"
    while activity_status_steam:
        print('SERVER IS UPDATING - PLEASE STAND BY')
        if activity_status_steam:
            sleep(10)
            break
        else:
            continue
    while valheim_server_status:
        print('SERVER SUCCESSFULLY STARTED - CONTINUING OPERATION')
        sleep(3)
        break


def requested_time():
    target_time_main = input("REQUESTED SERVER RESTART TIME: ")
    print('\n')
    return target_time_main


def user_message():
    # Set the target time for server restart then clear the screen
    print(clrs.OKGREEN + "All times must be input in 24hr format - TO END THIS PROGRAM PRESS CTRL + C\n")
    print(clrs.FAIL + "TIME MUST BE ENTERED AS 'XX:XX:XX' OTHERWISE THE PROGRAM WILL NOT WORK!!!\n" + clrs.ENDC)
    print(clrs.OKBLUE + "Please enter the time in hours and minutes (eg. 13:00 = 1:00 PM) \nyou would like to have"
                        " the server restart.\n" + clrs.ENDC)


def dir_check():
    cwd = os.getcwd()
    path = ('%s/batch_files' % cwd)
    exist = os.path.exists(path)
    print(clrs.WARNING + 'CHECKING FOR "batch_files" DIRECTORY' + clrs.ENDC)
    print('========================================================\n')
    print('EXISTENCE = ', exist)
    return exist


def file_check_server():
    cwd = os.getcwd()
    path1 = ('%s/batch_files/URDediServ.bat' % cwd)
    print('Does "URDediServ.bat" exist?:', os.path.isfile(path1))
    return os.path.isfile(path1)


def file_check_reset():
    cwd = os.getcwd()
    path2 = ('%s/batch_files/server_reset.bat' % cwd)
    print('Does "server_reset.bat" exist?:', os.path.isfile(path2))
    return os.path.isfile(path2)


def file_check_json():
    cwd = os.getcwd()
    path1 = ('%s/directory.json' % cwd)
    os.path.isfile(path1)
    return os.path.isfile(path1)
