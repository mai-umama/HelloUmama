A= input()


password = list(A.capitalize())

for i in range(len(password)):
    if password[i] == 's':
        password[i] = '$'
    elif password[i] == 'i':
        password[i] = '!'
    elif password[i] == 'o':
        password[i] = '()'

password.append('.')

password = ''.join(password)

print(password)
