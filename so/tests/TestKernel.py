'''
Created on 15/05/2015

@author: apiorno
'''
import unittest


from clases.Cpu import Cpu
from clases.Disk import Disk

from clases.Kernel import Kernel
from clases.Memory import Memory
from clases.Program import Program
from clases.Window import Window
from clases.Instruction import Instruction
from clases.MemoryManager import MemoryManager




class Test(unittest.TestCase):
    
    kernel=None
    cpu=None
    disk=None
    memory=None
    memoryManager=None
    queuesManager=None
    instruction=None
    window=None
    program=None


    def setUp(self):
        self.window=Window()
        self.instruction=Instruction('hola',self.window)
        self.program=Program('cacho',self.instruction)
        self.disk=Disk()
        self.disk.addProgram(self.program)
        self.memory = Memory(20)
        self.memoryManager = MemoryManager(self.memory)
        self.cpu = Cpu(self.memory)
        self.kernel=Kernel(self.cpu,self.disk,self.memoryManager,self.queuesManager)


    def loadTest(self):
        self.disk.addProgram(self.program)
        self.kernel.loadProgram(self.program)
        self.assertEqual(self.memory.freeSpace,19)



    def runTest(self):
        self.kernel.runProgram(self.program.getName())
        self.assertEqual(self.cpu.pcb,self.kernel.generateProcess(self.program))
        #Resvisa el assert, estas comparando dos instancias distintas y ademas accedes sin getter.
        
    def generateProcessTest(self):
        pcb=self.kernel.generateProcess(self.program)
        self.assertEqual(pcb.getFinalPc(),self.program.getInstructionsCount())
        self.assertEqual(pcb.getPc(),0)
        self.assertEqual(pcb.getName(),self.program.getName())
        

    def tearDown(self):
        self.kernel=None
        self.cpu=None
        self.disk=None
        self.memory=None
        self.memoryManager=None
        self.queuesManager=None
        self.instruction=None
        self.window=None
        self.program=None


    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()