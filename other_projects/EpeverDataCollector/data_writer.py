import influxdb_client
import os
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class DataWriter:
    def __init__(self):
        self.token = os.environ.get("INFLUXDB_TOKEN")
        self.org = "EpeverData"
        self.url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
        self.bucket = "EpeverData"
        self.write_client = InfluxDBClient(url=self.url, token=self.token, org=self.org)

        # Define the write api
        self.write_api = self.write_client.write_api(write_options=SYNCHRONOUS)

        self.data = {
            "point1": {
                "location": "Klamath",
                "species": "bees",
                "count": 23,
            },
            "point2": {
                "location": "Portland",
                "species": "ants",
                "count": 30,
            },
            "point3": {
                "location": "Klamath",
                "species": "bees",
                "count": 28,
            },
            "point4": {
                "location": "Portland",
                "species": "ants",
                "count": 32,
            },
            "point5": {
                "location": "Klamath",
                "species": "bees",
                "count": 29,
            },
            "point6": {
                "location": "Portland",
                "species": "ants",
                "count": 40,
            },
        }

        for key in self.data:
            point = (
                Point("census")
                .tag("location", self.data[key]["location"])
                .field(self.data[key]["species"], self.data[key]["count"])
            )
            self.write_api.write(bucket=self.bucket, org=self.org, record=point)
            time.sleep(1)  # separate points by 1 second

        print("Complete. Return to the InfluxDB UI.")
