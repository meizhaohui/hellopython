#Filename:locals_globals.py
LOVE_LANG = 'Python'
def change_lang():
    author = 'Guido van Rossum'
    print('locals_in_function:', locals())
    global LOVE_LANG
    LOVE_LANG = 'GO'
    print('globals_in_function:', globals())

print('locals_before:', locals())
print('globals_before:', globals())
change_lang()
print('locals_after:', locals())
print('globals_after:', globals())

