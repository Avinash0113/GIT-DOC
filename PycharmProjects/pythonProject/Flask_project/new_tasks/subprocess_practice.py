# import subprocess
#
# output = subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe",shell=True)
#
#Open google in python - Windows.
import subprocess
import webbrowser
url='https://google.com'
webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)