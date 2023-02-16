def hello():
    print("This is my first function")
hello()
hello()
def calculate(x=5,y=7):
    print(x*y)
calculate()
def majina(fname,lname):
    print(fname+" "+lname)
majina("Erick","Were")

def greetings(name, greeting="Hello"):
    print(greeting+" "+name)
greetings("Erick")
greetings("Niaje","Joan")
greetings("Joan","Niaje")

def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,9,1,8,17,45)
print(result)

def minimumvalue(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)
result=minimumvalue(1,2,3,4,5,6)
print(result)
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,8,2,7,1,5,4,2])
print(answer)
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)