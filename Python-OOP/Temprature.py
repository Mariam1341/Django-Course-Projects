class Temprature:
    celsius = 0
    fahrenheit = 0
    def convertFahrenheit(self,celsius):
        return (self.celsius * 1.8) + 32

    def convertCelsius(self,fahrenheit):
        return (self.fahrenheit - 32) / 1.8

temp = Temprature()
print(temp.convertFahrenheit(100))
print(temp.convertCelsius(100))