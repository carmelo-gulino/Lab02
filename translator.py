import string

import dictionary as d

class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()

    def printMenu(self):
        print("------------------------------")
        print("   Translation Aline-Italian")
        print("------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("------------------------------")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as d:
            for riga in d:
                riga = riga.rstrip().split()
                self.dizionario.addWord(riga[0].lower(), riga[1].lower())
        return self.dizionario

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pAggiunte = [entry[0]]
        for i in range(1, len(entry)):
            pAggiunta = self.dizionario.addWord(entry[0], entry[i])
            if pAggiunta != None:
                pAggiunte.append(pAggiunta)
        return pAggiunte

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzione = self.dizionario.translate(query)
        return traduzione

    def checkPuntoInterrogativo(self, query):
        c=0
        for i in query:
            if i == "?":
                c+=1
        if c==1:
            return True
        else:
            return False

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        for lettera in string.ascii_lowercase:
            parola = query.replace("?", lettera)
            try:
                t = self.dizionario.translateWordWildCard(parola)
                return t
            except KeyError:
                return None

    def stampaDizionario(self):
        return self.dizionario.__repr__()

    def controllaInserimento(self, entry):
        if len(entry)>=2:
            for riga in entry:
                if self.controllaParola(riga)==False:
                    return False
            return True
        else:
            return False

    def controllaParola(self, query):
        for lettera in query:
            if lettera<"a" or lettera>"z":
                return False
        return True