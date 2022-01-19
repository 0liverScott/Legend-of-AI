import datetime
import os
import time
import requests
from flask import Blueprint, url_for, render_template, request, send_from_directory, send_file

from werkzeug.utils import redirect, secure_filename


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/easteregg')
def god_saehan():
    return 'SaeHan is God of Python'

@bp.route('/')
def redirect_first():
    return redirect(url_for('main.mainpage'))

@bp.route('/main')
def mainpage():
    return render_template('main/main.html')

@bp.route('/altar_upload')
def altar():
    return render_template('altar/altar_upload.html')

@bp.route('/fail')
def fail():
    return render_template('altar/fail.html')

filenames = []

@bp.route('/altar_viewer/<now>/<count>')
def viewer(now, count):
    filenames = []
    count = int(count)
    for n in range(1, 100000):
        filenames.append("http://192.168.25.44:5000/static/%s/output_images/%05d.jpg" % (now, n))
    return render_template('altar/altar_viewer.html', filenames=filenames, count=count)

@bp.route('/filename/<now>', methods=['post'])
def filename(now):
    print(now)
    return '%s' % now


@bp.route('/fileupload', methods=['POST'])
def file_upload():
    files = request.files.getlist("file")
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    os.makedirs('C:/files/%s/videos/' % now, exist_ok=True)
    requests.post('http://192.168.25.250:5000/filename/%s' % now, now)
    for file in files:
        file.save(os.path.join('C:/files/%s/videos/' % now, file.filename))
    start = time.time()
    while True:
        end = time.time()
        timer = end - start
        if os.path.isfile('C:/files/%s/%s.zip' % (now, now)):
            return send_file(os.path.join('C:/files/%s/%s.zip' % (now, now)))
        elif timer > 30:
            return redirect(url_for('main.fail'))
    #return redirect(url_for('main.succeed'))




