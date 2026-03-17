import json
class Database:
    def __init__(self):
        pass

    def search(self,email,password):
        with open('db.json', 'r') as db_file:
            db = json.load(db_file)
        for item in db:
            if item == email:
                if password == item["password"]:
                    return 200
                else:
                    return 401
        return 404


    def create(self,name,email,password):
        with open('db.json', 'r') as db_file:
            db = json.load(db_file)
        for item in db:
            if item == email:
                return 409

        db[email] = {"name": name, "password": password}
        with open('db.json', 'w') as wf:
            wf = json.dump(db)
            return 200

    def delete(self,email,password):
        with open('db.json', 'r') as db_file:
            db = json.load(db_file)
        for item in db:
            if item == email:
                if password == item["password"]:
                  del db[item]
                  with open('db.json', 'w') as wf:
                    wf = json.dump(db)
                    return 200
        return 404

