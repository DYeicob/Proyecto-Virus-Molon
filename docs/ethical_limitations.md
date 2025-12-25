# ⚖️ Ethical and Technical Limitations

The following techniques were **deliberately excluded** from this project for safety and ethical reasons:

* **Memory Code Injection:** Techniques such as thread/process injection and process hollowing were avoided to prevent actual interference with system memory.
* **Kernel-Level Modifications:** No rootkits or kernel modifications were implemented.
* **Boot & Hardware Modification:** Modifying the bootloader process or reflashing the UEFI was excluded to avoid the risk of "bricking" or causing irreversible damage to the hardware.
* **Active Propagation:** Real-world spreading via email, WhatsApp, SMB, or wireless networks was strictly prohibited to prevent the simulation from escaping the laboratory environment.
* **Advanced Anti-Forensics:** Forensic evasion techniques and hiding data within the swap partition were excluded.

> **Note:** These techniques are outside the scope of this academic project because they are inherently dangerous, can cause irreversible system damage, and require specific legal authorizations and highly controlled environments.
