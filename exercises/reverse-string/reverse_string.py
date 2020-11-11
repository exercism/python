word = input(print("Enter word"))
reverse_word = ""
for i in range(len(word)-1,-1,-1):
  reverse_word = reverse_word + word[i]

print(reverse_word)  
