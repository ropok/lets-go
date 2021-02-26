# Basic concepts
1. Coding

   A. Code smell is a piece of code that made the whole code didn't well performed such as dead code, identical code. One of the smell code is duplicate code which between the code function look almost identical, so it needs to be eliminate one of them or combine the code function.
   For example:
   There were two functions of code
   ```python
   def sum(a, b):
      return a+b
   ```

   ```python
   def add(a, b):
      c = a+b
      return c
   ```

   The functions of code has the same return, so it will be better to refactor it with combine or eliminate one of them.

   B. Dependency Injection (DI) used to manage how class function depend on another class to be able to use. So it needs some kind of middleman to access that class. It is important when some classes may depend on another class, so instead of accessing that class directly, it will be better to create a constructor for that class.
   Without DI, the code may difficult for both maintain and scalable purpose due to more complex code if the classes may depend one to another and possible to cause slowing down performance.