from flask import Flask, request, jsonify, make_response,render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
from flask_assets import Environment, Bundle

from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import os
from flask_cors import CORS
import pandas as pd
import pprint
import json
import analysis.controller as cntrl
import analysis.data as data

file_path = os.path.abspath(os.getcwd()) + "/database.db"
print(file_path)
app = Flask(__name__)
CORS(app)
from util.assets import bundles
assets = Environment(app)

assets.register(bundles)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

db = SQLAlchemy(app)
# db.create_all()
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relation


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


class Product_abbreviation(db.Model):
    _tablename_ = 'product_abbreviation'
    ID = db.Column(db.Integer, primary_key=True)
    PROD_ABBR = db.Column(db.String(50), unique=True)


class State_abbreviation(db.Model):
    _tablename_ = 'state_abbreviation'
    ID = db.Column(db.Integer, primary_key=True)
    STATE_ABBR = db.Column(db.String(50), unique=True)


class Product(db.Model):
    _tablename_ = 'product_fact'
    AGENCY_ID_PRIMARY = db.Column(db.Integer, primary_key=True)
    AGENCY_ID = db.Column(db.Integer)
    PROD_ABBR_ID = db.Column(db.Integer, ForeignKey('product_abbreviation.ID'))
    PROD_LINE = db.Column(db.String(2))
    STATE_ABBR_ID = db.Column(db.Integer, ForeignKey('state_abbreviation.ID'))
    STAT_PROFILE_DATE_YEAR = db.Column(db.Integer)
    RETENTION_POLY_QTY = db.Column(db.Integer)
    POLY_INFORCE_QTY = db.Column(db.Integer)
    PREV_POLY_INFORCE_QTY = db.Column(db.Integer)
    NB_WRTN_PREM_AMT = db.Column(db.Float)
    WRTN_PREM_AMT = db.Column(db.Float)
    PREV_WRTN_PREM_AMT = db.Column(db.Float)
    PRD_ERND_PREM_AMT = db.Column(db.Float)
    PRD_INCRD_LOSSES_AMT = db.Column(db.Float)
    MONTHS = db.Column(db.Integer)
    RETENTION_RATIO = db.Column(db.Float)
    LOSS_RATIO = db.Column(db.Float)
    LOSS_RATIO_3YR = db.Column(db.Float)
    GROWTH_RATE_3YR = db.Column(db.Float)
    AGENCY_APPOINTMENT_YEAR = db.Column(db.Integer)
    ACTIVE_PRODUCERS = db.Column(db.Integer)
    MAX_AGE = db.Column(db.Integer)
    MIN_AGE = db.Column(db.Integer)
    VENDOR_IND = db.Column(db.String(10))
    VENDOR = db.Column(db.String(10))
    PL_START_YEAR = db.Column(db.Integer)
    PL_END_YEAR = db.Column(db.Integer)
    COMMISIONS_START_YEAR = db.Column(db.Integer)
    COMMISIONS_END_YEAR = db.Column(db.Integer)
    CL_START_YEAR = db.Column(db.Integer)
    CL_END_YEAR = db.Column(db.Integer)
    ACTIVITY_NOTES_START_YEAR = db.Column(db.Integer)
    ACTIVITY_NOTES_END_YEAR = db.Column(db.Integer)
    CL_BOUND_CT_MDS = db.Column(db.Integer)
    CL_QUO_CT_MDS = db.Column(db.Integer)
    CL_BOUND_CT_SBZ = db.Column(db.Integer)
    CL_QUO_CT_SBZ = db.Column(db.Integer)
    CL_BOUND_CT_eQT = db.Column(db.Integer)
    CL_QUO_CT_eQT = db.Column(db.Integer)
    PL_BOUND_CT_ELINKS = db.Column(db.Integer)
    PL_QUO_CT_ELINKS = db.Column(db.Integer)
    PL_BOUND_CT_PLRANK = db.Column(db.Integer)
    PL_QUO_CT_PLRANK = db.Column(db.Integer)
    PL_BOUND_CT_eQTte = db.Column(db.Integer)
    PL_QUO_CT_eQTte = db.Column(db.Integer)
    PL_BOUND_CT_APPLIED = db.Column(db.Integer)
    PL_QUO_CT_APPLIED = db.Column(db.Integer)
    PL_BOUND_CT_TRANSACTNOW = db.Column(db.Integer)
    PL_QUO_CT_TRANSACTNOW = db.Column(db.Integer)

    product_abbrevation = relation(Product_abbreviation)
    state_abbreviation = relation(State_abbreviation)


#db.create_all()
#df = pd.read_csv("../srccode/dataset/finalapi.csv")

'''def insertProdAbbr():
    # df.read_csv("/srccode/dataset/finalapi.csv")
    prod_list = df.PROD_ABBR.unique()
    #Product_abbreviation.query.delete()
    id = 1
    for prod in prod_list:
        new_prod = Product_abbreviation(ID=id,PROD_ABBR=prod)

        db.session.add(new_prod)
        db.session.commit()
        id += 1
        print("inserted",prod)

    #Product_abbreviation.query.delete()
    prods = Product_abbreviation.query.all()
    output = []
    for p in prods:
        p_data = {}
        p_data['ID'] = p.ID
        p_data['PROD_ABBR'] = p.PROD_ABBR
        output.append(p_data)
    print(output)

def insertStateAbbr():
    state_list = df.STATE_ABBR.unique()
    id = 100

    for state in state_list:
        new_state = State_abbreviation(ID=id, STATE_ABBR=state)

        db.session.add(new_state)
        db.session.commit()
        id += 1
        print("inserted", state)

    # Product_abbreviation.query.delete()
    states = State_abbreviation.query.all()
    output = []
    for s in states:
        s_data = {}
        s_data['ID'] = s.ID
        s_data['STATE_ABBR'] = s.STATE_ABBR
        output.append(s_data)
    print(output)
import importdata.converter as converter

def insertProduct():
    prods = Product_abbreviation.query.all()
    products_list = []
    for p in prods:
        p_data = {}
        p_data['ID'] = p.ID
        p_data['PROD_ABBR'] = p.PROD_ABBR
        products_list.append(p_data)
    print(products_list)
    states = State_abbreviation.query.all()
    states_list = []
    for s in states:
        s_data = {}
        s_data['ID'] = s.ID
        s_data['STATE_ABBR'] = s.STATE_ABBR
        states_list.append(s_data)
    print(states_list)
    #Product.query.delete()
    #print('deleted')
    #print(Product.query.all())
    idx=1
    for index,row in df.iterrows():
        if(index>=115595):
            #print(row.AGENCY_ID)
            #print(index+1)
            prod_id=converter.get_prod_id(row.PROD_ABBR,products_list)
            #print(prod_id,row.PROD_ABBR)
            state_id = converter.get_state_id(row.STATE_ABBR, states_list)
            #print(index+1,prod_id,row.PROD_ABBR,state_id, row.STATE_ABBR)
            new_product = Product(AGENCY_ID_PRIMARY=idx,AGENCY_ID=row.AGENCY_ID,PROD_ABBR_ID=prod_id,PROD_LINE=row.PROD_LINE, STATE_ABBR_ID=state_id,
                                            STAT_PROFILE_DATE_YEAR=row.STAT_PROFILE_DATE_YEAR,
                                            RETENTION_POLY_QTY = row.RETENTION_POLY_QTY,
                                            POLY_INFORCE_QTY = row.POLY_INFORCE_QTY,
                                            PREV_POLY_INFORCE_QTY = row.PREV_POLY_INFORCE_QTY,
                                            NB_WRTN_PREM_AMT = row.NB_WRTN_PREM_AMT,
                                            WRTN_PREM_AMT = row.WRTN_PREM_AMT,
                                            PREV_WRTN_PREM_AMT = row.PREV_WRTN_PREM_AMT,
                                            PRD_ERND_PREM_AMT = row.PRD_ERND_PREM_AMT,
                                            PRD_INCRD_LOSSES_AMT = row.PRD_INCRD_LOSSES_AMT,
                                            MONTHS = row.MONTHS,
                                            RETENTION_RATIO = row.RETENTION_RATIO,
                                            LOSS_RATIO = row.LOSS_RATIO,
                                            LOSS_RATIO_3YR = row.LOSS_RATIO_3YR,
                                            GROWTH_RATE_3YR = row.GROWTH_RATE_3YR,
                                            AGENCY_APPOINTMENT_YEAR = row.AGENCY_APPOINTMENT_YEAR,
                                            ACTIVE_PRODUCERS = row.ACTIVE_PRODUCERS,
                                            MAX_AGE = row.MAX_AGE,
                                            MIN_AGE = row.MIN_AGE,
                                            VENDOR_IND = row.VENDOR_IND,
                                            VENDOR = row.VENDOR,
                                            PL_START_YEAR = row.PL_START_YEAR,
                                            PL_END_YEAR = row.PL_END_YEAR,
                                            COMMISIONS_START_YEAR = row.COMMISIONS_START_YEAR,
                                            COMMISIONS_END_YEAR = row.COMMISIONS_END_YEAR,
                                            CL_START_YEAR = row.CL_START_YEAR,
                                            CL_END_YEAR = row.CL_END_YEAR,
                                            ACTIVITY_NOTES_START_YEAR = row.ACTIVITY_NOTES_START_YEAR,
                                            ACTIVITY_NOTES_END_YEAR = row.ACTIVITY_NOTES_END_YEAR,
                                            CL_BOUND_CT_MDS = row.CL_BOUND_CT_MDS,
                                            CL_QUO_CT_MDS = row.CL_QUO_CT_MDS,
                                            CL_BOUND_CT_SBZ = row.CL_BOUND_CT_SBZ,
                                            CL_QUO_CT_SBZ = row.CL_QUO_CT_SBZ,
                                            CL_BOUND_CT_eQT = row.CL_BOUND_CT_eQT,
                                            CL_QUO_CT_eQT = row.CL_QUO_CT_eQT,
                                            PL_BOUND_CT_ELINKS = row.PL_BOUND_CT_ELINKS,
                                            PL_QUO_CT_ELINKS = row.PL_QUO_CT_ELINKS,
                                            PL_BOUND_CT_PLRANK = row.PL_BOUND_CT_PLRANK,
                                            PL_QUO_CT_PLRANK = row.PL_QUO_CT_PLRANK,
                                            PL_BOUND_CT_eQTte = row.PL_BOUND_CT_eQTte,
                                            PL_QUO_CT_eQTte = row.PL_QUO_CT_eQTte,
                                            PL_BOUND_CT_APPLIED = row.PL_BOUND_CT_APPLIED,
                                            PL_QUO_CT_APPLIED = row.PL_QUO_CT_APPLIED,
                                            PL_BOUND_CT_TRANSACTNOW = row.PL_BOUND_CT_TRANSACTNOW,
                                            PL_QUO_CT_TRANSACTNOW = row.PL_QUO_CT_TRANSACTNOW
                                  )

            print(new_product.AGENCY_ID_PRIMARY,new_product.AGENCY_ID,new_product.PROD_ABBR_ID,new_product.PRD_ERND_PREM_AMT,new_product.LOSS_RATIO,new_product.PROD_LINE,new_product.MONTHS,new_product.ACTIVITY_NOTES_END_YEAR,new_product.PL_BOUND_CT_APPLIED)
            db.session.add(new_product)
            db.session.commit()
            print("inserted")
        idx+=1


def getProduct():
    prods = Product.query.all()
    for p in prods:
        print(p.AGENCY_ID_PRIMARY,p.AGENCY_ID)

'''
#insertProdAbbr()
#insertStateAbbr()
#insertProduct()
#getProduct()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users': output})


@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user': user_data})


@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    print('hit')
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'})


@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user.admin = True
    db.session.commit()

    return jsonify({'message': 'The user has been promoted!'})


@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted!'})


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        output.append(todo_data)

    return jsonify({'todos': output})


@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    todo_data = {}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete

    return jsonify(todo_data)


@app.route('/todo', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message': "Todo created!"})


@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    todo.complete = True
    db.session.commit()

    return jsonify({'message': 'Todo item has been completed!'})


@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message': 'Todo item deleted!'})

@app.route('/',methods=['post','get'])
def home():
    return render_template('home.html')

@app.route('/data_set',methods=['post','get'])
def dataset():
    return render_template('data_set.html')

@app.route('/report',methods=['post','get'])
def index():
    products=Product.query.with_entities(Product.AGENCY_ID.distinct()).all()
    #print(products)
    agency_id_list=[]
    for p in products:
        agency_id_list.append(p[0])
    print(agency_id_list)
    return render_template("index.html",agency_id=None,agency_list=agency_id_list)

@app.route('/report/get_id',methods=['POST'])
def getAgencyId():
    products = Product.query.with_entities(Product.AGENCY_ID.distinct()).all()
    # print(products)
    agency_id_list = []
    for p in products:
        agency_id_list.append(p[0])
    if request.method == 'POST':
        a_id = request.form['agency_id']
        print(a_id)
        return render_template("index.html",agency_id=a_id,agency_list=agency_id_list)
    else:
        return render_template("index.html", agency_id=None,agency_list=agency_id_list)

@app.route('/agency/<agency_id>',methods=['GET'])
def get_by_agency(agency_id):
    products=Product.query.filter_by(AGENCY_ID=agency_id).all()
    df_data = pd.DataFrame()
    for p in products:
        data_dict = {}
        #print(p.AGENCY_ID,p.PROD_LINE)
        data_dict['agency_id']=p.AGENCY_ID
        data_dict['prod_abbr_id'] = p.PROD_ABBR_ID
        data_dict['prod_line'] = p.PROD_LINE
        data_dict['state_abbr_id'] = p.STATE_ABBR_ID
        data_dict['year'] = p.STAT_PROFILE_DATE_YEAR
        data_dict['nb_wrtn_prem_amt']=p.NB_WRTN_PREM_AMT
        data_dict['total_wrtn_prem_amt'] = p.WRTN_PREM_AMT
        data_dict['prev_wrtn_prem_amt']=p.PREV_WRTN_PREM_AMT
        data_dict['ernd_prem_amt']=p. PRD_ERND_PREM_AMT
        data_dict['losses_amt']=p.PRD_INCRD_LOSSES_AMT
        data_dict['loss_ratio'] = p.LOSS_RATIO_3YR
        data_dict['growth_rate'] = p.GROWTH_RATE_3YR
        df = pd.DataFrame([data_dict], columns=data_dict.keys())
        df_data = pd.concat([df_data, df], axis=0).reset_index(drop=True)
        del df
    #print(df_data['agency_id'],df_data['year'],df_data['loss_ratio'])
    prods = Product_abbreviation.query.all()
    products_list = []
    for p in prods:
        p_data = {}
        p_data['ID'] = p.ID
        p_data['PROD_ABBR'] = p.PROD_ABBR
        products_list.append(p_data)
    #print(products_list)
    states = State_abbreviation.query.all()
    states_list = []
    for s in states:
        s_data = {}
        s_data['ID'] = s.ID
        s_data['STATE_ABBR'] = s.STATE_ABBR
        states_list.append(s_data)
    #print(states_list)
    #print(df_data)
    result_list = []
    new_analysis=cntrl.manage(df_data,products_list,states_list)
    dict_state_result=new_analysis.get_state_analysis_result()
    result_list.append(dict_state_result)
    dict_product_line_result=new_analysis.get_product_line_result()
    result_list.append(dict_product_line_result)
    dict_pl_cl_result=new_analysis.get_pl_cl_product()
    result_list.append(dict_pl_cl_result)

    amount_result=new_analysis.get_amount_analysis_result()
    result_list.append(amount_result)
    json_result = json.dumps(
        result_list,
        default=lambda df: json.loads(df.to_json()))

    return json_result


if __name__ == '__main__':
    app.run()

