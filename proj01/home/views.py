from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "*** home *** start ***<p />"
    str_out += "ホームです。<p />"
    str_out += "<a href='app01/'>app01</a><p />"
    str_out += "<a href='app02/'>app02</a><p />"
    str_out += "*** home *** end ***<p />"
    return HttpResponse(str_out)