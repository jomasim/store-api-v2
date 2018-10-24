from app.api.v2.database import DBConnection
from werkzeug.security import generate_password_hash
from psycopg2 import sql

cur = DBConnection.get_connection().cursor()


class User(object):

    ''' create user '''
    @staticmethod
    def create(data):
        hashed=generate_password_hash(data['paswword'])
        query = "INSERT INTO users (name,username,email,password,role)" \
                "VALUES('%s','%s', '%s', '%s', '%s')" % (
                    data['name'],data['username'],data['email'],hashed,data['role'])
        cur.execute(query)
        
    @staticmethod
    def exists(data):
        if data['email']:
            query="SELECT * FROM users WHERE email = '%s';" % data['email']
            cur.execute(query)
            return cur.fetchone()
        return False
