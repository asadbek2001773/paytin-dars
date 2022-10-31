
python={ 
    'integer':'butun son', 
    'float':'onlik son', 
    'boolean':'mantiqiy qiymat', 
    'for':'biror amalni qayta-qayta bajarishtsikli', 
    'if':'shartlarni tekshirish operatorlari', 
    'elif':'aks holda agar', 
    'else':'aks holda', 
    'get':"davom ettirish", 
    'sort':'tartiblash', 
    'sqrt':'ildizdan chiqarish' 
    } 
for key, value in sorted(python.items()): 
    print(f"{key.title()}-{value.title()}") 
 
 
 

print("\n>>>DAVLATLAR ") 
davlatlar={ 
    "O'zbekiston", 
    "aqsh", 
    "roosia", 
    "tojikiston", 
    "qirg'iziston", 
    "qozog'izton", 
    "malayziya", 
    "singapur", 
    "italia" 
    } 
for davlatlar in sorted (davlatlar): 
    print(davlatlar.title()) 
 
 

 
poytahtlar={ 
    "toshkent", 
    "washington", 
    "maskva", 
    "dushanbe", 
    "bishkek", 
    "nur sulton", 
    "kuala-lumpur", 
    "singapur", 
    "rim" 
    } 
for poytahtlar in sorted (poytahtlar): 
    print(poytahtlar.title()) 
 
 
davlatlar={ 
    "vatikan":"vatikan", 
    "ukraina":"kiyif", 
    "hindiston":"dehli", 
    "O'zbekiston":"toshkent", 
    "aqsh":"washington", 
    "roosia":"maskva", 
    "tojikiston":"dushanbe", 
    "qirg'iziston":"bishkek", 
    "qozog'izton":"nur sulton", 
    "malayziya":"kuala-lumpur", 
    "singapur":"singapur", 
    "italia":"rim" 
    } 
county=input("Qaysi davlatlarni poytahtini bilishni istaysiz?\n>>> ").lower() 
capital=davlatlar.get(county) 
if capital==None: 
    print("Kechirasiz, bizda bu haqda malumot yo'q") 
else: 
    print(f"{county.upper()}nning poytaxti {capital.title()}") 
 
 

menu={ 
      "sir":24, 
      "manti":31, 
      "qozon kabob":49, 
      "tandir somsa":12, 
      "osh":17, 
      "lag'mon":32, 
      "non":7, 
      "choy":6, 
      "shashlik":29, 
      "somsa":5, 
      "tabaka":11 
      } 
narh=0 
print("3ta taom buyurtma bering!\n>>> ") 
buyurtmalar=[] 
for i in range(5): 
  buyurtmalar.append(input(f"{i+1}-taom: ").lower()) 
 
for buyurtma in buyurtmalar: 
    if buyurtma in menu: 
        narh=narh+menu[buyurtma] 
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm ") 
    else: 
        print(f"kechirasiz, bizda {buyurtma} yo'q.");print(f"jami: {narh}")

