__author__ = 'bdm4'

# Author: Giampaolo Spagoni
# Title: Senior Solution Architec
# Team: Infor OS service
# Company: Infor
# Version : 1.0.0
# Date : 25th june 2018
#
# Example of getting token using OAUTH2, Authentication_code flow, for IONAPI
# Once got the token , make an IONAPI call for logged user
#
# This code has been revisited By Giampaolo Spagoni
# you can find the original code here : https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code

import requests, json
import subprocess
import sys

from filelist import welcome_mes, get_config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# Welcome message from filelist
welcome_mes()

# get the dictionary with all setting like ti, cn, ci, cs, ... from ionapi file
ionapi = get_config()
for k in ionapi:
    print(k + ' : ' + ionapi[k])

#authorize_url = "https://xip-12-1.infor.com/InforIntSTS/connect/authorize"
authorize_url = ionapi['pu'] + ionapi['oa']

#token_url = "https://xip-12-1.infor.com/InforIntSTS/connect/token"
token_url = ionapi['pu'] + ionapi['ot']

#callback url specified when the application was defined
#callback_uri = "http://localhost:3000/redirect.html"
callback_uri = ionapi['ru']

#test_api_url = "https://xip-12-1.infor.com:7443/infor/Mingle/SocialService.Svc/User/Detail"
test_api_url = ionapi['iu'] + '/' + ionapi['ti'] + '/Mingle/SocialService.Svc/User/Detail'

#client (application) credentials - located at apim.byu.edu
#client_id = 'infor~QLRoF3lbJTnYlRk7UEnNzVIXSCxuhN5Fer7fWTKba4o'
#client_secret = 'OouOV8LN5SsRvEh9QOIE-1NQmnQRNOfIClF2Dupa8lOzwAvIIS3ZptGsnG27sducuopeBLnnsayzgTXfDm4Xtw'
client_id = ionapi['ci']
client_secret = ionapi['cs']

#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'

# added by GS
chrome_driver = 'E:/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)
driver.get(authorization_redirect_url) 

try:
    WebDriverWait(driver, 300).until(EC.title_contains("localhost"))
#    print(driver.current_url)
    ret_code = driver.current_url
    pos_code = ret_code.find('code=')
#    print(pos_code)
    amp_code = ret_code.find('&')
#    print(amp_code)
    if (amp_code) >= 0:
        authorization_code = ret_code[pos_code+5:amp_code]
    else:
        authorization_code = ret_code[pos_code+5:]    
#    print(authorization_code)
finally:
#    print(ret_code)
#    print(authorization_code)
    driver.quit()
# end added by GS

print('**********************************************************************************')
#print ("go to the following url on the browser and enter the code from the returned url: ")
print ("---  " + authorization_redirect_url + "  ---")
print('**********************************************************************************')
#authorization_code = input('code: ')

# step I, J - turn the authorization code into a access token, etc
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print ("requesting access token")
print('**********************************************************************************')

access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print('**********************************************************************************')
print ("response")
#print('**********************************************************************************')
#print (access_token_response.headers)
#print('**********************************************************************************')
#print ('body: ' + access_token_response.text)

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
#print(tokens)
access_token = tokens['access_token']
expires_in = tokens['expires_in']
token_type = tokens['token_type']
refresh_token = tokens['refresh_token']

print('**********************************************************************************')
print('{')
print('  "access token": "' + access_token +'"')
print('  "expires_in": {} '.format(expires_in)) 
print('  "token_type": "' + token_type + '"')
print('  "refresh_token": "' + refresh_token + '"')
print('}')
print('**********************************************************************************')
print('API Endpoint : ' + test_api_url)
print('**********************************************************************************')

api_call_headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print('**********************************************************************************')
print (api_call_response.text)
print('**********************************************************************************')

