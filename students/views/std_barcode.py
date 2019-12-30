from django.http import HttpResponse
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart


class MyBarcodeDrawing(Drawing):
    def __init__(self, text_value, *args, **kw):
        barcode = createBarcodeDrawing('Code128', value=text_value, barHeight=10 * mm, humanReadable=True)
        Drawing.__init__(self, barcode.width, barcode.height, *args, **kw)
        self.add(barcode, name='barcode')


def barcode(request):
    #instantiate a drawing object

    d = MyBarcodeDrawing("HELLO WORLD")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')