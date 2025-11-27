from pathlib import Path
from .utils import log

KILLSWITCH_PATH = Path(r"C:\killswitch_mvs.txt")  # documentado en informe

def is_killswitched():
    if KILLSWITCH_PATH.exists():
        log(f"KILLSWITCH DETECTADO: {KILLSWITCH_PATH}")
        return True
    return False
