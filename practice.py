########################################
def remove_chars(word, n):
    print('Original string:', word)
    # Extract string from index n to the end
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

##############
print("New Change")