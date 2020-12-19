def variableExporter():
    """
    VEUILLEZ CHOISIR LE MODE D EXPORT POUR LA CORRESPONDANCE DES NOMS DES DONNEES A L ADRESSE CORRESPONDANT AU BUS CAN
    VOUS DEVEZ CHOISIR UN MODE CSV OU DICTIONNARY
    SI VOUS CHOISISSEZ LE MODE CSV MERCI DE METTRE DE LE NOM DU FICHIER JUSTE EN DESSOUS
    """
    #CSV ou DICTIONNARY (copiez collez les motes)
    mode = "Dictionnary"

    #Si vous avez choisi le mode csv mettez le path du fichier /!\
    #format: idBUSCANseparatorNAME
    path = "test.csv"
    separator = ","

    #Si vous avez choisi le mode dico veuillez entrer votre table de correspondance ici
    addresSummary={
        0:"timestamp",
        1:"VR1",
        2:"VR2",
        3:"VR3",
        4:"VR4",
        5:"V",
        6:"TR1",
        7:"TR2",
        8:"TR3",
        9:"TR4",
        10:"TM1",
        11:"TM2",
        12:"TM3",
        13:"TM4",
        14:"V1",
        15:"V2",
        16:"V3",
        17:"V4",
        18:"V5",
        19:"V6",
        20:"V7",
        21:"V8",
        22:"V9",
        23:"VS",
        24:"C1",
        25:"C2",
        26:"C3",
        27:"C4",
        28:"C5",
        29:"C6",
        30:"C7",
        31:"C8",
        32:"C9",
        33:"CS",
        34:"T1",
        35:"T2",
        36:"T3",
        37:"T4",
        38:"T5",
        39:"T6",
        40:"T7",
        41:"T8",
        42:"T9",
        43:"TS",
        44:"Long",
        45:"Lat"
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