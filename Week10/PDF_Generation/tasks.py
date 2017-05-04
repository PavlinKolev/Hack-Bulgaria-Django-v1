import os
import pdfkit
import json
from celery import group
from celery_app import app


@app.task
def create_pdf_from_url(url):
    if not os.path.isdir('pdfs'):
        os.mkdir('pdfs')

    if not os.path.exists('downloaded.json'):
        with open('downloaded.json', 'w') as f:
            f.writelines(json.dumps({create_pdf_from_url.request.id: url}))
    else:
        with open('downloaded.json', 'r+') as f:
            downloaded = json.load(f)
            downloaded[create_pdf_from_url.request.id] = url
            f.seek(0)
            f.truncate()
            f.writelines(json.dumps(downloaded))

    pdfkit.from_url(url, 'pdfs/{}.pdf'.format(create_pdf_from_url.request.id))
