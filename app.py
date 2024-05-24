from flask import Flask,request,render_template
from src.textsummarizer.pipeline.prediction import PredictionPipeline


application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict',methods=['GET','POST'])
def summarize():
    if request.method=='GET':
        return render_template('home.html')
    else:
        text=request.form.get('text')
        prediction = PredictionPipeline()
        summary=prediction.predict(text)
        return render_template('home.html',summary=summary)
    

if __name__=="__main__":
    app.run(host="0.0.0.0")  

