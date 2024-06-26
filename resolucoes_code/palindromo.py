# Vamos testar se uma palavra é um palíndromo

print("------#--------#--------#--------#------")
print("Vamos testar se uma palavra é um palíndromo.")
print("------#--------#--------#--------#------")

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

word = input("Enter a word: ")
if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")