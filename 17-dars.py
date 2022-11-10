# nums = [5,7,3,0,9,4,1,3,10,6,2]

# def bubble(nums):
#     n = len(nums)
#     swaps = 0
#     for i in range(n-1):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             swaps += 1
#     return swaps

# def bubble_sort(nums):
#     n = len(nums)
#     for _ in range(n-1):
#         if bubble(nums) == 0:
#             break
        
# bubble_sort(nums)




son = input("son kiriting>>>     ")


# def son_top():
#     while True:
#         a = int(input("son kiriting  "))
#         t_son = randon_randit(1,10)
#         if t_son < 5:
#             print(f"natogri men oylagan son bu emas")
#         elif t_son > 5:
#             print("men oylagan son bundan katta")
#         else:
#             print("togri")
#             break
        
        
# son_top()

         
     
        
     
        
def son_top(num):
    summa = 0  
    for x in range(len(son)):
        summa = summa + int(son[x])
    return summa

print(son_top(son))    


        
            

        


