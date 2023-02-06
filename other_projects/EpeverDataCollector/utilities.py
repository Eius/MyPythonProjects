import time


def seconds_to_next_minute():
    current_time = time.time()
    next_minute = (int(current_time) + 60)
    return next_minute - current_time
