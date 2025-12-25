"""
Client that performs direct beaconing to the C2 server (no proxies) at regular intervals.
Receives benign commands via JSON: {"cmd":"rickroll"}, etc.
"""
import requests
import time
from .utils import log
from .killswitch import is_killswitched
from .payloads import rickroll, popup_message

# Replace with your lab public IP or hostname
C2_URL = "http://<YOUR_PUBLIC_IP_OR_HOST>:5000/c2"  
AGENT_ID = "simulated_victim_01"
BEACON_INTERVAL = 5

def beacon_loop(max_duration_sec=60):
    """
    Main loop that polls the C2 server for instructions.
    Terminates if the killswitch is found or the maximum duration is reached.
    """
    start = time.time()
    while time.time() - start < max_duration_sec:
        if is_killswitched():
            log("Killswitch active: exiting beacon loop.")
            return
            
        try:
            # Send the POST request with the agent identifier
            r = requests.post(C2_URL, json={"agent": AGENT_ID}, timeout=4)
            
            if r.status_code == 200:
                data = r.json()
                cmd = data.get("cmd")
                
                if cmd:
                    log(f"C2: Received command '{cmd}'")
                    if cmd == "rickroll":
                        rickroll()
                    elif cmd == "popup":
                        popup_message()
                    else:
                        log(f"Unknown command: {cmd}")
            else:
                log(f"C2: HTTP response {r.status_code}")
                
        except Exception as e:
            log(f"C2: Beacon failure: {e}")
            
        # Wait for the next polling interval
        time.sleep(BEACON_INTERVAL)
