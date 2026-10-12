voornaam = input("Wat is je voornaam: ")
achternaam = input("Wat is je achternaam: ")
functietitel = input("Wat is functietitel: ")

naam = (f"{voornaam} {achternaam}").upper()
naamlengte = naam.__len__() + 10
print(naam)

print(f"+{"-" * naamlengte}+")
print(f"|{naam:^{naamlengte}}|")
print(f"|{functietitel:^{naamlengte}}|")
print(f"+{"-" * naamlengte}+")