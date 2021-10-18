from django.shortcuts import render, redirect, reverse, get_object_or_404


# Create your views here.
def faq(request):
    return render(request, 'pages/faq.html')
