import subprocess

def parse_exif(file):
    proc = subprocess.Popen(['exiftool', '-S', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    if hasattr(file, 'read'):
        # file-like object
        ret = proc.communicate(file.read())[0]
    else:
        # buffer
        ret = proc.communicate(file)[0]
    exif = {}
    for line in ret.splitlines():
        try:
            (tag, value) = line.split(': ')
        except:
            continue
        exif[tag] = value
    return exif