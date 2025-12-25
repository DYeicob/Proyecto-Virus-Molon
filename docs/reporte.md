# 📄 **FULL PROJECT REPORT – *molon-virus-project***

## 🧩 **1. Introduction**

This project is an **educational simulation** inspired by the architecture of real modular malware. It is implemented strictly using **safe, controlled, and harmless actions**.
Its purpose is to **study offensive and defensive cybersecurity techniques**, demonstrating:

* The modular architecture of a malicious agent.
* Command & Control (C2) infrastructure and communication.
* Common techniques such as persistence, infection emulation, fileless execution, mock ransomware, propagation, and social engineering.
* Real-world detection and mitigation strategies.

No component executes harmful actions. The project is designed to be executed in an **isolated virtual machine** for academic purposes.

---

# 🗂️ **2. Project Structure**

```text
molon-virus-project/
│
├── src/
│   ├── agent.py            # Main orchestrator
│   ├── migration_sim.py    # Process enumeration logic
│   ├── fileless_sim.py     # LOLBAS emulation
│   ├── persistence.py      # Harmless persistence (Scheduled Tasks)
│   ├── propagation.py      # USB discovery logic
│   ├── c2_client.py        # Beaconing & Polling logic
│   ├── killswitch.py       # Emergency stop mechanism
│   ├── payloads.py         # Benign actions (Rickroll, Popups)
│   └── utils.py            # Logging & timestamp utilities
│
├── server_c2/
│   ├── server.py           # Flask-based C2 Dashboard
│   └── requirements.txt
│
├── phishing_demo/
│   ├── email.html          # Social engineering lure
│   └── web_cringe/         # Mock credential harvesting page
│
├── docs/                   # Full English Documentation
│   ├── report.md
│   ├── ethical_limitations.md
│   └── run_instructions.md
│
├── tests/                  # Integrity & Logic testing
│   ├── test_killswitch.py
│   └── test_c2.py

```

---

# 🧪 **3. Detailed Module Description**

### **🧠 agent.py — Main Orchestrator**

Coordinates the entire lifecycle: loads modules, sends beacons to the C2, executes benign instructions, and constantly verifies the *killswitch* status.

### **🔀 migration_sim.py — Process Migration Emulation**

Demonstrates how malware "jumps" between processes. It enumerates running tasks (like `explorer.exe`) and logs which process would be targeted for injection in a real scenario.

### **🧬 fileless_sim.py — Fileless Execution (Benign LOLBAS)**

Mimics fileless malware by executing commands directly through system shells (PowerShell/Bash) without writing malicious binaries to disk.

### **📌 persistence.py — Persistence Simulation**

Implements visible and reversible persistence mechanisms (Scheduled Tasks on Windows or `.bashrc` entries on Linux) to demonstrate how threats survive reboots.

### **🔗 propagation.py — Simulated USB Propagation**

Identifies connected volumes and creates a **harmless text file** to illustrate how worms move laterally through removable media.

### **📡 c2_client.py — Command & Control Communication**

Handles periodic beacons and polls the Flask server for tasks such as displaying alerts, triggering the Rickroll, or simulating educational ransomware.

### **🛑 killswitch.py — Emergency Stop**

Monitors for a specific file (`stop.txt`). If detected, it immediately terminates the agent, demonstrating how researchers can neutralize global threats.

---

## **3.2. /server_c2 — Command and Control Server**

### **🖥️ server.py — Flask C2**

A centralized dashboard to monitor connected agents, deploy benign commands, and review execution logs in real-time.

---

## **3.3. /phishing_demo — Social Engineering Assets**

### **📧 email.html & 🌐 web_cringe/**

Mock assets designed to teach users how to identify suspicious links, poor UX, and psychological triggers used in phishing campaigns.

---

# 🛡️ **4. Ethical Safeguards & Risks**

To ensure total safety, the project **DOES NOT include:**
❌ Real encryption | ❌ Vulnerability exploits | ❌ Privilege escalation | ❌ Real process injection | ❌ Destructive payloads | ❌ Data exfiltration.

Everything is designed following **Academic Best Practices** and **Ethical Hacking Codes of Conduct**.

---

# 📦 **5. Conclusion**

This project serves as a comprehensive tool for understanding the modular architecture of modern threats. By building each stage of the lifecycle—from initial access to C2 coordination—I have gained a deep understanding of adversarial behavior and the defensive layers required to mitigate them.
