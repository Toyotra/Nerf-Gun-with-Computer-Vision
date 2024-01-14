a = int(input())
epic_list = [0, 1]

if a > 1:
    for i in range(a-2):
        epic_list.append(epic_list[i] + epic_list[i+1])
    print(epic_list[len(epic_list)-1] + epic_list[len(epic_list)-2] % 1000000007) 

else:
    print(1)