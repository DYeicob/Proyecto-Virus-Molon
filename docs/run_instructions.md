# Instrucciones de Ejecución en VM (Proyecto Virus Molón — Versión Académica)

Este proyecto debe ejecutarse **exclusivamente en una máquina virtual aislada**, nunca en el sistema anfitrión.

---

# 1. Requisitos del entorno

- **Máquina Virtual** (Windows o Linux)
- **Python 3.8+**
- **pip** instalado
- Conexión a Internet (solo para comunicar con el C2 local/remoto)

---

# 2. Crear entorno virtual y preparar dependencias

Dentro de la carpeta raíz del proyecto:

```bash
python -m venv venv
````

Activar el entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
pip install -r server_c2/requirements.txt
```

---

# 3. Ejecutar el servidor C2

En una terminal:

```bash
python server_c2/server.py
```

El panel estará disponible en:

```
http://0.0.0.0:5050/
```

Desde el navegador podrás enviar comandos **benignos** al cliente.

---

# 4. Ejecutar el cliente (virus académico)

En otra terminal, manteniendo el entorno virtual activo:

```bash
python src/core.py
```

Si todo funciona correctamente:

* Se realizará un "beacon" al C2 en menos de 60 segundos.
* El C2 podrá responder con un comando benigno.
* Se ejecutará un payload seguro como abrir un Rickroll o cambiar el fondo.

---

# 5. Probar el killswitch

El sistema debe deshabilitarse **automáticamente** si detecta un archivo, dominio o URL concreta.

## Windows

Crear archivo:

```bash
echo off > C:\killswitch.txt
```

## Linux/macOS

```bash
touch /tmp/killswitch
```

Al detectar el archivo, el cliente:

* detendrá su ejecución
* ignorará cualquier comando del C2
* no ejecutará payloads

---

# 6. Limpieza completa del entorno

Cuando termines las pruebas, elimina todo.

## Windows

```bash
rmdir /S /Q venv
rmdir /S /Q .
```

## Linux/macOS

```bash
rm -rf venv
rm -rf .
```

Con esto, la VM vuelve a su estado sin rastro del proyecto.

---

# 7. Notas importantes

* Este proyecto es **100% educativo** y no debe instalarse en un sistema real.
* Ningún módulo implementa técnicas dañinas.
* La “persistencia” es simulada.
* El C2 solo envía comandos triviales.
* No hay cifrado, exploits ni modificaciones del sistema real.
* El vector de infección es **ficticio**.

---
