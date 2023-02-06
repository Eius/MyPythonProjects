from datetime import datetime, timedelta


def seconds_to_next_measurement():
    current_time = datetime.now()
    target_time = datetime.now().replace(second=30, microsecond=0)
    target_time += timedelta(minutes=1)
    remaining_seconds = (target_time - current_time).total_seconds()
    return remaining_seconds
