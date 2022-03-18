from django.http import HttpResponse

def index(request):
    str_out = ""
    str_out += "*** app02 *** start ***<p />"
    str_out += "おはようございます。<p />"
    str_out += "Dec/09 AM 09:55<p />"
    str_out += "<a href='../'>Return</a><p />"
    str_out += "*** app02 *** end ***<p />"
    return HttpResponse(str_out)