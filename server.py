from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS, cross_origin



app = Flask(__name__)
api = Api(app)
CORS(app)

# class Book(Resource):
@app.route('/', methods=["GET","POST"])
def get():
    return { "status": { "code": 200},
            "response": {
                    "bookslist": [ {"name":"Wings of Fire",
                    "author":"A P J Abdul Kalam, Arun Tiwari"
                    },
                    {"name":"Harry Potter and the Half-Blood Prince",
                    "author":"J K Rowling"
                    },
                    {"name":"Long Walk to freedom",
                    "author":"Nelson Mandela"
                    },
                    {"name":"Harry Potter and the Half-Blood Prince",
                    "author":"J K Rowling"
                    } ]
                }
            }



#REST API route mapping.
#All REST APIs should be configured here with their target classes.
# api.add_resource(Book,'/')
