import threading
import time
from jarra import Jarra


class Reabastecedor(threading.Thread):
    """Hilo que recarga la jarra periódicamente."""

    def __init__(self, jarra: Jarra, cantidad_recarga: int, intervalo: float = 3.0):
        super().__init__(name="Reabastecedor")
        self._jarra = jarra
        self._cantidad_recarga = cantidad_recarga
        self._intervalo = intervalo
        self._activo = True

    def run(self) -> None:
        while self._activo:
            time.sleep(self._intervalo)
            self._jarra.recargar(self._cantidad_recarga)

    def detener(self) -> None:
        self._activo = False
