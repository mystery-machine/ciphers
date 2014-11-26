from random import seed, random
import fractions
from math import ceil

def caesar(text, key, inp):
        #"a" is the same as 97. "z" is 122.
        
        
    encrypted = ""
    for i in range(len(text)):
        
        if inp == "D":
            key = key * -1
        if text[i] == " ":
            encrypted += " "
        else:
            originalNum = ord(text[i]) - 97
            
            encryptedNum = (originalNum + key) % 26
            
            encrypted += chr(encryptedNum + 97)



    return encrypted

def vigenere(text, key, inp):

    #this can both decrypt and encrypt!!

    j = 0

    encrypted = ""

    while j < len(text):
        for i in range(len(key)):
            try:
                keynum = ord(key[i]) - 97
                #print(keynum)

                encrypted += caesar(text[j], keynum, inp)
                j+=1
            except IndexError:
                j +=1
                break
            

    print(encrypted)
    return encrypted

def atbash(text):
    #I think this can both encrypt and decrypt at the same time (or, it should).
    encrypted = ""
    #"a" is the same as 97. "z" is 122.
    for i in range(len(text)):
        if text[i] == " ":
            encrypted += " "
        else:
            letnum = ord(text[i]) - 97 #a is 0, z is 25
            encrypted += chr(((letnum - 25) * -1) + 97)

    print(encrypted)
    return encrypted


def a1z26En(text):
    encrypted = ""
    for i in range(len(text)):
        if text[i] == " ":
            encrypted += " "
        else:
            try:
                if text[i+1] == " ":
                    
                    encrypted += str((ord(text[i]) - 96)) 
                else:
                    encrypted += str((ord(text[i]) - 96)) + "-"
            except IndexError:
                encrypted += str((ord(text[i]) - 96)) 

    print(encrypted)
    return encrypted

def a1z26De(text):
    decrypted = ""
    words = text.split(" ")
    for i in range(len(words)):
        letters = words[i].split("-")
        for i in range(len(letters)):
            decrypted += chr(int(letters[i]) + 96)
        decrypted += " "

    print(decrypted)
    return decrypted


#ENIGMA START

def increment(password, j):

    #used in
        
        
    if password[j] < 25:
        password[j] +=1
    else:
        password[j] = 0
        j += 1
        increment(password, j)
    return
        
                                 

def enigma(text, password, inp):
    encrypted = ""
    
            
    for i in range(len(text)):
        if text[i] == " ":
            encrypted += " "
        temp = text[i]
        for j in range(len(pass_list)):
            temp = caesar(temp, password[j], inp)
                    
        encrypted += temp
        increment(password, 0)
        #print(password)

    print(encrypted)

#RSA START    

def rsaEn(p, q, text):
    n = p*q
    phi = (p-1)*(q-1)
    e = 0
    d = 0
    while d == 0 or d == e:
        e = ceil(random()*phi)
        if fractions.gcd(e, phi) == 1:
            
    
            for j in range(2, phi):
                if (j*e)%phi == 1:
                    d = j
                    break
                else:
                    d = 0
                    

    print(d, end = " ")
    
    print(n)

    encrypted = ""

    for i in range(len(text)):
        num = ord(text[i]) - 97
        c = (num**e)%n
        
        encrypted += str(c) + "-"

    print(encrypted)

def rsaDe(d, n, text):
    decrypted = ""
    textlist = text.split("-")
    for i in range(len(textlist)):
        m = (int(textlist[i]) ** d)%n
        decrypted += chr(m + 97)

    print(decrypted)
