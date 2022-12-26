from machine import Pin
import time, math

class BinaryLED():
    
    def __init__(self):
        self.pins = [16, 17, 18, 19, 20, 21, 22, 26, 27 ,28]
        self.bit_values = [math.pow(2,(x)) for x in range(len(self.pins))]
        self.show_pins = []
        
    def max_bit_value(self):
        return int(max(self.bit_values))
        

    def clear_LEDs(self) -> None:
        for pin in self.pins:
            led = Pin(pin, Pin.OUT)
            led.value(0)
            
    
    def calculate(self, number) -> list[int]:
        if number in self.bit_values:
            return [self.pins[self.bit_values.index(number)]]
        
        for bit_value in reversed(self.bit_values):
            if number >= bit_value:            
                number -= bit_value
                pin_index = self.bit_values.index(bit_value)
                self.show_pins.append(self.pins[pin_index])
            if number <= 0:
                return self.show_pins
        

    def display_pins(self, show_pins) -> None:
        for pin in show_pins:
            led = Pin(pin, Pin.OUT)
            led.value(1)
        time.sleep(10)
        self.clear_LEDs()
        
        
def main():
    binaryLED = BinaryLED()
    binaryLED.clear_LEDs()
    show_pins = binaryLED.calculate(int(input(f"Enter number 0 - {binaryLED.max_bit_value()}: ")))
    binaryLED.display_pins(show_pins)
    
    
if __name__ == "__main__":
    main()
