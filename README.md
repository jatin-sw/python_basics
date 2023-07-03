# python_basics
learning python basics

1. In Python, **while can also have else part. If we want to execute something when the while condition fails, then else gets executed.** There's also break statement to exit while.

2. In Python, **tuples are lists which are immutable written as '()' instead of '[]'.**
    There's unpacking too. 
    E.g. my_tuple = (1, 3, 5)
    x, y, z = my_tuple
    Here, x = 1, y = 3, z = 5
   
3. In Python, **every function returns 'None' by default. So all code paths may or may not have return statement.** There is also 'Try... except' for handling exceptions. Comments start with #.

4. In Python, if the **Class** is empty then we have to write 'pass' so that Python interpreter understands that it is empty. **Every method has 'self' as argument, just like Extended Methods in C#.** And we can have properties after defining class. They are called attributes here. Meaning **we can have p.x = 10 where p is an object of a class P. Now p2.x will give error.** Because x attribute is specific to object p, not p2. There is Inheritance also.

5. In Python, there is **Module.** Just **define classes, functions in separate file and reuse them.** 'import GreatestNumberModule' or 'from GreatestNumberModule import greatest_number' this way we can reuse.

6. In Python, **Packages have Modules.** One can write own Package in ExternalLibraries dirctory and including __init__ file. Then one can import specific Module within package or specific Function. **E.g., 'from P.M import F'; 'from P import M', 'import P', etc.**

7. The **[PyPi site](https://pypi.org/)** has several Python Packages that we can reuse in our programs. There's no need to reinvent the wheel!
