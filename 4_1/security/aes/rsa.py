import random
import sympy
import time


def check_prime(val):
    
    if val <= 3:
        return True
    elif val % 2 == 0 or val % 3 == 0:
        return False
    
    i = 5
    while i ** 2 <= val:
        if val % i == 0 or val % (i + 2) == 0:
            return False
        i += 6
        
    return True

def generate_prime(bit_size):
    
    min_value = 2 ** ( bit_size - 1 )
    max_value = 2 ** ( bit_size ) - 1
    prime = min_value
    
    while not check_prime(prime):
        prime = random.randint(min_value, max_value)
    
    return prime

def generate_distinct_primes(bit_size):
    
    p = generate_prime(bit_size // 2)
    q = generate_prime(bit_size // 2)

    if p == q:
        return generate_distinct_primes(bit_size)

    return (p,q)

def GCD(x, y):
    while(y):
        x = y
        y = x % y

    return abs(x)

def generate_keypair(bit_size):
    
    p, q = generate_distinct_primes(bit_size)    

    n = p * q

    phi_n = (p - 1) * (q - 1)

    min_e = 2 ** (bit_size // 2 - 1)
    max_e = 2 ** (bit_size // 2)
    
    e = random.randint(min_e, max_e)
    
    while e % phi_n == 0 or not GCD(e, phi_n) == 1:
        e = random.randint(min_e, max_e)

    d = pow( e, -1, phi_n )

    public_key = [ e, n ]
    private_key = [ d, n ]

    return public_key, private_key


def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = []
    for char in plaintext:
        ciphertext.append( pow(ord(char), e, n) )

    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ""
    for char in ciphertext:
        plaintext += chr(pow(char, d, n))

    return plaintext
