FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temperature = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if scale == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C")
    elif scale == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F")
    else:
        print("Invalid temperature")


if __name__ == "__main__":
    main()
