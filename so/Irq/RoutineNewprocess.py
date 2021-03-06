from Irq.Irq import Irq
from Irq.PidGenerator import PidGenerator
from Irq.Routine import Routine
from Program.Pcb import Pcb
from SchedullingAndQueuesManager.SchedulingLargePolitic import SchedullingLargePolitic
from Paginacion.PcbPaginacion import PcbPaginacion
import logging


class RoutineNewprocess(Routine):
    
    def __init__(self):
        self.pidGenerator=PidGenerator()
        self.largePolitic=SchedullingLargePolitic()
    
    def canHandle(self, irq):
        Routine.canHandle(self, irq)
        return irq==Irq.newProcess
    
    def handle(self,irq,cpu,program=None,ioInstruction=None):
        logging.debug('Running New Process Interruption')
        Routine.handle(self, irq,cpu,program,ioInstruction)
        if(cpu.getMemoryManager().loadProgram(program)):
            pcb=self.generateProcess(program,cpu)
            self.largePolitic.handleReadyProcess(pcb, cpu.getQueuesManager())
        else:
            self.largePolitic.handleWaitingProgram(program, cpu.queuesManager)
        
        
    def generateProcess(self,program,cpu):
        name=program.getName()
        pid=self.pidGenerator.generateNewPid()
        pc=0
        finalPc=program.getInstructionsCount()-1
        if(cpu.getMemoryManager().esContinua()):
            baseDir=cpu.getMemoryManager().getMemory().getNextIndex()
            return Pcb(name,pid,pc,finalPc,baseDir)
        else:
            baseDirs=program.getBaseDirs()
            return PcbPaginacion(name,pid,pc,finalPc,baseDirs)
    
   
    