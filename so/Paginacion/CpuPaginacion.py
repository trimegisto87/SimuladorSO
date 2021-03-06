import logging

from Irq.Irq import Irq
from clases.Cpu import Cpu


class CpuPaginacion(Cpu):

    def __init__(self,memoryManager,irqHandler):
        Cpu.__init__(self, memoryManager, irqHandler)
        
        
    def fetch(self):
        logging.debug('FETCHING.....')
        if(self.pcb != None):
            logging.info('Process: %s' % self.pcb.getName())
            actualBaseDirPage=self.pcb.getPages()
            
            instruccionActual =  self.memoryManager.getInstruction( actualBaseDirPage[0],self.pcb.getActualBaseDir())
            
            if(instruccionActual==None):
                return;
            self.actualInstruction=instruccionActual
            if(instruccionActual.isIO()):
                logging.info('fetching I/O instruction' )
                self.irqHandler.handle(Irq.io,self)
                return;
            logging.info('fetching CPU instruction' )
            instruccionActual.execute()
            self.pcb.incrementDir()
            if(self.memoryManager.isFinalInPage(actualBaseDirPage.__getitem__(0),self.pcb.getActualBaseDir())):
                self.pcb.setActualDir(0)
                self.pcb.getPages().pop() 
            if(self.pcb.getPages() == []):
                self.irqHandler.handle(Irq.kill,self)
                return;
        else:
            logging.info('No Process')
            self.callNext() 