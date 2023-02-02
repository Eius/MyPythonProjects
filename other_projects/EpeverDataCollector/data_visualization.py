import influxdb_client
from influxdb_client import WritePrecision
from flightsql import FlightSQLClient
import os


class DataVisualization:
    def __init__(self):
        self.query = """SELECT *
        FROM 'census'
        WHERE time >= now() - interval '24 hours'
        AND ('bees' IS NOT NULL OR 'ants' IS NOT NULL)"""

        # Define the query client
        self.query_client = FlightSQLClient(
            host="eu-central-1-1.aws.cloud2.influxdata.com",
            token=os.environ.get("INFLUXDB_TOKEN"),
            metadata={"bucket-name": "EpeverData"})

        # Execute the query
        self.info = self.query_client.execute(self.query)
        self.reader = self.query_client.do_get(self.info.endpoints[0].ticket)

        # Convert to dataframe
        self.data = self.reader.read_all()
        self.df = self.data.to_pandas().sort_values(by="time")
        print(self.df)