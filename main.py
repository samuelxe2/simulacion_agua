import logging
from typing import List
from jarra import Jarra
from persona import Persona
from reabastecedor import Reabastecedor


def configurar_logger() -> None:
    """Configura el formato del logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)s] %(message)s",
        datefmt="%H:%M:%S"
    )


def ejecutar_simulacion(modo: str) -> None:
    """Ejecuta la simulación en el modo indicado."""
    configurar_logger()
    modo = modo.lower()

    if modo not in ("lock", "semaphore"):
        logging.error("Modo inválido. Usa 'lock' o 'semaphore'.")
        return

    logging.info(f"🏁 Iniciando simulación en modo: {modo.upper()}\n")

    jarra = Jarra(capacidad_inicial=1000, modo=modo, max_concurrentes=2)
    personas: List[Persona] = [Persona(f"Persona-{i+1}", jarra) for i in range(6)]
    recargador = Reabastecedor(jarra, cantidad_recarga=400, intervalo=4)

    recargador.start()
    for persona in personas:
        persona.start()

    for persona in personas:
        persona.join()

    recargador.detener()
    recargador.join()

    logging.info(f"\n✅ Simulación finalizada (modo {modo.upper()}).")


if __name__ == "__main__":
    # --- Selección del modo ---
    print("=== Simulación Multihilo del Consumo de Agua ===")
    print("1. Modo LOCK (exclusión total)")
    print("2. Modo SEMAPHORE (acceso concurrente controlado)\n")

    opcion = input("Seleccione el modo [1/2]: ").strip()
    modo = "lock" if opcion == "1" else "semaphore"

    ejecutar_simulacion(modo)
