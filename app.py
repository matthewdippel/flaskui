from flask import Flask, render_template, request
from QueryHandler import QueryCharCountHandler
app = Flask(__name__)

Q = QueryCharCountHandler()
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        output = Q.handle(query)
    else:
        query = ""
        output = ""
    return render_template("home.html",  query=query,output=output)

@app.route('/sample/')
def sample():
    query="the quick red fox jumps over the lazy brown dog"
    output = Q.handle(query)
    return render_template("home.html", query=query, output=output)
    

if __name__=='__main__':
    app.run(debug=True)
