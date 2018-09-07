#pip install itchat
import itchat,json,time
from itchat.content import *

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()
#print(json.dumps(friends))
#itchat.send(msg="hello from leo",toUserName="@089c6818119875bddea11850d5fa6b91908e90da9fb2f8fd1e793f7ad1a370f1")
itchat.send(msg="hello, this is from leo's chat robot",toUserName="@f9f3bb3b5b9d2bdb2421a3e4aa3a94fda532e91a745535bbc4f7fa096f0306f8")

#@itchat.msg_register(msgType=TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)
#def text_reply(msg):
#    msg.user.send("received msg:%s, waiting for reply" % msg.text)
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print('myUserName=',myUserName)
    print('FromUserName=',msg['FromUserName'])
    remark_name=msg['User']['RemarkName']
    time.sleep(3)
    if not msg['FromUserName'] == myUserName:
        username=msg['User']['NickName']
        remarkname=msg['User']['RemarkName']
        defaultReply = 'testing ' + remarkname + ' chat robot';
        print('msg=',msg)
        print('username=',msg['User']['NickName'])
        itchat.send_msg(defaultReply,msg['FromUserName'])
 
itchat.auto_login(True)
itchat.run()
