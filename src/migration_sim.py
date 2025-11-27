"""
Simulación de 'migración' a otro proceso.
NO inyecta código ni altera memoria — solo detecta procesos y escribe en log.
"""
import psutil
from .utils import log

def simulate_migration():
    log("Simulación: buscando procesos objetivo para 'migrar' (simulado).")
    targets = []
    for p in psutil.process_iter(attrs=['pid','name']):
        name = (p.info['name'] or "").lower()
        if any(k in name for k in ["notepad", "explorer", "code", "python"]):
            targets.append((p.info['pid'], p.info['name']))
    if targets:
        pid, name = targets[0]
        log(f"Simulación: elegiría PID {pid} ({name}) como objetivo para migrar.")
    else:
        log("Simulación: no se hallaron procesos 'interesantes' (simulado).")
