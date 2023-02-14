import time
from bd_sender import BDSender
import datetime as dt

bd_sender = BDSender()
now = dt.datetime.now()
first_time_running = True
should_send = "n"
# nxzsaophlodaezbi
while True:
    try:
        if first_time_running:
            should_send = input("Do you want to sent today's birthday emails? (y/n): ")
            first_time_running = False

        if should_send == "exit":
            raise KeyboardInterrupt

        if should_send == "y":
            bd_sender.check_birthdays_and_send_emails()

        should_send = "y"

        # Check again tomorrow 8 am
        tomorrow = now.date() + dt.timedelta(days=1)
        tomorrow_8_am = dt.datetime.combine(tomorrow, dt.time(hour=8))
        delta = tomorrow_8_am - now
        print(f"{int(delta.total_seconds())} seconds until next check.")
        time.sleep(int(delta.total_seconds()))

    except (KeyboardInterrupt, EOFError):
        print("\nTerminating program...")
        exit()


