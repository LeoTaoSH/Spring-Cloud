# -*- coding: utf-8 -*-
import itchat
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
itchat.auto_login(hotReload=False)
xiaoice = itchat.search_mps(name='小冰')[0]['UserName']

who_send = None
@itchat.msg_register(itchat.content.TEXT)
def fw_ice(msg):
    msg_text = msg['Text']
    global who_send
    who_send = msg['FromUserName']
    itchat.send(msg_text, xiaoice)

    
@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def get_ice(msg):
    ice_msg = msg['Text']
    global who_send
    itchat.send(ice_msg, toUserName=who_send)
    
itchat.run()
