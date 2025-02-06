def lcm(a,b):
    for i in range(max(a,b),a*b):
        if i%a==0 and i%b==0:
            lcm=i
            break
    return lcm
print(lcm(20,30))
hcf=600/lcm(20,30)
print(int(hcf))