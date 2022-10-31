
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
 
 
print("\n>>>POTAHTLAR ") 
 
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
      "sir":15, 
      "manti":23, 
      "qozon kabob":45, 
      "tandir somsa":9, 
      "osh":20, 
      "lag'mon":22, 
      "non":4, 
      "choy":3, 
      "shashlik":12, 
      "somsa":6, 
      "tabaka":15 
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

