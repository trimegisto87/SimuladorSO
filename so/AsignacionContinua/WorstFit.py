from AsignacionContinua.RoutineBlock import RoutineBlock
class WorstFit(RoutineBlock):
    

    
    def blockFor(self,cantidad,listaDeBloques,mmu):
        list = filter(item.size > cantidad,listaDeBloques)#hay que ver que onda
        blockR = Block(1,100000000000000000000)
        for block in list:
            if(block.size > blockR.size):
                blockR = block
        
        
        mmu.sacarBloque(blockR)
        bloqueG  = super.recortarBLoque(blockR,pcb)
        bloqueP = super.bloquePequenioDe(bloqueG,blockR)
        mmu.agregarABloquesLibres(bloqueP)
        return blockG  