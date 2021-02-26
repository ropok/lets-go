# Algorithm

1. Nick's clothing store.
   1. input number of socks (n)
   2. `if n >= 1 and n <= 100`: goto iii, `else` back to i
   3. input sock's color available (ar)
   4. `if len(ar) >= 0 and len(ar) <= n`: goto v, `else` back to iii
   5. sellablePairs(ar)
      1. get a color
      2. pop color from ar
      3. compare to another
      4. if same color: pairs++, pop
      5. back to 3, til the end of color
      6. back to a, else return pairs