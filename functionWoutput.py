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
#--  Think about it like the stucture of the brain with its neurons and glia-neuros and the parts of the brain the prefontal for rational, 
#--  hyppocampus for read an write to the cerbrum to update all the functions.
#-- Dont think aabout it to mutch, or you'll start to explore the function of emotions them self? (management problems lol)
# -- ect, ect,

print(name)