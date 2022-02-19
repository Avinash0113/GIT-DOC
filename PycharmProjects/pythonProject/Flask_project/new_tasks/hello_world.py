# import time
# ?print("hello world")
#
# time.sleep(5)

# print("hello world")
# time.sleep(5)
# print("hello world")
# time.sleep(5)
# print("hello world")
# time.sleep(5)
# print("hello world")
from flask import Flask

app =Flask(__name__)

@app.route('/home')
def home():
    return {"Hi Avi":26}
    #return "Avinash"

app.run(port=8000)