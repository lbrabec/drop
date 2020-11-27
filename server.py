import os
import pathlib
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import notify2

from config import get_config

notify2.init("Drop")
app = Flask(__name__)
app.secret_key = "such secret, very wow!"


def allowed_file(filename):
    return True
    #return '.' in filename and \
    #       filename.rsplit('.', 1)[1].lower() in get_config().ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('file')
        padding = len(str(len(files)))
        cnt = 0
        for file in files:
            if file and allowed_file(file.filename):
                dropdir = os.path.expanduser(get_config().UPLOAD_FOLDER)
                pathlib.Path(dropdir).mkdir(parents=True, exist_ok=True) # FIXME do it better
                # ios does transparent conversion from heic to jpeg with random filename,
                # prefix the filenime with counter to keep files in the order they were uploaded
                filename = '{cnt:{fill}{width}}_'.format(cnt=cnt, fill='0', width=padding) + secure_filename(file.filename)
                # FIXME uploading files with the same filename (new subdir for each upload? timestamp?)
                print('saving file %s to %s' % (filename, dropdir))
                file.save(os.path.join(dropdir, filename))
                cnt += 1

        if cnt >= 0:
            n = notify2.Notification("Drop",
                                     "%d new file%s in %s" % (cnt,
                                                              "s" if cnt > 1 else "",
                                                              get_config().UPLOAD_FOLDER),
                                     "document-save-as-symbolic.symbolic")
            n.show()

        flash('File(s) successfully uploaded')
        return redirect(url_for('upload_file'))

    return render_template('index.html')


def run_server(debug=False):
    app.run(host="0.0.0.0", port=get_config().PORT, debug=debug)
