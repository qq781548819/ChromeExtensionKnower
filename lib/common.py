import locale
import json
import io
from codecs import BOM_UTF8
from collections import OrderedDict

def get_int(stri = ''):
    stri = stri.strip('+')
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
    return locale.atoi(stri)

def dict2file(dic = {}, path=''):
    if dic:
        dic = OrderedDict(dic)
        with io.open(path, 'a', encoding='utf-8') as f:
            json.dump(dic, f)
            f.write('\n')

class Error(Exception):
    pass

def do_ten_times_til_true(func):
    def _do_ten_times_til_true(*args, **kwargs):
        ret = False
        for i in range(10):
            try:
                ret = func(*args, **kwargs)
            except Exception as e:
                ret = False
            if ret:
                break
        return ret
    return _do_ten_times_til_true

def lstrip_bom(str_, bom=BOM_UTF8):
    if str_.startswith(bom):
        return str_[len(bom):]
    else:
        return str_
