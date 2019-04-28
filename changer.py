import os
import re
import requests
import shutil
import datetime as dt


def set_desktop_background(submission, folder):
    filename = _make_filename(folder, submission.title)
    if _check_file(filename, folder):
        return

    _load(submission.url, filename)
    _set_background(filename)
    _clear_resources(folder)


def _check_file(filename, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.exists(filename)


def _make_filename(folder, title):
    part = re.sub(r'\s', '_', f"{folder}/{title}.jpg")
    ending = re.sub(r'[^\x00-\x7F]', '', part)
    return f"{os.getcwd()}/{ending}"


def _load(url: str, filename: str):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            return True
    return False


def _set_background(filename):
    os.system(
        "gsettings set org.gnome.desktop.background picture-options 'centered'")
    os.system(
        f"gsettings set org.gnome.desktop.background picture-uri \"file:///{filename}\"")


def _clear_resources(folder):
    age_threshold = dt.datetime.now() - dt.timedelta(minutes=30)
    for f in os.listdir(folder):
        filename = f"{folder}/{f}"
        time = dt.datetime.fromtimestamp(os.path.getmtime(filename))
        if time < age_threshold:
            os.remove(filename)
