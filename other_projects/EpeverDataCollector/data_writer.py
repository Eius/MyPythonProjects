import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS, WritePrecision
from data_fetcher import DataFetcher
from typing import List

class DataWriter:
    def __init__(self, data_fetcher: DataFetcher):
        self.data_fetcher = data_fetcher
        self.token = os.environ.get("INFLUXDB_TOKEN")
        self.org = "EpeverData"
        self.url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
        self.bucket = "Epever_Data"
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_client = self.client.write_api(write_options=SYNCHRONOUS)

    def write_points(self, points: List[Point]) -> bool:
        response = self.write_client.write(bucket=self.bucket, record=points, write_precision=WritePrecision.S)
        if response is None:
            return True
        else:
            return False
