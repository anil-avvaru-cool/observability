from flask import Flask, request
import subprocess
import json
import os

app = Flask(__name__)

@app.route("/dynatrace", methods=["POST"])
def handle_problem():
    payload = request.json

    problem_title = payload["title"]
    affected_host = payload["hostName"]
    print("problem_title",problem_title)
    hostname = f"target_host={affected_host}"
    print("formatted host",hostname)
    # Save password in vault(prod) or in /etc/environment
    sudo_pass = os.environ.get('SUDO_PASS')

    subprocess.run([
        "ansible-playbook",
        "restart-webserver-playbook-v2.yaml",
        "-e", hostname,
        "-e", "service_name=apache2",
        "-e", f"ansible_become_pass={sudo_pass}",
        "-i","inventory.ini"
    ])

    return {"status": "triggered"}, 200

app.run(host="0.0.0.0", port=5000)