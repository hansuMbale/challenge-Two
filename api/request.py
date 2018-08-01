from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


class Request:

    def __init__(self,iD,fullname,Computer_ID,description,department):
        self.iD=iD
        self.fullname=fullname
        self.Computer_ID=Computer_ID
        self.description=description
        self.department=department
    
    def get_iD(self):
        return self.iD
    def get_fullname(self):
        return self.fullname
    def get_Computer_ID(self):
        return self.Computer_ID
    def get_description(self):
        return self.description
    def get_department(self):
        return self.department
    

    def update_request(self,iD,fullname,Computer_ID,decription, department):
        iD = int(iD) 
        new_request = {}
        if len(requests) > 0 and iD <= len(requests):
            new_request = {
                'iD':iD,
                'fullname':self.fullname,
                'Computer_ID': self.Computer_ID,
                'description':self.description,
                'department':self.department
            }
            requests[iD] = new_request
            return new_request
        return new_request 



    def __repr__(self):
        return repr(self._dict_)

requests=[]

class User:
    def __init__(self,user_id,fullname,email,username,password):
        self.user_id=user_id
        self.fullname=fullname
        self.email=email
        self.username=username
        self.password=password

    def get_user_id(self):
        return self.user_id
    def get_fullname(self):
        return self.fullname
    def get_email(self):
        return self.email
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def __repr__(self):
        return repr(self._dict_)

users=[]      


@app.route('/API/register',methods=['POST'])
def register_user():
    user_data=request.get_json()

    if not user_data:
        return jsonify({'message':'All fields required'}),400
    fullname=user_data.get('fullname')
    email=user_data.get('email')
    username=user_data.get('username')
    password=user_data.get('password')

        
    if not fullname or fullname=='':
        return jsonify({'message':'first fullname is required'}),400
    if not email or email==" ":
        return jsonify({'message':'email required'}),400
    if not username or username==" ":
        return jsonify({'message':'userfullname required'}),400
    if not password or password==" ":
        return jsonify({'messa':'gepassword required'}),400
   # user_data['id']=0
    #user_data['id']=len(users)
    users.append(user_data)
    return jsonify({'message':'has been successfully registered'}),201 


@app.route('/API/login', methods=['POST'])
def login_user():
    user_data = request.get_json()
    if not user_data:
        return jsonify({'message':'These fields are required'}),400

    username= user_data.get('username')
    password=user_data.get('password')

    return jsonify({'message': 'you are now logged in'})      


@app.route('/API/v1/users/requests', methods=['POST'])
def create_request():
    request_data = request.get_json()
    if not request_data:
        return jsonify({'message':'All fields are required'}),400

    fullname=request_data.get('fullname')
    Computer_ID=request_data.get('Computer_ID')
    description=request_data.get('description')
    department=request_data.get('department')

    if not fullname or fullname == " " or fullname==type(int):
        return jsonify({'message':'fullname is invalid'}),400
    if not Computer_ID or Computer_ID == " ":
        return jsonify({'message':'Computer_ID  required'}),400
    if not description or description == " ":
        return jsonify({'message':'please enter description'}),400
    if not department or department == " ":
        return jsonify({'message':'department required'}),400

    requests.append(request_data)
    return jsonify({'message':' you have created a request'}),201


@app.route('/API/v1/users/requests', methods=['GET'])
def get_all_user_requests():
    if len(requests)>0:
        return jsonify({'message':requests}),302
    else:
        return jsonify({'message': 'There were no requests found'}),201 

@app.route('/API/v1/users/requests/<int:request_id>', methods=['GET'])
def get_a_request(request_id):
    for a_request in requests:
        if a_request.get['id']==requests:
            return jsonify({'User requests ':a_request})

    return jsonify({'message':'request not found'})

@app.route('/API/v1/users/requests/<int:request_id>', methods=['PUT'])
def update_user_request(request_id):
    new_request= request.get_json()
    for a in requests:
        if a:
            fullname=new_request.get('fullname')
            Computer_ID=new_request.get('Computer_ID')
            description=new_request.get('description')
            department=new_request.get('department')
        return jsonify({'message':'request has been updated'})
    return jsonify({'message':'Request not updated'})

if __name__ == "__main__":  
    app.run(debug=True)

