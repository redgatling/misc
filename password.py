password = input("password: ")
strength = "BAD"

is_long = False
has_lower = False
has_upper = False
has_digits = False
has_punc = False
quality_flag = False

digits = "1234567890"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punc = "#$%&\'()*+,-./:;<=>!?@[\\]^_`{|}~"

if len(password) > 10:
    is_long = True

for c in password:
    print(c)
    if c in digits:
        has_digits = True
    if c in lower:
        has_lower = True
    if c in upper:
        has_upper = True
    if c in punc:
        has_punc = True
    if not quality_flag:
        quality_flag = is_long and has_digits and has_lower and has_upper and has_punc
    else:
        break

if quality_flag:
    strength = "GOOD"

if password.lower().find("kaspersky") != -1:
    strength = "BAD"

print(strength)
