# ==========================================
# Python OOP Assessment: Smart Home System
# Concepts: Classes, Inheritance, Polymorphism
# ==========================================

class SmartDevice:
    def __init__(self, device_name, location):
        self.device_name = device_name
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"[{self.location}] {self.device_name} is now TURNED ON.")

    def turn_off(self):
        self.is_on = False
        print(f"[{self.location}] {self.device_name} is now TURNED OFF.")

    def status(self):
        state = "On" if self.is_on else "Off"
        print(f"Device: {self.device_name} | Location: {self.location} | Status: {state}")


# Inheritance & Polymorphism: SmartLight overrides status
class SmartLight(SmartDevice):
    def __init__(self, device_name, location, brightness=100):
        super().__init__(device_name, location)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        print(f"[{self.location}] {self.device_name} brightness set to {self.brightness}%")

    def status(self):
        state = "On" if self.is_on else "Off"
        print(f"Smart Light: {self.device_name} | Location: {self.location} | Status: {state} | Brightness: {self.brightness}%")


# Inheritance: SmartThermostat 
class SmartThermostat(SmartDevice):
    def __init__(self, device_name, location, target_temp=22):
        super().__init__(device_name, location)
        self.target_temp = target_temp

    def set_temperature(self, temp):
        self.target_temp = temp
        print(f"[{self.location}] {self.device_name} target temperature set to {self.target_temp}°C")


if __name__ == "__main__":
    print("--- Smart Home Automation OOP Demo ---")
    
    # Creating unique objects
    living_room_light = SmartLight("Living Room Main Light", "Living Room", 80)
    bedroom_thermostat = SmartThermostat("AC Unit", "Bedroom", 21)

    # Testing functionality
    living_room_light.turn_on()
    living_room_light.set_brightness(50)
    living_room_light.status()

    print("-" * 40)

    bedroom_thermostat.turn_on()
    bedroom_thermostat.set_temperature(19)
    bedroom_thermostat.status()