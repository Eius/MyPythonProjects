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
            .tag("location", str(self.location))
            .field("Solar voltage", float(self.get_solar_voltage()))
            .field("Solar current", float(self.get_solar_current()))
            .field("Solar power", float(self.get_solar_power()))
            .time(datetime.utcnow()),
            # Measurement 2
            Point("load_status")
            .tag("location", str(self.location))
            .field("Load voltage", float(self.get_load_voltage()))
            .field("Load current", float(self.get_load_current()))
            .field("Load power", float(self.get_load_power()))
            .time(datetime.utcnow()),
            # Measurement 3
            Point("battery_status")
            .tag("location", str(self.location))
            .field("Battery voltage", float(self.get_battery_voltage()))
            .field("Battery current", float(self.get_battery_current()))
            .field("Battery power", float(self.get_battery_power()))
            .field("Battery state of charge", int(self.get_battery_state_of_charge()))
            .field("Battery temperature", float(self.get_battery_temperature()))
            .field("Maximum battery voltage today", float(self.get_maximum_battery_voltage_today()))
            .field("Minimum battery voltage today", float(self.get_minimum_battery_voltage_today()))
            .time(datetime.utcnow()),
            # Measurement 4
            Point("controller_status")
            .tag("location", str(self.location))
            .tag("Over temperature", str(self.is_device_over_temperature()))
            .field("Controller temperature", float(self.get_controller_temperature()))
            .field("Charging mode", str(self.get_charging_mode()))
            .time(datetime.utcnow()),
        ]
        print(f"Solar voltage: {float(self.get_solar_voltage())}")
        print(f"Solar voltage: {float(self.get_solar_current())}")
        print(f"Solar voltage: {float(self.get_solar_power())}")

        print(f"Load voltage: {float(self.get_load_voltage())}")
        print(f"Load current: {float(self.get_load_current())}")
        print(f"Load power: {float(self.get_load_power())}")

        print(f"Battery voltage: {float(self.get_battery_voltage())}")
        print(f"Battery current: {float(self.get_battery_current())}")
        print(f"Battery power: {float(self.get_battery_power())}")

        print(f"Is device over temperature: {str(self.is_device_over_temperature())}")
        print(f"Controller temperature: {int(self.get_controller_temperature())}")
        print(f"Charging mode: {str(self.get_charging_mode())}")
        return points
