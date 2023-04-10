import urllib.parse

def createQR(size = 150, data = ""):
    parametres = urllib.parse.urlencode({
        'size': str(size) + "x" + str(size),
        'data': data
    })
    api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parametres
    return api_link
