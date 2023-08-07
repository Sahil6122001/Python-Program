def search(element, list):
    if element in list:
        print("the element is present in list")
    else:
        print("not found")
my_list = [10,20,30,49]
search(10,my_list)
search(99,my_list)