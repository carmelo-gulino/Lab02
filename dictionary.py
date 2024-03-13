import translator as tr
class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, pAliena, pItaliana):
        try:
            if pItaliana not in self.dizionario[pAliena]:
                self.dizionario[pAliena].append(pItaliana)
                return pItaliana
            else:
                print(f"'{pItaliana}' già presente")
        except KeyError:
            self.dizionario[pAliena] = []
            self.dizionario[pAliena].append(pItaliana)
            return pItaliana

    def translate(self, pAliena):
        return self.dizionario[pAliena]

    def translateWordWildCard(self, parola):
        return self.dizionario[parola]

    def __repr__(self):
        elenco = ""
        for key in self.dizionario:
            elenco += key + " = "
            for parola in self.dizionario[key]:
                elenco += parola+" "
            elenco+="\n"
        return elenco

    def __getitem__(self, item):
        return self.dizionario[item]