from epevermodbus.driver import EpeverChargeController
from influxdb_client import Point
from datetime import datetime
from typing import List


class DataFetcher(EpeverChargeController):
    def __init__(self, com_port):
        super().__init__(com_port, 1)
        self.location = "Garage"

    def get_points(self) -> List[Point]:
        points = [
            # Measurement 1
            Point("solar_status")
            .tag("location", self.location)
            .field("Solar voltage", self.get_solar_voltage())
            .field("Solar current", self.get_solar_current())
            .field("Solar power", self.get_solar_power())
            .time(datetime.utcnow()),
            # Measurement 2
            Point("load_status")
            .tag("location", self.location)
            .field("Load voltage", self.get_load_voltage())
            .field("Load current", self.get_load_current())
            .field("Load power", self.get_load_power())
            .time(datetime.utcnow()),
            # Measurement 3
            Point("battery_status")
            .tag("location", self.location)
            .field("Battery voltage", self.get_battery_voltage())
            .field("Battery current", self.get_battery_current())
            .field("Battery power", self.get_battery_power())
            .field("Battery state of charge", self.get_battery_state_of_charge())
            .field("Battery temperature", self.get_battery_temperature())
            .field("Maximum battery voltage today", self.get_maximum_battery_voltage_today())
            .field("Minimum battery voltage today", self.get_minimum_battery_voltage_today())
            .time(datetime.utcnow()),
            # Measurement 4
            Point("controller_status")
            .tag("location", self.location)
            .field("Controller temperature", self.get_controller_temperature())
            .field("Device over temperature", self.is_device_over_temperature())
            .field("Charging mode", self.get_charging_mode())
            .time(datetime.utcnow()),
        ]
        return points
