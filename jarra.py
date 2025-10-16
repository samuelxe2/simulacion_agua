import threading
import logging
import time
import random


class Jarra:
    """Recurso compartido que representa una jarra de agua."""

    def __init__(self, capacidad_inicial: int, modo: str = "lock", max_concurrentes: int = 1):
        """
        :param capacidad_inicial: Cantidad inicial de agua en ml
        :param modo: 'lock' o 'semaphore'
        :param max_concurrentes: Número máximo de hilos concurrentes en modo semáforo
        """
        self._agua_disponible = capacidad_inicial
        self._capacidad_maxima = capacidad_inicial
        self._modo = modo.lower()

        if self._modo == "semaphore":
            self._sync = threading.Semaphore(max_concurrentes)
        else:
            self._sync = threading.Lock()

    def beber(self, cantidad: int, nombre: str) -> None:
        """Sección crítica controlada por Lock o Semaphore."""
        with self._sync:
            if self._agua_disponible >= cantidad:
                logging.info(f"{nombre} está bebiendo {cantidad} ml de agua.")
                time.sleep(random.uniform(0.1, 0.5))
                self._agua_disponible -= cantidad
                logging.info(f"Agua restante: {self._agua_disponible} ml.")
            else:
                logging.info(f"{nombre} quiso beber {cantidad} ml, pero no hay suficiente agua.")

    def recargar(self, cantidad: int) -> None:
        """Permite al reabastecedor agregar agua."""
        with self._sync:
            if self._agua_disponible < self._capacidad_maxima:
                recarga_real = min(cantidad, self._capacidad_maxima - self._agua_disponible)
                self._agua_disponible += recarga_real
                logging.info(f"🔄 Jarra recargada con {recarga_real} ml. Nivel actual: {self._agua_disponible} ml.")
            else:
                logging.info("⚠️ La jarra ya está llena, no se recargó.")
