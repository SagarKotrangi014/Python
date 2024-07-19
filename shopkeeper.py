'''You have x no. of 5 rupee coins and y no. of 1 rupee coins. 
You want to purchase an item for amount z. 
The shopkeeper wants you to provide exact change. 
You want to pay using minimum number of coins. 
How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.
'''

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    while rupees_to_make>0:
        if rupees_to_make>=5 and no_of_five>0:
            five_needed+=1
            rupees_to_make-=5
            no_of_five-=1
        elif rupees_to_make>=1 and no_of_one>0:
            one_needed+=1
            rupees_to_make-=1
            no_of_one-=1
        else:
            print(-1)
            return
  
    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)
    
make_amount(28,8,5)