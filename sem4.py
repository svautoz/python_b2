with open('./list.txt', 'r') as file:
    string = file.readline()
    lst = string.split(' ')
    lst = [int(i) for i in lst]
    print(lst)
    new_list = [(i, i**2) for i in lst if i % 2 ==0]
    print(new_list)

