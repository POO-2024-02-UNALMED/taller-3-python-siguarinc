from televisores.marca import Marca
from televisores.control import Control
class TV:
    _numTV=0
    def __init__(self, marca, estado):
        self._marca= marca
        self._estado= estado
        self._canal= 1
        self._precio= 500
        self._volumen= 1
        self._control= None
        TV._numTV+=1
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self, m):
        self._marca= m

    def getCanal(self):
        return self._canal
    
    def setCanal(self, c):
        if self._estado==True:
            if c>=1 and c<=120:
                self._canal=c

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, p):
        self._precio= p

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, v):
        if self._estado==True:
            if v>=1 and v<=7:
                self._volumen=v

    def getControl(self):
        return self._control
    
    def setControl(self, c):
        self._control= c

    def turnOn(self):
        self._estado=True

    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if(self._estado==True):
            if(self._canal>=1 and self._canal<120):
                self._canal+=1
    
    def canalDown(self):
        if(self._estado==True):
            if(self._canal>1 and self._canal<=120):
                self._canal-=1
    
    def volumenUp(self):
        if(self._estado==True):
            if(self._volumen>=0 and self._volumen<7):
                self._volumen+=1
    
    def volumenDown(self):
        if(self._estado==True):
            if(self._volumen>0 and self._volumen<=7):
                self._volumen-=1

    @classmethod
    def setNumTV(cls,nt):
        cls._numTV=nt
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    




    


