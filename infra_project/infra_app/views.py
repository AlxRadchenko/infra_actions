from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "У меня все получилось, я типа молодец, хотя и не понимаю, что делаю!"
    )


def second_page(request):
    return HttpResponse("А это вторая страница!")
