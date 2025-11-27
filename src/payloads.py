import webbrowser, os, subprocess
from .utils import log

def rickroll():
    log("Payload: Rickroll (seguro) se va a abrir en el navegador.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def popup_message():
    log("Payload: Intentando mostrar popup inofensivo (sólo Windows).")
    if os.name == "nt":
        try:
            subprocess.run([
                "powershell", "-NoProfile", "-Command",
                '[System.Windows.MessageBox]::Show("¡Simulación MVS! (inofensivo)")'
            ], shell=True, check=False)
            log("Popup mostrado (simulado).")
        except Exception as e:
            log(f"Popup falló: {e}")
    else:
        log("Popup no soportado en este OS - omitiendo.")
