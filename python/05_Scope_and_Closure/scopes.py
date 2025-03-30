username = "garvit"


def fun1():
    username = "Rakhecha"  # if function ke andar usename nhi hai to wo username ko global me search karega
    print(username)

print(username)
fun1()

x = 20

def fun2():
    global x 
    x = 12


print(x)
fun2()
print(x)

def first():
    v = 99
    def second():
        print(v)
    return second

closureOfFirst = first()
closureOfFirst()

def number(num):
    def actual(x):
        return x ** num
    return actual
    return actual(5)

cube = number(3)
# print(cube)
print(cube(5))