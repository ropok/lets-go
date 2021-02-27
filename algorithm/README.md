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

2. Bill the avid hiker.
   1. input n
   2. `if n >= 2`: goto iii, `else`: error
   3. input s
   4. `if len(s) == n`: goto v, `else`: error
   5. countingValleys()
      1. for step in s:
         1. temp = sea_level
         2. `if step = U`: sea_level++, `if step = D`: sea_level--
         3. `if temp = 0 and sea_level = -1`: temp_valley += 0.5
         4. `if temp = -1 and sea_level = 0`: temp_valley += 0.5
         5. repeat
      2. valley = floor(temp_valley)
      3. return valley

   3. pseudo GoLang 1.345.679
      1. input number
      2. while number !=0 :
         1. num = number % 10
         2. outputs.append(num*zeros)
         3. number = number // 10
         4. zeros = zeros*10
      3. for output in reversed(output):
         1. print(output)

   4. Andrew's lamp trip
      1. declare int lamp = 0, int switches = 100
      2. lamp = lamp + switches (first trip)
      3. for trip in range (2, switches):
         1. while trip**n < 100:
            1. lamp += 1
            2. n += 1
      4. print lamp