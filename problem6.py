import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water!!",
            message = "The Adequate Intake for total water, based on median intakes, is 3.7 litres (130 imp fl oz; 130 US fl oz) per day for human males older than 18, and 2.7 litres (95 imp fl oz; 91 US fl oz) per day for human females older than 18",
            app_icon = "D:\python practice\glass.ico",
            timeout = 6
        )
        time.sleep(60*60)
