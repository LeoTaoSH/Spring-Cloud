import time;
from ansible.constants import LOCALHOST

localtime = time.localtime(time.time())

localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime
print "hello python"
import calendar

cal = calendar.month(2017, 9)
print "Here is the calendar:"
print cal

import thread
# import time

# Define a function for the thread
def print_time(threadName, delay): 
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

# Create two threads as follows
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
    thread.start_new_thread(print_time, ("Thread-3", 5,))
except:
    print "Error: unable to start thread"

while 1:
    pass
