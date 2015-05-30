
import unittest
from clases.Cpu import Cpu
from clases.Pcb import Pcb
from clases.Instruction import Instruction
from clases.Memory import Memory
from clases.Window import Window
from clases.IrqKill import IrqKill
from clases.ReadyQueuePriority import ReadyQueuePriority
from clases.WaitingQueue import WaitingQueue 
from clases.QueuesManager import QueuesManager
from clases.MemoryManager import MemoryManager
from clases.FIFO import FIFO
from clases.IrqHandler import IrqHandler
from clases.IoWaitingQueue import IoWaitingQueue

class TestCpu(unittest.TestCase):
    cpu=None
    window=None
    inst=None
    mem=None
    pcb=None

    def setUp(self):
        self.window=Window()
        self.pcb=Pcb('proceso',1,0,1,0)
        self.pcb2=Pcb('proceso2',1,0,1,0)
        self.pcb3=Pcb('proceso3',1,0,1,0)
        self.inst=Instruction('hola',self.window)
        self.mem=Memory(20)
        self.mem.put(0, self.inst)
        self.readyQueue = ReadyQueuePriority()
        self.ioWaitingQueue =IoWaitingQueue()
        self.readyQueue.put(self.pcb2)
        self.readyQueue.put(self.pcb3)
        self.waitingQueue = WaitingQueue()
        self.queuesManager = QueuesManager(self.readyQueue,self.waitingQueue,self.ioWaitingQueue)
        self.politicaFIFO = FIFO(self.queuesManager)
        self.irqHandler = IrqHandler(self.politicaFIFO)
        self.memoryManager = MemoryManager(self.mem)
        self.cpu=Cpu(self.memoryManager,self.irqHandler)
        
        

    def tearDown(self):
        self.cpu=None
        self.window=None
        self.inst=None
        self.mem=None
        self.pcb=None


    def testFetch(self):
        self.cpu.setProcess(self.pcb)
        self.cpu.fetch()
        
        self.assertEqual(self.pcb.getPc(),1)
        self.assertEqual(self.window.getCantContents(),1)
        self.assertEqual(self.window.get(0), 'hola')
        self.assertEqual(self.cpu.getIrqHandler().cantIrqs(),1)
        self.assertTrue(isinstance(self.cpu.getIrqHandler().get(0), IrqKill))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()