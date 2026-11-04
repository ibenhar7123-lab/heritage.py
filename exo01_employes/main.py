import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo01_employes.employe import Employe
from exo01_employes.manager import Manager
from exo01_employes.developpeur import Developpeur

e = Employe("Alice", 2000)
m = Manager("Bob", 2500, 800)
d = Developpeur("Charlie", 2200, "Python")

for personne in [e, m, d]:
    print(personne)
# Alice gagne 2000 €
# Bob gagne 3300 €
# Charlie gagne 2700 €
