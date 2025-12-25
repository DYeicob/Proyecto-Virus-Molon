import sys
from pathlib import Path

# Ensure server_c2 is in the import path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import json
import pytest

# Import the server module (server_c2/server.py)
from server_c2 import server as c2mod

@pytest.fixture
def client():
    """Flask testing client fixture"""
    app = c2mod.app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_set_and_get_command(client):
    """
    Tests the Command and Control workflow:
     - Verify a command can be set via /set (form POST)
     - Verify the /c2 endpoint returns that command and clears it after delivery
    """
    # Step 1: Set the command
    rv = client.post("/set", data={"cmd": "rickroll"}, follow_redirects=True)
    assert rv.status_code == 200

    # Step 2: Agent sends a beacon to the C2 server
    resp = client.post("/c2", json={"agent": "test_agent"})
    assert resp.status_code == 200
    data = resp.get_json()
    
    # Verify the JSON contains the command we just set
    assert "cmd" in data
    assert data["cmd"] == "rickroll"

    # Step 3: Verify the command is cleared after delivery (server behavior)
    resp2 = client.post("/c2", json={"agent": "test_agent"})
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    
    # The 'cmd' should now be empty or reset
    assert data2.get("cmd", "") == ""
