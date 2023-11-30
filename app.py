from flask import Flask, render_template, request, jsonify

import psycopg2
from datetime import datetime
from decimal import Decimal

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})

#newraghid is here
#raghid is testing2
conn = psycopg2.connect(database='435_project', user='postgres',
                        password='MyPassw0rd', host='10.169.43.78', port='5432')
# conn = psycopg2.connect(database='435lProject', user='postgres',
#                         password='Hisham882003!', host='127.0.0.1', port='5432')

cursor = conn.cursor()
