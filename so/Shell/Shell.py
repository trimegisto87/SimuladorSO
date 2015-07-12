from os.path import os


class Shell():

    def __init__(self, kernel,commandHandler):
        self.kernel=kernel
        self.commandHandler=commandHandler
        self.successCommands=[]
        os.chdir("C:/")
        self.root = os.getcwd()
        
    def readCommand(self,command,param= None,file=None):
        success=self.commandHandler.handle(command,param,self,file)
        self.addOrDiscard(success,command) 
        return success
    
    def addOrDiscard(self,success,command):
        if(success):
            self.successCommands.append(command)
            
    def successCommandCount(self):
        return self.successCommands.__len__()
    
    def getSuccessCommands(self):
        return self.successCommands
    
    def showData(self,data):
        print(data)
        
    def getKernel(self):
        return self.kernel