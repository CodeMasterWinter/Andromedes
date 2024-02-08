from django.shortcuts import render


def business_card(request):

    context = {

    }

    return render(request, 'andromedesweb/business-card.html', context)