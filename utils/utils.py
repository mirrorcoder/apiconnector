import string
import hashlib
import uuid

BASE_LIST = string.digits + string.ascii_letters# + '_-'


BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))
from HTMLParser import HTMLParser

def gen_password():
    return hashlib.md5(str(uuid.uuid4())).hexdigest()[:6]

class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def base62_decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]
    return ret


def base62_encode(integer, base=BASE_LIST):
    """
    Converts the given integer to the base62 numeral system.
    Example: 61 -> Z, 62 -> 10, 123 -> 1Z, 124 -> 20
    Used to reduce the size of tokens.
    """
    length = len(base)
    ret = ''
    while integer:
        ret = base[integer % length] + ret
        integer /= length

    return ret
