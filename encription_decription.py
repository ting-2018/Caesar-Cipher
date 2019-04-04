# def input_key():
#     a = input("input: E")
import string

alpha_list = list(string.ascii_lowercase)

k = int(input("Enter a shift key for Caesar Cipher (it should be integer and 0-25)\n"))

while (k<0) or (k>25):
    k = int(input("Your key should be 0 - 25\n"))

message = input('Enter your message (Just a string)\n').lower()

dic={}

for i in range(0,26):
    dic[alpha_list[i]] = i

print(dic)

def encription(message):
    x = []

    for c in list(message):
        x.append(dic[c])

    print(x)

    y = []

    for i in range(0, len(x)):
        y.append((x[i] + k) % 26)

    print(y)

    cipher_text = ''

    for i in y:
        for key in dic:
            if i == dic[key]:
                cipher_text = (cipher_text + key).upper()
    return cipher_text


# decription
def decription(c):
    decrept_y = []
    for i in c:
        for key in dic:
            if i == key:
                decrept_y.append(dic[key])
    print(decrept_y)
    g=[]
    for i in range(0, len(decrept_y)):
        g.append((decrept_y[i] - k) % 26)

    print(g)
    decrept_text = ''

    for i in g:
        for key in dic:
            if i == dic[key]:
                decrept_text = (decrept_text + key).upper()

    return decrept_text

cipher_text = encription(message)
print("The cipher text of message '" + message + "' is: " + cipher_text)

c = list(cipher_text.lower())
decrept_text = decription(c)
print("The recovered plain text is : " + decrept_text)

retrieved_cipher_text = 'QVIREFVGL ZJ DJG LMKXGZMA'

retrieved_cipher_text = retrieved_cipher_text.split()
print(retrieved_cipher_text)
decrept_recieve_text = ''
for i in retrieved_cipher_text:
    decrept_recieve_text = decrept_recieve_text + decription(i.lower())+ ' '

print(decrept_recieve_text)