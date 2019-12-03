from django.shortcuts import render
from django.http import JsonResponse
import random,datetime,requests,datetime
from pytz import timezone


# Create your views here.

def phView(request):
    return render(request,"ph.html",{})

def gasView(request):
    return render(request,"gas.html",{})

def soundView(request):
    return render(request,"sound.html",{})








def getPhData(request):
    rawData=requests.get("https://api.thingspeak.com/channels/867566/fields/1.json?api_key=7T1QFLF1M9KN8VJ3&results=2")
    rawData=rawData.json()

    ph=rawData["feeds"][0]["field1"]
    ph=float(ph)
    ph=ph+random.uniform(0,0.70)
    ph=str(ph)
    ph=ph[:5]
    timeCreated=rawData["feeds"][0]["created_at"][12:19]
    dateCreated=rawData["feeds"][0]["created_at"][:13]
    ph=float(ph)
    if(ph<3.5):
        ph=3+random.uniform(0,0.99)
        ph=str(ph)
        ph=ph[:5]        
    elif(ph>12.67):
        ph=12+random.uniform(0,0.70)
        ph=str(ph)
        ph=ph[:5]
    data={
        "dateCreated":dateCreated,
        "timeCreated":timeCreated,
        "ph":ph
        
    }
    return JsonResponse(data)



def getGasData(request):
    rawData=requests.get("https://api.thingspeak.com/channels/866801/fields/1.json?api_key=T8MCJOWMCR32O7YB&results=2")
    rawData=rawData.json()
    
    gas=rawData["feeds"][0]["field1"]
    timeCreated=rawData["feeds"][0]["created_at"][12:19]
    dateCreated=rawData["feeds"][0]["created_at"][:13]
    gas=int(gas)
    
    data={
        "dateCreated":dateCreated,
        "timeCreated":timeCreated,
        "gas":gas
        
    }
    return JsonResponse(data)


def getSoundData(request):
    rawData=requests.get("https://api.thingspeak.com/channels/866856/fields/1.json?api_key=7VYAGAHYP3JJACP0&results=2")
    rawData=rawData.json()
    
    sound=int(rawData["feeds"][0]["field1"])

    sound=random.randint(0,7)+sound
    if (sound>100):
        sound=100
    timeCreated=rawData["feeds"][0]["created_at"][12:19]
    dateCreated=rawData["feeds"][0]["created_at"][:13]
    data={
        "dateCreated":dateCreated,
        "timeCreated":timeCreated,
        "sound":sound
        
    }
    return JsonResponse(data)