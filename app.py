import os
from flask import Flask, send_from_directory, abort, url_for, redirect
from user_model_api import user_model_api

app = Flask(__name__)
app.register_blueprint(user_model_api, url_prefix='/api/model')

DATA_DIR = '/data'

@app.route('/')
def index():
    return redirect(url_for('browse', path=''))

@app.route('/browse/')
@app.route('/browse/<path:path>')
def browse(path=''):
    current_path = os.path.join(DATA_DIR, path)

    # Prevent directory traversal
    if not os.path.abspath(current_path).startswith(os.path.abspath(DATA_DIR)):
        abort(400)

    if not os.path.exists(current_path):
        return abort(404)

    if os.path.isdir(current_path):
        items = os.listdir(current_path)
        
        # Sort directories and files
        dirs = sorted([item for item in items if os.path.isdir(os.path.join(current_path, item))])
        files = sorted([item for item in items if os.path.isfile(os.path.join(current_path, item))])

        html = f'<h1>Contents of /{path}</h1><ul>'
        
        if path:
            parent_path = os.path.dirname(path)
            html += f'<li><a href="{url_for("browse", path=parent_path)}">..</a></li>'

        for d in dirs:
            dir_path = os.path.join(path, d)
            html += f'<li><a href="{url_for("browse", path=dir_path)}">{d}/</a></li>'
        
        for f in files:
            file_path = os.path.join(path, f)
            html += f'<li><a href="{url_for("download_file", filename=file_path)}">{f}</a></li>'
            
        html += '</ul>'
        return html
    else:
        abort(404)

@app.route('/files/<path:filename>')
def download_file(filename):
    # Security check
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.abspath(file_path).startswith(os.path.abspath(DATA_DIR)):
        abort(400)

    if not os.path.isfile(file_path):
        abort(404)
        
    return send_from_directory(DATA_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
