from flask import *
from datetime import *
from pprint import pprint
import random
import string

passwordGenerator = Blueprint("PasswordGenerator", __name__, static_folder="static",
                              template_folder="templates")


@passwordGenerator.route("/passwordgenerator", methods=["POST", "GET"])
def PasswordGenerator():

    if request.method == "POST":
        data = request.form
        pwlength = int(data.get('lengthpw'))
        allNumbers = data.get('numbers')
        allCharacters = data.get('characters')

        characters = list(string.ascii_letters)

        if(allNumbers == "on"):
            characters = list(string.ascii_letters + string.digits)

        if(allCharacters == "on"):
            characters = list(string.ascii_letters + "!@#$%^&*()")

        if(allCharacters == "on" and allNumbers == "on"):
            characters = list(string.ascii_letters +
                              string.digits + "!@#$%^&*()")

        password = []

        for i in range(pwlength):
            password.append(random.choice(characters))

        random.shuffle(password)
        password = "".join(password)

        return render_template("passwordgenerator.html", data=password)
    else:
        return render_template("passwordgenerator.html")
