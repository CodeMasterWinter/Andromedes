from django.shortcuts import render


def index(request):

    context = {

    }

    return render(request, "andromedesweb/index.html", context)

def business_card(request):

    context = {

    }

    return render(request, 'andromedesweb/business-card.html', context)