'''
FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.

A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. 
Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.

Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. 
The delivery charges are as mentioned below:
_________________________________________________________________________________________
Distance in kms              | For first 3kms, For next 3kms, For the remain
-----------------------------|-----------------------------------------------------------
Delivery charge in Rs per km |0,3,6
_____________________________|____________________________________________________________

Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer. 

The below information must be used to check the validity of the data provided by the customer: 

Type of food must be V for vegetarian and N for non-vegetarian.

Distance in kms must be greater than 0.

Quantity ordered should be minimum 1.

If any of the input is invalid, the bill amount should be considered as -1.
'''


def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if food_type not in ['V', 'N'] or quantity_ordered<1 or distance_in_kms<=0:
        return -1
    
    cost_per_plate=120 if food_type=='V' else 150
    if distance_in_kms<=3:
        delivery_charge=0
    elif distance_in_kms<=6:
        delivery_charge=3*(distance_in_kms-3)
    else:
        delivery_charge=3*3+6*(distance_in_kms-6)
    
    bill_amount=quantity_ordered*cost_per_plate+delivery_charge
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)