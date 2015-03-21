#cipher text
def encrypt(sentence1, key):
    code = ""
    for char in sentence1:
        c = ord(char) + int(key)
        code = code + chr(c)
    return code
def decrypt(sentence2, key):
    code = ""
    for char in sentence2:
        c = ord(char) - int(key)
        code = code + chr(c)
    return code
choice = raw_input("Enter 1 for encryption or 2 for decryption - ")
print "For example: "
print "Message : You just have to decide if you want to be Tigger or Eeyore"
print "Encrypted message where key=1 : Zpv!kvtu!ibwf!up!efdjef!jg!zpv!xbou!up!cf!Ujhhfs!ps!Ffzpsf"
sentence = raw_input("Enter the string - ")
while True:
    key = raw_input("Enter the key, a number between 1 and 25 - ")
    if int(key)>0 and int(key)<26:
        break
if (choice == "1"):
    answer = encrypt(sentence, key)
    print "The encrypted string is : " + answer
elif (choice == "2"):
    answer = decrypt(sentence, key)
    print "The decrypted string is : " + answer
