from flask import Flask, render_template, request
from bitmoji import bitmoji_webp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            snap = request.form['snap']
            bitmoji_url = bitmoji_webp(snap=snap)
            return render_template(
                'index.html',
                bitmoji=bitmoji_url
            )
        return render_template(
            'index.html',
            bitmoji=None
        )
    except:
        return render_template(
            'index.html',
            bitmoji=None
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
