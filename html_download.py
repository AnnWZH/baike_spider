'''
Created on Jan 24, 2017

@author: weida
'''
import urllib.request


class htmlDownload(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response=urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
    
    



