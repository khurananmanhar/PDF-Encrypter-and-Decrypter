import pikepdf
from tqdm import tqdm
file = input()
passwords = [line.strip() for line in open("wordlist.txt")]

for password in tqdm(passwords, "Cracking PDF Files"):
    try:
        with pikepdf.open(file, password=password) as pdf:
            print("+Password Found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue