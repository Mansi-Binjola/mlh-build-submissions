string = input("enter string:")

# method 1
print(string[::-1])

# method 2
reverse_string = ""
for i in range(len(string)-1,-1,-1):
    reverse_string+=string[i]
print(reverse_string)
