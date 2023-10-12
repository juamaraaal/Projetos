#Celcius
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)

print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)
print("A temperatura em Kelvin é:", temperatura_kelvin)

#Kelvin
def kelvin_para_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def kelvin_para_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

temperatura_kelvin = float(input("Digite a temperatura em Kelvin: "))

temperatura_fahrenheit = kelvin_para_fahrenheit(temperatura_kelvin)
temperatura_celsius = kelvin_para_celsius(temperatura_kelvin)

print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)
print("A temperatura em graus Celsius é:", temperatura_celsius)

#Fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_para_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return kelvin

temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
temperatura_kelvin = fahrenheit_para_kelvin(temperatura_fahrenheit)

print("A temperatura em graus Celsius é:", temperatura_celsius)
print("A temperatura em Kelvin é:", temperatura_kelvin)