from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
# Create your views here.

@csrf_exempt
def postDatos(request):
    convert = str(request.body).replace("b'", "").rstrip("'")
    dataPostJson = json.loads(convert)
    url = 'http://localhost:8010/api/v1/customerdata/'

    respuesta = """{
        "status":"exito",
        "code":"200",
        "response":""
    }"""
    respuesta = json.loads(respuesta)
    if dataPostJson['payer_id'] == '':
        #Si el request no tiene payer_id manda a llamar el servicio para insertar 1 nuevo dato
        payload = """{
            "data": {
                "banner_message": "<p><span>Welcome</span> to Mr X's website</p>",
                "LAST_PAYMENT_DATE": "",
                "theme_name": "Mexico Mexico",
                "user_profile_image": "https://i.imgur.com/LMhM8nn.jpg",
                "ENABLED_FEATURES": {
                    "CERTIFICATES_INSTRUCTOR_GENERATION": true,
                    "ENABLE_COURSEWARE_SEARCH": true,
                    "ENABLE_EDXNOTES": true,
                    "ENABLE_DASHBOARD_SEARCH": true,
                    "INSTRUCTOR_BACKGROUND_TASKS": true,
                    "ENABLE_COURSE_DISCOVERY": true
                },
                "displayed_timezone": "America/mexico",
                "language_code": "es",
                "CREATION_DATE": "",
                "user_email": "yordycruz96@gmail.com",
                "SUBSCRIPTION": "basic"
            }
        }"""
        payload = json.loads(payload)
        if dataPostJson['payment_status'] == 'Completed':
            #si el request tiene el payment_status = Complete se actualiza el item_name=que trae el request
            payload['data']['LAST_PAYMENT_DATE'] = dataPostJson['payment_date']
            payload['data']['SUBSCRIPTION'] = dataPostJson['item_name']
        else:
            #si el request tiene el payment_status != Complete se actualiza el item_name=free
            payload['data']['SUBSCRIPTION'] = 'free'
            payload['data']['ENABLED_FEATURES']['CERTIFICATES_INSTRUCTOR_GENERATION'] = 'false'
            payload['data']['ENABLED_FEATURES']['ENABLE_COURSEWARE_SEARCH'] = 'false'
            payload['data']['ENABLED_FEATURES']['ENABLE_EDXNOTES'] = 'false'
            payload['data']['ENABLED_FEATURES']['ENABLE_DASHBOARD_SEARCH'] = 'false'
            payload['data']['ENABLED_FEATURES']['INSTRUCTOR_BACKGROUND_TASKS'] = 'false'
            payload['data']['ENABLED_FEATURES']['ENABLE_COURSE_DISCOVERY'] = 'false'

        payload['data']['LAST_PAYMENT_DATE'] = str(datetime.datetime.now())
        payload['data']['CREATION_DATE'] = str(datetime.datetime.now())

        header1 = {'Content-Type':'application/json'}
        resPost = requests.request('POST', url, headers=header1, data=json.dumps(payload))
        
        respuesta['response'] = resPost.text
    else :
        #si el request contiene payer_id manda a llamar el servicio para actualizar
        response = requests.get(url + dataPostJson['payer_id'] + '/')
        data = response.json()
        
        if dataPostJson['payment_status'] == 'Completed':
            #si el request tiene el payment_status = Complete se actualiza el item_name=que trae el request
            data['data']['LAST_PAYMENT_DATE'] = dataPostJson['payment_date']
            data['data']['SUBSCRIPTION'] = dataPostJson['item_name']
            if dataPostJson['item_name'] == 'free':
                data['data']['ENABLED_FEATURES']['CERTIFICATES_INSTRUCTOR_GENERATION'] = 'false'
                data['data']['ENABLED_FEATURES']['ENABLE_COURSEWARE_SEARCH'] = 'false'
                data['data']['ENABLED_FEATURES']['ENABLE_EDXNOTES'] = 'false'
                data['data']['ENABLED_FEATURES']['ENABLE_DASHBOARD_SEARCH'] = 'false'
                data['data']['ENABLED_FEATURES']['INSTRUCTOR_BACKGROUND_TASKS'] = 'false'
                data['data']['ENABLED_FEATURES']['ENABLE_COURSE_DISCOVERY'] = 'false'
            else:
                data['data']['ENABLED_FEATURES']['CERTIFICATES_INSTRUCTOR_GENERATION'] = 'true'
                data['data']['ENABLED_FEATURES']['ENABLE_COURSEWARE_SEARCH'] = 'true'
                data['data']['ENABLED_FEATURES']['ENABLE_EDXNOTES'] = 'true'
                data['data']['ENABLED_FEATURES']['ENABLE_DASHBOARD_SEARCH'] = 'true'
                data['data']['ENABLED_FEATURES']['INSTRUCTOR_BACKGROUND_TASKS'] = 'true'
                data['data']['ENABLED_FEATURES']['ENABLE_COURSE_DISCOVERY'] = 'true'
        else:
            #si el request tiene el payment_status != Complete se actualiza el item_name=free y ENABLED_FEATURES todos en false
            data['data']['SUBSCRIPTION'] = 'free'
            data['data']['ENABLED_FEATURES']['CERTIFICATES_INSTRUCTOR_GENERATION'] = 'false'
            data['data']['ENABLED_FEATURES']['ENABLE_COURSEWARE_SEARCH'] = 'false'
            data['data']['ENABLED_FEATURES']['ENABLE_EDXNOTES'] = 'false'
            data['data']['ENABLED_FEATURES']['ENABLE_DASHBOARD_SEARCH'] = 'false'
            data['data']['ENABLED_FEATURES']['INSTRUCTOR_BACKGROUND_TASKS'] = 'false'
            data['data']['ENABLED_FEATURES']['ENABLE_COURSE_DISCOVERY'] = 'false'

        header2 = {'Content-Type':'application/json'}
        resPut = requests.request('PUT', url + dataPostJson['payer_id'] + '/', headers=header2, data=json.dumps(data))
        respuesta['response'] = resPut.text

    return HttpResponse(str(respuesta))