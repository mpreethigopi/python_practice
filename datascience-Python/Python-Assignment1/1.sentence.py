"""1.	Accept five words as input and print the sentence formed by these words after adding a space 
between consecutive words and a full stop at the end."""


sentence=[]
def get_words():
    no_of_words=5
    for data in range(no_of_words):
        word=str(input(f"Enter the word{data+1}: "))
        sentence.append(word)
    return sentence

def display_sentence():
    #for j in sentence:
    user_sentence=" ".join(sentence).capitalize()    
    print("The user sentence is :", user_sentence+".")


get_words()
display_sentence()





