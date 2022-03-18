from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "*** app01 *** start ***<p />"
    str_out += "こんにちは<p />"
    str_out += "Dec/09 AM 09:45<p />"
    str_out += "<a href='../'>Return</a><p />"
    str_out += "*** app01 *** end ***<p />"
    return HttpResponse(str_out)