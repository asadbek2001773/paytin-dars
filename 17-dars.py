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




# son = input("son kiriting>>>     ")


# def son_top():
#     while True:
#         a = int(input("son kiriting  "))
#         t_son = 'randon_randit'(1,10)
#         if t_son < 5:
#             print(f"natogri men oylagan son bu emas")
#         elif t_son > 5:
#             print("men oylagan son bundan katta")
#         else:
#             print("togri")
#             break
        
        
# son_top()

         
     
        
     
        
# def son_top(num):
#     summa = 0  
#     for x in range(len(son)):
#         summa = summa + int(son[x])
#     return summa

# print(son_top(son))    




# def meni_dostlarim(sanjar,shagzod,anvar,jovohir,begzod):
#     """Foydalanuvchidan yaqin dosti kimligini aniqlovchi funksiya"""
#     print("bular yaqin dostlarim")
#     for n in range(1,5):
#         meni_dostlarim.append(int(input(f"{n}-dostingizni kiriting:")))



# print()
    

            

        
# def toliq_ism_yasa(ism , familya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familya.title()}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kechikib kelgan talabalar : {talaba1} va {talaba2} ")
# print(f"Darstan qochib ketgan talabalar : {talaba2}")

# def toliq_ism_yasa(ism, familya, otasining_ismi=""):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism}  {otasining_ismi} {familya}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov', 'abrorvich')   
     
# print(f"Darsga kechikib kelgan talabalar : {talaba1} va {talaba2} ")

    


# def avto_info(kampanya, model, rangi, karopka,yili, narh=None):
#     avto = {
#         "kampanya" : kampanya,
#         "model" : model,
#         "color" : rangi,
#         "box" : karopka,
#         "year" : yili,
#         "price" : narh
#         }
#     return avto

# avto1 = ("GM", "Malibu", "OQ", "Aftamat", 2020 )
# avto2 = ("GM", "Nexia", "Metalika", "Ruchnoy", 2015, 10000)
# print("Onlayin bozordagi mavjud avtomabilar:")
# avtolar = [avto1,avto2]
# for avto in avtolar:
#     if avto["price"]:
#         narh = f"{avto['price']}$"
#     else:
#         narh = 'Nomalum'
#     print(f"{avto['color']},{avto['model']}. Narhi: {narh}")
    


# def oraliq(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(1,21,3))




def avto_info(kampanya, model, rangi, karopka,yili, narh=None):
    avto = {
        "company" : kampanya,
        "model" : model,
        "color" : rangi,
        "box" : karopka,
        "year" : yili,
        "price" : narh
        }
    return avto


print("Savatizmizdagi mashinalar royhatini shakilantiramz.")
avtolar = []
while True:
    print("Mashina malumotlarini kiriting:")
    kampanya = input("Ishlab chiqaruvchi: ")
    model = input("model:")
    rangi = input("rangi: ")
    karopka = input("karopka: ")
    yili = input("yili:")
    narh = input("narhi:")
    avtolar.append(avto_info(kampanya, model, rangi, karopka,yili, narh))
    jovoblar = input("Yana avto qoshamizmi? (yes/no): ")
    if jovoblar == ('no'):
        break



print("bizni mashinalar")
for avto in avtolar:
    if avto["price"]:
        narh = avto["price"]
    else:
        narh = 'bimima'
    q = (f"{avto['company']},{avto['model']},{avto['color']},{avto['box']},{avto['year']},{avto['price']}")
    print(q.title())       
      































    




