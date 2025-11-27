"""
Cliente que hace beaconing directo al servidor C2 (sin proxys), en intervalos.
Recibe comandos benignos en JSON: {"cmd":"rickroll"} etc.
"""
import requests
import time
from .utils import log
from .killswitch import is_killswitched
from .payloads import rickroll, popup_message

C2_URL = "http://<TU_IP_PUBLICA_O_HOST>:5000/c2"  # sustituye por tu IP/host de laboratorio
AGENT_ID = "victima_simulada_01"
BEACON_INTERVAL = 5

def beacon_loop(max_duration_sec=60):
    start = time.time()
    while time.time() - start < max_duration_sec:
        if is_killswitched():
            log("Killswitch activo: saliendo de beacon loop.")
            return
        try:
            r = requests.post(C2_URL, json={"agent": AGENT_ID}, timeout=4)
            if r.status_code == 200:
                data = r.json()
                cmd = data.get("cmd")
                if cmd:
                    log(f"C2: recibido comando '{cmd}'")
                    if cmd == "rickroll":
                        rickroll()
                    elif cmd == "popup":
                        popup_message()
                    else:
                        log(f"Comando desconocido: {cmd}")
            else:
                log(f"C2: respuesta HTTP {r.status_code}")
        except Exception as e:
            log(f"C2: fallo en beacon: {e}")
        time.sleep(BEACON_INTERVAL)
