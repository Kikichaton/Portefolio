tab=[]


a=0; six=0; total=0
for i in range(6):
    while(a<1 or a>6):
        a=(int(input("veuillez saisir une valeur comprise entre 1 et 6 : ")))
    tab[i]=a
    if(a==6):
        six=six+1
    total=total+a; a=0
if(total>20):
    print("vous avez gangez 300000€")
if(six>3):
    print("vous avez gagnez 400000€")
else:
    print("vous avez perdu")
print(tab)
