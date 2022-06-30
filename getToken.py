import requests
def getLolData(username, password):
       
    url = 'https://auth.riotgames.com/api/v1/authorization/'

    headers = {
                    'Accept-Encoding': 'deflate, gzip', 
                    'user-agent': 'RiotClient/44.0.1.4223069.4190634 (lol-client)', 
                    'Cache-Control': 'no-cache', 
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Accept-Language': "*"
                }
    payload = {
                    'acr_values': 'urn:riot:bronze',
                    'claims': '',
                    'client_id': 'riot-client',
                    'nonce': '1',
                    'redirect_uri': 'http://localhost/redirect',
                    'response_type': 'token id_token',
                    'scope': 'openid link ban lol_region'
                }
    payload2 = {'type':'auth','username':f'{username}','password':f'{password}','remember':'','language':'en_US'}

    requestHeaders = {'Accept':'application/json',
        'Pragma':'no-cache', 
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
        'Authorization':'',
        'Accept-Language': "*"}

    session = requests.Session()
    post_req = session.post(url=url, headers=headers, json=payload, timeout=15)
    r = session.put(url=url, headers=headers, json=payload2, timeout=15).json()


    uri = r["response"]["parameters"]["uri"]
    tokens = [x.split("&")[0] for x in uri.split("=")]
    r = session.get(url="https://auth.riotgames.com/userinfo/", headers=requestHeaders, timeout=15).json()
    return tokens[1]

print(getLolData("Drarsong", "!DonOtEaTtheYe11OwSnow"))