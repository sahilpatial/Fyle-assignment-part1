import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection

app = Flask(__name__)

app.config.from_object('config.ProductionConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from model import Bank



alchemy = 'postgresql+psycopg2://lptzfenupmbzuj:33302222e95e7355014d650f5a4e264a4c2431fe668d7a33842539a4f081f209@ec2-35-174-35-242.compute-1.amazonaws.com:5432/dcvic7e9ur27ku'
engine = create_engine(alchemy)
connection = engine.connect()

def autocomplete(keyword, limit, offset):
    if limit == None: limit = 5
    if offset == None: offset = 0
    sql_query = f'''select
                   *
                   from
                   branches
                   where
                   branch like '%%{keyword}%%'
                   order by ifsc
                   limit {limit} ; '''
    trans = connection.begin()
    record = connection.execute(sql_query)
    trans.commit()
    record = record.fetchall()

    return record


@app.route('/api/branches/autocomplete')
def auto_branch():
    q = request.args
    
    
    data = autocomplete(q.get("q").upper(), q.get("limit"), q.get("offset"))

    return jsonify({'branches': [dict(row) for row in data]})

def getBranch(keyword, limit, offset):
    if limit == None: limit = 5
    if offset == None: offset = 0
    sql_query = f'''
                    select
                *
                from
                branches
                where
                address like '%%{keyword}%%'
                or branch like '%%{keyword}%%'
                or city like '%%{keyword}%%'
                or district like '%%{keyword}%%'
                or state like '%%{keyword}%%'
                
                order by
                ifsc
                limit
                {limit} 
                offset {offset};
            '''
    trans = connection.begin()
    record = connection.execute(sql_query)
    trans.commit()
    record = record.fetchall()

    return record

@app.route('/api/branches')
def branch():
    q = request.args

    data = getBranch(q.get("q").upper(), q.get("limit"), q.get("offset"))

    return jsonify({'branches': [dict(row) for row in data]})


if __name__ == '__main__':
    app.run()