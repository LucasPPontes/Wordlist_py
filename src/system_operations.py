import os
import time
import socket
import itertools
import string

print("""
   _____ ______ _____            _____   ____  _____    _____  ______  __          ______  _____  _____  _      _____  _____ _______ 
  / ____|  ____|  __ \     /\   |  __ \ / __ \|  __ \  |  __ \|  ____| \ \        / / __ \|  __ \|  __ \| |    |_   _|/ ____|__   __|
 | |  __| |__  | |__) |   /  \  | |  | | |  | | |__) | | |  | | |__     \ \  /\  / / |  | | |__) | |  | | |      | | | (___    | |   
 | | |_ |  __| |  _  /   / /\ \ | |  | | |  | |  _  /  | |  | |  __|     \ \/  \/ /| |  | |  _  /| |  | | |      | |  \___ \   | |   
 | |__| | |____| | \ \  / ____ \| |__| | |__| | | \ \  | |__| | |____     \  /\  / | |__| | | \ \| |__| | |____ _| |_ ____) |  | |   
  \_____|______|_|  \_\/_/    \_\_____/ \____/|_|  \_\ |_____/|______|     \/  \/   \____/|_|  \_\_____/|______|_____|_____/   |_|   
                                                                                                                                     
                                                                                                                                     
""")

usr_min = int(input("Digite o minimo de caracteres desejado: "))
usr_max = int(input("Digite o máximo de caracteres desejado: "))
user_char = input("Digite os caracteres EX: (0123) para números (abcd) para letras ($#@) para caracteres especiais: ")

def generate_wordlist(min,max,char):
    cont = 0
    #character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    
    with open("wordlist.txt","w") as file:

        for i in range(min,max + 1):
            for j in itertools.product(char,repeat=i):
                word = "".join(j)
                file.write(word)
                file.write("\n")  
    print("Wordlist gerada com sucesso!. Arquivo wordlist.txt criado")

generate_wordlist(usr_min, usr_max, user_char)