import re

phones = [
    '800-555-1212',
    '800 555 1212',
    '800.555.1212',
    '(800) 555-1212',
    '1-800-555-1212',
    '800-555-1212-1234',
    '800555+1212 1234',    
    '800-555-1212x1234',
    '800-555-1212 ext. 1234',
    'work 1-(800) 555.1212 #1234'
]

phonePattern = re.compile(r'''
    # cislo muze začít kdekoliv
    (\d{3}) # cislo oblasti napr '800'
    \D*
    (\d{3}) #hlavní linka
    \D* # nepovinný oddělovač 
    (\d{4}) # zbytek čísla
    \D* #nepovinný oddělovač
    (\d*) #nepovinna klapka
    $ #konec retezce
    ''', re.VERBOSE) #VERBOSE možnost okecat regulární výraz

clearPhones = [phonePattern.search(x).groups()  for  x in phones]
norPhone = [ a +'-'+ b +'-'+ c + ('-' + d if d != '' else '')   for a, b, c, d in clearPhones]
clearPhones
norPhone
