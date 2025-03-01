x = int(input())
ans  = x 
count = 0 

while True : 
      temp1 = ans // 10
      temp2 =  ans % 10 
      temp3 = (temp1 + temp2 ) % 10
      ans = (temp2 * 10 ) + temp3 
      count += 1 
      if ( ans == x ) :
          break

print(count)