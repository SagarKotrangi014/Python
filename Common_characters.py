'''
Write a python program to display all the common characters between two strings. 
Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. 
Perform case sensitive string comparison wherever necessary.

'''


def find_common_characters(msg1,msg2):
    common_characters=""
    
    for char in msg1.replace(" ", ""):
    
        if char in msg2 and char not in common_characters:
            common_characters+=char
            
    if not common_characters:
        return -1
    return common_characters

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)