from flask import *
from datetime import *
import requests
from pprint import pprint
import json

apicall = Blueprint("apicall", __name__, static_folder="static",
                    template_folder="templates")


@apicall.route("/apicall")
def apiCall():
    theheaders = {'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
                  'x-rapidapi-key': '052d87d6d6mshf4106b2dbf31b7fp110709jsnb31d3bc22e50'
                  }

    response_API = requests.get(
        'https://covid-19-data.p.rapidapi.com/country/code', headers=theheaders, params={'code': 'nl'})

    content = json.loads(response_API.content)

    return render_template("apicall.html", data=content)
