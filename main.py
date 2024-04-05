wymyslone_a = 10.4

def pole(bok_a):
    return bok_a*bok_a

print(pole(wymyslone_a))


wymyslone_b = 8.2

def poleprost(bok_a,bok_b):
    return bok_a*bok_b

print(poleprost(wymyslone_a,wymyslone_b))

print(pole(5))

# NA NASTEPNE ZAJECIA ZNAJOMOSC SKLADNI MARKDOWNA
# JAK PISAC DOKUMENTACJE NA REPOZYTORIA

def oblicz_pole_trojkata_podstawa_wysokosc(a, h):
    pole = 0.5 * a * h
    return pole

# Przykładowe długości podstawy i wysokości trójkąta
a = 5
h = 8

pole = oblicz_pole_trojkata_podstawa_wysokosc(a, h)
print("Pole trójkąta o podstawie długości", a, "i wysokości", h, "wynosi:", pole)