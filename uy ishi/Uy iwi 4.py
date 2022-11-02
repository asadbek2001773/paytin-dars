 # son = int(input("Juft son kiriting! "))
# print("raxmat")if  son % 2== 0 else  print("toq son ")



# yosh = int(input("Yoshinngizni kiriting: "))
# if yosh <= 4:
#     print("Sizga kirish bepul.")
# elif yosh <= 18:
#     print("Sizga kirish 10000 sum.")
# elif yosh >= 18:
#     print("Sizga kirish 20000 sum.")
# elif yosh<=60:
#     print("Sizga kirish bepul")



# sonlar = [26,29]
# print (sonlar)
# a=38
# s=36
# print(29 > 26)
# print(56 < 59)



# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,1000000000000000000000000):
#     if not (son % n):
#         print(f"{son} son {n} ga toliqsiz bolinadi")

# til = input("Tilni tanlang:  uz/en/ru ?")

# if til == "uz":
#     print("Asalomu aleykum")
# elif til == "en":
#     print ("Hello")
# else:
#     print("uz/en lardan birini tanlang")


# yosh = "18"
# print(yosh.isdigit())



# yosh = input("Yoshingiz nechida? ")
# if yosh.isdigit():
#     yosh = float(yosh)
# else:
#     print("Matinli raqam")
    
    
from random import randint

a = randint(1,600)
b = randint(1,500)

c = int (input("{} x {} = ".format(a,b)))

if c == (a + b):
    print("To'gri! :)")
else:
    print("Xato! :(")

import math
from random import randint
print("O'zingizni sinab koring")
print ("Hohlagan amalingizni bajaring")
masalan = ["Ko'paytirish", "bolish","qoshish", "ayirish"]
for a in masalan:
    print(a, end= ("\n"))
amal = input("Tanlagan amalingizni kiriting:  ")
if amal.lower() == "kopaytirish" :
    q = 0
    for n in range(1, 6):
        a = randint(1,20)
        b = randint(1,20)
        c = int(input("{} - {} = ".format(a , b)))
        if c == (a + b):
            print("To'gri! :)")
            q = q + 1
    
#         else:
#             print("hato! :(")
#     f = 20 * q
#     print(f"Siz {f}% ishladingiz. ")
# elif amal.lower() == "bolish" :
#     q = 0
#     for n in range(1, 6):
#         a = randint(100, 1000)
#         b = randint(1,20)
#         c = int(input("{} : {} = ".format(a , b)))
#         if c == float(math.ceil(a / b)):
#             print("To'gri! :)")
#             q = q + 1
    
#         else:
#             print("hato! :(")
#     f = 20 * q
#     print(f"Siz {f}% ishladingiz. ")
# elif amal.lower() == "qoshish" :
#     q = 0
#     for n in range(1, 6):
#         a = randint(1,100)
#         b = randint(1,100)
#         c = int(input("{} + {} = ".format(a , b)))
#         if c == (a + b):
#             print("To'gri! :)")
#             q = q + 1
    
#         else:
#             print("hato! :(")
#     f = 20 * q
#     print(f"Siz {f}% ishladingiz. ")
# elif amal.lower() == "ayirish" :
#     q = 0
#     for n in range(1, 6):
#         a = randint(1,100)
#         b = randint(1,100)
#         c = int(input("{} - {} = ".format(a , b)))
#         if c == (a - b):
#             print("To'gri! :)")
#             q = q + 1
    
#         else:
#             print("hato! :")
#     f = 20 * q
#     print(f"Siz {f}% ishladingiz. ")

    
    
    
    
    
    
    
    
    
    
    
    
    
# son = int(input("Juft son kiriting: "))
# if son % 2 != 0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")
    
    
# #2
# yosh = int(input("Yoshingiz nechida? "))

# if yosh <= 4 or yosh >= 60: 
#     narh = 0
# elif yosh < 18:     
#     narh = 10000
# else:               
#     narh = 20000
    
# print(f"Chipta {narh} so'm")


# #3
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x}={y}")
# elif x < y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


# #4
# mahsulotlar = [
#     "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun",
# ]

# savat = []
# # for n in range(5):
# #     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")
    
    
    
# #4
# mahsulotlar = [
#     "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun",
# ]


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
    
# # 5
# users = ["alisher1983", "aziza", "yasina", "umar"]

# login = input("Yangi login tanlang: ")

# if login in users:
#     print("Login band, yangi login tanalng!")
# else:
#     print("Xush kelibsiz!")
    
    
# # # 6
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2, 11):
#     if not (son % n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# 1
# for x in range(1,11):
#     print(x, end=(" "))


# # 2
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in sonlar:
#     print(x, end=(" "))


# # 3
# narsalar = ['olma', 43, 'un', 'qalam', 6, 90, 'yilkan']

# for a in narsalar:
#     print(a, end=(", "))
    

# # # 4
# til = input("Tilni tanlang: uz/en/ru ? ")

# if til == 'uz':
#     print("Assalomu alaykum")
# elif til == 'en':
#     print("HELLO")
# else:
#     print("uz/en lardan birini tanlang")

# # ikkita tasodifiy son
# from random import randint

# a = randint(1, 11)
# b = randint(1, 11)

# c = int(input('{} + {} = '.format(a, b)))

# if c == (a + b):
#     print("To`g`ri! :)")
# else:
#     print("Xato! :(")
    

# a = ["a", "b", "c"]

# son = 1
# for b in a:
#     print(son, "-", b, end=("\n"))
#     son += 1
    
    
# import math as m
# a = int(input("a ni kiriting    "))
# b = int(input("b ni kiriting    "))
# d = int(input("d ni kiriting    "))
# c =m.sqrt(a*b/m.sqrt(b+(d**2)))
# print(c)
    

    
    