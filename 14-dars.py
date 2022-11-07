# print("Kiritilgan soning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora :
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print ("Dastur to'xtadi")


# print("Kiritilgan soning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol +="(dasturni toxtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print ("Dastur tugadi")



# print("Kiritilgan soning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol +="(dasturni toxtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print ("Dastur tugadi")


# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2}ga teng")
    

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2}ga teng")

    
# from random import randint

# a = randint(1,600)
# b = randint(1,500)

# c = int (input("{} x {} = ".format(a,b)))
# savol ="(dasturni toxtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while True:

#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         if c == (a * b):
#             print("To'gri! :)")
#         else:
#             print("Xato! :(")


# from random import randint
# import math
# savol = "dastur tugaganda 'exit' deb yozing" 
# ishora = True
# while ishora  : 
#     a = randint(1,600)
#     b = randint(1,500)
#     c = int (input("{} x {} = ".format(a,b)))
#     if a*b == c:
#         print("togri")
#     else:
#         print("xato")
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break


# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)
        
# import math
# print("Kiritilgan sonning ildizini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# while True:
#     son = input(savol)
#     if son == 'exit':
#         break
#     else:
#         if int(son) <0:
#             print("iltimo minus son kiritmang")
#         else:
#             print(math.sqrt(float(son)))
# print('Dastur to\'xtadi!')

son = 0
while son<10:
    if son%2==0:
        continue
    else:
        print(son)
    son += 1













