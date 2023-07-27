import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY'] = 'qgjjbvcxsdfghjnbvcmnbvcjhgfdnbvc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Emp(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=True)
    email=db.Column(db.String(100),nullable=True)
    phone=db.Column(db.String(20),nullable=True)

@app.route('/add-emp',methods=['POST'])
def addEmp():
    data=request.get_json()
    emp=Emp.query.filter_by(email=data['email']).first()
    if emp:
        if emp.email==data['email']:
            return jsonify({'message':"Email Allready used"})
    user=Emp(name=data['name'],email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':"Emp Data Added"})

@app.route('/c_table',methods=['GET'])
def c_table():
    with app.app_context():
        db.create_all()
    return jsonify({'message':'Table Created'})



if __name__=='__main__':
    app.run(debug=True)