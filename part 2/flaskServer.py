from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def info():
    return (render_template('index.html'))
@app.route('/about')
def about():
    return (render_template('about.html'))
@app.route('/blogger')
def blogger():
    return (render_template('blogger.html'))

if __name__=="__main__":
    app.run(debug=True)
