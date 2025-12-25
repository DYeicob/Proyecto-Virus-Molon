import time
from pathlib import Path

# Path to the log file used for recording simulation events
LOGFILE = Path("mvs_sim.log")

def log(msg):
    """
    Records an event message with a timestamp to both the console and a local log file.
    Essential for forensic tracking and simulation auditing.
    """
    # Generate a standard ISO-like timestamp
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] {msg}"
    
    # Print to standard output (console)
    print(line)
    
    # Append the log entry to the log file using UTF-8 encoding
    with LOGFILE.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
