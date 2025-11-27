"""
Simula propagación creando archivos de texto inocuos en unidades extraíbles detectadas.
NO copia ejecutables ni envía nada por la red.
"""
import os
from .utils import log

def simulate_propagation_usb():
    if os.name != "nt":
        log("Propagación simulada: demo implementada para Windows sólo.")
        return
    for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
        path = f"{letter}:\\"
        try:
            if os.path.exists(path):
                target = os.path.join(path, "MVS_SIMULADO_README.txt")
                with open(target, "w", encoding="utf-8") as f:
                    f.write("Simulación: archivo inocuo de propagación. No ejecutar.\n")
                log(f"Propagación simulada: archivo creado en {path}")
        except Exception as e:
            log(f"Propagación simulada: fallo en {path}: {e}")
