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