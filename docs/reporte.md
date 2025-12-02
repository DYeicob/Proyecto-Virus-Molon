# 📄 **REPORTE COMPLETO DEL PROYECTO – *proyecto-virus-molon***

## 🧩 **1. Introducción**

Este proyecto es una **simulación educativa** inspirada en el funcionamiento real de un malware modular, pero implementado estrictamente con **acciones seguras, controladas e inofensivas**.
Su propósito es **aprender técnicas de ciberseguridad ofensiva y defensiva**, así como demostrar:

* Arquitectura modular de un agente malicioso.
* Comunicación con un servidor C2 (Command & Control).
* Técnicas comunes como persistencia, infección, fileless execution, ransomware fake, propagación, phishing visual, etc.
* Cómo se detectan y mitigan en la vida real.

Ningún componente ejecuta acciones dañinas.
Todo el proyecto está pensado para ser ejecutado en una **máquina virtual** con fines académicos.

---

# 🗂️ **2. Estructura del proyecto**

```
proyecto-virus-molon/
│
├── src/
│   ├── agent.py
│   ├── migration_sim.py
│   ├── fileless_sim.py
│   ├── persistence.py
│   ├── propagation.py
│   ├── c2_client.py
│   ├── killswitch.py
│   ├── payloads.py
│   └── utils.py
│
├── server_c2/
│   ├── server.py
│   └── requirements.txt
│
├── phishing_demo/
│   ├── email.html
│   └── web_cringe/
│       ├── index.html
│       └── style.css
│
├── docs/
│   ├── informe.md
│   ├── ethical_limitations.md
│   └── run_instructions.md
│
├── tests/
│   ├── test_killswitch.py
│   └── test_c2.py
│
├── .gitignore
├── LICENSE
├── README.md
├── instrucciones_virus.txt 
└── requirements.txt
```

---

# 🧪 **3. Descripción detallada de cada módulo**

---

## **3.1. /src — Código del agente simulado**

---

### ### **🧠 agent.py — Agente principal del “virus” simulado**

Coordina todo el funcionamiento:

* Carga cada módulo.
* Envía beacon al C2 cada X segundos.
* Ejecuta órdenes benignas recibidas del servidor.
* Verifica el *killswitch*.
* Escribe logs en `utils.py`.

Simula el comportamiento de un malware modular real sin afectar el sistema.

---

### **🔀 migration_sim.py — Simulación de “infección” o migración**

Explica cómo un malware real saltaría entre procesos.

Pero en esta simulación:

* Solo enumera procesos.
* Imita la selección de un proceso “objetivo”.
* Simula la “migración” escribiendo un mensaje en logs.

---

### **🧬 fileless_sim.py — Simulación de ejecución fileless (LOLBAS benigno)**

Imita el estilo de malware fileless:

* Ejecuta comandos inocuos.
* Jamás escribe archivos en áreas críticas.
* Solo demuestra la técnica de “ejecución en memoria”.

Ejemplo usado: ejecutar PowerShell o bash con `echo`.

---

### **📌 persistence.py — Persistencia simulada**

Simula agregar persistencia:

* En Windows: tarea programada ficticia.
* En Linux: entrada simulada en `.bashrc`.

No modifica el sistema real.
Solo escribe registros y muestra cómo sería el ataque.

---

### **🔗 propagation.py — Propagación a USB simulada**

Enumeración de volúmenes (Windows/Linux)
Crea **un archivo inocuo** como mecanismo demostrativo.

Nunca copia binarios ni intenta auto-replicarse.

---

### **📡 c2_client.py — Comunicación con el servidor C2**

Implementa:

* Beacon periódico.
* Petición de comandos al servidor Flask.
* Ejecución de tareas seguras:

  * mostrar un popup
  * imprimir un mensaje
  * ejecutar rickroll
  * simular cifrado fake

---

### **🛑 killswitch.py — Parada de emergencia**

Busca un archivo llamado:

```
stop.txt
```

Si existe:

* Apaga el agente.
* Notifica al servidor.
* Escribe un log.

Demuestra cómo un malware real puede incluir desactivación remota.

---

### **🎉 payloads.py — “Payloads” seguros y divertidos**

Incluye:

* Rickroll (abre YouTube)
* Popup
* Cambiar fondo *simulado*
* Mensaje de terminal
* Falso ransomware educativo (NO cifra nada)

---

### **🧰 utils.py — Utilidades y logs**

Proporciona:

* Función de logging.
* Timestamps.
* Captura de errores.
* Estructura común usada por todo el agente.

---

## **3.2. /server_c2 — Servidor de Comando y Control**

---

### **🖥️ server.py — C2 con Flask**

Incluye:

* Panel web simple.
* Últimos agentes conectados.
* Enviar comandos benignos.
* Ver logs del agente.
* Modo killswitch.

Todo el C2 es local y seguro.

---

### **📦 requirements.txt**

Librerías necesarias para ejecutar el servidor.

---

## **3.3. /phishing_demo — Material educativo de phishing**

---

### **📧 email.html — Email ridículo de phishing**

Un correo humorístico que simula un phishing pésimo a propósito.
Contiene un enlace a un archivo inocuo (o simplemente una frase clicable).

Sirve para explicar:

* Ingeniería social.
* Elementos visuales sospechosos.
* Errores típicos.

### **🌐 web_cringe/**

Página web extremadamente cutre que simula:

* Formularios falsos.
* Robos de credenciales ficticios.
* Colores chillones y mala UX.

Es completamente inofensiva y no almacena datos.

---

## **3.4. /docs — Documentación del proyecto**

---

### **📝 informe.md**

Versión imprimible del reporte.

### **⚖️ ethical_limitations.md**

Documento que explica:

* Qué técnicas se omitieron por seguridad.
* Por qué no se implementó nada peligroso.
* Separación entre simulación (“proof of concept”) y malware real.

### **⚙️ run_instructions.md**

Instrucciones para:

* Ejecutar en VM
* Probar módulo por módulo
* Activar el C2
* Desactivar el agente
* Limpiar el entorno

---

## **3.5. /tests — Pruebas unitarias**

---

### **test_killswitch.py**

Prueba que el agente:

* Detecta `stop.txt`
* Se apaga correctamente
* No ejecuta payloads tras la desactivación

### **test_c2.py**

Prueba:

* Que el servidor devuelve comandos
* Que el cliente los interpreta
* Que la comunicación responde correctamente

---

# 📄 **4. Flujo de ejecución del proyecto**

1. Se lanza el servidor C2 (`python server.py`).
2. El agente se inicia (`python agent.py`).
3. El agente:

   * envía beacon
   * recibe comandos
   * registra actividad
4. El profesor o alumno envía un comando desde el panel:

   * popup
   * mensaje
   * rickroll
   * ransomware simulado
5. El agente ejecuta el payload.
6. Si se crea `stop.txt`, el malware simulado se apaga.

---

# 🛡️ **5. Riesgos y medidas éticas**

El proyecto **NO incluye:**

❌ cifrado real
❌ explotación de vulnerabilidades
❌ escalada de privilegios
❌ inyección real en procesos
❌ persistencia real
❌ propagación real a dispositivos USB
❌ robo de datos
❌ cargas maliciosas auténticas

Todo está diseñado siguiendo:

* Buenas prácticas académicas.
* Ética de hacking.
* Cumplimiento de seguridad en entornos controlados.

---

# 🧠 **6. Lecciones aprendidas**

Este proyecto demuestra:

* Cómo funciona la arquitectura modular de un malware.
* Qué medidas toman los atacantes para evadir defensas.
* Cómo se comunican con servidores externos.
* Qué técnicas usan (persistencia, migración, propagación…).
* Cómo defender, detectar y responder.

---

# 📦 **7. Conclusión**

Este proyecto es una herramienta completa para aprender conceptos clave de ciberseguridad ofensiva y defensiva, sin poner en riesgo ningún sistema.
Su diseño modular, la documentación, las pruebas unitarias y el C2 permiten estudiar el ciclo de vida de un malware, desde su ejecución hasta su control y su apagado seguro.
