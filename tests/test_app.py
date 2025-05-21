import subprocess
import os
import app

def test_greet_function():
    assert app.greet("Yazan") == "Hello, Yazan!"

def test_app_output():
    # Run app.py as a script and check printed output
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app.py"))
    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Hello, world!"