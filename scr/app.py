from flask import Flask
from flask import render_template
from flaskext.mysql import MSQL

app = Flask (__name__)
mysql = MYSQL()

if __name__ == "__main__":
    app.run(debug=True)
    


