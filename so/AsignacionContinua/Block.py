class Block:
    
    def __init__(self,inicio,fin):
        self.inicio = inicio
        self.fin = fin
        self.program = None
    
    def size(self):
        return self.fin - self.inicio +1
    
    def getProgram(self):
        return self.program
    
    def setProgram(self,program):
        self.program = program
    
    def getInicio(self):
        return self.inicio
    
    def setFin(self,fin):
        self.fin = fin
        
    def setInicio(self,inicio):
        self.inicio = inicio
    
    def getFin(self):
        return self.fin
    
    def getIsFree(self):
        return self.isFree
    
    
        
    
    