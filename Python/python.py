key_dict = {}
no_of_rooms = int(input())
ss = input().strip()
for i in ss:
    if i.islower() in key_dict:
        key_dict[i] += 1
    else:
        key_dict[i] = 1
    

