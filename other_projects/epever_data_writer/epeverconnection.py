# ako si postaviť vlastný epever kábel pre linux:
# https://ross-warren.co.uk/2021/08/14/building-a-cable-to-connect-my-epever-charge-controller/

from epevermodbus.driver import EpeverChargeController

class EpeverConnection:

    def __init__(self, com_port):
            self.c = EpeverChargeController(com_port, 1)

    def get_values(self):
        data = {
                    "solar_voltage": self.c.get_solar_voltage(),
                    "solar_current": self.c.get_solar_current(),
                    "solar_power": self.c.get_solar_power(),
                    "load_voltage": self.c.get_load_voltage(),
                    "load_current": self.c.get_load_current(),
                    "load_power": self.c.get_load_power(),
                    "battery_current": self.c.get_battery_current(),
                    "battery_voltage": self.c.get_battery_voltage(),
                    "battery_state_of_charge": self.c.get_battery_state_of_charge(),
                    "battery_temperature": self.c.get_battery_temperature(),
                    "remote_battery_temperature": self.c.get_remote_battery_temperature(),
                    "controller_temperature": self.c.get_controller_temperature(),
                    "day_time": self.c.is_day(),
                    "night_time": self.c.is_night(),
                    "maximum_battery_voltage_today": self.c.get_maximum_battery_voltage_today(),
                    "minimum_battery_voltage_today": self.c.get_minimum_battery_voltage_today(),
                    "device_over_temperature": self.c.is_device_over_temperature(),
                    "rated_charging_current": self.c.get_rated_charging_current(),
                    "rated_load_current": self.c.get_load_current(),
                    "battery_real_rated_voltage": self.c.get_battery_real_rated_voltage(),
                    "battery_type": self.c.get_battery_type(),
                    "battery_capacity": self.c.get_battery_capacity(),
                    "temperature_compensation_coefficient": self.c.get_temperature_compensation_coefficient(),
                    "over_voltage_disconnect_voltage": self.c.get_over_voltage_disconnect_voltage(),
                    "charging_limit_voltage": self.c.get_charging_limit_voltage(),
                    "over_voltage_reconnect_voltage": self.c.get_over_voltage_reconnect_voltage(),
                    "equalize_charging_voltage": self.c.get_equalize_charging_voltage(),
                    "boost_charging_voltage": self.c.get_boost_charging_voltage(),
                    "float_charging_voltage": self.c.get_float_charging_voltage(),
                    "boost_reconnect_charging_voltage": self.c.get_boost_reconnect_charging_voltage(),
                    "low_voltage_reconnect_voltage": self.c.get_low_voltage_reconnect_voltage(),
                    "under_voltage_recover_voltage": self.c.get_under_voltage_recover_voltage(),
                    "under_voltage_warning_voltage": self.c.get_under_voltage_warning_voltage(),
                    "low_voltage_disconnect_voltage": self.c.get_low_voltage_disconnect_voltage(),
                    "discharging_limit_voltage": self.c.get_discharging_limit_voltage(),
                    "battery_rated_voltage": self.c.get_battery_rated_voltage(),
                    "default_load_on_off_in_manual_mode": self.c.get_default_load_on_off_in_manual_mode(),
                    "equalize_duration": self.c.get_equalize_duration(),
                    "boost_duration": self.c.get_boost_duration(),
                    "battery_discharge": self.c.get_battery_discharge(),
                    "battery_charge": self.c.get_battery_charge(),
                    "charging_mode": self.c.get_charging_mode()
                }

        # Remove unwanted spaces from data keys
        data = {k.replace(" ", ""): v for k, v in data.items()}
        return data

    def get_statuses(self):
        status = {
            "battery_status": self.c.get_battery_status(),
            "charging_equipment_status": self.c.get_charging_equipment_status(),
            "discharging_equipment_status": self.c.get_discharging_equipment_status()
        }
        status = {k.replace(" ", ""): v for k, v in status.items()}
        return status