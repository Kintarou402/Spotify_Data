{"filter":false,"title":"views.py","tooltip":"/proj01/app02/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":9,"column":32},"action":"insert","lines":["from django.http import HttpResponse","","def index(request):","    str_out = \"\"","    str_out += \"*** app02 *** start ***<p />\"","    str_out += \"おはようございます。<p />\"","    str_out += \"Dec/09 AM 09:55<p />\"","    str_out += \"<a href='../'>Return</a><p />\"","    str_out += \"*** app02 *** end ***<p />\"","    return HttpResponse(str_out)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":32},"end":{"row":9,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1647500066143,"hash":"9fb77cc0503359d923f605b8327e9eb3381aad46"}