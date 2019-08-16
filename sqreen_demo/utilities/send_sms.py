#Reference: https://www.smscountry.com/bulk-smsc-api-documentation


def send_sms():
    import urllib.request, urllib.parse
    from sqreen_demo.config import (
        SMS_COUNTRY_USERNAME, SMS_COUNTRY_PASSWORD, SMS_COUNTRY_SID, SUBJECT,
        MOBILE_NUMBER_TO_SEND_SMS
    )
    base_url = 'http://api.smscountry.com/SMSCwebservice_bulk.aspx'
    values = {
        'user': SMS_COUNTRY_USERNAME,
        'passwd': SMS_COUNTRY_PASSWORD,
        'message': SUBJECT,
        'mobilenumber': MOBILE_NUMBER_TO_SEND_SMS,
        'mtype': 'N',
        'DR': 'Y'
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    request = urllib.request.Request(base_url, data)
    response = urllib.request.urlopen(request)
    #print (response.read().decode('utf-8'))
    return
