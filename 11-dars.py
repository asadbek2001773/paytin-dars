# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'nok':30000
#     }
# print('Do\kondagi mahsulotlar:')
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
    
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'    
#      }
# # print(telefonlar.values())
# # print("Foydalanuvchilar quydagi telifoni ishlatishadi:")
# # for tel in telefonlar.values():
# #     print(tel)


    
# print('Foydalanuvchidan quydagi telifonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)
    
    
    
# python_words = {
#     "integer":'Butun son',
#     "float":"O'nlik son",
#     "boolean":"Mantiqiy qiymat",
#     "for":"Bironamalni qayta qayta bajarish tsikli",
#     "if":"SHartlarni tekshirish operatori",
#     "elif":"aks holda agar",
#     "else":"aks holda"
#     }
# for key, value in sorted(python_words.items()):
#     print(f'{key.title()} - {value.title()}')
    
    

# davlatlar = {
#     "O'zbekistan":"toshkent",
#     "aqsh":"vashington d.c",
#     "rassiya":"maskva",
#     "tojikiztan":"dushanbe",
#     "qirgisiston":'beshkek',
#     "qozogiston":"nursulton",
#     "malaziya":"kuala-Lompur",
#     "singapur":"singapur",
#     "italya":"rim"
#     }
# country = input("Qaysi davlatni poytaxtini bilishni istaysiz:").lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz bizda bu haqida malumot yoq")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()}")
    


# menu = {
#         "osh":20000,
#         "lagmon":22000,
#         "non":4000,
#         "choy":5000,
#         "shashlik":12000,
#         "somsa":6000,
#         "tabaka":15000
#         }
# narx = 0
# print("3 ta taom buyurtma bering.")
# buyurtmalar =[]
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         narx = narx + menu[buyurtma]
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q")
# print(f"Jami: {narx}")



import turtle

t =()
turtle.Turtle()
for i in t:
    range(50)
t.forward(50)
t.right(144)
turtle.done()

























    