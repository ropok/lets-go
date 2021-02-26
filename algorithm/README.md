# Algorithm

1. Nick's clothing store.
   1. input number of socks (n)
   2. `if n >= 1 and n <= 100`: goto 3, `else` back to 1
   3. input sock's color available (ar)
   4. `if len(ar) >= 0 and len(ar) <= n`: goto 5, `else` back to 3
   5. sellablePairs(ar)
      1. get a color
      2. pop color from ar
      3. compare to another
      4. if same color: countSame++, pop
      5. back to 3, til the end of color
      6. `if countSame > 1`: goto 7, `else`:  `pairs = 0`
      7. `if countSame % 2 = 0`: `pairs = countSame/2`, `else`: `pairs = (countSame-1)/2`
      8. finalPairs += pairs
      9. back to 1