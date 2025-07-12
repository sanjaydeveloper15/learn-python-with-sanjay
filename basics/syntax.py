from colorama import init, Fore, Style
init(autoreset=True) # don't need to reset styles manually

print(Fore.RED + "Hello from Python Syntax!")
print(Fore.CYAN + "This is a basic syntax example.")
print(Fore.LIGHTGREEN_EX + "Let's explore some basic operations:")   

print(f"{Fore.WHITE}Python Strings")
print(f"{Fore.MAGENTA}---- 1. Python Indentation -----")
print(F"{Fore.LIGHTCYAN_EX}Indentation is crucial in Python. It defines the blocks of code.")

if 5 < 2:
    print(f"{Fore.GREEN}5 is greater than 2")
else:
    print(f"{Fore.YELLOW}5 is not greater than 2")

print(f"{Fore.MAGENTA}---- 2. Python Semicolon ; -----")
print(f"{Fore.LIGHTMAGENTA_EX}Hello"); print(f"{Fore.LIGHTYELLOW_EX}Sanjay!");

print(f"{Fore.MAGENTA}---- 3. Python Variables -----")

x: int = 5 #if I define string value then it will also work, but it is not good practice
print(f"{Fore.LIGHTGREEN_EX}x = {x}")
# Type hinting is optional but recommended for better code clarity
y: str = "Sanjay" # doesn't need type hinting, but it's good practice
z: float = 3.14
is_active: bool = True  
print(f"{Fore.LIGHTBLUE_EX}x = {x}, y = {y}")