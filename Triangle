#Create a code which is able to identify the valid triangle.
#use the triangle theory 'sum of two sides of a triangle is greater than the third side'

def is_a_triangle(a,b,c):
    if a+b<=c or b+c<=a or c+a<=b:
        return False
    return True
print(is_a_triangle(3,4,5))


#triangle area using the heron's formula
#p = (a + b + c) / 2
#(p * (p - a) * (p - b) * (p - c)) ** 0.5

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

