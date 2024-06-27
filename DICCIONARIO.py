cheetosenbabilonia = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "RIZZ": "Una persona carismatica, o que tenga abilidad de atraer a otras personas",
            "NIGGARDLY": "Una persona no generosa con el dinero, avariciosas",
            "BABELICO": "Algo relativo a la torre de Babel, o algo confuso e unintelegible",
            "BAHORRINA": "Algo sucio",
            "CREEPY": "Algo que asuste",
            "SHEESH": "Sorpresa, algo que no seria facil.",
            "FUL": "Algo fallido o falso"
            }
print("Hola, yo te voy a ayudar con unas pocas palabras que no sepas.")
names = input("Pero primero, escribe tu nombre")
print("Hola",names,"!")
print("Ahora", names ,", añade 5 palabras que no sepas.")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
    if word in cheetosenbabilonia.keys():
        print(cheetosenbabilonia[word])
    else:
        print("Esta palabra nisiquiera yo la conozco")
