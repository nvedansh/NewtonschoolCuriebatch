def posSum(list):
    odd_list = [element for element in list if element % 2 != 0]
    even_list = [element for element in list if element % 2 == 0]
    return [sum(odd_list), sum(even_list)]