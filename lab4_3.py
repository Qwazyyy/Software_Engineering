import datetime
import time


def display_current_time_for_5_seconds():
    end_time = time.time() + 5
    while time.time() < end_time:
        now = datetime.datetime.now()
        print(now.strftime("%d-%m-%Y %H:%M:%S"))
        time.sleep(1)


if __name__ == "__main__":
    display_current_time_for_5_seconds()
