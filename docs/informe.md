# INFORME DEL PROYECTO — Virus “Molón” Académico

**Asignatura:** Ciberseguridad  
**Alumno:**  
**Fecha:**  

---

## 1. Objetivos del proyecto

Resumen del propósito académico:

- Entender vectores de infección de forma controlada
- Analizar persistencia no maliciosa
- Simular un C2 benigno
- Incluir payloads seguros
- Añadir killswitch documentado

---

## 2. Arquitectura general del proyecto

Explicar los módulos:

- `src/core.py` — flujo principal
- `src/persistence.py` — persistencia simulada
- `src/killswitch.py` — desactivación
- `src/c2_client.py` — comunicaciones C2 benignas
- `server_c2/` — panel C2 Flask
- `phishing_demo/` — vector de infección ficticio

Incluye un diagrama (puedes pegar uno creado en Excalidraw).

---

## 3. Vector de infección (ficticio)

- Email ridículo (`phishing_demo/email.html`)
- Página web cringe (`phishing_demo/web_cringe/`)
- El archivo descargado **no contiene nada peligroso**, solo simula el flujo.

Explica por qué no se hace daño real.

---

## 4. Persistencia

Describe lo que implementaste (ejemplo):

- Tarea programada simulada
- Registro (solo educativo)
- Avoid malware real

---

## 5. C2 (Command & Control) benigno

Explica:

- Servidor en Flask
- Cliente en `src/c2_client.py`
- Solo recibe comandos tipo “rickroll”, “mostrar alerta”, etc.
- Sin proxies, sin cifrado encubierto

---

## 6. Payload seguro

Ejemplos permitidos:

- Cambiar fondo del escritorio
- Mostrar ventanas emergentes
- Reproducir un sonido
- Abrir un vídeo de YouTube (rickroll)

---

## 7. Killswitch

Explicar:

- Ruta exacta del killswitch  
- Si existe, **el programa entero se autodeshabilita**

---

## 8. Limitaciones éticas

Ver archivo `ethical_limitations.md`.

---

## 9. Instrucciones de ejecución

Ver `run_instructions.md`.

---

## 10. Conclusión

Reflexión sobre lo aprendido.
