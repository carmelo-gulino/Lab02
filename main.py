import translator as tr

t = tr.Translator()

c = 0
while(True):

    t.printMenu()
    if c==0:
        t.loadDictionary("dictionary.txt")

    # Add input control here!
    try:
        txtIn = input()
        if int(txtIn) == 1:
            print("Ok, quale parola devo aggiungere?\n")
            txtInStr = input().lower()
            entry = txtInStr.split()
            if t.controllaInserimento(entry):
                pAggiunte = t.handleAdd(entry)
                print(pAggiunte)
                print("Aggiunta!")
            else:
                print("Parola non valida")
        elif int(txtIn) == 2:
            print("Ok, quale parola devo tradurre?\n")
            txtIn = input()
            query = txtIn.lower()
            try:
                if t.controllaParola(query):
                    traduzione = t.handleTranslate(query)
            except KeyError:
                print("Parola non trovata")
        elif int(txtIn) == 3:
            print("Ok, quale parola devo cercare?\n")
            txtIn = input()
            query = txtIn.lower()
            if t.checkPuntoInterrogativo(query):
                traduzioni = t.handleWildCard(query)
                if traduzioni!=None:
                    print(traduzioni)
                else:
                    print("Parola non trovata")
            else:
                print("Inserire un punto interrogativo")
        elif int(txtIn) == 4:
            print(t.stampaDizionario())
        elif int(txtIn) == 5:
            break
        else:
            print("Comando non valido\n")
    except ValueError:
        print("Errore di input\n")
    c+=1


