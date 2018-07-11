# _*_ coding: utf-8 _*_
import md5

def md5_encode(str):
    return md5.new(str).hexdigest()