import requests
import json

class Test_API:

    #a) Test the Register API by registering the user successfully using https://reqres.in/api/register and by logging in using the data used for the registration
    def test_Register_Login(self):

        #Register user
        req_RegisterUser = "https://reqres.in/api/register"
        file = open("JsonFiles/RegisterUser.json", 'r')
        file_write = open("JsonFiles/DeleteContent.json", 'w')
        register_input = file.read()
        register_input = json.loads(register_input)
        res_RegisterUser = requests.post(req_RegisterUser, register_input)
        json.dump(res_RegisterUser.json(),file_write)
        assert res_RegisterUser.status_code == 200


        #Login User
        req_Login = "https://reqres.in/api/login"
        res_Login = requests.post(req_Login, register_input)
        assert res_Login.status_code == 200

    #b) Using details of the user created in step a,  Delete the user registered above and assert an unsuccessful login attempt on login API https://reqres.in/api/
    def test_Delete_Login(self):
        file = open("JsonFiles/RegisterUser.json", 'r')
        file_delete = open("JsonFiles/DeleteContent.json", 'r')
        register_input = file.read()
        register_input = json.loads(register_input)
        input = file_delete.read()
        data = json.loads(input)
        req = "https://reqres.in/api/users/"+str(data['id'])+""
        res = requests.delete(req)
        assert res.status_code == 204

        # Login User
        req_Login = "https://reqres.in/api/login"
        res_Login = requests.post(req_Login, register_input)
        assert res_Login.status_code != 200


    #c) Assert a resource on https://reqres.in/api/unknown where page=1 and ID=2, year=2001
    def test_Unkown(self):
        req = "https://reqres.in/api/unknown"
        flag = 0
        res = requests.get(req)
        json_res = res.json()
        assert json_res['page'] == 1
        for data in json_res['data']:
            if data['id'] == 2 and data['year'] == 2001:
                flag = 1
        assert flag == 1

    #d) Assert a user on https://reqres.in/api/users?page=2 where the assertion is passed if the payload contains user with ID=7, Lastname =Lawson
    def test_ListUser(self):
        req = "https://reqres.in/api/users?page=2"
        flag = 0
        res = requests.get(req)
        json_res = res.json()
        for data in json_res['data']:
            if data['id'] == 7 and data['last_name'] == "Lawson":
                flag = 1
        assert flag == 1

    #e) Assert the payload in API https://reqres.in/api/users/2 where it will check for first_name as "John" and fails the test if it's not "John"
    def test_SingleUser(self):
        req = "https://reqres.in/api/users/2"
        res = requests.get(req)
        json_res = res.json()
        assert json_res['data']['first_name'] == "John"