from __future__ import annotations
class Marca:
    def __init__(self,nombre):
        self._nombre=nombre

    def getNombre(self):
        return self._nombre
    def setNombre(self, n):
        self._nombre= n