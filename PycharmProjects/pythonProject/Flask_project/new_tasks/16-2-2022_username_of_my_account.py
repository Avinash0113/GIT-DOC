import os
import subprocess
output=os.getenv("USERNAME")
print(output)
output1=os.getenv("hostname")
print(output1)

# OS module provides a portable way of using operating system dependent functionality.
# os.getenv() method in Python returns the value of the environment variable key
# if it exists otherwise returns the default value.
# Syntax: os.getenv(key, default = None)


# output1=os.getenv("USERPROFILE")
# output2=os.getenv("PATH")
#
# print(output1)
# print(output2)

var_1=subprocess.run("whoami",shell=True)
print(var_1)