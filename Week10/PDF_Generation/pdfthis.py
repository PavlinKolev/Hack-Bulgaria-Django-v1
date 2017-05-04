import sys
import json
from tasks import create_pdf_from_url


def dispatch(command, arg):
    if command == 'download':
        result = create_pdf_from_url.delay(arg)
        print("PDF for {} will be generated. Check with this UUID: {}".format(arg, result.id))
    elif command == 'check':
        result = create_pdf_from_url.AsyncResult(arg)
        with open('pdfs/downloaded.json', 'r') as f:
            downloaded = json.load(f)
            url = downloaded[result.id]
            if result.ready:
                print("PDF for {} is located in pdfs/{}.pdf".format(url, result.id))
            else:
                print("PDF for {} is not ready yet.".format(url))


if __name__ == '__main__':
    command = sys.argv[1].strip()
    arg = sys.argv[2].strip()

    dispatch(command, arg)
