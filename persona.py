import threading
import time
import random
from jarra import Jarra


class Persona(threading.Thread):
    """Hilo que representa a una persona que intenta beber agua."""

    def __init__(self, nombre: str, jarra: Jarra):
        super().__init__(name=nombre)
        self._jarra = jarra

    def run(self) -> None:
        cantidad = random.randint(100, 300)
        time.sleep(random.uniform(0.2, 1.0))
        self._jarra.beber(cantidad, self.name)
