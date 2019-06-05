from flask import Flask, render_template

app = Flask(__name__)


@app.route('/map1')
def map1_page():
    return render_template('map1.html')


@app.route('/map2')
def map2_page():
    return render_template('map2.html')


@app.route('/map3')
def map3_page():
    return render_template('map3.html')


@app.route('/map4')
def map4_page():
    return render_template('map4.html')


@app.route('/map5')
def map5_page():
    return render_template('map5.html')


@app.route('/map6')
def map6_page():
    return render_template('map6.html')


@app.route('/map7')
def map7_page():
    return render_template('map7.html')


@app.route('/map8')
def map8_page():
    return render_template('map8.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
