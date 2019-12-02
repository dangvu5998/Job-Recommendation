import json
from flask import Flask
from flask import jsonify, request, abort
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np

from utils import get_embedding, parse_description
from constants import ADDRESSES, PROPERTY_WEIGHTS

app = Flask(__name__)
CORS(app)

def get_embedding_from_row(row):
    embedding = None
    embedding = get_embedding(row['skills'], [row['level']], \
                    (row['salary_min'] + row['salary_max']) // 2)
    return embedding
jobs_df = pd.read_csv('data/jobs.csv')
jobs_df['skills'] = jobs_df['skills'].apply(lambda x: json.loads(x.replace("'", '"')))
jobs_df['benefits'] = jobs_df['benefits'].apply(lambda x: json.loads(x.replace("'", '"')))
jobs_df['level'] = jobs_df['level'].apply(str.lower)
jobs_df['address'] = jobs_df['address'].apply(str.lower)
jobs_df['embedding'] = jobs_df.apply(get_embedding_from_row, axis=1)
SERIALIZE_PROPERTIES = ['title', 'company_title', 'description', 'address',
       'level', 'skills', 'benefits', 'id', 'salary_min', 'salary_max']

@app.route("/")
def hello():
    return jsonify({'greeting': "Hello, World!"})

@app.route("/api/search/")
def search():
    description = request.args.get('description')
    address = request.args.get('address')
    salary = request.args.get('salary')
    try:
        limit = int(request.args.get('limit', 20))
        offset = int(request.args.get('offset', 0))
    except:
        limit = 20
        offset = 0
    total = 1000
    result = {
        'jobs': [],
        'total': total
    }
    if offset > 1000:
        return jsonify(result)

    try:
        salary = int(salary)
    except:
        salary = None
    skills = []
    levels = []
    if description is not None:
        skills, levels = parse_description(description)
        print(skills, levels)
    embedding = get_embedding(skills, levels, salary)
    candidate_df = jobs_df
    if isinstance(address, str):
        address = address.lower().strip()
        if address in ADDRESSES:
            candidate_df = candidate_df[candidate_df['address'] == address].copy()
    candidate_embeddings = np.asarray(list(candidate_df['embedding']))
    candidate_distance = np.sum(np.sqrt(((candidate_embeddings - embedding) * PROPERTY_WEIGHTS) ** 2), axis=1) / np.sum(candidate_embeddings, axis=1)
    candidate_df['distance'] = candidate_distance
    candidate_df = candidate_df.sort_values(by='distance')
    candidate_df = candidate_df[SERIALIZE_PROPERTIES]
    candidate_df = candidate_df.iloc[offset: offset + limit]
    candidate_result = candidate_df.to_dict('records')
    result = {
        'jobs': candidate_result,
        'total': total
    }
    return jsonify(result)

@app.route("/api/jobs/<int:job_id>")
def get_one_job(job_id):
    job = jobs_df[jobs_df['id'] == job_id]
    if len(job) == 0:
        return abort(404)
    result = job.iloc[0][SERIALIZE_PROPERTIES].to_dict()
    for key in result:
        try:
            result[key] = int(result[key])
        except:
            pass
    return jsonify({
        'job': result
    })
