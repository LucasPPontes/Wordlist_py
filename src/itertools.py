import itertools

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "slaeu"
n = 8

wordlist = []

for xs in itertools.product(nums, repeat=n):
    passwd = "".join(xs)
    print(passwd)
    wordlist.append(passwd)

with open("words.txt","w") as file:
    file.write("\n".join(wordlist))     

