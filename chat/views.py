from django.shortcuts import render

def message_page(request):
    return render(request, "chat/message_page.html")
