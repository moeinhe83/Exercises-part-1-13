# Practice_13

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 13', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lang = ('python', 'javascript', 'java', 'c#', 'c++')

# Work On Values
print(max(number))
print(min(number))
print(max(lang, key=len))
print(min(lang, key=len))

# Finish
# Create By Moein Heshmati
