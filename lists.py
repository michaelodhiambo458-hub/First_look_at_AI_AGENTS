name_list=["Mike","Ruth","Kennedy","Owen","Tabitha"]
number_list=[19,23,23,24,25]
name_list.append("Malick")
number_list.append(26)


for index,name in enumerate(zip(name_list,number_list),start=1):
    print(index,name)