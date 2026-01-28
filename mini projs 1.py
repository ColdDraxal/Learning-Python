def get_num():
    """This function is to create list of integers"""
    num=input("Enter numbers seperated by space: ")
    numlist=[int(x) for x in num.split()]
    # numlist=[int(x) for x in num.replace(","," ").split()]
    return numlist
# print(get_num())

def find_max(number):
    """This function is to find the largest number in list"""
    largest_num=number[0]
    for x in number:
        if x>largest_num:
            largest_num=x
    return largest_num


def find_min(number):
    """This function is to find the smallest number list"""
    smallest_num=number[0]
    for x in number:
        if x<smallest_num:
            smallest_num=x
    return smallest_num

def def_sum(number):
    """This function is to find sum of the list"""
    total=0
    for  x in number:
        total+=x
    return total


def find_average(number):
    """This function is to find average of the numbers in list"""
    average=def_sum(number)/len(number)
    return average

nums=get_num()
print(nums)
print(find_max(nums))
print(find_min(nums))
print(def_sum(nums))
print(find_average(nums))
