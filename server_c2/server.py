from flask import Flask, request, jsonify, render_template_string, redirect
app = Flask(__name__)

command_store = {"cmd": ""}

HTML = """
<!doctype html>
<title>C2 Simulado</title>
<h1>C2 Dashboard (simulado, benigno)</h1>
<form action="/set" method="post">
  <label>Comando (rickroll / popup / ''):</label>
  <input name="cmd" />
  <input type="submit" value="Enviar" />
</form>
<p>Comando actual: {{cmd}}</p>
"""

@app.route("/")
def index():
    return render_template_string(HTML, cmd=command_store["cmd"])

@app.route("/set", methods=["POST"])
def set_cmd():
    cmd = request.form.get("cmd", "").strip()
    command_store["cmd"] = cmd
    return redirect("/")

@app.route("/c2", methods=["POST"])
def c2():
    data = request.get_json(silent=True) or {}
    agent = data.get("agent", "unknown")
    cmd = command_store.get("cmd", "")
    resp = {"cmd": cmd}
    # opcional: limpiar comando para que se entregue una sola vez
    command_store["cmd"] = ""
    app.logger.info(f"Beacon from {agent}, delivering cmd: {cmd}")
    return jsonify(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
