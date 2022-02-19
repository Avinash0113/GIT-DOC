import subprocess
import time
time.sleep(5)
output = subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
time.sleep(5)
output1 = subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
time.sleep(5)
output2 = subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe", stdout=subprocess.PIPE, encoding="utf-8", shell=True)


# output_string = output.stdout
# print(output.stdout)
# print(output.stderr)