from colorama import init, Fore, Style
init(autoreset=True)  # don't need to reset styles manually

str = "Hello Buddy!"
str2 = "Hello Sanjay!"

print(f"{Fore.RED} Length of string: {len(str)}")
print("Check is Hello:","Hello" not in str) 

print("Slice 0 to 5:",str[0:5])

print(f"UpperCase: {str.upper()}")
print(f"LowerCase: {str.lower()}")
print(f"Capitalize: {str.capitalize()}")

print(f"Title Case: {str.title()}")
print(f"Swap Case: {str.swapcase()}")

print(f"Count of 'o': {str.count('o')}")
print(f"Find 'Buddy': {str.find('Buddy')}")

print(f"Concatenate: {str}, {str2}")