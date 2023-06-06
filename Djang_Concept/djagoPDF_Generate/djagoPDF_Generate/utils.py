import os  # A stream implementation using an in-memory bytes buffer
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .settings import BASE_DIR, STATICFILES_DIRS

                       # It inherits BufferIOBase
 
 
#pisa is a html2pdf converter using the ReportLab Toolkit,
#the HTML5lib and pyPdf.
 
#difine render_to_pdf() function
 
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)

    STATICFILES_DIRS = [os.path.join(BASE_DIR,'templates/static/images'),]
    print(STATICFILES_DIRS)


     
    context={
        "title":"HTML TO PDF",
        "Qualification":"Education", 
        "image":"STATICFILES_DIRS/Leo.png",
        "image1": "STATICFILES_DIRS/Picture.jpg"
        }
    html  = template.render(context)
    result = BytesIO()
 
     #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None