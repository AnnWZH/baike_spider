'''
Created on Jan 24, 2017

@author: weida
'''
import url_manager
import html_download
import html_parser
import html_output
import traceback

class spriderMain(object):
    def __init__(self):
        self.urls=url_manager.urlManager()
        self.download=html_download.htmlDownload()
        self.parser=html_parser.htmlParser()
        self.output=html_output.htmlOutput()
        
    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print ("craw %d: %s"%(count,new_url))
                html_cont=self.download.download(new_url)
                new_urls,new_data=self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                if count==10:
                    break
                count=count+1
            except:
                print('craw faild:')
                traceback.print_exc()
            
        self.output.output_html()

if __name__=='__main__':
    root_url='http://baike.baidu.com/view/21087.htm'
    obj_spider=spriderMain()
    obj_spider.craw(root_url)
    
