import time
import psutil
from plyer import notification

print("Started....")

cBatteryPercent = 0
pBatteryPercent = 0

if psutil.sensors_battery().power_plugged:#If charging is active
    pBatteryPercent = 0
    while True:
        cBattery = psutil.sensors_battery()
        CurrentBatterPercent = cBattery.percent
        cBatteryPercent = CurrentBatterPercent
        if cBatteryPercent >= pBatteryPercent:
            title = "Battery Percent Reminder" #display notification title
            message = f'Your current battery percent is {CurrentBatterPercent}'
            notification.notify(title = title , message = message)
            pBatteryPercent = cBatteryPercent + 1
        time.sleep(1)    

