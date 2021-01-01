## voici le projet d'snt
def convertisseur():
    valeur_précéedente = []
    while True:
        valeurm = float(input("longeur du chemin affiché en cm: "))
        valeurr = valeurm * (2/1.3)
        valeur_précéedente.append(str(valeurr))
        print("cette distance est de "+str(valeurr)+" km en réalité")

convertisseur()
