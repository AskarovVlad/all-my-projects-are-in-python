wizard_list = ["паучьи лапки", "жабий палец", "глаз тритона", "перхоть дракона", 'Gopa mamonta', "Grusha",
               "Shlyapa"]
#[start:stop:step]
wizard_list2 = wizard_list[::2]
print(wizard_list2)
wizard_list3 = wizard_list[1:5:3]
print(wizard_list3)
print(wizard_list)
print(wizard_list[0])
wizard_list[2] = 'mohnatka enota'
print(wizard_list)
print(wizard_list[2])
print(wizard_list[0:3])
wizard_list.append('шаурма')
print(wizard_list)
del wizard_list[6]
print(wizard_list)
wizard_list.pop()
print(wizard_list)
print(wizard_list[0])
wizard_list.pop(0)
print(wizard_list)
wizard_list[0], wizard_list[1] = wizard_list[1], wizard_list[0]
print(wizard_list)
wizard_list.pop(1)
print(wizard_list)
wizard_list2 = ["mama", "papa", "lesia"]
wizard_list3 = [wizard_list, wizard_list2]
print(wizard_list3)
print(wizard_list3[1][1])
wizard_list3 = wizard_list + wizard_list2
print(wizard_list3)
print(wizard_list3[4:])
print(wizard_list3[4:6])

