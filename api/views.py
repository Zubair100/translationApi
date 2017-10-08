from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from api.models import Animal, ProtectionStatus


@csrf_exempt
def translate(request):

    body = request.body
    ##oadedjson = json.dumps(body)

    jsonbody = json.loads(body)

    #translate here
    words = jsonbody['responses'][0]['textAnnotations'][0]['description']

    translatedText = translate_text(words, 'en')

    #data = ""
    #for word in words.split(" "):
    #    data = json.load(urllib3.urlopen('http://environment.ehp.qld.gov.au/species/?op=speciessearch&kingdom=animals&species' + word))

    splitUpMenu = translatedText.split("\n")

    print(splitUpMenu)

    result = ""

    for words in splitUpMenu:
        print("hi")
        if (words == ''):
            continue
        else:
            result += get_format_text(words.split(" "))

    data = {"text": result}

    return JsonResponse(data)
# Create your views here.

def get_format_text(splitUpWords):
    result = ""
    for word in splitUpWords:
        print(word)
        checkit = Animal.objects.filter(animal_names__icontains=word)
        if checkit.exists():
            endangered = ProtectionStatus.objects.filter(animal_id=checkit[0])[0].animal_protection_status
            result += " " + "<span style = \"color:#FF0000;\">" + word + "(" + str(endangered) + ")" + "</span>"
        else:
            result += " " + word

    return result + "\n"



def translate_text(text, target):
    # Translates text into the target language.

    from google.cloud import translate

    translate_client = translate.Client()

    import six
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    result = translate_client.translate(
        text, target_language=target)

    #    print(u'Text: {}'.format(result['input']))
    # print(u'Translation: {}'.format(result['translatedText']))

    return result['translatedText']

#   print(u'Detected source language: {}'.format(
#       result['detectedSourceLanguage']))


# targetDef = 'en'
# example_text = "Hola saludos desde"
# translate_text(example_text, targetDef)



