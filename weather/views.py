from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+ '&appid=a680cb287c60eaf3e2c194d73c2a76a9').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': '('+str(json_data['coord']['lon']) + ', '+ str(json_data['coord']['lat'])+')',
            'temp':str(float(json_data['main']['temp'])-273.0)+' C',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
        }
    else:
        city=''
        data={}
    return render(request, 'index.html',{'city':city, 'data':data})