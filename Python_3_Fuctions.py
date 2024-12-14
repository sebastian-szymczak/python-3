def f(liczba1=3, liczba2=2, operator="+", *args, **kwargs):
    '''

    Opis co robi funkcja
 
    Parameters
    ----------
        liczba1: typ
            Opis parametru
 
        liczba2: typ
            Opis parametru
 
        operator: typ
            Opis parametru
 
        *args: typ
            Opis parametru
 
        **kwargs: typ
            Opis parametru
 
    Returns
    -------
        typ zwracany
            Opis
 
    '''
    # print(args)
    # print(kwargs)
    wynik = "Nieznany operator"
    if operator == '+':
        wynik = liczba1 + liczba2
    elif operator == '-':
        wynik = liczba1 - liczba2
    elif operator == '*':
        wynik = liczba1 * liczba2
    elif operator == '/':
        wynik = liczba1 / liczba2
   
    return wynik, args, kwargs

 
print(f(1))
print(f(99, 2, '-'))
print(f(9.102, 4.2312, '*'))
print(f('99', '2'))
print(f())
print(f(operator='*'))
print(f(operator='/', liczba1=5, liczba2=10))
print(f(10, operator='/'))
print(f(9.102, 4.2312, '*', 0, 1, 2, 3))
print(f(9.102, 4.2312, '*', 0, 1, 2, 3, liczba3=10))
print(f(9.102, 4.2312, '*', 0, 1, 2, 3, [1, 2, 3], liczba3=10))
 
wynik = f()
print(wynik[0])

