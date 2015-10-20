# top level wrapper to run the autocaller app
import os

from autocaller.app import app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    if port == 3000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)