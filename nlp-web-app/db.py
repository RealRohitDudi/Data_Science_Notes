import json
class Database:
    def search(self,email,password):
        with open('data.json','r') as df:
            data = json.load(df)
        if email in data:
            if password == data[email][1]:
              return 200
        else:
            return 404
    def create(self,email,name,password):
        with open('data.json','r') as df:
            data = json.load(df)
        if email in data:
            return 409
        else:
            data[email] = [name,password]
            with open('data.json','w') as df:
                json.dump(data,df)
            return 200