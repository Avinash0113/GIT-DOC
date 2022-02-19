import subprocess
import time
output=subprocess.call([r"C:\Program Files\Google\Chrome\Application\chrome.exe",r"www.google.com"],shell=True)
time.sleep(5)
output_1=subprocess.run([r"C:\Program Files\Google\Chrome\Application\chrome.exe",r"https://www.facebook.com/"],shell=True)
time.sleep(5)
output_2=subprocess.call([r"C:\Program Files\Google\Chrome\Application\chrome.exe",r"www.youtube.com"],shell=True)