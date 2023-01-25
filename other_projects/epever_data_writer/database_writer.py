import sqlite3
from datetime import datetime

class DatabaseWriter:
    def __init__(self):
        # Connect to sqlite3
        self._conn = sqlite3.connect("epever_logs.db")
        self._cursor = self._conn.cursor()

        # Get current date and time
        now = datetime.now()
        self._current_time = now.strftime('%d-%m-%Y %H:%M:%S')
    
    def __write_data_to_table(self, data):
        columns = ', '.join(data.keys())
        d_values = ', '.join('?' * len(data))
        query = f'INSERT INTO epever_data ({columns}, time) VALUES({d_values}, ?)'
        self._cursor.execute(query, (*data.values(), self._current_time))

    def __write_statuses_to_table(self, statuses):
        for status_group in statuses:
            columns = ', '.join(statuses[status_group].keys())
            d_values = ', '.join('?' * len(statuses[status_group]))
            query = f'INSERT INTO {status_group} ({columns}, time) VALUES({d_values}, ?)'
            self._cursor.execute(query, (*statuses[status_group].values(), self._current_time))

    def write_to_database(self, data, statuses):
        self.__write_data_to_table(data)
        self.__write_statuses_to_table(statuses)

        # Save the changes
        self._conn.commit()

    def finish(self):
        # Save the changes
        self._conn.commit()

        # Close the connection
        self._conn.close()

