meme_dict = { 
    "CRINGE": "Algo excepcionalmente raro o embarazoso", 
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL" : "una respuesta a una broma", 
    "SHEESH": "ligera desaprobación", "XD": 
    "Respuesta a algo que da mucha risa" 
    }

word = input("Escribe la palabra q no entiendas :D")
word = word.upper()

if word in meme_dict.keys():
    print("el significado de " + word +" es " + meme_dict[word])
else:
    print("esta palabra no existe o esta mal escrita")
