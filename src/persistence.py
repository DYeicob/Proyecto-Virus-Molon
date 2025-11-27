import os
import sys
from .utils import log

def simulate_persistence_windows():
    """
    Crea una tarea programada reversible que lanza el script al inicio de sesión.
    Visible y reversible mediante schtasks /delete.
    """
    try:
        this_py = os.path.abspath(sys.argv[0])
        cmd = f'schtasks /Create /F /SC ONLOGON /TN "MVS_Simulacion" /TR "{sys.executable} {this_py}"'
        os.system(cmd)
        log("Persistencia simulada: tarea programada creada (inofensiva).")
    except Exception as e:
        log(f"Persistencia simulada falló: {e}")

def simulate_persistence_unix():
    # No escribe automáticamente en perfiles para no tocar el sistema del usuario.
    log("Persistencia simulada (Unix): sugerir añadir linea inofensiva a ~/.bashrc (NO aplicada).")
