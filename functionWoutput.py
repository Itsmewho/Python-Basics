# AKA the return funciton

def format_name(f_name, l_name):
    name = f_name.title()
    return f"{name}"
name = format_name("jordy","jordy")

#For now it seems to overcomplicate things
#But, for bigger projects you can write functions, place them in an other folder, with the structure:
# -main.py
#   -childeren.py
#       -silbings.py
#           -granny.py ?
# Guess here come's the practicality of OOP.

print(name)