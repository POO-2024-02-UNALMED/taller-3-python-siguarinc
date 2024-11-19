from televisores.tv import TV
class Control:
    def __init__(self,tv):
        self.tv=tv 

    def turnOn(self,tv):
        tv.turnOn()

    def turnOff(self,tv):
        tv.turnOff()

    def canalUp(self,tv):
        tv.canalUp()

    def canalDown(self,tv):
        tv.canalDown()

    def volumenUp(self,tv):
        tv.volumenUp()

    def volumenDown(self,tv):
        tv.volumenDown()

    def setCanal(self,c,tv):
        tv.setCanal(c)

    def setVolumen(self,v,tv):
        tv.setVolumen(v)
    
    def enlazar(self,tv):
        self.tv=tv
        tv.setContro(self)
    
    @classmethod  
    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv=tv
