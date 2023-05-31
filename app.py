from flask import Flask , render_template , request 
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def short():
    if request.method == 'POST':
        url=request.form['url']
        surl=pyshorteners.Shortener().tinyurl.short(url)
        
    return render_template('index.html', url=surl)    
        

if __name__ == '__main__':
    app.run(debug=True)