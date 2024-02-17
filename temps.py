class Temps():
    def get_temps(self, h, m, s):
        self.heures = h 
        self.minutes = m 
        self.secondes = s
        
    def __init__(self, h=0, m=0, s=0):
        self.get_temps(h, m, s)
        
    def get_heures(self):
        return self.heures
    
    def get_minutes(self):
        return self.minutes
    
    def get_secondes(self):
        return self.secondes
    
    def afficher(self):
        print(f"{self.heures}h {self.minutes}m {self.secondes}s")
        
    
    def ajouter_temps(self, t1, t2):
        self.secondes = t1.secondes + t2.secondes
        self.minutes = t1.minutes + t2.minutes + (int(self.secondes/60))
        self.heures = t1.heures + t2.heures + (int(self.minutes/60))
        self.minutes %= 60
        self.secondes %= 60
        
t1 = Temps()
t2 = Temps()
#t3 = Temps()
t1.get_temps(4,43,59)
t2.get_temps(1,20,32)
t1.get_heures()
t1.afficher()
t2.afficher()
#t3.ajouter_temps(t1, t2)
#t3.get_temps()