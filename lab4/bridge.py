class Device:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        return "Телевизор включен"
    
    def turn_off(self):
        return "Телевизор выключен"

class Radio(Device):
    def turn_on(self):
        return "Радио включено"
    
    def turn_off(self):
        return "Радио выключено"

class Remote:
    def __init__(self, device):
        self.device = device
    
    def power(self):
        pass

class BasicRemote(Remote):
    def power(self):
        return self.device.turn_on()

class AdvancedRemote(Remote):
    def power(self):
        return self.device.turn_on() + " на полной громкости"

if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    basic = BasicRemote(tv)
    print(basic.power())
    
    advanced = AdvancedRemote(radio)
    print(advanced.power())
