from minimalmodbus import NoResponseError
from epeverconnection import EpeverConnection
from database_writer import DatabaseWriter
import time
import logging

# Database update interval in seconds
UPDATE_INTERVAL = 5

# Create empty object for epeverconnection
connection = None

# Create new DatabaseWriter
db_writer = DatabaseWriter()

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename='logs.log',
                    encoding='utf-8',
                    level=logging.DEBUG)

while True:
    try:
        # If epever connection is not set, try to connect
        if connection is None:

            # Input the name of com port the epever cable is using
            com_port = "com" + input("Input the number of COM PORT: ")

            # Connect to epever device
            connection = EpeverConnection(com_port)
            print("Data cable was recognized...")
            logging.info("Data cable was recognized.")
            continue

        else:
            # Get values and battery/equipment statuses from epever device
            data = connection.get_values()
            statuses = connection.get_statuses()
            print("Data tranfer from epever device was successful...")
            logging.info("Data tranfer from epever device was successful.")

            # Write values to database
            db_writer.write_to_database(data, statuses)
            print("Data was successfully added to database...")
            logging.info("Data was successfully added to database.")

        # Extract data every 60 seconds
        time.sleep(UPDATE_INTERVAL)

    except NoResponseError:
        print("No communication with the device (no answer). "
              "Check your connection to the epever device and try again.")
        logging.critical(f"Exception: NoResponseError. No data was received from the epever device!")
        connection = None
        continue

    except WindowsError:
        print("Data cable was not recognized. Check your number of COM PORT and try again.")
        logging.critical(f"Exception: WindowsError. Data cable was not recognized!")
        connection = None
        continue

    except KeyboardInterrupt:
        print("\nExiting program...")
        logging.warning("Program was terminated.")
        break

db_writer.finish()
exit()
