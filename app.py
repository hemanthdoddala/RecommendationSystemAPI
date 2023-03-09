import os
import psycopg2
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.debug = True
db_url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(db_url)

@app.route("/")
def hello_world():
    return jsonify("Hello, World!")

@app.get("/getUsers")
@cross_origin()
def getUsers():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("select distinct userid from ratings order by userid")
            data = cursor.fetchall()
    return {"users": [x[0] for x in data]}

@app.route("/getTopRecommendations")
def getTopRecommendations():
    return "Top Recommendations"

@app.route("/getTopRecommendationsGenres")
def getTopRecommendationsByGenres():
    return "Top Recommendations By Genres"

@app.route("/getSimilarRecommendations")
def getSimilarRecommendations():
    return "Similar Recommendations"
