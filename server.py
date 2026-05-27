"""
Portfolio Local Server
======================
Run with:  python server.py
Then open: http://localhost:5000

Requires: pip install flask
"""

from flask import Flask, send_from_directory
import os, webbrowser, threading, time

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

def open_browser():
    time.sleep(1.2)
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  🌊  Nompumelelo Blessing Nzama — Portfolio")
    print("="*50)
    print("  Server running at: http://localhost:5000")
    print("  Press Ctrl+C to stop")
    print("="*50 + "\n")
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
