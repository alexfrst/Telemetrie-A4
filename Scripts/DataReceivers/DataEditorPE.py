def variableExporter():
    """
    VEUILLEZ CHOISIR LE MODE D EXPORT POUR LA CORRESPONDANCE DES NOMS DES DONNEES A L ADRESSE CORRESPONDANT AU BUS CAN
    VOUS DEVEZ CHOISIR UN MODE CSV OU DICTIONNARY
    SI VOUS CHOISISSEZ LE MODE CSV MERCI DE METTRE DE LE NOM DU FICHIER JUSTE EN DESSOUS
    """
    #CSV ou DICTIONNARY (copiez collez les motes)
    mode = "Dictionnary"

    #Si vous avez choisi le mode csv mettez le path du fichier /!\
    #format: [IDBUSCAN] [separator] [NAME]
    path = "testPE.csv"
    separator = ","

    #Si vous avez choisi le mode dico veuillez entrer votre table de correspondance ici
    addresSummary={
        0:"vitesse",
        1:"conso",
    }
    if mode == "CSV":
        print("mode csv sélectionné")
        dico = {}
        file = open(path,"r")
        for ligne in file:
            l = ligne.split(separator).replace('\n',"")
            dico[l[0]]=l[1]
        addresSummary = dico
    keys = []
    for key in addresSummary.keys():
        if str(key).isdigit():
            keys.append(key)
        else:
            print("error with key",key)
    maxi = max(keys)
    result = ["" for i in range(maxi+1)]
    for key in keys:result[key]=addresSummary[key]
    return result        
print(variableExporter())