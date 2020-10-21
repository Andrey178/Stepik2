from simplecrypt import decrypt, DecryptionException

with open("D:\Programming\encrypted.bin", 'rb') as inf:
    encrypted = inf.read()
with open("D:\Programming\passwords.txt") as inf:
    passwrds = []
    for line in inf:
        passwrds.append(line.strip())
print(encrypted)
print(passwrds)
for _ in passwrds:
    try:
        print(decrypt(_, encrypted).decode('utf8'))
        #print(decrypt(_, encrypted))
        break
    except DecryptionException as e:
        print('Wrong password', e)