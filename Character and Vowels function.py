#!/usr/bin/env python
# coding: utf-8

# In[7]:


def count_letter(string, letter):
    count = 0 #Define the initial count
    for c in string: #The string will be compared with the letter define by the user 
        if c == letter:
            count += 1
    return count

def count_vowels(string):
    vowels = "aeiou" # Define the vowels
    count  = 0 #Initialize the count = 0
    for vowel in vowels:
        count += count_letter(string,vowel)
    return count

input_string = input("Enter a string ")
input_string = input_string.lower()
input_letter = input("Enter a character: ")
input_letter = input_letter.lower()

print("Count of letter {}: {}".format(input_letter,count_letter(input_string,input_letter)))
print("Count of vowels: {}".format(count_vowels(input_string)))


    


# In[ ]:





# In[ ]:




