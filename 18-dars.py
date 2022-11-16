# def talabani_bohola(ismlar):
#     baholar = {}
#     while ismlar :
#         ism = ismlar.pop()
#         baho = input(f"Talaba{ism.title()}ning bahosini kiriting:  ")
#         baholar[ism] = int(baho)
#     return baholar


# baho = talabani_bohola(["ali","vali",])
# print(baho)



talaba = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} ning bahosini kiriting:  ")
        baholar[ism] = int(baho)
    return baholar



baholar = bahola(talaba[:])
print(baholar)
print(talaba)

for baho in baholar.values():
    print(f"{talaba.pop().title()} ning bahosi - {baho}  ")
    




























