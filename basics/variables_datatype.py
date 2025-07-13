
import colorama
import random
from colorama import init, Fore, Style
init(autoreset=True)  # Automatically reset styles after each print

print(f"{Fore.MAGENTA}---- Variable & DataType -----")

x = 5
y = "Sanjay"
z = True

print(f"{Fore.LIGHTBLUE_EX}x = {x}, y = {y}, z = {z}")
print(f"{Fore.YELLOW}Type of x {type(x)}")
print(f"{Fore.GREEN}Type of y {type(y)}")
print(f"{Fore.CYAN}Type of z {type(z)}")

# Complex numbers are useful in scientific and engineering calculations.
varComplex = 1j + 3 + 2j
print(f"{Fore.MAGENTA}Complex number: {varComplex}")
print(f"{Fore.LIGHTMAGENTA_EX}Real part: {varComplex.real}")
print(f"{Fore.LIGHTCYAN_EX}Imaginary part: {varComplex.imag}") 

print(f"{Fore.MAGENTA}---- Type Conversion (Casting) -----")

print(f"{Fore.RED} Converting z to int: {int(z)}")
print(f"{Fore.BLUE} Converting x to string: {str(x)}")
print(f"{Fore.LIGHTGREEN_EX} Converting y to boolean: {bool(y)}")

print(f"{Fore.MAGENTA}---- Generate Random Numbers -----")

random_range = random.randrange(1000, 9999) # can't include 9999
print(f"{Fore.LIGHTYELLOW_EX}Random number between 1000 and 9999: {random_range}")

random_number = random.randint(1000, 9999) # can include both endpoints
print(f"{Fore.LIGHTCYAN_EX}Random integer between 1000 and 9999: {random_number}")