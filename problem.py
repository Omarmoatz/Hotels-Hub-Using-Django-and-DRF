


l1 = [1, 3, 4, 5, 7, 9, 11]

# case 1
l2 = [4, 5, 7] # valid True
l3 = [5, 7] # valid True
l4 = [1, 3, 4, 5] # valid True
l5 = [5, 7, 9, 11] # valid True

# case 2
l6 = [3, 7, 9] # invalid False
l7 = [1, 3, 5] # invalid False

# solve it !!!

# def is_part_of(elements, sub_elements) -> bool:
#     start_index = 0
#     elements = elements[start_index:]
#     for i in sub_elements:
#         for index, y in enumerate(elements):
#             print(i, y, index)
#             print(elements, start_index)
#             if i == y:
#                 start_index = index              
#                 print(elements, start_index)
#                 break
#             # return False
#     return True



# def is_part_of(elements, sub_elements) -> bool:
#     length = len(sub_elements)
#     for index, num in enumerate(elements):
#         if sub_elements[0] == num:
#             for x in range(length):
#                 print(x)
#                 if sub_elements[x] != elements[index+x]:
#                     return False
#             return True


# def is_part_of(elements, sub_elements) -> bool:
#     n, m = len(elements), len(sub_elements)
#     # print(n, m)
#     for i in range(n - m + 1):
#         # print(i)
#         # print(elements[i:i + m])
#         if elements[i:i + m] == sub_elements:
#             return True
    
#     return False

def is_part_of(elements, sub_elements) -> bool:
    n, m = len(elements), len(sub_elements)
    # Iterate through the bigger list to find the sublist in sequence
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if elements[i + j] != sub_elements[j]:
                match = False
                break
        if match:
            return True
    
    return False


v1 = is_part_of(l1, l2) # True
v2 = is_part_of(l1, l3) # True
v3 = is_part_of(l1, l4) # True
v4 = is_part_of(l1, l5) # True
v5 = is_part_of(l1, l6) # False
v6 = is_part_of(l1, l7) # False

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)