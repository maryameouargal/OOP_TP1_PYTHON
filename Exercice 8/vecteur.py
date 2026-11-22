class Vecteur2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        # addition de deux vecteurs 
        return Vecteur2D(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre: 'Vecteur2D') -> 'Vecteur2D':
        # soustraction de deux vecteurs
        return Vecteur2D(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire: float) -> 'Vecteur2D':
        # multiplication par un nombre (scalaire)
        return Vecteur2D(self.x * scalaire, self.y * scalaire)

    def __eq__(self, autre: object) -> bool:
        # égalité 
        if not isinstance(autre, Vecteur2D):
            return False
        return self.x == autre.x and self.y == autre.y

    def __hash__(self):
        # nécessaire car on redéfinit __eq__ : on rend le vecteur utilisable dans un set
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Vecteur2D({self.x}, {self.y})"