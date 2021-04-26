T = input().strip()
while(not T.isdigit()):
    T = input().strip()
i = 0
while(i < int(T)):
    orgn_str = input().strip()
    mid = int(len(orgn_str)/2)
    left_str = orgn_str[:mid]
    right_str = orgn_str[mid:]
    left_str = left_str[::-1]
    right_str = right_str[::-1]
    strg = left_str + right_str
    print(strg)