'''
Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?

'''

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    rabbit_count=(legs-2*heads)/2
    
    chicken_count=heads-rabbit_count
    
    if rabbit_count>=0 and chicken_count>=0 and int(rabbit_count)==rabbit_count and int(chicken_count)==chicken_count:
        print(int(chicken_count),int(rabbit_count))
    else:
        print(error_msg)
    
#Provide different values for heads and legs and test your program
solve(20,60)