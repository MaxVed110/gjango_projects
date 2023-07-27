import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(requests):
    return HttpResponse('Hello')


def about(requests):
    html = "    <nav> <h2>MENU</h2><h2>MAN</h2></nav>"
    return HttpResponse(html)


def test(requests):
    html = "<h1>ELLERY X M'O CAPSULE</h1>" \
           "<p >Known for her sculptural takes on traditional tailoring, Australian arbiter of" \
           "cool" \
           "Kym Ellery teams up with Moda Operandi.</p>" \
           "<p c>$52.00</p>"
    return HttpResponse(html)
