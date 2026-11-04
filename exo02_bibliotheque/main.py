import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo02_bibliotheque.livre import Livre
from exo02_bibliotheque.magazine import Magazine

docs = [
    Livre("1984", 1949, "George Orwell"),
    Magazine("Science & Vie", 2023, 456),
    Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"),
]

for d in docs:
    d.afficher()
