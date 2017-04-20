#!/usr/bin/env python
# coding: utf-8

import site
import sys
print("~~~~~~~~~~~~~path~~~~~~~~~~~~~~~~\n")
print(sys.path)
#print("~~~~~~~~~~~~~prefix~~~~~~~~~~~~~~~~\n")
#print(sys.prefix)
#print("~~~~~~~~~~~~~exec_prefix~~~~~~~~~~~~~~~~\n")
#print(sys.exec_prefix)
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
#print(__file__)

import youtube_dl
import json

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def get_info(cachedir,url,username, password,sitekey):
    options = {
        'format': 'best',  #'best[height<=480]/best',#'best',  # choice of qualit
        'nocheckcertificate': True,
        'skip_download':True,
        'cachedir': cachedir,
        'youtube_include_dash_manifest': False
    }

    if (len(username) > 2 and len(password) > 2) :
        options['username'] = username;
        options['password'] = password;

    sitekeys = {
        'youtube'       : 'Youtube',
        'dailymotion'   : 'Dailymotion',
        'xvideos'       : 'XVideos',
        'nicovideo'      : 'Niconico',
    }

    if sitekey in sitekeys :
        key=sitekeys[sitekey]
    
    with youtube_dl.YoutubeDL(options) as ydl:
        if (len(key) > 2 ) :
            meta = ydl.extract_info(url, download=False, ie_key=key)
            print(key)

        if not meta:
            meta = ydl.extract_info(url, download=False)
            print("not meta %s" % meta)

    return json.dumps(meta, sort_keys=True, indent=4)
#        meta = ydl.extract_info(url, download=False,process=False)
#        meta = ydl.extract_info(url, download=False)
#        return json.dumps(meta, sort_keys=True, indent=4)

#def get_info(url):
#    try:
#        print("get_info ok %s" %url)
#        options = {
#            'format': 'best[height<=480]/best',#'best',  # choice of qualit
#            'nocheckcertificate': True,
#            'geturl': True,
#        }
#        with youtube_dl.YoutubeDL(options) as ydl:
#            meta = ydl.extract_info(url, download=False)
#            print('uploader    : %s' %(meta['url']))
#            print(json.dumps(meta, sort_keys=True))
#            return json.dumps(meta, sort_keys=True, indent=4)
#    except Exception:
#        print("Error extracting info:")
#        print(traceback.format_exc())
#        raise

def download(url, output_file, progress_cb):
    def progress_hook(event):
        progress_cb(json.dumps(event, sort_keys=True, indent=4))
    
    try:
        print("Going to download %s to %s" % (url, output_file))
        ytb = youtube_dl.YoutubeDL({
                                   "nocheckcertificate": True,
                                   "progress_hooks": [progress_hook],
                                   "restrictfilenames": True,
                                   "nooverwrites": True,
                                   "format": "best[ext=mp4]",
                                   "outtmpl": output_file,
                                   })
                                   
        ytb.download([(url)])
    except Exception:
        print("Error downloading file:")
        print(traceback.format_exc())
        raise

#get_info('https://www.youtube.com/watch?v=TjaM0tdxtYA')

#class MyLogger(object):
#
#    def debug(self, msg):
#        pass
#
#    def warning(self, msg):
#        pass
#
#    def error(self, msg):
#        print(msg)
#
#
#def my_hook(d):
#    print('my_hook ... %s' % d['status'])
#    if d['status'] == 'finished':
#        print('Done downloading, now converting ...')
#
options = {
    'format': 'best[height<=480]/best',#'best',  # choice of qualit
    'nocheckcertificate': True,
    'geturl': True,
}

with youtube_dl.YoutubeDL(options) as ydl:
    meta = ydl.extract_info('https://www.youtube.com/watch?v=TjaM0tdxtYA', download=False)
    print('uploader    : %s' %(meta['url']))

#ydl_opts = {
#    'format': 'bestaudio/best',
#    'logger': MyLogger(),
#    'progress_hooks': [my_hook],
#    'nocheckcertificate': True,
#}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    meta = ydl.extract_info('https://www.youtube.com/watch?v=TjaM0tdxtYA', download=False)
#    print('uploader    : %s' %(meta['uploader']))
#    ydl.download([unicode('https://www.youtube.com/watch?v=TjaM0tdxtYA')])
