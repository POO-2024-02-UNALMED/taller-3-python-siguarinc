from televisores.marca import Marca
from televisores.control import Control
class TV:
    numTV=0
    def __init__(self, marca,canal,precio,estado,volumen,control):
        self.marca= marca
        self.canal= 1
        self.precio= 500
        self.estado= estado
        self.volumen= 1
        self.control= control
    def __init__(self, marca, estado):
        self.marca= marca
        self.estado= estado

    def getMarca(self):
        return self.marca
    
    def setMarca(self, m):
        self.marca= m

    def getCanal(self):
        return self.canal
    
    def setCanal(self, c):
        if(self.estado==True):
            if (c>=1 and c<=120):
                self.canal=c

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, p):
        self.precio= p

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, v):
        if(self.estado==True):
            if (v>=1 and v<=7):
                self.volumen=v

    def getControl(self):
        return self.control
    
    def setControl(self, c):
        self.control= c
        
    def turnOn(self):
        self.estado=True

    def turnOff(self):
        self.estado=False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if(self.estado==True):
            if(self.canal>=1 and self.canal<120):
                self.canal+=1
    
    def canalDown(self):
        if(self.estado==True):
            if(self.canal>1 and self.canal<=120):
                self.canal-=1
    
    def volumenUp(self):
        if(self.estado==True):
            if(self.volumen>=0 and self.volumen<7):
                self.volumen+=1
    
    def volumenDown(self):
        if(self.estado==True):
            if(self.volumen>0 and self.volumen<=7):
                self.volumen-=1

    @classmethod
    def setNumTV(cls,nt):
        cls.numTV=nt
    def getNumTV(cls):
        return cls.numTV
    
    




    


