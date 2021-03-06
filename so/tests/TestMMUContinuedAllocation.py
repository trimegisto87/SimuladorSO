import unittest

from AsignacionContinua.BestFit import BestFit
from AsignacionContinua.FirstFit import FirstFit
from AsignacionContinua.MMUContinuedAllocation import MMUContinuedAllocation
from AsignacionContinua.PhysicalMemoryContinuedAllocation import PhysicalMemoryContinuedAllocation
from AsignacionContinua.WorstFit import WorstFit
from IO.Window import Window
from Program.Instruction import Instruction
from Program.Program import Program


class TestMMUContinuedAllocation(unittest.TestCase):
    


    def setUp(self):
        self.memory1 = PhysicalMemoryContinuedAllocation(10)
        self.memory2 = PhysicalMemoryContinuedAllocation(10)
        self.memory3 = PhysicalMemoryContinuedAllocation(10)
        
        self.bestFit = BestFit()
        self.worstFit = WorstFit()
        self.firstFit = FirstFit()
        self.window = Window()
    
        self.mmubestFit = MMUContinuedAllocation(self.memory1,self.bestFit)
        self.mmuworstFit = MMUContinuedAllocation(self.memory2,self.worstFit)
        self.mmufirstFit = MMUContinuedAllocation(self.memory3,self.firstFit)
        
        instruction1=Instruction('hello',self.window)
        instruction2=Instruction('hello',self.window)
        instruction3=Instruction('hello',self.window)
        instruction4=Instruction('hello',self.window)
        instruction5=Instruction('hello',self.window)
        instruction6=Instruction('hello',self.window)
        
        
        self.program1 = Program('program1',instruction2,instruction1,instruction3)
        
        self.program2 = Program('program2',instruction4,instruction1,instruction2,instruction5)
        
        self.program3 = Program('program3',instruction1,instruction2,instruction3,instruction4,instruction5,instruction6)
    
    
    def testLoadProgram(self):
        
        #load de mmuBestFit
        
        self.assertEquals(self.memory1.getFreeSpace(),10)
        self.mmubestFit.loadProgram(self.program1)
        self.assertEquals(self.memory1.getFreeSpace(),7)
        self.mmubestFit.loadProgram(self.program3)
        self.assertEquals(self.memory1.getFreeSpace(),1)
        
        #load de mmuWorstFit
    
        self.assertEquals(self.memory2.getFreeSpace(),10)
        self.mmuworstFit.loadProgram(self.program2)
        self.assertEquals(self.memory2.getFreeSpace(),6)
        self.mmuworstFit.loadProgram(self.program3)
        self.assertEquals(self.memory2.getFreeSpace(),0)
        
        #load de mmuFirstFit
        self.assertEquals(self.memory3.getFreeSpace(),10)
        self.mmufirstFit.loadProgram(self.program1)
        self.assertEquals(self.memory3.getFreeSpace(),7)
        self.mmufirstFit.loadProgram(self.program3)
        self.assertEquals(self.memory3.getFreeSpace(),1)
        self.mmufirstFit.loadProgram(self.program3)
        self.assertEquals(self.memory3.getFreeSpace(),1)
        
    
    def testcleanMemory(self):
            
        #cleanMemory de mmuBestFit
        self.mmubestFit.loadProgram(self.program1)
        self.mmubestFit.loadProgram(self.program3)
        self.assertEquals(self.memory1.getFreeSpace(),1)
        self.mmubestFit.cleanMemory(self.program1)
        self.assertEquals(self.memory1.getFreeSpace(),4)
        
        self.mmubestFit.cleanMemory(self.program3)
        self.assertEquals(self.memory1.getFreeSpace(),10)
               
        #caso en que debe compactar
        self.mmubestFit.loadProgram(self.program1)
        self.mmubestFit.loadProgram(self.program2)
        self.mmubestFit.cleanMemory(self.program1)
        self.mmubestFit.loadProgram(self.program3)
        self.assertEquals(self.memory1.getFreeSpace(),0)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    