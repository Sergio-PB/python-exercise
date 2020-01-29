import os

def get_work_dir():
    work_dir = os.environ.get('VIRTUAL_ENV', '')
    if work_dir is not '':
        work_dir = '/'.join(work_dir.split('/')[:-1])
    else:
        work_dir = os.getcwd()
    return work_dir

def reversed_name(name):
    return name[::-1]