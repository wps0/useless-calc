from django.http import HttpResponse


# from django.shortcuts import render

# Create your views here.
from django.template import loader

from calc.models import CalculationHistoryEntry


def index(request):
    # Minus w order by daje kolejność descneding
    latest_operations = CalculationHistoryEntry.objects.order_by("-date")[:5]
    template = loader.get_template("calc/index.html")
    context = {
        'latest_operations': latest_operations
    }
    return HttpResponse(template.render(context, request))


def addition(request, nr1, nr2):
    return get_http_response(request, "{0} + {1}".format(nr1, nr2), nr1 + nr2)


def subtraction(request, nr1, nr2):
    return get_http_response(request, "{0} - {1}".format(nr1, nr2), nr1 - nr2)


def multiplication(request, nr1, nr2):
    return get_http_response(request, "{0} * {1}".format(nr1, nr2), nr1 * nr2)


def division(request, nr1, nr2):
    if nr2 == 0:
        return HttpResponse("Nr2 cannot be equal to 0!")
    return get_http_response(request, "{0} / {1}".format(nr1, nr2), nr1 / nr2)


def get_http_response(request, calculation, result):
    che = CalculationHistoryEntry(calculation=calculation + " = " + str(result))
    che.save()
    template = loader.get_template("calc/result.html")
    context = {
        "calculation": calculation,
        "result": str(result)
    }
    return HttpResponse(template.render(context, request))
