from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    return HttpResponse("<h1 style='color: red;'>Salom dunyo</h1>")

def about(request: HttpRequest):
    return HttpResponse("<h1 style='color: red;'>Bu bizmiz😄</h1>")


def contact(request: HttpRequest):
    return HttpResponse("<input type='text'>Salom</input><h1 style='color: red;'>+996 550 240 777</h1>")


def video(request: HttpRequest):
    return HttpResponse("<iframe src='https://www.youtube.com/embed/ISDSmaSubTM?si=H3QcnCN76jsr2o2A' title='YouTube video player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' referrerpolicy='strict-origin-when-cross-origin' allowfullscreen></iframe>")
