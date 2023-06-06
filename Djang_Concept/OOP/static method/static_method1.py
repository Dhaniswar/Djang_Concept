class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9

fahrenheit = TemperatureConverter.celsius_to_fahrenheit(100)
print(fahrenheit)

celsius = TemperatureConverter.fahrenheit_to_celsius(180)
print(celsius)

