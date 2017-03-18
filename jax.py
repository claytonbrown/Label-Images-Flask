import http.client

conn = http.client.HTTPSConnection("directline.botframework.com")

headers = {
    'authorization': "BotConnector lDY5KBvMIAk.cwA.Syc.f1xSKRRz4vU_VhkIKJwJWt0MvAyT1Z2d4vHFrz25gps",
    'accept': "application/json",
    'cache-control': "no-cache",
    'postman-token': "b28d44de-ebf0-f687-1b1c-39c63d771dff"
    }

conn.request("POST", "/api/conversations/", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
