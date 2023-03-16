from django.core.files.storage import FileSystemStorage
import json
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from usermanagement.models import CustomUser
from usermanagement.helpers.CheckEmail import EmailBackend


# Create your views here.

def getUserLoged(user):
    if user is not None:
        data = {
            "message": "Success Request",
            "code": 200,
            "data": [
                {
                    "id": user.id,
                    "type": user.user_type,
                    "email": user.email
                }
            ]
        }
        return data
    else:
        data = {
            "message": "Error none",
            "code": 500,
            "data": []
        }
        return data


def getMessage(message, statut):
    if statut == 200:
        data = {
            "message": message,
            "code": 200,
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


@csrf_exempt
def dologin(request):
    if request.method != 'POST':
        fp = getMessage("Denied", 500)
        return JsonResponse(fp)
    else:
        # Authenticate
        user = EmailBackend.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user is not None:
            if user.user_type == '1':
                fp = getUserLoged(user)
                return JsonResponse(fp)
            elif user.user_type == '2':
                fp = getUserLoged(user)
                return JsonResponse(fp)
            else:
                fp = getUserLoged(user)
                return JsonResponse(fp)
        else:
            fp = getMessage(f"Error User {user}  does't exist !", 500)
            return JsonResponse(fp)


def GetUserDetails(request):
    if request.user is not None:
        fp = getUserLoged(request.user)
        return JsonResponse(fp)
    else:
        fp = getMessage(f"Login First", 500)
        return JsonResponse(fp)


@csrf_exempt
def logout(request):
    if request.user is not None:
        logout(request)
        result = {
            "code": 200,
            "message": "success"
        }
    return JsonResponse(result)


@csrf_exempt
def agence_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # pict = request.FILES.get('profile_pic')
        # fs = FileSystemStorage()
        # filename = fs.save(pict.name, pict)
        # pict_url = fs.url(filename)
        try:
            agence = CustomUser.objects.create_user(
                email=email, password=password, user_type=2)
            agence.address = address
            agence.save()
            fp = getMessage("Success Created", 200)
            return JsonResponse(fp)

        except Exception as e:
            fp = getMessage("Could Not Add " + str(e), 500)
            return JsonResponse(fp)
    else:
        fp = getMessage("Please fulfil all requirements", 500)
        return JsonResponse(fp)


@csrf_exempt
def wib_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # pict = request.FILES.get('profile_pic')
        # fs = FileSystemStorage()
        # filename = fs.save(pict.name, pict)
        # pict_url = fs.url(filename)
        try:
            wid = CustomUser.objects.create_user(
                email=email, password=password, user_type=1, first_name=first_name)
            wid.address = address
            wid.save()
            fp = getMessage("Success Created", 200)
            return JsonResponse(fp)

        except Exception as e:
            fp = getMessage("Could not add" + str(e), 500)
            return JsonResponse(fp)
    else:
        messages.error(request, "Please fulfil all requirements")
        fp = getMessage("Please fulfil all requirements", 500)
        return JsonResponse(fp)


@csrf_exempt
def client_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # pict = request.FILES.get('profile_pic')
        # fs = FileSystemStorage()
        # filename = fs.save(pict.name, pict)
        # pict_url = fs.url(filename)
        try:
            client = CustomUser.objects.create_user(
                email=email, password=password, user_type=1, first_name=first_name, last_name=last_name)
            client.address = address
            client.save()
            fp = getMessage("Success Created", 200)
            return JsonResponse(fp)

        except Exception as e:
            fp = getMessage("Could Not Add " + str(e), 500)
            return JsonResponse(fp)
    else:
        messages.error(request, "Please fulfil all requirements")
        fp = getMessage("Please fulfil all requirements", 500)
        return JsonResponse(fp)
