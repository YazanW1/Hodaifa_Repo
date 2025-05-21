import subprocess
import os

def test_hello_output():
    # Get the absolute path to Hello.py (parent folder)
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Hello.py"))

    result = subprocess.run(
        ["python", script_path],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "hello world"
