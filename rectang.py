class Rectangle():
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def get_largeur(self):
        return self.largeur
    
    def get_hauteur(self):
        return self.hauteur 
    
    def set_largeur(self, new_largeur):
        self.largeur = new_largeur
    
    def set_hauteur(self, new_hauteur):
        self.hauteur = new_hauteur 
        
    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)
    
    def surface(self):
        return (self.largeur * self.hauteur)
    
    def afficher(self):
        print('La hauteur est: ', self.hauteur)
        print('La largeur est: ', self.largeur)
        
R = Rectangle(2, 3)
R.afficher()

print('Le périmetre est:', R.perimetre())
print('La surface est:', R.surface())