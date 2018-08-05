import json
from urllib.request import urlopen
from urllib.parse import urlencode


def getCountry(strings):
    """
    params = {"address": strings}
    ucode = urlencode(params, encoding="utf-8")

    response = urlopen("https://maps.googleapis.com/maps/api/geocode/json?" + ucode).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("results")[0].get("formatted_address")
    """
    dist = {"origins": city1, "destinations": city2}
    ucode = urlencode(dist, encoding="utf-8")

    response = urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?" + ucode).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("rows")[0].get("elements")[0].get("distance").get("text")


city1, city2 = input().split(), input().split()
#city1 = input().split()
#city2 = input().split()
print(getCountry("ssss"))



