"""
Main agent orchestrating the simulation.
Covers: Simulated infection, simulated fileless execution, harmless persistence,
simulated propagation, C2 beaconing, payload trigger in <60s, and killswitch check.
"""
from .utils import log
from .killswitch import is_killswitched
from .migration_sim import simulate_migration
from .fileless_sim import simulate_fileless
from .persistence import simulate_persistence_windows, simulate_persistence_unix
from .propagation import simulate_propagation_usb
from .c2_client import beacon_loop
from .payloads import rickroll

import time, os

def main():
    log("=== MolonVirusSim (simulated agent) starting ===")
    
    # Check for the emergency stop trigger
    if is_killswitched():
        log("Killswitch detected. Aborting execution.")
        return

    # 1. Entry Vector / Simulated Click
    log("Entry Vector: Simulated 'cringe' phishing/web lure. Downloading harmless executable.")
    
    # 1a. Simulated 'Migration' (Process injection emulation)
    simulate_migration()
    
    # 1b. Simulated Fileless Execution (LOLBAS emulation)
    simulate_fileless()

    # 2. Persistence (Harmless implementation)
    if os.name == "nt":
        simulate_persistence_windows()
    else:
        simulate_persistence_unix()

    # 3. Simulated Propagation (USB infection emulation)
    simulate_propagation_usb()

    # 4. C2: Beacon loop for a maximum of 60s; executes command if received
    # This aligns with the 'Direct Connection' and 'Time Limit' rules
    beacon_loop(max_duration_sec=60)

    # 5. Default Payload if no C2 command was received within the 60s window
    if not is_killswitched():
        log("No C2 command received. Triggering default payload.")
        rickroll()

    log("=== MolonVirusSim (simulated agent) finished ===")

if __name__ == "__main__":
    main()
