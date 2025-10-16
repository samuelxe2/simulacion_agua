# 💧 Simulación Multihilo del Consumo de Agua

Este proyecto simula el consumo y la reposición de agua utilizando **programación concurrente en Python**.  
Cada **persona** consume cierta cantidad de agua de una **jarra compartida**, mientras un **reabastecedor** la rellena cuando se agota.

La simulación se puede ejecutar en **dos modos distintos**:
1. **Modo Lock (Bloqueo Mutuo)**: usa un `Lock` para garantizar acceso exclusivo a la jarra.
2. **Modo Semaphore (Semáforo)**: usa un `Semaphore` que permite cierto grado de acceso simultáneo controlado.

---

## 📁 Estructura del proyecto

simulacion_agua/
│
├── main.py # Ejecuta la simulación (elige modo Lock o Semaphore)
├── jarra.py # Clase Jarra: almacena el nivel de agua
├── persona.py # Clase Persona: simula el consumo de agua
├── reabastecedor.py # Clase Reabastecedor: repone el agua
├── init.py # Marca el paquete como módulo de Python
└── requirements.txt # Dependencias del proyecto

yaml
Copiar código

---

## ⚙️ Requisitos

- Python **3.10 o superior**
- No requiere librerías externas (usa solo módulos estándar)
  
Para entornos más vistosos o pruebas automáticas, puedes instalar opcionalmente:
```bash
pip install rich colorlog pytest
🚀 Ejecución
Abre una terminal en la carpeta del proyecto y ejecuta:

🔒 Modo Lock (bloqueo mutuo)
bash
Copiar código
python main.py lock
🚦 Modo Semaphore (semáforo)
bash
Copiar código
python main.py semaphore
Durante la ejecución, verás mensajes como:

csharp
Copiar código
[Persona-1] consumió 2L. Nivel actual: 8L
[Persona-2] consumió 3L. Nivel actual: 5L
[Reabastecedor] repuso 5L. Nivel actual: 10L
🧠 Conceptos clave
Threading: cada persona y el reabastecedor son hilos independientes.

Lock: asegura exclusión mutua; un solo hilo puede usar la jarra a la vez.

Semaphore: permite acceso controlado de múltiples hilos simultáneamente.

Sincronización: garantiza que no se produzcan inconsistencias en el nivel de agua.

🧩 Ejemplo de salida esperada (modo Lock)
csharp
Copiar código
Simulación en modo LOCK iniciada.
[Persona-1] consumió 2L. Nivel actual: 8L
[Persona-2] consumió 3L. Nivel actual: 5L
[Reabastecedor] repuso 5L. Nivel actual: 10L
Simulación finalizada.
📘 Créditos
Autor: Samuel Sánchez Peña
Carrera: Ingeniería de Sistemas
Fecha: Octubre 2025

Proyecto académico sobre concurrencia y sincronización en Python.

🧾 Licencia
Este proyecto se distribuye bajo la licencia MIT, lo que permite su libre uso y modificación con fines académicos o personales.
