import json
import requests,datetime

from flask import Flask,render_template,request
import urllib.request as myrequest

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def weather_page():
    if request.method == 'POST':
        city = request.form["city"]
    # else:
    #     city = 'Bangalore'
        print(city)

        api = "d6d7893903cd64ec4de8aa42901aefac"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)

        response = requests.get(url).json()
        print(response)

        if response['cod'] == 200:
            print(response['weather'][0]['icon'])
            data = {"temp": response.get("main")["temp"],
                    "city":response.get("name"),
                    "longitude":response["coord"]["lon"],
                    "latitude":response['coord']['lat'],
                    "sunrise":datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),
                    "sunset":datetime.datetime.fromtimestamp(response.get('sys')['sunset']),
                    "status":200,
                    "icon":response['weather'][0]['icon']}
            return render_template("home.html", mydata=data)
        elif response['cod'] == '404' or response['cod'] == '400':
            data = {"message":response['message'],
                    "status":response['cod']}
            return render_template("home.html",mydata=data)

    else:
        data = None
        return render_template("home.html",mydata=data)

app.run()

#http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=997ea79e1c9575bd4f087cf90e68205d
# "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid"=997ea79e1c9575bd4f087cf90e68205d

# --when api is source and using urllib library -> very old and basic library--
# source = myrequest.urlopen(url).read()
# print(source)

# data = json.loads(response)
# data = {"temp":list_of_data["main"]["temp"]}
# print(data["temp"])