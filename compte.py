class Compte():
    def __init__(self, balance=0):
        self.balance = balance
        
    def get_balance(self):
        return self.balance
    
    def deposer(self, montant):
        self.balance += montant
    
    def retirer(self, montant):
        self.balance -= montant
    
    def ajouter_interet(self, taux_i):
        self.balance *= (1+ taux_i)
        
compte1 = Compte()
compte2 = Compte(3000)
compte1.deposer(100)
compte2.retirer(1000)
compte1.ajouter_interet (0.3)
print(compte1.get_balance())
print(compte2.get_balance())      
  
