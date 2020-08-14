BACKEND CHALLENGE
=====================

- Autor: Yordy Cruz
- Tel: +52 5611820006
- Mail: yordycruz96@gmail.com 


Instalación
=====================

Pasos para correr el proyecto

```
cd payments
virtualenv venv
myvenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install requests
python manage.py runserver
```

Ejecución de pruebas
====================

Request

```
Url: http://127.0.0.1:8000/payments/paypal/
Method: POST
Headers: Content-Type: application/json
Body: {"protection_eligibility":"Eligible","address_status":"confirmed","payer_id":"abd125f2-ed22-4e96-a938-5e8e7df937c4","payment_date":"20%3A12%3A59+Jan+13%2C+2009+PST","payment_status":"Completed","notify_version":"2.6","verify_sign":"AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf","receiver_id":"S8XGHLYDW9T3S","txn_type":"express_checkout","item_name":"medium","mc_currency":"USD","payment_gross":"19.95","shipping":"0.0"}
```

Response

```
{'status': 'exito', 'code': '200', 'response': '{"id":"abd125f2-ed22-4e96-a938-5e8e7df937c4","data":{"banner_message":"
<p><span>Welcome</span> to Mr X\'s website</p>
","LAST_PAYMENT_DATE":"20%3A12%3A59+Jan+13%2C+2009+PST","theme_name":"Mexico
Mexico","user_profile_image":"https://i.imgur.com/LMhM8nn.jpg","ENABLED_FEATURES":{"CERTIFICATES_INSTRUCTOR_GENERATION":"true","ENABLE_COURSEWARE_SEARCH":"true","ENABLE_EDXNOTES":"true","ENABLE_DASHBOARD_SEARCH":"true","INSTRUCTOR_BACKGROUND_TASKS":"true","ENABLE_COURSE_DISCOVERY":"true"},"displayed_timezone":"America/mexico","language_code":"es","CREATION_DATE":"2020-08-14
13:48:18.768254","user_email":"yordycruz96@gmail.com","SUBSCRIPTION":"medium"}}'}
```

cURL

```
curl -i \ -X POST -d ""{\"protection_eligibility\":\"Eligible\",\"address_status\":\"confirmed\",\"payer_id\":\"abd125f2-ed22-4e96-a938-5e8e7df937c4\",\"payment_date\":\"20%3A12%3A59+Jan+13%2C+2009+PST\",\"payment_status\":\"Completed\",\"notify_version\":\"2.6\",\"verify_sign\":\"AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf\",\"receiver_id\":\"S8XGHLYDW9T3S\",\"txn_type\":\"express_checkout\",\"item_name\":\"medium\",\"mc_currency\":\"USD\",\"payment_gross\":\"19.95\",\"shipping\":\"0.0\"}"" \ -H "Content-Type: application/json" \ http://127.0.0.1:8000/payments/paypal/
```

Response

```
HTTP/1.1 200 OK
Date: Fri, 14 Aug 2020 22:43:08 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Content-Type: text/html; charset=utf-8
X-Frame-Options: DENY
Content-Length: 700
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{'status': 'exito', 'code': '200', 'response': '{"id":"abd125f2-ed22-4e96-a938-5e8e7df937c4","data":{"banner_message":"<p><span>Welcome</span> to Mr X\'s website</p>","LAST_PAYMENT_DATE":"20%3A12%3A59+Jan+13%2C+2009+PST","theme_name":"Mexico Mexico","user_profile_image":"https://i.imgur.com/LMhM8nn.jpg","ENABLED_FEATURES":{"CERTIFICATES_INSTRUCTOR_GENERATION":"true","ENABLE_COURSEWARE_SEARCH":"true","ENABLE_EDXNOTES":"true","ENABLE_DASHBOARD_SEARCH":"true","INSTRUCTOR_BACKGROUND_TASKS":"true","ENABLE_COURSE_DISCOVERY":"true"},"displayed_timezone":"America/mexico","language_code":"es","CREATION_DATE":"2020-08-14 13:48:18.768254","user_email":"yordycruz96@gmail.com","SUBSCRIPTION":"medium"}}'}
```
