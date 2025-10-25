import subprocess

# Path to your shell script
numbers.sh = "/path/to/your/script.sh"

# Run the shell script
result = subprocess.run(["bash", numbers.sh], capture_output=True, text=True)

# Output the result
print("Output:", result.stdout)
print("Error:", result.stderr)

