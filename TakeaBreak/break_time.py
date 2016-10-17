import webbrowser
import time

count = 1
while (count <= 3):
    time.sleep(10)
    print ("This program statrted on " + time.ctime())
    webbrowser.open("http://www.youtube.com/watch?v=0sw54Pdh_m8")
    count += 1
