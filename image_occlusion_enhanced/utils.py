# -*- coding: utf-8 -*-
####################################################
##                                                ##
##           Image Occlusion Enhanced             ##
##                                                ##
##      Copyright (c) Glutanimate 2016-2017       ##
##       (https://github.com/Glutanimate)         ##
##                                                ##
####################################################

"""
Common reusable utilities
"""

import os, re

from aqt import mw

import urlparse, urllib
from Imaging.PIL import Image

def path2url(path):
    """URL-encode local path"""
    return urlparse.urljoin(
      'file:', urllib.pathname2url(path.encode('utf-8')))

def fname2img(path):
    """Return HTML img element for given path"""
    fname = os.path.split(path)[1]
    return '<img src="%s" />' % fname

def img2path(img, nameonly=False):
    """Extract path or file name out of HTML img element"""
    imgpatt = r"""<img.*?src=(["'])(.*?)\1"""
    imgregex = re.compile(imgpatt, flags=re.I|re.M|re.S)
    fname = imgregex.search(img)
    if not fname:
        return None
    if nameonly:
        return fname.group(2)
    fpath = os.path.join(mw.col.media.dir(),fname.group(2))
    if not os.path.isfile(fpath):
        return None
    return fpath

def imageProp(image_path):
    """Get image width and height"""
    image = Image.open(image_path)
    width, height = image.size
    return width, height
