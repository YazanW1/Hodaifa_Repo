import subprocess

def test_hello_output():
    result = subprocess.run(
        ["python", "Hello.py"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "hello world"