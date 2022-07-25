def find_smallest_int(arr):
    return sorted(arr)[0]

print (find_smallest_int([78, 56, 232, 12, 11, 43]))
print (find_smallest_int([0, 1-2**64, 2**64]))

# def sum_two_smallest_numbers(numbers):
#     return sorted(numbers)[0] + sorted(numbers)[1]

# print(sum_two_smallest_numbers([1,2,3]))
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
# def is_divide_by(number, a,b):
#     if number==None or a==None or b==None:
#         return False
#     div_a = number % a
#     div_b = number % b
#     if div_a != 0 or div_b != 0:
#         return False
#     else:
#         return True

# print(is_divide_by(33,1,33))
# print(is_divide_by(8,3,4))
# print(is_divide_by(10000,5,-3))

# def make_upper_case(s):
#    return s.upper()

# print(make_upper_case("check"))



# from ast import Or
# def sum_array(arr):
#     if arr == None or len(arr)<= 2:
#         return 0
#     return sum(sorted(arr)[1:1])

# print(sum_array([1,1,2,3,1]))
# print(sum_array([]))
# print(sum_array(None))

# from ast import Num

# def solution(number):
#     if (int(number/3)) > 0:
#         nos3 = [*range(0, number, 3)]
#     else:
#         nos3 = []
#     if (int(number/5)) > 0:
#         nos5 = [*range(0, number, 5)]
#     else:    
#         nos5=[]    
#     nos = [*set(nos3+nos5)]
#     ans = sum(nos)
#     if ans < 0:
#        ans = 0
#     return ans


# print(solution(200))
    


# from audioop import reverse
# def reverse_seq(n):
#     nos = []
#     for i in range(n+1):
#         nos.append(i)
#     nos.sort(reverse=True)
#     nos.pop()
#     return nos
    
# print(reverse_seq(5))

# def find_average(numbers):
#     total = 0
#     length =len(numbers)
#     for n in numbers:
#         total = total + n
    
    


# print(find_average([1, 6, 3]))


# 25/07/22
# def square_sum(numbers):
#     numberList = []
#     total = 0
#     for n in numbers:
#         total = total + n*n
#     return total

# print (square_sum([1,2]))


# def number_to_string(num):
#     return f'{num}'

# print(type(number_to_string(67)))
