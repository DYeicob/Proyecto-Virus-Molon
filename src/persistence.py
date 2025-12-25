import os
import sys
from .utils import log

def simulate_persistence_windows():
    """
    Creates a reversible scheduled task that launches the script upon user logon.
    Visible and easily removable using: schtasks /delete /TN "MVS_Simulation"
    """
    try:
        # Get the absolute path of the current script
        this_py = os.path.abspath(sys.argv[0])
        
        # Construct the command to create a Scheduled Task
        # /SC ONLOGON: Trigger when the user logs in
        # /TN: Task Name
        # /TR: Task Run (command to execute)
        cmd = f'schtasks /Create /F /SC ONLOGON /TN "MVS_Simulation" /TR "{sys.executable} {this_py}"'
        
        os.system(cmd)
        log("Simulated Persistence: Scheduled task created (harmless).")
    except Exception as e:
        log(f"Simulated Persistence (Windows) failed: {e}")

def simulate_persistence_unix():
    """
    Simulated Persistence for Unix-like systems.
    To maintain safety, this does not automatically write to user profiles.
    """
    # In a real scenario, this would involve adding a line to ~/.bashrc or a crontab entry.
    log("Simulated Persistence (Unix): Proposes adding a harmless line to ~/.bashrc (NOT applied for safety).")
