## voici le projet d'snt
def convertisseur():
    x = True
    valeur_précéedente = []
    while x == True :
        valeurm = float(input("longeur du chemin affiché en cm: "))
        valeurr = valeurm * (2/1.3)
        valeur_précéedente.append(str(valeurr))
        print("cette distance est de "+str(valeurr)+" km en réalité")
        print(valeur_précéedente)

convertisseur()