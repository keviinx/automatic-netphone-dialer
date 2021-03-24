from pynput.keyboard import Controller
import time
import subprocess
from datetime import datetime
from threading import Timer

#===== CONFIGURATION =====

path_to_program = 'C:\\Program Files (x86)\\SwyxIt!\\SwyxIt!.exe' # put location of phone software here
phone_number = '0012345678912'
language = 'en' # en or de
meeting_room = "123456789#" # put meeting room number and # at the back
start_time_hour = 9 # put the hour time you want to call
start_time_minute = 15 # put the minute time you want to call

#=========================

datetime_today = datetime.today() # get today
datetime_toexecute = datetime_today.replace(day=datetime_today.day+1, hour=start_time_hour, minute=start_time_minute-1, second=52, microsecond=0) # time setting to be executed
delta_time = datetime_toexecute - datetime_today # delta time calculation

exact_timetoexecute = delta_time.seconds+1 # get the exact seconds to execute by adding 1

def dial_phone():
    keyboard = Controller()

    # send this command to powershell or cmd
    # C:\"Program Files (x86)"\SwyxIt!\SwyxIt!.exe -d 0012345678912
    # %ProgramFiles(x86)%\SwyxIt!\SwyxIt!.exe
    subprocess.call([path_to_program, '-d', phone_number])

    time.sleep(6) # sleep for 6 seconds
    if language == 'en':
        keyboard.type("2#") # type 2#
    else:
        keyboard.type("1#") # type 1#

    time.sleep(1) # sleep for 1 second
    keyboard.type(meeting_room) # type the meeting room

    time.sleep(1) # sleep for 1 second
    keyboard.type("#") # no extension

# Start the dialing process
process = Timer(exact_timetoexecute, dial_phone)
process.start()
