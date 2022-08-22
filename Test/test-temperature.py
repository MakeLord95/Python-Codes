fahrenheit_str = input("Syötä lämpötila Fahrenheit arvoina: ")
fahrenheit = float(fahrenheit_str)

celsius = (fahrenheit - 32) * 5 / 9

print("Lämpötila Celsius arvoina: " + str(celsius))

print(f"Lämpötila Celsius arvoina:  {celsius:6.2f}")
