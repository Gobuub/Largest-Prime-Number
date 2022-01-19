def is_prime(n):
    '''
        This funciton takes a number and check if it is prime or not
        
        Parameters.
        -----------
        
        An integer
        
        Returns.
        ---------
        
        1 if n is prime or less than 1
        0 if n is not a prime number
    '''
    x = 2
    if n <= 1:
        return 1
    else:
        while (x * x) <= n:
            if n%x==0:
                return 0
            x = x + 1
        return 1

def prime_factor(n):
    '''
        This function extract the factors of an integer and store it in a list if it is a prime number
        
    Parameters.
    -----------
        Function must receive a positive integer
    
    Returns.
    --------
        If n is a negative integer returns a message saying that number is incorrect.
        If n is a positive integer returns the largest prime factor of n.
    '''
    prime_factors = []
    if n < 0:
        return (f'{n} es un número negativo y no puede tener factorial primo')
    else:
        i = 2 
        num = n
        while i*i<=n:
            
            prime = is_prime(i)

            if prime == 1 and num%i==0:
    
                num = num/i
              
                prime_factors.append(i)
            
                if num%i == 0:
                   
                    while num%i == 0:
                        num = num/i
                else:
                    
                    num = round(num*i)
                    
                    i+=1
            else:
                i+=1
    #print(prime_factors)
                
    return print(f'{prime_factors[-1]} es el factorial primo mas alto de {n}')
                        