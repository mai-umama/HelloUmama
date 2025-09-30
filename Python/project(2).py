import random
import string
pass_len = 8
charVal= string.ascii_letters + string.digits + string.punctuation

password =""
for i in range(pass_len):
   password += (random.choice(charVal))

print("Your random password is :", password)

# ******list comprehension ******** (this will make the code smaller reduce some lines)

# import random
# import string
# pass_len = 8
# charVal= string.ascii_letters + string.digits + string.punctuation

# res = "".join([random.choice(charVal) for i in range(pass_len)])

# print(res)