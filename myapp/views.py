from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)