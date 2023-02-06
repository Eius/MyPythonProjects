from serial import SerialException

from data_writer import DataWriter
from data_fetcher import DataFetcher
import time
import logging
from utilities import seconds_to_next_measurement

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs/logs.log',
                    encoding='utf-8',
                    level=logging.DEBUG)

COM_PORT = input("COM port:")

try:
    fetcher = DataFetcher(COM_PORT)
    writer = DataWriter(fetcher)
except SerialException:
    print("COM port doesn't exist.")
    print("Terminating program...")
    exit()

while True:
    seconds_remaining = seconds_to_next_measurement()
    print(f"Next measurement in: {seconds_remaining}")
    time.sleep(seconds_remaining)

    # Fetch data from epever controller
    points = fetcher.get_points()

    # Write data to database, return true if successful, false otherwise
    was_successful = writer.write_points(points)
    if not was_successful:
        logging.warning("Write to database failed.")
        print("Write to database failed.")
        raise Exception("Write to database was not successful")
    else:
        print("Write to database was successful.")
        logging.info("Write to database was successful.")
