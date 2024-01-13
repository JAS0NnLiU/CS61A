# Lecture 2 Functions

## Expressions

add                (         2        ,          3              )

operater             operand         operand   

## Names, Assignment and User-Defined Functions

radius = 10

可同时赋值多个

area， circ = pi * radius * radius, 2 * pi * radius

若再改变radius,area和circ不会随之改变

from operator import add, mul

def square(x):

​		return mul(x, x)

types of expressions:
primitive expressions: number or numeral, name, strign

call expressions: 



## Environments Diagrams

Execution rule of assignment statements:

1. Evaluate all expressions to the right of = from left to right
2. Bind all names to the left of = to the resulting values in the current frame



## Defining Functions

def <name> (<formal parameters>):

​		return <return expression>

a name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.

from operator import mul

def square(square)：

​		return mul(square, square)



# Lecture 3 Control

## print and none

None indicates that nothing returned

print(None)  将输出None

None is not displayed by the interpreter as the value of  an expression



## Pure Functions & Non-Pure Functions

Pure Functions: just return values

Non-Pure Functions: have side effects

e.g. 

print(print(1), print(2))

ouput :

1

2

None None



## Multiple Environments

 an environment is a sequence of frames

names have no meaning without environments

names have different meanings in different environments



## Miscellaneous  Python Features

division:

from operator import truediv, floordiv, mod

2013 / 10      truediv(2013, 10)   201.3

2013 // 10     floordiv(2013, 10)    201

2013 % 10     mod(2013, 10)        3



python - i ex.py可以进行交互式

python -m doctest ex.py 测试文档中的例子



可以使用默认值占位，如果没有输入值使用默认值

def divide_exact(n , d=10):



## Conditional Statements

def absolute_value(x):

​		if x <  0:

​				return -x

​		elif x == 0:

​				return 0

​		else:

  			  return x

False values:  False, 0,  ' ', None

True values: anything else



## Iteration

i, total = 0, 0

while i < 3:

​		i = i+1

​		total = total + i

## Prime Factorization

def prime_factors(n):

​		"""Print the prime factors of n in non-decreasing order."""

​		while n > 1:

​				k = smallest_prime_factor(n)

​				n = n // k

​				print(k)

def smallest_prime_factor(n):

​		k = 2

​		while n % k != 0:

​				k = k + 1

​		return k



# Lecture 4  Higher-Order Functions

## Iteration example

def fib(n):
		pred, curr = 0, 1

​		k = 1

​		while k < n:

​				pred, curr = curr, pred + curr

​		return curr

## Designing Functions

A pure function's behavior is the relationship it creates between input and output

## Higher-order Functions

A function that takes a function as an argument or returns a function as a return value

assert + 语句 +' 语句为False的显示 '

## Functions as Return Values

def make_adder(n):

​		"""Return a function that takes one argument K and Return  K+N.

​		>>>add_three = make_adder(3)

​		>>>add_three(4)

​		7

​		"""

​		def adder(k):

​				return k+n

​		return adder

## Lambda Expressions

square = lambda x: x * x

square(4)   **equals**  (lambda x: x * x)(4)

vs Def Statements:

Only the def statement gives the function  an intrinsic name

## Return

def search(f):

​		x = 0

​		while not f(x):

​				x += 1

return x



def inverse(f):

​		return lambda y: search(lambda x: f(x) == y)



## Control

and : return the last value if every value is true

...True and 1 and 2 and 17

17

or 



# Lecture 5 Environments

## Higher-Order Functions Example

def repeat(f, x):

​		while f(x) != x:

​				x = f(x)

​		return x

def g(y):

​		return (y + 5) // 3

## Environments for Nested Definitions

def make_adder(n):

​		def adder(k):

​				return k + n

​		return adder

adder_three = make_adder(3)

add_three(4)



## Local Names

ERROR:

def f(x, y):

​		return g(x)

def g(a):
		return a + y

f(1, 2)
