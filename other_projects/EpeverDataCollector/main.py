import reader as reader
from flightsql import FlightSQLClient
from influxdb_client import InfluxDBClient
import os

token = os.environ.get("INFLUXDB_TOKEN")
org = "EpeverData"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"
bucket = "EpeverData"
influx_client = InfluxDBClient(url=url, token=token, org=org)

query = "from(bucket: \"" + bucket + "\") |> range(start: -48h)"

result = influx_client.query_api().query(query)
for record in result[0]:
    print(record.get_value())
