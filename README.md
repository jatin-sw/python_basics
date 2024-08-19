# python_basics
learning python basics

1. In Python, **while can also have else part. If we want to execute something when the while condition fails, then else gets executed.** There's also break statement to exit while.

2. In Python, **tuples are lists which are immutable written as '()' instead of '[]'.**
    There's unpacking too. 
    E.g. my_tuple = (1, 3, 5)
    x, y, z = my_tuple
    Here, x = 1, y = 3, z = 5
   
3. In Python, **every function returns 'None' by default. So all code paths may or may not have return statement.** There is also 'Try... except' for handling exceptions. Comments start with #. **There's else part to try... except. The else part executes if the try block doesn't raise any exception. To throw exception, the keyword is raise.**

4. In Python, if the **Class** is empty then we have to write 'pass' so that Python interpreter understands that it is empty. **Every method has 'self' as argument, just like Extended Methods in C#.** And we can have properties after defining class. They are called attributes here. Meaning **we can have p.x = 10 where p is an object of a class P. Now p2.x will give error.** Because x attribute is specific to object p, not p2. There is Inheritance also.

5. In Python, there is **Module.** Just **define classes, functions in separate file and reuse them.** 'import GreatestNumberModule' or 'from GreatestNumberModule import greatest_number' this way we can reuse.

6. In Python, **Packages have Modules.** One can write own Package in ExternalLibraries dirctory and including __init__ file. Then one can import specific Module within package or specific Function. **E.g., 'from P.M import F'; 'from P import M', 'import P', etc.**

7. The **[PyPi site](https://pypi.org/)** has several Python Packages that we can reuse in our programs. There's no need to reinvent the wheel!

8. In Python, **List Comprehension** creates a list from something else like string, list, dictionary.\
Format - \[new_item for item in list1 if test\] \
e.g. even_squares = [n**2 for n in l if n % 2 == 0]\
Similarly for **Dictionary comprehension**,\
Format - {new_key:new_val for (key, val) in dict.items() if test} \
e.g. farenhite = {city:tem_c*9/5 + 32 for (city, temp_c) in celsius.items()}

9. In Python, ***args** is for unlimited arguments. ****kwargs** is for unlimited keyword arguments. ***args is a Tuple** while ****kwargs is a dictionary**. \
   e.g., \
   def my_func1(*args): \
       sum = 0
       print(args) \
       print(args[1]) \
       for n in args: \
           sum += n \
       return sum \
   

   def my_func2(**kwargs): \
       print(kwargs) \
       print(kwargs.get("key1")) \
       

   my_func1(1, 4, 5, 8) -> (1, 4, 5, 8); 4; 18 \
   my_func2(MI="Tom", Oppenheimer="Cillian") -> {"MI":"Tom", "Oppenheimer":"Cillian"}; "Tom"

10. Python has **Special Functions**, also called **dunder functions**. They start and end with double underscores i.e., **\_\_\<name\>\_\_**. \
    e.g., \
    my_class(): \
        def \_\_init\_\_(self, num): \
            self.num = num \
        def \_\_pow\_\_(self, other): \
            return self.num ** other \
    \

    **Whenever an instance of my_class is raised by power of other, it will give the result of num ** other.** \
    **The \_\_init\_\_ method is kind of a constructor with the difference being the object is already created before \_\_init\_\_ call.** \
    **Everything in Python is an object.**
    
12. The **[Dive into Python 3](https://diveintopython3.net/index.html)** is one of the best resources to learn Python3.
