from numpy import sqrt
def isprime(n):
    """Checking if the entering number is prime."""
    if n==0:
        return False
    elif n==1:
        return False
    else:
        n_new = sqrt(n)//1
        for i in range(2,int(n_new)+1):
            if n%i==0:
                return False
        return True