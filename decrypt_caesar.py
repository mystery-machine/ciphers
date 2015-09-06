#you have to call this with python3.

def caesar(text, key, inp):
    #"a" is the same as 97. "z" is 122.
    #"A" is 65 "Z" is 90.
        
        
    encrypted = ""
    if inp == "D":
        key = key * -1
    for i in range(len(text)):
        
        
        if not text[i].isalpha():
            encrypted += text[i]
        elif text[i].isupper():

            originalNum = ord(text[i]) - 65
            
            encryptedNum = (originalNum + key) % 26
            
            encrypted += chr(encryptedNum + 65)


        elif text[i].islower():
            originalNum = ord(text[i]) - 97
            
            encryptedNum = (originalNum + key) % 26
            
            encrypted += chr(encryptedNum + 97)



    return encrypted

#DECRYPTION

entext = open("/home/gftext.txt", "r") #here's where you put the file you want to decrypt
#just put an input thing here so that you can choose any file you want

print(entext.readline())
entext.seek(0)

def decrypt(file):
    temp = file
    
    stats = ["e", "t", "a", "o", "i", "n", "s"]
    text = file.read()
    occ = {}
    for i in range(26):
        occ[chr(i + 97)] = 0

    for i in range(len(text)):
        
        if text[i].islower() or text[i].isupper():
            
            occ[text[i].lower()] += 1

    for i in range(26):
        print(chr(i + 97) + ": " + str(occ[chr(i+97)]))

    #getting the letter with the maximum value
    maxletter = ["", 0]
    for keys in occ:
        if occ[keys] > maxletter[1]:
            maxletter = [keys, occ[keys]]

    #now we have to assume that this max letter is "E"

    let = 0

    while True:
        key = ord(maxletter[0]) - ord(stats[let])
        print(key)
        file.seek(0)
        print(caesar(file.readline(), key, "D"))
        file.seek(0)
        while True:
            inp = input("Does this sentence make sense to you? [y/n]")
            if inp == "y":
                return(caesar(file.read(), key, "D"))
                
            elif inp != "n":
                print("Please enter a proper response ('y' or 'n').")
            else:
                let += 1
                break
                

    #however, there's a chance that it's not 

    

decrypt(entext)

entext.close()
