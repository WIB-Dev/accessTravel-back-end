def getMessage(message, statut, data=None):
    if statut == 200:
        data = {
            "message": message,
            "code": 200,
            "data": data
        }
        return data

    if statut == 201:
        data = {
            "message": message,
            "code": 201,
            "data": []
        }
        return data

    if statut == 500:
        data = {
            "message": message,
            "code": 500,
            "data": []
        }
        return data

    if statut == 404:
        data = {
            "message": message,
            "code": 404,
            "data": []
        }
        return data