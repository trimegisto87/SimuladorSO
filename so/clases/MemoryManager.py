class MemoryManager:
    
    def __init__(self,memory):
        self.memory=memory
       
    def getMemory(self):
        return self.memory
    
    def addinstructionsToMemory(self,program):
        if(self.memory.freeSpace()>=program.getInstructionsCount()):       
            for instruction in program.getInstructions():
                index=self.memory.getNextIndex() 
                self.memory.put(index,instruction)
            return True;   
        else:
            return False
    
    def memoryFree(self):
        return self.memory.freeSpace()
