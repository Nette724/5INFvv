Bedrag = float(input("geef het bedrag in: "))
bronvaluta = input("geef de bronvaluta in (EUR, USD): ").strip().upper()

if bronvaluta == "EUR":
    doelvaluta = "USD"
    resultaat = Bedrag * 1.1
if bronvaluta == "USD":
    doelvaluta = "EUR"
    resultaat = Bedrag / 1.1

    print(f"{Bedrag:.2f} {bronvaluta} is gelijk aan {resultaat:.2f} {doelvaluta}.")

