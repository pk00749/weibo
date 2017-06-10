# -*- coding: utf-8 -*-
from weibo import *
   
def press_sina_weibo():  
   
    #APP_KEY = '687541622'#星际
    APP_KEY = '2950957667'#魔兽
    #APP_SECRET = 'd1a74922267853537be0ac4dac1738a3'#星际
    APP_SECRET = 'c6183f75a585a96fc0bf525fd019741c'#魔兽
    
   
    CALLBACK_URL = 'http://www.uacool.com/login/callback'  
      
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
    print client.get_authorize_url()  
      
    r = client.request_access_token(raw_input("input code:").strip())  
    client.set_access_token(r.access_token, r.expires_in)  
      
    print client.post.statuses__update(status=u'Sorry to you, this is just a testing. Please ignore me. - from My client for weibo')  
      
if __name__ == '__main__':  
    press_sina_weibo()  
