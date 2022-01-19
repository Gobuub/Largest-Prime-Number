from src.functions import prime_factor as pf
from src.functions import is_prime

if __name__ == "__main__":
    print('Bienvenido Largest Prime Number Calculator')
    
    n= int(input('Introduce un número mayor que 0: \n'))
    
    pf(n)