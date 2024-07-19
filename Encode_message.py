'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. 
Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.


'''

def encode(message):
    encoded_message=""
    count=1
    
    for i in range(1, len(message)):
        if message[i]==message[i-1]:
            count+=1
        else:
            encoded_message+=str(count)+message[i-1]
            count=1
            
    encoded_message+=str(count)+message[-1]
    
    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)