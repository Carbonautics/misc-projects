T = input().strip()
while(not T.isdigit()):
    T = input().strip()
def CountTrailingZeros(n): 
      
    # declare bitset of 64 bits 
    bit = bin(n)[2:] 
    bit = bit[::-1] 
  
    zero = 0; 
  
    for i in range(len(bit)): 
        if (bit[i] == '0'): 
            zero += 1
              
        # if '1' comes then break 
        else: 
            break
  
    return zero
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
i = 0
while(i < int(T)):
    x = input().strip()
    if int(x) < 2: print('0')
    num = factorial(int(x))
    number = CountTrailingZeros(int(num))
    print(number)
    i+=1