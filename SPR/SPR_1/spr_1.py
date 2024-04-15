# Metoda matoda trapezów

def TrapezF(a, b, n):
    def f(x):
        return -x**3 + 2 * x**2 + x
     
    dx = (b - a) / 2
    suma = 0

    for i in range(n):
        suma += ((f(a + dx * i) + f(a + dx * i + dx)) * dx) / 2
    
    return suma

def TrapezG(a, b, n):
    def g(x):
        return -x**3 + 2 * x**2 + x + 1
       
    dx = (b - a) / 2
    suma = 0

    for i in range(n):
        suma += ((g(a + dx * i) + g(a + dx * i + dx)) * dx) / 2
    
    return suma

def Worki(powierzchnia_dzialki):
    worek = 5
    kilogramy_jednego_worka = 5**2

    kilogramy = powierzchnia_dzialek / kilogramy_jednego_worka
    ile_workow = kilogramy / worek

    return ile_workow

dzialkaF = TrapezF(0, 2, 19)
dzialkaG = TrapezG(0, 2, 19)

powierzchnia_dzialek = dzialkaF + dzialkaG
print(f"1. Dolna część: {dzialkaF}")
print(f"2. Górna część: {dzialkaG}")
print(f"3. Pod rzeką powierzchnia dziłki wynosi: {dzialkaF}")
print(f"4. Trzeba {Worki(powierzchnia_dzialek)} worków.")
