import webbrowser, os, subprocess
from .utils import log

def rickroll():
    """
    Simulated Payload: Opens a safe URL in the default browser.
    Mimics 'Actions on Objectives' without causing actual harm.
    """
    log("Payload: Executing safe Rickroll. Opening browser.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def popup_message():
    """
    Simulated Payload: Displays a benign message box (Windows only).
    Demonstrates the ability to interact with the UI of the target host.
    """
    log("Payload: Attempting to display harmless popup (Windows only).")
    if os.name == "nt":
        try:
            # Using PowerShell to invoke a system message box
            # This is a common LOLBAS technique to interact with the user
            subprocess.run([
                "powershell", "-NoProfile", "-Command",
                '[System.Windows.MessageBox]::Show("MVS Simulation! (harmless)")'
            ], shell=True, check=False)
            log("Popup displayed successfully (simulated).")
        except Exception as e:
            log(f"Popup execution failed: {e}")
    else:
        log("Popup not supported on this OS - skipping execution.")
