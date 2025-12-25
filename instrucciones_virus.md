# 🛠️ What Should a "Cool" Virus Do?

## 1. Infection (Make sure deleting your file doesn't stop it)
Enter through a fun vector—create a ridiculous phishing email or one of those "cringe" websites you guys are so good at. Make it download "the bug."

* **Method A:** Infect another process (**Migration**), e.g., by injecting a thread into its memory space.
* **Method B:** Go **Fileless** (LOLBAS).



## 2. Persistence and Stealth (Make sure reboots don't stop it)
Register a scheduled task, hide in the registry, or use the `motd` (Linux has some pretty ridiculous systems for achieving persistence). Ensure the bug executes every time the machine restarts.
If you want to be truly evil, overwrite the machine's boot process to survive system restores (or reflash the UEFI to survive a format xd).

You can use a **Rootkit** to mess with the AVs; if you hide in the swap space, you'll be able to evade most forensic analysts.



## 3. Propagation [Optional] (Make it replicate)
Send emails, copy yourself to USB drives, attack Wi-Fi networks, SMB, shared folders, send WhatsApp messages—whatever you feel like. This point is 100% optional since it won't be evaluated.

## 4. C2 (Make sure you know you've successfully infected)
Contact a public IP you own without being detected. You can use **beaconing**, encryption, etc. Here, you can code a super cool control panel that allows you to execute actions on the victims.



## 5. Payload (The fireworks)
When the ideal conditions are met (at most 60s from the initial click), your virus must do something. That "something" could be changing the desktop background, playing a Rickroll, or encrypting all the files on the machine...

---

## 📜 Rules:

* **No Proxies or Tor:** That’s cheating. Direct connection to the C2 only. This IP must be permanently active and must not filter access to any port by IP, country, etc. No hiding behind CDNs.
* **No Time Bombs:** Everything must happen within a maximum of 60 seconds from the initial click (if the payload is coded in the C2, it must have a bot that sends the action in under 60 seconds).
* **Documentation:** You cannot use techniques that are not included in the report you submit.
* **Safety First:** You must not cause real, irreversible damage (accidents happen, and someone might misclick and execute this in a real environment).
* **Killswitch is Mandatory:** You must hide a killswitch—this means a file, domain, or URL which, if it exists, will deactivate the virus. You must document this in your report.
