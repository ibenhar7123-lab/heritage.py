from .employe import Employe


class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        super().__init__(nom, salaire_base)
        self.prime = prime

    def salaire_total(self):
        return self.salaire_base + self.prime
