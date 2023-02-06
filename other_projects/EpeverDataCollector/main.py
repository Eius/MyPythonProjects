from data_writer import DataWriter
from data_fetcher import DataFetcher
import time
import logging
from utilities import seconds_to_next_minute

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.log',
                    encoding='utf-8',
                    level=logging.DEBUG)

COM_NUMBER = input("Číslo Com Port-u:")

fetcher = DataFetcher("com" + COM_NUMBER)
writer = DataWriter(fetcher)

while True:
    if seconds_to_next_minute() <= 1.2:
        time.sleep(2)
        points = fetcher.get_points()
        was_successful = writer.write_points(points)
        if not was_successful:
            logging.warning("Zápis do databázy zlyhal.")
            raise Exception("Writing to database was not successful")
        else:
            logging.info("Meranie bolo úspešne zapísané do dazabázy.")

    time.sleep(seconds_to_next_minute())
