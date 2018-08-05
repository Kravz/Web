import json
from urllib.request import urlopen
from urllib.parse import urlencode


def getCountry(strings):
    params = {"address": strings}
    ucode = urlencode(params, encoding="utf-8")

    response = urlopen("https://maps.googleapis.com/maps/api/geocode/json?" + ucode).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("results")[0].get("formatted_address")


print(getCountry("Бердянск сильпо"))



