__author__ = 'xead'
import pickle
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print "Preparing classifier"
start_time = time.time()
with open('sentiment_model.pkl') as f:
    model = pickle.load(f)
print "Classifier is ready"
print time.time() - start_time, "seconds"

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        logfile = open("demo_logs.txt", "a", "utf-8")
	print text
	print >> logfile, "<response>"
	print >> logfile, text
        prediction_message = model.predict([text])
        print prediction_message
	print >> logfile, prediction_message
	print >> logfile, "</response>"
	logfile.close()
	
    return render_template('hello.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
