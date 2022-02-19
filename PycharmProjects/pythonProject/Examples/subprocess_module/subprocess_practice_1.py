import subprocess
from pprint import pprint

output = subprocess.run("ping", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
output_string = output.stdout
print(output.stdout)
print(output.stderr)

print(output.returncode)
pprint(output.stdout)