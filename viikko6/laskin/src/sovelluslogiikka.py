class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = []

    def miinus(self, operandi):
        self._edellinen_arvo.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edellinen_arvo.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edellinen_arvo.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        if self._edellinen_arvo:
            self._arvo = self._edellinen_arvo.pop()

    def arvo(self):
        return self._arvo
