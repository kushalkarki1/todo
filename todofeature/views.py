from django.shortcuts import render


def home(request):
    return render(request, "home.html")


# GET -> get data from server
# POST
# PUT
# PATCH
# DELETE