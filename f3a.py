from FinbotV1.finbotpy import *
from multiprocessing import Pool, Process
from datetime import datetime
from datetime import timedelta, date
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import asyncio, pytz, pafy, time, timeit, random, sys, ast, re, os, json, threading, subprocess, string, codecs, tweepy, ctypes, urllib, urllib.parse, ffmpy, shutil, atexit, youtube_dl
from FinbotServer.protocol import TCompactProtocol
from FinbotServer.transport import THttpClient
from FinbotV1.finbot.ttypes import LoginRequest
import json, requests, FinbotService

botStart = time.time()
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

loop = asyncio.get_event_loop()
with open('finbotLogged.json', 'r') as fp:
    run_bot = json.load(fp)
    
if run_bot['kang'] == "":
    kang = LINE()
else:
	try:
		kang = (run_bot['kang'])
    except:
    	run_bot['kang'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    kang = LINE()

if run_bot['kang1'] == "":
    kang1 = LINE()
else:
	try:
		kang1 = (run_bot['kang1'])
    except:
    	run_bot['kang1'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    kang1 = LINE()

if run_bot['kang2'] == "":
    kang2 = LINE()
else:
	try:
		kang2 = (run_bot['kang2'])
    except:
    	run_bot['kang2'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    kang2 = LINE()

if run_bot['fino1'] == "":
    fino1 = LINE()
else:
	try:
		fino1 = (run_bot['fino1'])
    except:
    	run_bot['fino1'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    fino1 = LINE()

if run_bot['fino2'] == "":
    fino2 = LINE()
else:
	try:
		fino2 = (run_bot['fino2'])
    except:
    	run_bot['fino2'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    fino2 = LINE()

if run_bot['fino3'] == "":
    fino3 = LINE()
else:
	try:
		fino3 = (run_bot['fino3'])
    except:
    	run_bot['fino3'] = ""
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
    fino3 = LINE()

oepoll = OEPoll(kang)
kangSettings = kang.getSettings()
kang1Settings = kang1.getSettings()
kang2Settings = kang2.getSettings()
fino1Settings = fino1.getSettings()
fino2Settings = fino2.getSettings()
fino3Settings = fino3.getSettings()

kangMID = kang.profile.mid
kangMID = kang.getProfile().mid
Amid = fino1.getProfile().mid
Bmid = fino2.getProfile().mid
Cmid = fino3.getProfile().mid
Dmid = kang1.getProfile().mid
Emid = kang2.getProfile().mid

KAC = [fino1,fino2,fino3]
KIC = [kang,fino1,fino2,fino3,kang1]
Bots = [kangMID,Amid,Bmid,Cmid,Dmid,Emid]

Master = ["u4d2f1c2fbee16358f12c749f406cfbf0"]
Creator = ["u4d2f1c2fbee16358f12c749f406cfbf0"]

responsename1 = fino1.getProfile().displayName
responsename2 = fino2.getProfile().displayName
responsename3 = fino3.getProfile().displayName
responsename4 = kang1.getProfile().displayName

settBot = codecs.open("finbot.json","r","utf-8")
backupsOpen = codecs.open("backup.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")

Bot_Run = json.load(settBot)
Bot_Create = json.load(backupsOpen)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

protectqr = []
protectname = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
msg_dict = {}
msg_dict1 = {}
wait = {
    "finbot":True
}

Logged1 = 'WIN'
Headers = {
        'User-Agent': "Line/8.3.3",
        'X-Line-Application': "DESKTOPWIN\t8.3.FinBOT\t18.99",
        "x-lal": "ja-US_US",
    }
Logged2 = 'MAC'   
Headers2 = {
        'User-Agent': "Line/8.4.1 iPad4,1 9.0.2",
        'X-Line-Application': "DESKTOPMAC 10.10.5-YOSEMITE-x64    MAC 10.8.5",
        "x-lal": "ja-US_US",
    }
    
Logged3 = 'CHROMEOS'
Headers3 = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "CHROMEOS\t5.5.1\tFinBot-PCT\tV1.5\10.13.2",
    "x-lal": "ja-US_US",
    }
    
def headers2():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "IOSIPAD\t6.9\tFinBot-PC\t6.9",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers3():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "WIN10\t5.5.1\tFinBot-PCT\tV1.5\10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers4():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPMAC\t5.5.1\tFinBot-PCT\tV1.5\10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headers5():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPWIN\t5.5.1\tFinBot-PCT\tV1.5\10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers 
     
def headers6():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "CLOVAFRIENDS\t5.5.1\tFinBot-PCT\tV1.5\10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers

if Bot_Run["restartBot"] != None:
    kang1.sendMessage(Bot_Run["restartBot"], "🄵🄸🄽 🄱🄾🅃\nRestart")
try:
    Bot_Run["assist"] = {}
    Bot_Run["assist"][kangMID] = True
    Bot_Run["assist"][Amid] = True
    Bot_Run["assist"][Bmid] = True
    Bot_Run["assist"][Cmid] = True
    Bot_Run["assist"][Dmid] = True
    Bot_Run["assist"][Emid] = True
    backupData()
    print ("ই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅\nRunning...")
except:
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅\nRunning...")
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

def autoRestart():
    if time.time() - botStart > int(Bot_Run["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()

def backupData():
    try:
        backup = Bot_Run
        f = codecs.open('finbot.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = Bot_Create
        f = codecs.open('backup.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print (error)
        return False

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                kang.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def restart_program():
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═\nRestarted\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def restartBot():
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═\nRestarting\nPlease Wait...\n")
    backupData() #Restart and backup data
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 針D %02d 時間H %02d 分M %02d 秒S' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 針D %02d 時間H %02d 分M %02d 秒S' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "[ 合計Total {} ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i.) " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n╚══[ ┅═ই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅ ]"
        kang1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang1.sendMessage(to, "[ INFO Mention member] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "は hai..? ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Bot_Run["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang1.getGroup(to).name))
                except:
                    no = "\n╚══ই۝🄵🄸🄽 🄱🄾🅃۝ईई"
        kang1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang1.sendMessage(to, "[ INFO Sider Member] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ようこそWelcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = kang1.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Bot_Run["welcome"]+"\nGrup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang1.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        kang1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang1.sendMessage(to, "[ INFO Welcome Member] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang1.sendMessage(to, "[ INFO ] Send MentionV1 Error :\n" + str(error))

def sendMentionV1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        fino1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        fino1.sendMessage(to, "[ INFO ] Send MentionV1 Error :\n" + str(error))

def sendMentionV2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        fino2.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        fino2.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def sendMentionV3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        fino3.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        fino3.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def sendMentionV4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang1.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Bot_Run["keyCommand"]):
        cmd = pesan.replace(Bot_Run["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

groupParam = ""
def SiriMalvado(target):
    fino1.kickoutFromGroup(groupParam,[target])
    fino2.kickoutFromGroup(groupParam,[target])
    fino3.kickoutFromGroup(groupParam,[target])

def patada(target):
    random.choice(KAC).kickoutFromGroup(groupParam,[target])

def finbot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if Bot_Run["autoAdd"] == True:
                kang.findAndAddContactsByMid(op.param1)
                kang.sendMessage(op.param1, "\n私を追加してくれてありがとう...\n申し訳ありません\n あなたはブロックされています.\n 自動ブロックシステム")
            if Bot_Run["autoBlock"] == True:
                kang.sendMessage(op.param1, "申し訳ありません...Autoblock！自動ブロックがアクティブです。")
                kang.blockContact(op.param1)
            if Bot_Run["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in Master:
                    if (Bot_Run["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        fino1.findAndAddContactsByMid(op.param1)
                        fino1.sendMessage(op.param1, Bot_Run["message"])
                        fino2.findAndAddContactsByMid(op.param1)
                        fino2.sendMessage(op.param1, Bot_Run["message"])
                        fino3.findAndAddContactsByMid(op.param1)
                        fino3.sendMessage(op.param1, Bot_Run["message"])
                        kang1.findAndAddContactsByMid(op.param1)
                        kang1.sendMessage(op.param1, Bot_Run["message"])

        if op.type == 0:
            return
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if kang.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(op.param1)
                            kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            X = kang.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            fino1.updateGroup(X)
                            fino1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            Bot_Run["blacklist"][op.param2] = True
                            kang2.kickoutFromGroup(op.param1,[op.param2])
                            kang2.leaveGroup(op.param1)
                except:
                    try:
                        if fino1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in Master:
                                Ticket = fino1.reissueGroupTicket(op.param1)
                                kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                X = kang2.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kang2.updateGroup(X)
                                fino2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                Bot_Run["blacklist"][op.param2] = True
                                kang2.kickoutFromGroup(op.param1,[op.param2])
                                kang2.leaveGroup(op.param1)
                    except:
                        try:
                            if fino2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in Master:
                                    Ticket = fino2.reissueGroupTicket(op.param1)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    X = fino2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    fino2.updateGroup(X)
                                    fino3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    Bot_Run["blacklist"][op.param2] = True
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    kang2.leaveGroup(op.param1)
                        except:
                            try:
                                if fino3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in Master:
                                        Ticket = fino3.reissueGroupTicket(op.param1)
                                        kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        X = fino3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        fino3.updateGroup(X)
                                        fino1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        Bot_Run["blacklist"][op.param2] = True
                                        kang2.kickoutFromGroup(op.param1,[op.param2])
                                        kang2.leaveGroup(op.param1)
                            except:
                                try:
                                    if kang1.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in Master:
                                            Ticket = kang1.reissueGroupTicket(op.param1)
                                            kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            X = kang1.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kang1.updateGroup(X)
                                            kang1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            Bot_Run["blacklist"][op.param2] = True
                                            kang2.kickoutFromGroup(op.param1,[op.param2])
                                            kang2.leaveGroup(op.param1)
                                except:
                                    pass
            if Bot_Run["nyusup"] == True:
                try:
                    if kang.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(op.param1)
                            fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    pass
            if op.param3 == '1':
                if op.param1 in protectname:
                    try:
                        if op.param2 not in Bots and op.param2 not in Master:
                        	group = kang1.getGroup(op.param1)
                        group.name = Bot_Run["pro_name"][op.param1]
                        kang1.updateGroup(group)
                        kang1.sendMessage(op.param1, "Group Name protected\nYou have been warned..!")
                        kang1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        Bot_Run["blacklist"][op.param2] = True
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in Master:
                            	group = fino1.getGroup(op.param1)
                            group.name = Bot_Run["pro_name"][op.param1]
                            fino1.updateGroup(group)
                            fino1.sendMessage(op.param1, "Group Name protected\nYou have been warned..!")
                            Bot_Run["blacklist"][op.param2] = True
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in Master:
                                	group = fino2.getGroup(op.param1)
                                group.name = Bot_Run["pro_name"][op.param1]
                                fino2.updateGroup(group)
                                fino2.sendMessage(op.param1, "Group Name protected\nYou have been warned..!")
                                fino2.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                Bot_Run["blacklist"][op.param2] = True
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in Master:
                                    	group = fino3.getGroup(op.param1)
                                    group.name = Bot_Run["pro_name"][op.param1]
                                    fino3.updateGroup(group)
                                    fino3.sendMessage(op.param1, "Group Name protected\nYou have been warned..!")
                                    fino3.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    Bot_Run["blacklist"][op.param2] = True
                                except:
                                    pass
            if op.param3 == '1':
                if op.param1 in Bot_Run['pname']:
                    try:
                        G = fino1.getGroup(op.param1)
                    except:
                        try:
                            G = fino2.getGroup(op.param1)
                        except:
                            try:
                                G = fino3.getGroup(op.param1)
                            except:
                                pass
                    G.name = Bot_Run['pro_name'][op.param1]
                    try:
                        fino1.updateGroup(G)
                    except:
                        try:
                            fino2.updateGroup(G)
                        except:
                            try:
                                fino3.updateGroup(G)
                            except:
                                pass
                    if op.param2 in Bots and op.param2 in Master:
                        pass
                    else:
                        try:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                                kang1.sendMessage(op.param1,"No permission! \nPlease do not change group name")

        if op.type == 13:
            if kangMID in op.param3:
                if Bot_Run["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in Master:
                        kang.acceptGroupInvitation(op.param1)
                        ginfo = kang.getGroup(op.param1)
                        kang.sendMessage(op.param1,"السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ" +str(ginfo.name))
                        kang.sendMessage(op.param1,"Maaf pm dulu izin\njangan asal comot\natau undang lewat Qr")
                        kang.leaveGroup(op.param1)
                    else:
                        kang.acceptGroupInvitation(op.param1)
                        ginfo = kang.getGroup(op.param1)
                        kang.sendMessage(op.param1,"السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ" +str(ginfo.name))
            if kangMID in op.param3:
                G = kang.getGroup(op.param1)
                if Bot_Run["autoJoin"] == True:
                    if Bot_Run["limiter"]["on"] == True:
                        if len(G.members) <= Bot_Run["limiter"]["members"]:
                            kang.acceptGroupInvitation(op.param1)
                            group = kang.getGroup(op.param1)
                            kang.sendMessage(op.param1,"Maaf jumlah member\n " + str(group.name) + " kurang dari " + str(Bot_Run["limiter"]["members"]))
                            kang.leaveGroup(op.param1)
                        else:
                            kang.acceptGroupInvitation(op.param1)
                    else:
                        kang.acceptGroupInvitation(op.param1)
                elif Bot_Run["limiter"]["on"] == True:
                    if len(G.members) <= Bot_Run["limiter"]["members"]:
                        kang.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in Bot_Run["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kang.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                if Bot_Run["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Master:
                        fino1.acceptGroupInvitation(op.param1)
                        ginfo = fino1.getGroup(op.param1)
                        contact = fino1.getGroup(op.param2)
                        fino1.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino1.leaveGroup(op.param1)
                    else:
                        fino1.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                if Bot_Run["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Master:
                        fino2.acceptGroupInvitation(op.param1)
                        ginfo = fino2.getGroup(op.param1)
                        contact = fino2.getGroup(op.param2)
                        fino2.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino2.leaveGroup(op.param1)
                    else:
                        fino2.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                if Bot_Run["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Master:
                        fino3.acceptGroupInvitation(op.param1)
                        ginfo = fino3.getGroup(op.param1)
                        contact = fino3.getGroup(op.param2)
                        fino3.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino3.leaveGroup(op.param1)
                    else:
                        fino3.acceptGroupInvitation(op.param1)
            if Dmid in op.param3:
                if Bot_Run["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Master:
                        kang1.acceptGroupInvitation(op.param1)
                        ginfo = kang1.getGroup(op.param1)
                        contact = kang1.getGroup(op.param2)
                        kang1.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        kang1.leaveGroup(op.param1)
                    else:
                        kang1.acceptGroupInvitation(op.param1)
            if Bot_Run["BLinviter"] == True:
            	if op.param2 in Bot_Run["blacklist"]:
                	random.choice(KIC).cancelGroupInvitation(op.param1,[op.param3])
            	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in Bot_Run["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KIC).cancelGroupInvitation(op.param1, matched_list)
                    #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in Master:
                    try:
                        group = fino1.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            fino1.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = fino2.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                fino2.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = fino3.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    fino3.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kang1.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kang1.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in Bot_Run["blacklist"]:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = kang1.getGroup(op.param1)
                contact = kang1.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                kang1.sendImageWithURL(op.param1, image)
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in Master:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                fino3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots or Master:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in Bot_Run["blacklist"]:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Bot_Run["blacklist"]:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Bot_Run["blacklist"]:
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 in Bot_Run["blacklist"]:
                if op.param2 not in Bots or Master:
                    try:
                        if op.param3 not in Bot_Run["blacklist"]:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                            print ("[32] fino1 BL CANCELED")
                    except:
                        try:
                            if op.param3 not in Bot_Run["blacklist"]:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                                print ("[32] fino2 BL CANCELED")
                        except:
                            try:
                                if op.param3 not in Bot_Run["blacklist"]:
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    print ("[32] fino3 BL CANCELED")
                            except:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots or Master:
                    Bot_Run["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19:
            if kangMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino1.kickoutFromGroup(op.param1,[op.param2])
                        fino1.inviteIntoGroup(op.param1,[op.param3])
                        kang.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                            fino2.inviteIntoGroup(op.param1,[op.param3])
                            kang.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino3.kickoutFromGroup(op.param1,[op.param2])
                                fino3.inviteIntoGroup(op.param1,[op.param3])
                                kang.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kang1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kang1.updateGroup(G)
                                    Ticket = kang1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang1.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino1.kickoutFromGroup(op.param1,[op.param2])
                                        fino1.inviteIntoGroup(op.param1,[op.param3])
                                        kang.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino2.inviteIntoGroup(op.param1,[op.param3])
                                            fino2.kickoutFromGroup(op.param1,[op.param2])
                                            kang.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino2.kickoutFromGroup(op.param1,[op.param2])
                        fino2.inviteIntoGroup(op.param1,[op.param3])
                        fino1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino3.kickoutFromGroup(op.param1,[op.param2])
                            fino3.inviteIntoGroup(op.param1,[op.param3])
                            fino1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kang1.kickoutFromGroup(op.param1,[op.param2])
                                kang1.inviteIntoGroup(op.param1,[op.param3])
                                fino1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino2.kickoutFromGroup(op.param1,[op.param2])
                                    fino3.updateGroup(G)
                                    Ticket = fino3.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang2.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino2.kickoutFromGroup(op.param1,[op.param2])
                                        fino2.inviteIntoGroup(op.param1,[op.param3])
                                        fino1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino3.inviteIntoGroup(op.param1,[op.param3])
                                            fino3.kickoutFromGroup(op.param1,[op.param2])
                                            fino1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino3.kickoutFromGroup(op.param1,[op.param2])
                        fino3.inviteIntoGroup(op.param1,[op.param3])
                        fino2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                            fino1.inviteIntoGroup(op.param1,[op.param3])
                            fino2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kang1.kickoutFromGroup(op.param1,[op.param2])
                                kang1.inviteIntoGroup(op.param1,[op.param3])
                                fino2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    fino1.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino3.kickoutFromGroup(op.param1,[op.param2])
                                        fino3.inviteIntoGroup(op.param1,[op.param3])
                                        fino2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kang1.inviteIntoGroup(op.param1,[op.param3])
                                            kang1.kickoutFromGroup(op.param1,[op.param2])
                                            fino2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        kang1.kickoutFromGroup(op.param1,[op.param2])
                        kang1.inviteIntoGroup(op.param1,[op.param3])
                        fino3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kang2.kickoutFromGroup(op.param1,[op.param2])
                            kang2.inviteIntoGroup(op.param1,[op.param3])
                            fino3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino1.kickoutFromGroup(op.param1,[op.param2])
                                fino1.inviteIntoGroup(op.param1,[op.param3])
                                fino3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kang1.kickoutFromGroup(op.param1,[op.param2])
                                    fino2.updateGroup(G)
                                    Ticket = fino2.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang2.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    #sw2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kang1.kickoutFromGroup(op.param1,[op.param2])
                                        kang.inviteIntoGroup(op.param1,[op.param3])
                                        fino3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino1.kickoutFromGroup(op.param1,[op.param2])
                                            kang.inviteIntoGroup(op.param1,[op.param3])
                                            fino3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino3.kickoutFromGroup(op.param1,[op.param2])
                        fino3.inviteIntoGroup(op.param1,[op.param3])
                        kang1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                            fino2.inviteIntoGroup(op.param1,[op.param3])
                            kang1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino1.kickoutFromGroup(op.param1,[op.param2])
                                fino1.inviteIntoGroup(op.param1,[op.param3])
                                kang1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang2.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino3.kickoutFromGroup(op.param1,[op.param2])
                                        fino3.inviteIntoGroup(op.param1,[op.param3])
                                        kang1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kang.inviteIntoGroup(op.param1,[op.param3])
                                            fino1.kickoutFromGroup(op.param1,[op.param2])
                                            kang1.acceptGroupInvitation(op.param1)
                                        except:
                                            kang2.kickoutFromGroup(op.param1,[op.param2])
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino3.kickoutFromGroup(op.param1,[op.param2])
                        fino3.inviteIntoGroup(op.param1,[op.param3])
                        kang1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                            fino2.inviteIntoGroup(op.param1,[op.param3])
                            kang1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino1.kickoutFromGroup(op.param1,[op.param2])
                                fino1.inviteIntoGroup(op.param1,[op.param3])
                                kang1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang2.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino3.kickoutFromGroup(op.param1,[op.param2])
                                        fino3.inviteIntoGroup(op.param1,[op.param3])
                                        kang1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino1.inviteIntoGroup(op.param1,[op.param3])
                                            fino1.kickoutFromGroup(op.param1,[op.param2])
                                            kang1.acceptGroupInvitation(op.param1)
                                        except:
                                            kang2.inviteIntoGroup(op.param1,[op.param3])
                                            kang1.acceptGroupInvitation(op.param1)
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    Bot_Run["blacklist"][op.param2] = True
                    try:
                        fino3.kickoutFromGroup(op.param1,[op.param2])
                        kang.inviteIntoGroup(op.param1,[op.param3])
                        kang2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                            fino2.inviteIntoGroup(op.param1,[op.param3])
                            kang2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino1.kickoutFromGroup(op.param1,[op.param2])
                                kang.inviteIntoGroup(op.param1,[op.param3])
                                kang2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kang.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kang.kickoutFromGroup(op.param1,[op.param2])
                                    kang.updateGroup(G)
                                    Ticket = kang.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kang2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang2.updateGroup(G)
                                    kang2.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino3.kickoutFromGroup(op.param1,[op.param2])
                                        fino3.inviteIntoGroup(op.param1,[op.param3])
                                        kang2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino1.inviteIntoGroup(op.param1,[op.param3])
                                            fino1.kickoutFromGroup(op.param1,[op.param2])
                                            kang2.acceptGroupInvitation(op.param1)
                                        except:
                                            kang.inviteIntoGroup(op.param1,[op.param3])
                                            kang2.acceptGroupInvitation(op.param1)
                return

        if op.type == 55:
            try:
                if op.param1 in Bot_Run["readPoint"]:
                   if op.param2 in Bot_Run["readMember"][op.param1]:
                       pass
                   else:
                       Bot_Run["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
            if Bot_Run['setWicked'][op.param1]==True:
                if op.param1 in Bot_Run['setTime']:
                    Name = kang1.getContact(op.param2).displayName
                    Ppname = kang1.getContact(op.param2).pictureStatus
                    if Name in Bot_Run['setSider'][op.param1]:
                        pass
                    else:
                        Bot_Run['setSider'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        kang1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Ppname)
            if op.param2 in Bot_Run["blacklist"]:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kang.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if Bot_Run["scanner"] == True:
                    kang.sendChatChecked(to, msg_id)
                if to in Bot_Run["scanPoint"]:
                    if sender not in Bot_Run["scanROM"][msg.to]:
                        Bot_Run["scanROM"][msg.to][sender] = True
                if Bot_Run["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            kang.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            kang.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        print (error)
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = kang.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = kang.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 65:
            if Bot_Run["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = kang.getGroup(at)
                                ryan = kang.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                kang.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                kang.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = kang.getGroup(at)
                                ryan = kang.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                kang.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if Bot_Run["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = kang.getGroup(at)
                                ryan = kang.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                kang.sendMessage(at, str(ret_))
                                kang.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["finbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if Bot_Run["talkban"] == True:
                   if msg._from in Bot_Run["Talkblacklist"]:
                      try:
                          random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(KAC).kickoutFromGroup(msg.to, [msg._from])
 
        if op.type == 26:
           text = msg.text
           if msg.text in Bot_Run["TalkList"]:
              if Bot_Run["autokick"] == True:
                if msg._from not in Bots or Master:
                   try:
                   	random.choice(KIC).sendMessage(msg.to,"Ngapain hayoo...? \n\n???")
                   	random.choice(KIC).kickoutFromGroup(msg.to, [msg._from])
                   except:
                   	random.choice(KIC).sendMessage(msg.to,"Mau Ngapain kak?\n\nHati2 anda menucapkan kata larangan...!")

        if op.type == 26:
           if wait["finbot"] == True:
               if Bot_Run["ResponPc"] == True:
                 if msg.toType == 0:
                     kang.sendChatChecked(msg._from,msg.id)
                     contact = kang.getContact(msg._from)
                     #kang.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                     kang.sendMessage(msg._from, "╔═══════════════╗\n「Auto Reply」\n  ??🄸🄽 🄱🄾🅃\nHaii... {}".format(contact.displayName) + "\n Mohon maaf....!\nIni adalah pesan otomatis, \nJika ada yang penting hubungi saya nanti\n Terima Kasih\n\n╚═══════════════╝")
               if "MENTION" in msg.contentMetadata.keys() != None:
                 if Bot_Run['detectMention'] == True:
                     contact = kang.getContact(msg._from)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  #kang1.sendImageWithURL(msg._from,ret_)
                                  sendMessageWithMention(msg._from,Bot_Run["Respontag"])
                                  break

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if Bot_Run["MentionKick"] == True:
                     contact = kang1.getContact(msg._from)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  kang1.sendMessage(msg.to,"don't tag me")
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg._from])
                                  break

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 1:
                 if msg._from in Master:
                    if Bot_Run["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = kang.server.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Bot_Run["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            kang1.sendMessage(msg.to, "Add image success")
                        Bot_Run["Img"] = {}
                        Bot_Run["Addimage"] = False
               if msg.contentType == 2:
                 if msg._from in Master:
                    if Bot_Run["Addvideo"]["status"] == True:
                        path = kang1.downloadObjectMsg(msg.id)
                        videos[Bot_Run["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang1.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(Bot_Run["Addvideo"]["name"])))
                        Bot_Run["Addvideo"]["status"] = False                
                        Bot_Run["Addvideo"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in Master:
                    if Bot_Run["Addaudio"]["status"] == True:
                        path = kang1.downloadObjectMsg(msg.id)
                        audios[Bot_Run["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang1.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(Bot_Run["Addaudio"]["name"])))
                        Bot_Run["Addaudio"]["status"] = False                
                        Bot_Run["Addaudio"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in Master:
                    if Bot_Run["Addsticker"]["status"] == True:
                        stickers[Bot_Run["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang1.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(Bot_Run["Addsticker"]["name"])))
                        Bot_Run["Addsticker"]["status"] = False                
                        Bot_Run["Addsticker"]["name"] = ""
               if msg.contentType == 1:
                 if msg._from in Master:
                    if Bot_Run["changePicture"] == True:
                       path1 = fino1.downloadObjectMsg(msg_id)
                       path2 = fino2.downloadObjectMsg(msg_id)
                       path3 = fino3.downloadObjectMsg(msg_id)
                       path4 = kang1.downloadObjectMsg(msg_id)
                       Bot_Run["changePicture"] = False
                       fino1.updateProfilePicture(path1)
                       fino1.sendMessage(msg.to, Bot_Run["Responcft"])
                       fino2.updateProfilePicture(path2)
                       fino2.sendMessage(msg.to, Bot_Run["Responcft"])
                       fino3.updateProfilePicture(path3)
                       fino3.sendMessage(msg.to, Bot_Run["Responcft"])
                       kang1.updateProfilePicture(path4)
                       kang1.sendMessage(msg.to, Bot_Run["Responcft"])
                 if msg._from in Master:
                     if kangMID in Bot_Run["foto"]:
                         path = kang.downloadObjectMsg(msg.id)
                         del Bot_Run["foto"][kangMID]
                         kang.updateProfilePicture(path)
                         kang.sendMessage(msg.to,Bot_Run["Responcft"])
                 if msg._from in Master:
                     if Amid in Bot_Run["foto"]:
                         path = fino1.downloadObjectMsg(msg.id)
                         del Bot_Run["foto"][Amid]
                         fino1.updateProfilePicture(path)
                         fino1.sendMessage(msg.to,Bot_Run["Responcft"])
                 if msg._from in Master:
                     if Bmid in Bot_Run["foto"]:
                         path = fino2.downloadObjectMsg(msg.id)
                         del Bot_Run["foto"][Bmid]
                         fino2.updateProfilePicture(path)
                         fino2.sendMessage(msg.to,Bot_Run["Responcft"])
                 if msg._from in Master:
                     if Cmid in Bot_Run["foto"]: 
                         path = fino3.downloadObjectMsg(msg.id)
                         del Bot_Run["foto"][Cmid]
                         fino3.updateProfilePicture(path)
                         fino3.sendMessage(msg.to,Bot_Run["Responcft"])
                 if msg._from in Master:
                     if Dmid in Bot_Run["foto"]:
                         path = kang1.downloadObjectMsg(msg_id)
                         del Bot_Run["foto"][Dmid]
                         kang1.updateProfilePicture(path)
                         kang1.sendMessage(msg.to,Bot_Run["Responcft"])
                 if msg._from in Master:
                     if Emid in Bot_Run["foto"]:
                         path = kang2.downloadObjectMsg(msg_id)
                         del Bot_Run["foto"][Emid]
                         kang2.updateProfilePicture(path)
                         kang2.sendMessage(msg.to,Bot_Run["Responcft"])

               if msg.contentType == 2:
                   if msg._from in Master:
                       if kangMID in Bot_Run["video"]:
                            path = kang.downloadObjectMsg(msg_id)
                            del Bot_Run["video"][kangMID]
                            kang.updateProfileVideoPicture(path)
                            kang.sendMessage(msg.to,"Photo Profile switch to video")

               if msg.toType == 2:
                 if msg._from in Master:
                   if Bot_Run["groupPicture"] == True:
                     path = kang1.downloadObjectMsg(msg_id)
                     Bot_Run["groupPicture"] = False
                     kang1.updateGroupPicture(msg.to, path)
                     kang1.sendMessage(msg.to, Bot_Run["Responcft"])

               if msg.contentType == 13:
                  if Bot_Run["invite1"] == True:
                    if msg._from in Master:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fino1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fino1.sendMessage(msg.to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in Bot_Run["blacklist"]:
                                fino1.sendMessage(msg.to,"Failure invitation, " + _name + "Blacklist user")
                                fino1.sendMessage(msg.to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fino1.findAndAddContactsByMid(target)
                                    fino1.inviteIntoGroup(msg.to,[target])
                                    fino1.sendMessage(msg.to,"Target invited : \n ➡" + _name)
                                    Bot_Run["invite1"] = False
                                    break
                                except:
                                    try:
                                        fino1.findAndAddContactsByMid(invite)
                                        fino1.inviteIntoGroup(op.param1,[invite])
                                        Bot_Run["invite1"] = False
                                    except:
                                        fino1.sendMessage(msg.to,"Negative, Error invitation")
                                        Bot_Run["invite1"] = False
                                        break

                  if Bot_Run["invite2"] == True:
                    if msg._from in Master:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fino2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fino2.sendMessage(msg.to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in Bot_Run["blacklist"]:
                                fino2.sendMessage(msg.to,"Failure invitation, " + _name + "Blacklist user")
                                fino2.sendMessage(msg.to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fino2.findAndAddContactsByMid(target)
                                    fino2.inviteIntoGroup(msg.to,[target])
                                    fino2.sendMessage(msg.to,"Target invited : \n ➡" + _name)
                                    Bot_Run["invite2"] = False
                                    break
                                except:
                                    try:
                                        fino2.findAndAddContactsByMid(invite)
                                        fino2.inviteIntoGroup(op.param1,[invite])
                                        Bot_Run["invite2"] = False
                                    except:
                                        fino2.sendMessage(msg.to,"Negative, Error invitation")
                                        Bot_Run["invite2"] = False
                                        break

                  if Bot_Run["invite3"] == True:
                    if msg._from in Master:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = fino3.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                fino3.sendMessage(msg.to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in Bot_Run["blacklist"]:
                                fino3.sendMessage(msg.to,"Failure invitation, " + _name + "Blacklist user")
                                fino3.sendMessage(msg.to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    fino3.findAndAddContactsByMid(target)
                                    fino3.inviteIntoGroup(msg.to,[target])
                                    fino3.sendMessage(msg.to,"Target invited : \n ➡" + _name)
                                    Bot_Run["invite3"] = False
                                    break
                                except:
                                    try:
                                        fino3.findAndAddContactsByMid(invite)
                                        fino3.inviteIntoGroup(op.param1,[invite])
                                        Bot_Run["invite3"] = False
                                    except:
                                        fino3.sendMessage(msg.to,"Negative, Error invitation")
                                        Bot_Run["invite3"] = False
                                        break

               if msg.contentType == 13:
                 if Bot_Run["contact"] == True:
                    msg.contentType = 0
                    kang1.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kang1.getContact(msg.contentMetadata["mid"])
                        path = kang1.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        kang1.sendMessage(msg.to,"♐ Nama : " + msg.contentMetadata["displayName"] + "\n♐ MID : " + msg.contentMetadata["mid"] + "\n♐ Status Msg : " + contact.statusMessage + "\n♐ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kang1.sendImageWithURL(msg.to, image)
                 if msg._from in Master:
                  if Bot_Run["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in Bot_Run["blacklist"]:
                        kang1.sendMessage(msg.to,"This user is already blacklist")
                        Bot_Run["wblacklist"] = False
                    else:
                        Bot_Run["wblacklist"] = True
                        Bot_Run["blacklist"][msg.contentMetadata["mid"]] = True
                        kang1.sendMessage(msg.to,Bot_Run["ResponWBL"])
                        Bot_Run["wblacklist"] = False
                 if msg._from in Master:
                  if Bot_Run["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in Bot_Run["blacklist"]:
                        del Bot_Run["blacklist"][msg.contentMetadata["mid"]]
                        kang1.sendMessage(msg.to,Bot_Run["ResponDBL"])
                        Bot_Run["dblacklist"] = False
                    else:
                        kang1.sendMessage(msg.to,"No blacklist")
                        Bot_Run["dblacklist"] = False
                 if msg._from in Master:
                  if Bot_Run["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in Bot_Run["Talkblacklist"]:
                        kang1.sendMessage(msg.to,"This user is already Talkblacklist")
                        Bot_Run["Talkwblacklist"] = False
                    else:
                        Bot_Run["Talkwblacklist"] = True
                        Bot_Run["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        kang1.sendMessage(msg.to,Bot_Run["ResponWTBL"])
                        Bot_Run["Talkwblacklist"] = False
                 if msg._from in Master:
                  if Bot_Run["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in Bot_Run["Talkblacklist"]:
                        del Bot_Run["Talkblacklist"][msg.contentMetadata["mid"]]
                        kang1.sendMessage(msg.to,Bot_Run["ResponDTBL"])
                        Bot_Run["Talkdblacklist"] = False
                    else:
                        kang1.sendMessage(msg.to,"No Talkblacklist")
                        Bot_Run["Talkdblacklist"] = False
                 if msg._from in Master:
                  if Bot_Run["addbackupmem"] == True:
                    if msg.contentMetadata["mid"] in Bot_Create["backupmem"]:
                        kang1.sendMessage(msg.to,"正常にThis user has been backuped(ˋ ・ω・´)")
                        Bot_Run["addbackupmem"] = False
                    else:
                        Bot_Run["addbackupmem"] = True
                        Bot_Create["backupmem"][msg.contentMetadata["mid"]] = True
                        kang1.sendMessage(msg.to,"れましたBackuped(ˋ ・ω・´)")
                        Bot_Run["addbackupmem"] = False
                 if msg._from in Master:
                  if Bot_Run["dbackupmem"] == True:
                    if msg.contentMetadata["mid"] in Bot_Create["backupmem"]:
                        del Bot_Create["backupmem"][msg.contentMetadata["mid"]]
                        kang1.sendMessage(msg.to,"正したDeleted(ˋ ・ω・´)")
                        Bot_Run["dbackupmem"] = False
                    else:
                        Bot_Run["dbackupmem"] = True
                        kang1.sendMessage(msg.to,"正常にNo added(ˋ ・ω・´)")
                        Bot_Run["dbackupmem"] = False

               if msg.contentType == 16:
                 if Bot_Run["checkPost"] == True:
                     try:
                         ret_ = "╔════[ Post Detail ]"
                         if msg.contentMetadata["serviceType"] == "GB":
                             contact = kang1.getContact(sender)
                             auth = "\n╠❐ Author : {}".format(str(contact.displayName))
                         else:
                             auth = "\n╠❐ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                         purl = "\n╠❐ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                         ret_ += auth
                         ret_ += purl
                         if "mediaOid" in msg.contentMetadata:
                             object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                             if msg.contentMetadata["mediaType"] == "V":
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                 ret_ += murl
                             else:
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                             ret_ += ourl
                         if "stickerId" in msg.contentMetadata:
                             stck = "\n╠❐ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                             ret_ += stck
                         if "text" in msg.contentMetadata:
                             text = "\n╠❐ Note : {}".format(str(msg.contentMetadata["text"]))
                             ret_ += text
                         ret_ += "\n╚══[ 🄵🄸🄽 🄱🄾🅃 ]"
                         kang1.sendMessage(to, str(ret_))
                     except:
                         kang1.sendMessage(msg.to,"Invalid Post")
               if msg.contentType == 7:
                if Bot_Run["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            kang1.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang1.downloadFileURL(data)
                               kang1.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            kang1.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang1.downloadFileURL(data)
                               kang1.sendImage(msg.to,path)

               if msg.contentType == 0:
                    if Bot_Run["AutoRead"] == True:
                        fino1.sendChatChecked(msg.to, msg_id)
                        fino2.sendChatChecked(msg.to, msg_id)
                        fino3.sendChatChecked(msg.to, msg_id)
                        kang1.sendChatChecked(msg.to, msg_id)
                        kang2.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                    	for sticker in stickers:
                         if msg._from in Master:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              kang1.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in Master:
                           if text.lower() == image:
                              kang1.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in Master:
                           if text.lower() == audio:
                              kang1.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in Master:
                           if text.lower() == video:
                              kang1.sendVideo(msg.to, videos[video])
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "@login" or cmd == "bot on":
                            if msg._from in Master:
                                wait["finbot"] = True
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                kang1.sendMessage(msg.to, "🔄 @Relogin \n❏ Day : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n❏ Time : [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        elif cmd == "@logout" or cmd == "bot off":
                            if msg._from in Master:
                                wait["finbot"] = False
                                kang1.sendMessage(msg.to, "@Logout")
                        if cmd == "siri:on" or cmd == "siri on":
                            if msg._from in Master:
                                wait["finbot"] = True
                                Bot_Run["unsendMessage"] = True
                                random.choice(KIC).sendMessage(msg.to, "すでにオンだよ(｀・ω・´)")
                        if cmd == "siri:off" or cmd == "siri off":
                            if msg._from in Master:
                                wait["finbot"] = True
                                Bot_Run["unsendMessage"] = False
                                random.choice(KIC).sendMessage(msg.to, "すでにオンだよ(｀・ω・´)")

                        elif cmd == "set" or cmd == 'sett':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╔═══════════\n"
                                md+="║۝🄵🄸🄽 🄱🄾🅃۝\n"
                                md+="╠═══════════\n"
                                if Bot_Run["autoJoin"] == True: md+="║❏〘 Auto join 〙『 📲 』\n"
                                else: md+="║❏〘 Auto join 〙『 📴 』\n"
                                if Bot_Run["autoAdd"] == True: md+="║❏〘 Auto add 〙『 📲 』\n"
                                else: md+="║❏〘 Auto add 〙『 📴 』\n"
                                if Bot_Run["autoBlock"] == True: md+="║❏〘 Auto block 〙『 📲 』\n"
                                else: md+="║❏〘 Auto block 〙『 📴 』\n"
                                if Bot_Run["autoLeave"] == True: md+="║❏〘 Auto leave 〙『 📲 』\n"
                                else: md+="║❏〘 Auto leave 〙『 📴 』\n"
                                if Bot_Run["AutoRead"] == True: md+="║❏〘 Auto read 〙『 📲 』\n"
                                else: md+="║❏〘 Auto read 〙『 📴 』\n"
                                if Bot_Run["invite1"] == True: md+="║❏〘 Auto Inv 〙『 📲 』\n"
                                else: md+="║❏〘 Auto Inv 〙『 📴 』\n"
                                if Bot_Run["autokick"] == True: md+="║❏〘 Warning 〙『 📲 』\n"
                                else: md+="║❏〘 Warning 〙『 📴 』\n"
                                if Bot_Run["addbackupmem"] == True: md+="║❏〘 Backup mem 〙『 📲 』\n"
                                else: md+="║❏〘 Backup mem 〙『 📴 』\n"
                                if Bot_Run["checkPost"] == True: md+="║❏〘 CheckPost 〙『 📲 』\n"
                                else: md+="║❏〘 CheckPost 〙『 📴 』\n"
                                if Bot_Run["contact"] == True: md+="║❏〘 Contact 〙『 📲 』\n"
                                else: md+="║❏〘 Contact 〙『 📴 』\n"
                                if Bot_Run["changePicture"] == True: md+="║❏〘 Change pict 〙『 📲 』\n"
                                else: md+="║❏〘 Change pict 〙『 📴 』\n"
                                if Bot_Run["nyusup"] == True: md+="║❏〘 Mode Nyusup 〙『 📲 』\n"
                                else: md+="║❏〘 Mode Nyusup 〙『 📴 』\n"
                                if Bot_Run["limiter"]["on"] == True: md+="║❏〘 limiter 〙" + "『 " + str(Bot_Run["limiter"]["members"]) + " 』" + "\n"
                                else: md+="􀠁􀆩􏿿║❏〘 limiter 〙:『 📴 』\n"
                                if Bot_Run["scanner"] == True: md+="║❏〘 Scanner 〙『 📲 』\n"
                                else: md+="║❏〘 Scanner 〙『 📴 』\n"
                                if Bot_Run["detectMention"] == True: md+="║❏〘 Respon 〙『 📲 』\n"
                                else: md+="║❏〘 Respon 〙『 📴 』\n"
                                if Bot_Run["detectMention1"] == True: md+="║❏〘 Respon cont 〙『 📲 』\n"
                                else: md+="║❏〘 Respon cont 〙『 📴 』\n"
                                if Bot_Run["ResponPc"] == True: md+="║❏〘 Respon PC 〙『 📲 』\n"
                                else: md+="║❏〘 Respon PC 〙『 📴 』\n"
                                if Bot_Run["MentionKick"] == True: md+="║❏〘 Respon kick 〙『 📲 』\n"
                                else: md+="║❏〘 Respon kick 〙『 📴 』\n"
                                if Bot_Run["unsendMessage"] == True: md+="║❏〘 unsend Msg 〙『 📲 』\n"
                                else: md+="║❏〘 unsend Msg 〙『 📴 』\n"
                                if msg.to in welcome: md+="║❏〘 Welcome 〙『 📲 』\n"
                                else: md+="║❏〘 Welcome 〙『 📴 』\n"
                                md+="╠═══════════\n"
                                md+="║۝🄿🅁🄾🅃🄴🄲🅃۝\n"
                                md+="╠═══════════\n"
                                if Bot_Run["talkban"] == True: md+="║❏〘 Talkban 〙『 📲 』\n"
                                else: md+="║❏〘 Talkban 〙『 📴 』\n"
                                if Bot_Run["pname"] == True: md+="║❏〘 Lockname 〙『 📲 』\n"
                                else: md+="║❏〘 Lockname 〙『 📴 』\n"
                                if msg.to in protectname: md+="║❏〘 Proname 『 📲 』\n"
                                else: md+="║❏〘 Proname 〙『 📴 』\n"
                                if msg.to in protectqr: md+="║❏〘 Proqr 〙『 📲 』\n"
                                else: md+="║❏〘 Proqr 〙『 📴 』\n"
                                if msg.to in protectjoin: md+="║❏〘 Projoin 〙『 📲 』\n"
                                else: md+="║❏〘 Projoin 『 📴 』\n"
                                if msg.to in protectkick: md+="║❏〘 Promember 『 📲 』\n"
                                else: md+="║❏〘 Promember 〙『 📴 』\n"
                                if msg.to in protectinvite: md+="║❏〘 Proinvite 『 📲 』\n"
                                else: md+="║❏〘 Proinvite 〙『 📴 』\n"
                                if msg.to in protectcancel: md+="║❏〘 Protcancel 〙『 📲 』\n"
                                else: md+="║❏〘 Protcancel 〙『 📴 』\n╚═══════════\n"
                                kang1.sendMessage(msg.to, md+"╔═══════════\n" + "║〘 日付 〙: ["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "╠═══════════\n" + "║〘 時間 〙[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "╚═══════════")

                        elif cmd == "creator" or cmd == 'owner':
                            if msg._from in Master:
                                kang1.sendMessage(msg.to,"╔═══════════\n║Creator \n║〘 ۝🄵🄸🄽 🄱🄾🅃۝ 〙\n╠═══════════\n║http://line.me/ti/p/~kangnur04\n╚═══════════") 
                                ma = ""
                                for i in Creator:
                                    ma = kang1.getContact(i)
                                    kang1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "siri:グル作成者" or msg.text.lower() == 'siri:グル作成者':
                            if msg._from in Master:
                                kang1.sendMessage(msg.to,"グルを作ったのはこの人だよ☆") 
                                ma = ""
                                for i in Creator:
                                    ma = kang1.getContact(i)
                                    kang1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               arr = []
                               today = datetime.today()
                               future = datetime(2018,3,1)
                               hari = (str(future - today))
                               comma = hari.find(",")
                               hari = hari[:comma]
                               blockedlist = kang.getBlockedContactIds()
                               creator = kang.getContact(kangMID)
                               teman = kang.getAllContactIds()
                               gid = kang.getGroupIdsJoined()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               eltime = time.time() - mulai
                               bot = runtime(eltime)
                               ret_ = "╔═════════════"
                               ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Creator 』:{}".format(creator.displayName)
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║ 日付 : {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                               ret_ += "\n║ グループ : {}".format(str(len(gid)))
                               ret_ += "\n║ 友人 』: {}".format(str(len(teman)))
                               ret_ += "\n║ ブロック : {}".format(str(len(blockedlist)))
                               ret_ += "\n║ 失効した 』: {}".format(hari)
                               ret_ += "\n║ バージョン : 🄵🄸🄽 🄱🄾🅃 V.4"
                               ret_ += "\n║ 時間 : {}".format(datetime.strftime(timeNow,'%Y-%m-%d'))
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Runtime 』"
                               ret_ += "\n║ {}".format(bot)
                               ret_ += "\n╚═════════════"
                               kang1.sendMessage(msg.to,str(ret_))
                               #kang1.sendMessage(msg.to, None, contentMetadata={'mid': kangMID}, contentType=13)

                        elif cmd == "me" or msg.text.lower() == 'me':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang1.sendMessage(msg.to,None,contentMetadata = {'mid': kangMID}, contentType=13)

                        elif ("fancytext " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               text = msg.text.replace("fancytext ", "")
                               kang1.kedapkedip(msg.to, text)

                        elif ("kedip " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                text = msg.text.replace("kedip ", "")
                                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                                kang1.sendMessage(msg.to, t1 + text + t2)
                               #kang1.kedapkedip(msg.to, text)

                        elif cmd == "oi" or cmd == 'all':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                group = kang.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                cb = ""
                                cb2 = ""
                                strt = int(0)
                                akh = int(0)
                                for md in nama:
                                    akh = akh + int(6)
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + int(7)
                                    akh = akh + 1
                                    cb2 += "@nrik \n"
                                cb = (cb[:int(len(cb)-1)])
                                kang.sendMessage(msg.to,cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)

                        elif msg.text.lower() == "mid":
                               kang1.sendMessage(msg.to, msg._from)

                        elif text.lower() == "welcome":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   ginfo = kang1.getGroup(msg.to)
                                   gcreator = ginfo.creator.displayName
                               except:
                                   gcreator = "Gcreator puskun boss"
                               else:
                                   ret_ = "Di Group"
                                   ret_ += "\n{}".format(ginfo.name)
                                   ret_ +="\n{}".format(gcreator)
                                   kang1.sendMessage(msg.to,str(ret_))
                                   kang1.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)

                        elif text.lower() == "wc":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   ginfo = kang.getGroup(msg.to)
                                   gcreator = ginfo.creator.displayName
                               except:
                                   gcreator = "Gcreator puskun boss"
                               else:
                                   ret_ = "Di Group"
                                   ret_ += "\n{}".format(ginfo.name)
                                   ret_ +="\n{}".format(gcreator)
                                   kang.sendMessage(msg.to,str(ret_))
                                   kang.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)

                        elif ("Mid " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang1.getContact(key1)
                               kang1.sendMessage(msg.to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " +key1)
                               kang1.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("info " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang1.getContact(key1)
                               kang1.sendMessage(msg.to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " +key1+"\n『 User Bio 』 : "+str(mi.statusMessage))
                               kang1.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(kang1.getContact(key1)):
                                   kang1.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   kang1.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif ("token mac" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit4': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang1.sendMessage(msg.to, '{}'.format(qr))
                        elif ("token win10" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit3': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang1.sendMessage(msg.to, '{}'.format(qr))
                        elif ("token ios" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit2': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang1.sendMessage(msg.to, '{}'.format(qr))
                        elif ("token done" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit5': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang1.sendMessage(msg.to,"Give thanks for ۝🄵🄸🄽 🄱🄾🅃۝\nCheck ur authToken at inbox")
                            	kang1.sendMessage(msg._from, '{}'.format(qr))

                        elif msg.text.lower().startswith("loginwin"):
                          if msg.from_ in Master:
                            separate = msg.text.split(" ")
                            jmlh = int(separate[1])
                            for x in range(jmlh):
                                Headers.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                transport.setCustomHeaders(Headers)
                                protocol = TCompactProtocol.TCompactProtocol(transport)
                                client = FinbotService.Client(protocol)
                                qr = client.getAuthQrcode(keepLoggedIn=1, systemName=Logged1)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    kang1.sendMessage(msg.to,"Starting white true")
                    kang1.sendMessage(msg.to,"Except")
                    kang1.sendMessage(msg.to,str(link))
                    Headers.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers).text)
                    Headers.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = FinbotService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                else:
                    kang1.sendMessage(msg.to, "Finbot has been made with header 1 as DesktopWin")
                    kang1.sendMessage(msg.to,str(res.authToken))
					
            elif msg.text.lower().startswith("loginmac"):
              if msg.from_ in Master:
                separate = msg.text.split(" ")
                jmlh = int(separate[1])
                for x in range(jmlh):
                    Headers2.update({'x-lpqs' : '/api/v4/TalkService.do'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = FinbotService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName=Logged2)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    kang1.sendMessage(msg.to,"Starting... ")
                    kang1.sendMessage(msg.to,"Except")
                    kang1.sendMessage(msg.to,str(link))
                    Headers2.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers2).text)
                    Headers2.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = FinbotService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                else:
                    kang1.sendMessage(msg.to, "Finbot has been made with header 2 as Desktopmac")
                    kang1.sendMessage(msg.to,str(res.authToken))
                
                        elif cmd == "cek. " or cmd == 'crash':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, None, contentMetadata={'mid': "ud108eea8074da128b9cd064a8a28e27a,'"}, contentType=13)

                        elif cmd == "mybot" or cmd == 'contact bot':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Run["assist"] == {}:
                                    kang1.sendMessage(msg.to,"バックBOT")
                              else:
                                    ma = ""
                                    for i in Bot_Run["assist"]:
                                        ma = kang1.getContact(i)
                                        kang1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "allbot" or cmd == 'listbot':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                ma = ""
                                a = 0
                                for m_id in Bot_Run["assist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang1.getContact(m_id).displayName + "\n"
                                kang1.sendMessage(msg.to,"ই۝🄵🄸🄽 🄱🄾🅃۝ईई\n\n"+ma+"\nTotal👉『 %s 』AllBots" %(str(len(Bot_Run["assist"]))))

                        elif cmd == "cstm":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                ma = ""
                                mb = ""
                                a = 0
                                b = 0
                                for m_id in Master:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang1.getContact(m_id).displayName + "\n"
                                for m_id in Bot_Run["assist"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang1.getContact(m_id).displayName + "\n"
                                kang1.sendMessage(msg.to,"ই۝🄵🄸🄽 🄱🄾🅃۝ईई\n\nMaster:\n"+ma+"\nBots:\n"+mb+"\nTotal『 %s 』" %(str(len(Master)+len(Bot_Run["assist"]))))

                        elif cmd == "cstmpro":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang1.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +kang1.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +kang1.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +kang1.getGroup(group).name + "\n"
                                gid = protectname
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +kang1.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +kang1.getGroup(group).name + "\n"
                                kang1.sendMessage(msg.to,"ই۝🄵🄸🄽 🄱🄾🅃۝ईई\n▪Cust Protection\n\n▪URL Pro :\n"+ma+"\n▪KICKER Pro :\n"+mb+"\n▪JOINER Pro  :\n"+md+"\n▪CANCEL Pro :\n"+mc+"\n▪Pro Gname :\n"+me+"\n▪Pro Invite :\n"+mf+"\n▪Total「%s」Mode protection is being Maintained" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectname)+len(protectinvite))))

                        elif text.lower() == "delchat":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   kang.removeAllMessages(op.param2)
                                   #kang.sendMessage(to, "『 Done 』")
                               except:
                                   pass

                        elif text.lower() == "rechat":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   fino1.removeAllMessages(op.param2)
                                   fino2.removeAllMessages(op.param2)
                                   fino3.removeAllMessages(op.param2)
                                   kang1.removeAllMessages(op.param2)
                                   kang1.sendMessage(msg.to,"『 Removed 』")
                               except:
                                   pass
 
                        elif text.lower() == "kicker delchat":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   G = kang1.getGroup(msg.to)
                                   ginfo = kang1.getGroup(msg.to)
                                   G.preventedJoinByTicket = False
                                   kang1.updateGroup(G)
                                   invsend = 0
                                   Ticket = kang1.reissueGroupTicket(msg.to)
                                   kang2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                   #sw2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                   G = kang1.getGroup(msg.to)
                                   G.preventedJoinByTicket = True
                                   kang1.updateGroup(G)
                                   kang2.removeAllMessages(op.param2)
                                   #sw2.removeAllMessages(op.param2)
                                   kang2.sendMessage(msg.to,"『 Log chat deleted 』")
                                   #sw2.sendMessage(msg.to,"『 Log chat deleted 』")
                                   kang2.leaveGroup(msg.to)
                                   #sw2.leaveGroup(msg.to)
                               except:
                                   pass
 
                        elif cmd.startswith("fbroadcast: "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               friends = kang.getAllContactIds()
                               for friend in friends:
                               	kang.sendMessage(friend, "[ Broadcast ]\n{}".format(str(text)))
                               	kang.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                        elif cmd.startswith("broadcast: "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               groups = kang.getGroupIdsJoined()
                               for group in groups:
                                   kang.sendMessage(group,"『 Broadcast 』\n{}".format(str(text)))
                                   kang.sendMessage(msg.to, "▪Berhasil broadcast ke {} group".format(str(len(groups))))

                        elif text.lower() == "mykey":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Mykey」\n▪「 " + str(Bot_Run["keyCommand"]) + " 」")
 
                        elif cmd.startswith("setkey "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang1.sendMessage(msg.to, "▪Gagal mengganti key")
                               else:
                                   Bot_Run["keyCommand"] = str(key).lower()
                                   kang1.sendMessage(msg.to, "「Setkey」\n▪「{}」".format(str(key).lower()))
                        elif text.lower() == "resetkey":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               Bot_Run["keyCommand"] = ""
                               kang1.sendMessage(msg.to, "「Setkey」\n▪Refresh")

                        elif cmd == "reboot":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "『 再起動... 🔄 』")
                               Bot_Run["restartPoint"] = msg.to
                               restartBot()

                        elif cmd == "restart":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang1.sendMessage(msg.to,"『 Restarting... 🔄 』")
                               eltime = time.time() - mulai
                               rest = "再起動👌\n" +waktu(eltime)
                               kang1.sendMessage(msg.to,rest)
                               Bot_Run["restartPoint"] = msg.to
                               restart_program()

                        elif cmd == "runtime" or cmd == 'deploy':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               eltime = time.time() - mulai
                               bot_ = "╔═════════════"
                               bot_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               bot_ += "\n╠═════════════"
                               bot_ += "\n║『 Deploy Time 』"
                               bot_ += "\n║{}".format(waktu(eltime)) 
                               bot_ += "\n╚═════════════"
                               kang1.sendMessage(msg.to,str(bot_))

                        elif cmd == "info group" or cmd == "ginfo":
                          if msg._from in Master:
                            try:
                                G = kang1.getGroup(msg.to)
                                ret_ = ""
                                try:
                                	gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║{}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║{}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║ {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                kang1.sendMessage(to, str(ret_))
                                kang1.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd == ".group" or cmd == 'lg':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = kang1.getGroupIdsJoined()
                               for i in gid:
                                   G = kang1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               kang1.sendMessage(msg.to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』)\n│▪Check Group member type⇣\n│[Ex] Member 1\n│\n│▪Check List Group type⇣\n│[Ex] Group 1\n╰──────────")
                        elif cmd == "f1g":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino1.getGroupIdsJoined()
                               for i in gid:
                                   G = fino1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               fino1.sendMessage(msg.to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』\n╰──────────")
                        elif cmd == "f2g":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino2.getGroupIdsJoined()
                               for i in gid:
                                   G = fino2.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               fino2.sendMessage(msg.to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』\n╰──────────")
                        elif cmd == "f3g":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino3.getGroupIdsJoined()
                               for i in gid:
                                   G = fino3.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               fino3.sendMessage(msg.to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』\n╰──────────")

                        elif cmd.startswith("f1group "):
                          if msg._from in Master:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = fino1.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino1.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(fino1.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║  {}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║  {}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║  {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║  {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                fino1.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("f2group "):
                          if msg._from in Master:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = fino2.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino2.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(fino2.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 ??🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║{}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║{}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║ {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                fino2.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("f3group "):
                          if msg._from in Master:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = fino3.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino3.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(fino3.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║{}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║{}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║ {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                fino3.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("f1member "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = fino1.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino1.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n║⇨ "+ str(no) + ". " + mem.displayName
                                fino1.sendMessage(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 Group 』 :  " + str(G.name) + " \n╠═════════════" + "\n║『 User Name Member 』" + "\n╠═════════════" + ret_ + "\n╠═════════════" + "\n║『 Total Member %i 』" % len(G.members) + "╚═════════════")
                            except: 
                                pass

                        elif cmd.startswith("f2member "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = fino2.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino2.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n║⇨ "+ str(no) + ". " + mem.displayName
                                fino2.sendMessage(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 Group 』 :  " + str(G.name) + " \n╠═════════════" + "\n║『 User Name Member 』" + "\n╠═════════════" + ret_ + "\n╠═════════════" + "\n║『 Total Member %i 』" % len(G.members) + "╚═════════════")
                            except: 
                                pass

                        elif cmd.startswith("f3member "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = fino3.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = fino3.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n║⇨ "+ str(no) + ". " + mem.displayName
                                fino3.sendMessage(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 Group 』 :  " + str(G.name) + " \n╠═════════════" + "\n║『 User Name Member 』" + "\n╠═════════════" + ret_ + "\n╠═════════════" + "\n║『 Total Member %i 』" % len(G.members) + "╚═════════════")
                            except: 
                                pass

                        elif cmd.startswith("leaveall: "): #By gid
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            groups = fino1.getGroupIdsJoined()
                            groups = fino2.getGroupIdsJoined()
                            groups = fino3.getGroupIdsJoined()
                            groups = kang1.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = kang.getGroup(i)
                                ginfo = fino1.getGroup(i)
                                ginfo = fino2.getGroup(i)
                                ginfo = fino3.getGroup(i)
                                ginfo = kang1.getGroup(i)
                                if ginfo == group:
                                    fino1.sendMessage(i,"ᴍᴀᴀғ...!\nᴏᴡɴᴇʀ ᴋᴀᴍɪ ᴍᴇɴʏᴜʀᴜʜ ᴘᴜʟᴀɴɢ\n\nᴡᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ sᴇᴍᴜᴀɴʏᴀ... ")
                                    fino1.leaveGroup(i)
                                    fino2.leaveGroup(i)
                                    fino3.leaveGroup(i)
                                    kang1.leaveGroup(i)
                                    #fino5.leaveGroup(i)
                                    kang1.sendMessage(msg.to,"Out from group\n" +str(ginfo.name))

                        elif cmd.startswith("back: "): #by name
                          if msg._from in Master:
                            sep = msg.text.replace("back: ","")
                            groups = fino1.getGroupIdsJoined()
                            groups = fino2.getGroupIdsJoined()
                            groups = fino3.getGroupIdsJoined()
                            groups = kang1.getGroupIdsJoined()
                            for i in groups:
                                ginfo = fino1.getGroup(i).name
                                ginfo = fino2.getGroup(i).name
                                ginfo = fino3.getGroup(i).name
                                ginfo = kang1.getGroup(i).name
                                if ginfo == sep:
                                    fino1.sendMessage(i,"Maaf...! Sahabat  " +ginfo+"\nᴏᴡɴᴇʀ ᴋᴀᴍɪ ᴍᴇɴʏᴜʀᴜʜ ᴘᴜʟᴀɴɢ\nᴡᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ sᴇᴍᴜᴀɴʏᴀ...")
                                    fino2.sendMessage(i,"Maaf...! Sahabat  " +ginfo+"\nᴏᴡɴᴇʀ ᴋᴀᴍɪ ᴍᴇɴʏᴜʀᴜʜ ᴘᴜʟᴀɴɢ\nᴡᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ sᴇᴍᴜᴀɴʏᴀ...")
                                    fino3.sendMessage(i,"Maaf...! Sahabat  " +ginfo+"\nᴏᴡɴᴇʀ ᴋᴀᴍɪ ᴍᴇɴʏᴜʀᴜʜ ᴘᴜʟᴀɴɢ\nᴡᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ sᴇᴍᴜᴀɴʏᴀ...")
                                    kang1.sendMessage(i,"Maaf...! Sahabat  " +ginfo+"\nᴏᴡɴᴇʀ ᴋᴀᴍɪ ᴍᴇɴʏᴜʀᴜʜ ᴘᴜʟᴀɴɢ\nᴡᴀssᴀʟᴀᴍᴜ'ᴀʟᴀɪᴋᴜᴍ sᴇᴍᴜᴀɴʏᴀ...")
                                    fino1.leaveGroup(i)
                                    fino2.leaveGroup(i)
                                    fino3.leaveGroup(i)
                                    kang1.leaveGroup(i)
                                    kang1.sendMessage(msg.to,"Beres out boss dari: "+ginfo)

                        elif cmd == "f1friend" or cmd == 'f1f':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino1.getAllContactIds()
                               for i in gid:
                                   G = fino1.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fino1.sendMessage(msg.to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "f2friend" or cmd == 'f2f':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino2.getAllContactIds()
                               for i in gid:
                                   G = fino2.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fino2.sendMessage(msg.to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "f3friend" or cmd == 'f3f':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = fino3.getAllContactIds()
                               for i in gid:
                                   G = fino3.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               fino3.sendMessage(msg.to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "f1url":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   x = fino1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      fino1.updateGroup(x)
                                   gurl = fino1.reissueGroupTicket(msg.to)
                                   fino1.sendMessage(msg.to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "f2url":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   x = fino2.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      fino2.updateGroup(x)
                                   gurl = fino2.reissueGroupTicket(msg.to)
                                   fino2.sendMessage(msg.to,"╔═════════════" + "\n║『 ই۝??🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "f3url":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   x = fino3.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      fino3.updateGroup(x)
                                   gurl = fino3.reissueGroupTicket(msg.to)
                                   fino3.sendMessage(msg.to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "glink":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   x = kang1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      kang1.updateGroup(x)
                                   gurl = kang1.reissueGroupTicket(msg.to)
                                   kang1.sendMessage(msg.to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║ http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "f1ourl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   fino1.updateGroup(X)
                                   fino1.sendMessage(msg.to,Bot_Run["ResponUrl"])

                        elif cmd == "f2ourl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino2.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   fino2.updateGroup(X)
                                   fino2.sendMessage(msg.to,Bot_Run["ResponUrl"])

                        elif cmd == "f3ourl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino3.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   fino3.updateGroup(X)
                                   fino3.sendMessage(msg.to, Bot_Run["ResponUrl"])

                        elif cmd == "ourl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = kang1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kang1.updateGroup(X)
                                   kang1.sendMessage(msg.to, Bot_Run["ResponUrl"])

                        elif cmd == "f1curl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   fino1.updateGroup(X)
                                   fino1.sendMessage(msg.to, Bot_Run["ResponCurl"])

                        elif cmd == "f2curl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino2.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   fino2.updateGroup(X)
                                   fino2.sendMessage(msg.to, Bot_Run["ResponCurl"])

                        elif cmd == "f3curl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = fino3.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   fino3.updateGroup(X)
                                   fino3.sendMessage(msg.to, Bot_Run["ResponCurl"])

                        elif cmd == "curl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = kang1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kang1.updateGroup(X)
                                   kang1.sendMessage(msg.to, Bot_Run["ResponCurl"])

                        elif cmd == "addimage":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if msg.toType == 2:
                                Bot_Run["Addimage"] = True
                                kang1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "allfoto" or cmd == 'cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["changePicture"] = True
                                kang1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "cfotogroup" or cmd == 'cfg':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if msg.toType == 2:
                                Bot_Run["groupPicture"] = True
                                kang1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "updatefoto" or cmd == 'myft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][kangMID] = True
                                kang1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "f1cfoto" or cmd == 'f1cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][Amid] = True
                                fino1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "f2cfoto" or cmd == 'f2cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][Bmid] = True
                                fino2.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "f3cfoto" or cmd == 'f3cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][Cmid] = True
                                fino3.sendMessage(msg.to,Bot_Run["ResponCcft"])
 
                        elif cmd == "f4cfoto" or cmd == 'f4cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][Dmid] = True
                                kang1.sendMessage(msg.to,Bot_Run["ResponCcft"])

                        elif cmd == "k1cfoto" or cmd == 'k1cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["foto"][Emid] = True
                                kang2.sendMessage(msg.to,Bot_Run["ResponCcft"])
                            else:
                                kang1.sendMessage(msg.to, "▪Kicker tidak disni boss")

                        elif cmd == "cvp" or cmd == 'cvideo':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["video"][kangMID] = True
                                kang1.sendMessage(msg.to,"Send your video.....")
                                
                        elif cmd.startswith("cname: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.displayName = string
                                kang.updateProfile(profile)
                                kang1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("f1name: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino1.getProfile()
                                profile.displayName = string
                                fino1.updateProfile(profile)
                                fino1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("f2name: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino2.getProfile()
                                profile.displayName = string
                                fino2.updateProfile(profile)
                                fino2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("f3name: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino3.getProfile()
                                profile.displayName = string
                                fino3.updateProfile(profile)
                                fino3.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("captename: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang1.getProfile()
                                profile.displayName = string
                                kang1.updateProfile(profile)
                                kang1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("kickername: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang2.getProfile()
                                profile.displayName = string
                                kang2.updateProfile(profile)
                                kang2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("kicker2name: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = sw2.getProfile()
                                profile.displayName = string
                                sw2.updateProfile(profile)
                                sw2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("allname: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang1.getProfile()
                                profile.displayName = string
                                kang1.updateProfile(profile)
                                kang1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                                profile = fino1.getProfile()
                                profile.displayName = string
                                fino1.updateProfile(profile)
                                fino1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                                profile = fino2.getProfile()
                                profile.displayName = string
                                fino2.updateProfile(profile)
                                fino2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                                profile = fino3.getProfile()
                                profile.displayName = string
                                fino3.updateProfile(profile)
                                fino3.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                                profile = kang1.getProfile()
                                profile.displayName = string
                                kang1.updateProfile(profile)
                                kang1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("cbio: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.statusMessage = string
                                kang.updateProfile(profile)
                                kang.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("allbio: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = fino1.getProfile()
                                profile.statusMessage = string
                                fino1.updateProfile(profile)
                                fino1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                            if len(string) <= 500:
                                profile = fino2.getProfile()
                                profile.statusMessage = string
                                fino2.updateProfile(profile)
                                fino2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                            if len(string) <= 500:
                                profile = fino3.getProfile()
                                profile.statusMessage = string
                                fino3.updateProfile(profile)
                                fino3.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")
                            if len(string) <= 500:
                                profile = kang1.getProfile()
                                profile.statusMessage = string
                                kang1.updateProfile(profile)
                                kang1.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd.startswith("k1bio: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang2.getProfile()
                                profile.statusMessage = string
                                kang2.updateProfile(profile)
                                kang2.sendMessage(msg.to,Bot_Run["ResponCname"] + string + "")

                        elif cmd == "mention" or cmd == 'sepi':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               group = kang1.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 100:
                                   mentionMembers(msg.to, nama)
                               if jml > 100 and jml < 200:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 200 and jml < 300:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 300 and jml < 400:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 400 and jml < 500:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, 399):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (400, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "joinall":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                fino1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kang2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #fino5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino3.updateGroup(G)
 
                        elif cmd == ".. ":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                ginfo = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fino1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kang1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kang2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino3.updateGroup(G)

                        elif cmd == "fin1" or cmd == 'f1 in':
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                fino1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino1.updateGroup(G)

                        elif cmd == "fin2" or cmd == 'f2 in':
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                fino2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino2.updateGroup(G)

                        elif cmd == "fin3" or cmd == 'f3 in':
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                fino3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino3.updateGroup(G)

                        elif cmd == "kicker join" or cmd == 'k1 in':
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                kang2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kang2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kang2.updateGroup(G)

                        elif cmd == "kicker2 join" or cmd == 'k2 in':
                            if msg._from in Master:
                                G = kang1.getGroup(msg.to)
                                ginfo = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang1.updateGroup(G)
                                invsend = 0
                                Ticket = kang1.reissueGroupTicket(msg.to)
                                sw2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.01)
                                G = sw2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw2.updateGroup(G)

                        elif cmd == "talk join" or cmd == 'talk in':
                            if msg._from in Master:
                                G = fino1.getGroup(msg.to)
                                ginfo = fino1.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                fino1.updateGroup(G)
                                invsend = 0
                                Ticket = fino1.reissueGroupTicket(msg.to)
                                kang1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kang1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kang1.updateGroup(G)

                        elif cmd == "talk" or cmd == '. ':
                            if msg._from in Master:
                                kang.inviteIntoGroup(msg.to,[Dmid])
                                kang1.acceptGroupInvitation(msg.to)
                            else:
                            	kang1.sendMessage(msg.to,Bot_Run["ResponAbsen"])

                        elif cmd == "hei" or cmd == 'inv all':
                            if msg._from in Master:
                                kang1.inviteIntoGroup(msg.to,[Amid,Bmid,Cmid,Emid])
                                #kang1.inviteIntoGroup(msg.to,[Bmid])
                                #kang1.inviteIntoGroup(msg.to,[Cmid])
                                fino1.acceptGroupInvitation(msg.to)
                                fino2.acceptGroupInvitation(msg.to)
                                fino3.acceptGroupInvitation(msg.to)
                                kang2.acceptGroupInvitation(msg.to)
 
                        elif cmd == "finbye" or cmd == '... ':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                kang1.sendMessage(msg.to, "さようなら...!"+str(G.name))
                                fino1.leaveGroup(msg.to)
                                fino2.leaveGroup(msg.to)
                                fino3.leaveGroup(msg.to)
                                #fino4.leaveGroup(msg.to)
                                #fino5.leaveGroup(msg.to)
                                #kang2.leaveGroup(msg.to)

                        elif cmd == "fin1bye" or cmd == 'out all':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                kang1.sendMessage(msg.to, "さようなら....!"+str(G.name))
                                fino1.leaveGroup(msg.to)
                                fino2.leaveGroup(msg.to)
                                fino3.leaveGroup(msg.to)
                                #fino4.leaveGroup(msg.to)
                                #fino5.leaveGroup(msg.to)

                        elif cmd == "byeme" or cmd == 'byebye':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                kang1.sendMessage(msg.to, "さようなら...!"+str(G.name))
                                kang1.leaveGroup(msg.to)

                        elif cmd == "kicker bye" or cmd == 'k1bye':
                            if msg._from in Master:
                                G = kang2.getGroup(msg.to)
                                kang2.leaveGroup(msg.to)

                        elif cmd == "kicker2 bye" or cmd == 'k2bye':
                            if msg._from in Master:
                                G = sw2.getGroup(msg.to)
                                sw2.leaveGroup(msg.to)

                        elif cmd == "crot" or cmd == 'kick on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	Bot_Run["autokick"] = True
                            	Bot_Run["BLinviter"] = True
                            	fino1.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                            	fino2.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                            	fino3.sendMessage(msg.to,Bot_Run["ResponAbsen"])

                        elif cmd == "crit" or cmd == 'kick off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	Bot_Run["autokick"] = False
                            	Bot_Run["BLinviter"] = False
                            	kang1.sendMessage(msg.to,Bot_Run["ResponAbsen"])

                        elif cmd == "ꦾꦃ" or cmd == 'xx':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                fino1.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                fino2.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                fino3.sendMessage(msg.to,Bot_Run["ResponAbsen"])

                        elif cmd == "absen" or cmd == 'xxx':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                fino1.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                fino2.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                fino3.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                kang.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                kang1.sendMessage(msg.to,Bot_Run["ResponAbsen"])
                                kang2.sendMessage(msg.to,Bot_Run["ResponAbsen"])

                        elif cmd == "respon" or cmd == 'responsename':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                fino1.sendMessage(msg.to,responsename1)
                                fino2.sendMessage(msg.to,responsename2)
                                fino3.sendMessage(msg.to,responsename3)

                        elif cmd == "spres" or cmd == 'sprespon':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                get_profile_time_start = time.time()
                                get_profile = kang1.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = kang1.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = kang1.getContact(kangMID)
                                get_contact_time = time.time() - get_contact_time_start
                                kang1.sendMessage(msg.to, "╔═════════════\n║【Speed Respon】\n╠═══════════════\║▪➣Get Profile\n║   %.10f\n╠═══════════════\n║▪➣Get Contact\n║   %.10f\n╠═══════════════\n║▪➣Get Group\n║   %.10f\n╚═══════════════" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               start = time.time()
                               kang1.sendMessage(msg.to,"🔄... ")
                               elapsed_time = time.time() - start
                               fino1.sendMessage(msg.to, "{} /scnds".format(str(elapsed_time)))
                               fino2.sendMessage(msg.to, "{} /scnds".format(str(elapsed_time)))
                               fino3.sendMessage(msg.to, "{} /scnds".format(str(elapsed_time)))

                        elif cmd == "netbot" or cmd == 'net':
                            if msg._from in Master:
                                start = time.time()
                                kang2.sendMessage(to,"u4d2f1c2fbee16358f12c749f406cfbf0", '.')
                                elapsed_time = time.time() - start
                                fino1.sendMessage(msg.to, "%s" % (elapsed_time))
                                
                                start2 = time.time()
                                kang2.sendMessage(to,"u4d2f1c2fbee16358f12c749f406cfbf0", '.')
                                elapsed_time = time.time() - start2
                                fino2.sendMessage(msg.to, "%s" % (elapsed_time))
                                
                                start3 = time.time()
                                kang2.sendMessage(to,"u4d2f1c2fbee16358f12c749f406cfbf0", '.')
                                elapsed_time = time.time() - start3
                                fino3.sendMessage(msg.to, "%s" % (elapsed_time))
                                
                                start4 = time.time()
                                kang2.sendMessage(to,"u4d2f1c2fbee16358f12c749f406cfbf0", '.')
                                elapsed_time = time.time() - start4
                                kang1.sendMessage(msg.to, "%s" % (elapsed_time))

                        elif cmd == "lurking on" or cmd == "setlastpoint":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Bot_Run['readPoint'][msg.to] = msg_id
                                 Bot_Run['readMember'][msg.to] = {}
                                 kang1.sendMessage(msg.to, "Set the lastseens' point(｀・ω・´)\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurking off" or cmd == "resetseen":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Bot_Run['readPoint'][msg.to]
                                 del Bot_Run['readMember'][msg.to]
                                 kang1.sendMessage(msg.to, "Set the lastseens dissable\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers" or cmd == "viewlastseen":
                          if msg._from in Master:
                            if msg.to in Bot_Run['readPoint']:
                                if Bot_Run['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Bot_Run['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Seens ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(kang.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        kang1.sendMessage(msg.to,textx+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]",contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')},contentType = 0)
                                    except:
                                        pass
                                    try:
                                        del Bot_Run['readPoint'][msg.to]
                                        del Bot_Run['readMember'][msg.to]
                                    except:
                                        pass
                                    Bot_Run['readPoint'][msg.to] = msg.id
                                    Bot_Run['readMember'][msg.to] = {}
                                else:
                                    kang1.sendMessage(msg.to, "Seens empty...")
                            else:
                                    kang1.sendMessage(msg.to, "Please type lurking on/setlastpoint before.. ")

                        elif cmd == "sider on" or cmd == 'cctv on':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  kang1.sendMessage(msg.to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status in maintained』\n╚════════════")
                                  del Bot_Run['setTime'][msg.to]
                                  del Bot_Run['setSider'][msg.to]
                                  del Bot_Run['setWicked'][msg.to]
                              except:
                                  pass
                              Bot_Run['setTime'][msg.to] = msg.id
                              Bot_Run['setSider'][msg.to] = ""
                              Bot_Run['setWicked'][msg.to]=True

                        elif cmd == "sider off" or cmd == 'cctv off':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              if msg.to in Bot_Run['setTime']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  Bot_Run['setWicked'][msg.to]=False
                                  kang1.sendMessage(msg.to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status dissable』\n╚════════════")
                              else:
                                  kang1.sendMessage(msg.to, "Not sett")
#==========================[/TEXTTOSPEEC/FIN]===========================
                        elif msg.text.lower().startswith("say-"):
                          if msg._from in Master:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("say-" + lang + " ","")
                             if lang not in Bot_Run["wlist_textToSpeech"]:
                             	return kang1.sendMessage(to, "Language not found")
                             tts = gTTS(text=say, lang=lang)
                             tts.save("tts.mp3")
                             kang1.sendAudio(to,"tts.mp3")
#==========================[TRANSLATOR/FIN]===========================
                        elif msg.text.lower().startswith("tr-"):
                          if msg._from in Master:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("tr-" + lang + " ","")
                             if lang not in Bot_Run["wlist_translate"]:
                             	return kang1.sendMessage(to, "Language not found")
                             translator = Translator()
                             hasil = translator.translate(say, dest=lang)
                             A = hasil.text
                             kang1.sendMessage(to, str(A))

                        elif ("Gn " in msg.text):
                          if msg._from in Master:
                              X = kang1.getGroup(msg.to)
                              X.name = msg.text.replace("Gn ","")
                              kang1.updateGroup(X)

                        elif 'lc ' in text.lower():
                          if msg._from in Master:
                              try:
                                  typel = [1001,1002,1003,1004,1005,1006]
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  a = kang1.getContact(u).mid
                                  s = kang1.getContact(u).displayName
                                  hasil = kang1.getHomeProfile(mid=a)
                                  st = hasil['result']["homeId"]
                                  for i in range(len(st)):
                                      test = st[i]
                                      result = test['posts']['postInfo']['postId']
                                      kang1.like(str(sender), str(result), likeType=random.choice(typel))
                                      kang1.comment(str(sender), str(result), 'Manual like by: 🄵🄸🄽 🄱🄾🅃')
                                  kang1.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                              except Exception as e:
                                  kang1.sendMessage(receiver, str(e))

                        elif 'gc ' in text.lower():
                          if msg._from in Master:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cname = kang1.getContact(u).displayName
                                  cmid = kang1.getContact(u).mid
                                  cstatus = kang1.getContact(u).statusMessage
                                  cpic = kang1.getContact(u).picturePath
                                  #print(str(a))
                                  kang1.sendMessage(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                  kang1.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                  if "videoProfile='{" in str(kang1.getContact(u)):
                                      kang1.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                  else:
                                      kang1.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                              except Exception as e:
                                  kang1.sendMessage(receiver, str(e))

                        elif cmd.startswith("spamtag "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(Bot_Run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                kang1.sendMessage(msg.to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                kang1.sendMessage(msg.to,str(e))
                                    else:
                                        kang1.sendMessage(msg.to,"Total limited 1000")

                        elif cmd.startswith("hii "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(Bot_Run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                kang.sendMessage(msg.to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                kang.sendMessage(msg.to,str(e))
                                    else:
                                        kang.sendMessage(msg.to,"Total Limited 1000")

                        elif cmd == "spamcall" or cmd == 'naik':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                             if msg.toType == 2:
                                group = kang1.getGroup(msg.to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Bot_Run["limitCall"])
                                kang1.sendMessage(msg.to, "{} Call Reissued".format(str(Bot_Run["limitCall"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        kang1.acquireGroupCallRoute(msg.to)
                                        kang1.inviteIntoGroupCall(msg.to, contactIds=members)
                                     except Exception as e:
                                        kang1.sendMessage(msg.to,str(e))
                                else:
                                    kang1.sendMessage(msg.to,"Limited list")

                        elif 'get-idline: ' in msg.text:
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              msgs = msg.text.replace('.get-idline: ','')
                              conn = kang.findContactsByUserid(msgs)
                              if True:
                                  kang.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  kang.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif cmd.startswith("idline "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = kang1.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                kang1.sendContact(to, anu)
                            except Exception as e:
                                kang1.sendMessage(msg.to, str(e))

                        elif cmd.startswith("saveimg "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                Bot_Run["Addimage"]["status"] = True
                                Bot_Run["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                kang1.sendMessage(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("rmimg "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                kang1.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                kang1.sendMessage(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimg":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             kang1.sendMessage(to, ret_)

                        elif cmd.startswith("addvideo "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                Bot_Run["Addvideo"]["status"] = True
                                Bot_Run["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Silahkan kirim videonya...") 
                            else:
                                kang1.sendMessage(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                kang1.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                kang1.sendMessage(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             kang1.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")

                        elif cmd.startswith("addmp3 "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                Bot_Run["Addaudio"]["status"] = True
                                Bot_Run["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                kang1.sendMessage(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                kang1.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                kang1.sendMessage(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listmp3":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             kang1.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")                                   
                        elif cmd.startswith("addsticker "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                Bot_Run["Addsticker"]["status"] = True
                                Bot_Run["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                kang1.sendMessage(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang1.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                kang1.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             kang1.sendMessage(to, ret_)

                        elif 'Welcome ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Welcome Msg Enable\nDi Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Welcome Msg Disable\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Proqr ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect qr sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protect qr Enable\nDi Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Protect qr Disable\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect qr sudah tidak aktif"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Proname ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Proname ','')
                              if spl == 'on':
                                  if msg.to in protectname:
                                       msgs = "Protect nama group sudah aktif"
                                  else:
                                       protectname.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protecting group name\nIn Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectname:
                                         protectname.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Protect group name\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect nama grup sudah tidak aktif"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Promem ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Promem ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect member sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protect member Enable\nDi Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Protect member Disable\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect member sudah tidak aktif"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Projoin ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join turn on"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protect join Enable\nDi Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Protect join Disable\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join turn off"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Proinv ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Proinv ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = ""
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protect" +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Invite pro" +str(ginfo.name)
                                    else:
                                         msgs = "Protecting"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = ""
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protect" +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Cancel pro" +str(ginfo.name)
                                    else:
                                         msgs = "Protecting"
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectname:
                                       msgs = ""
                                  else:
                                       protectname.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = kang.getGroup(msg.to)
                                      msgs = "All protect on\nAt Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = kang.getGroup(msg.to)
                                      msgs = "All protect on\nAt Group : " +str(ginfo.name)
                                  kang1.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectname:
                                         protectname.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "All protection off\nAt Group : " +str(ginfo.name)
                                    else:
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "All protect off\nAt Group : " +str(ginfo.name)
                                    kang1.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif ("Mek " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = kang1.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang1.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang1.reissueGroupTicket(msg.to)
                                           kang2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           kang2.kickoutFromGroup(msg.to, [target])
                                           kang2.leaveGroup(msg.to)
                                           X = kang1.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           kang1.updateGroup(X)
                                       except:
                                           pass

                        elif ("hai " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = kang1.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang1.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang1.reissueGroupTicket(msg.to)
                                           sw2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw2.kickoutFromGroup(msg.to, [target])
                                           sw2.leaveGroup(msg.to)
                                           X = kang1.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           kang1.updateGroup(X)
                                       except:
                                           pass

                        elif text.lower() == 'mal@sirichan':
                            gs = kang.getGroup(msg.to)
                            gs = fino1.getGroup(msg.to)
                            gs = fino2.getGroup(msg.to)
                            gs = fino3.getGroup(msg.to)
                            gs = kang1.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriMalvado,sirilist)
                                    p.close()
                                    p.terminate()
                                    p.join()
                                except:
                                    p.close()
                                    return

                        elif ("Dam " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           fino1.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Dim " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           fino2.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Dum " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           fino3.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif cmd == "warning on" or cmd == 'kick on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autokick"] = True
                                kang1.sendMessage(msg.to,"Ucapan larangan aktif")

                        elif cmd == "warning off" or cmd == 'kick off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autokick"] = False
                                kang1.sendMessage(msg.to,"Kalimat larangan dinonaktifkan")

                        elif cmd == "contact on" or cmd == 'c on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["contact"] = True
                                Bot_Run["checkPost"] = False
                                kang1.sendMessage(msg.to,"Contact detection enable")

                        elif cmd == "contact off" or cmd == 'c off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["contact"] = False
                                kang1.sendMessage(msg.to,"Contact detection dissable")

                        elif cmd == "checkpost on" or cmd == 'post on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["checkPost"] = True
                                Bot_Run["contact"] = False
                                kang1.sendMessage(msg.to,"Contact post detection enable")

                        elif cmd == "checkpost off" or cmd == 'post off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["checkPost"] = False
                                kang1.sendMessage(msg.to,"Contact post detection dissable")

                        elif cmd == "respon on" or cmd == 'rsp on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["detectMention"] = True
                                Bot_Run["detectMention1"] = False
                                kang1.sendMessage(msg.to,"Auto respon enable")

                        elif cmd == "respon off" or cmd == 'rsp off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["detectMention"] = False
                                kang1.sendMessage(msg.to,"Auto respon dissable")

                        elif cmd == "respon1 on" or cmd == 'rsp1 on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["detectMention1"] = True
                                Bot_Run["detectMention"] = False
                                kang1.sendMessage(msg.to,"Auto respon1 Enable")

                        elif cmd == "respon1 off" or cmd == 'rsp1 off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["detectMention1"] = False
                                kang1.sendMessage(msg.to,"Auto respon1 Disable")

                        elif cmd == "autojoin on" or cmd == 'join on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoJoin"] = True
                                kang1.sendMessage(msg.to,"Autojoin enable")

                        elif cmd == "autojoin off" or cmd == 'join off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoJoin"] = False
                                kang1.sendMessage(msg.to,"Autojoin dissable")

                        elif cmd == "autoleave on" or cmd == 'leave on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoLeave"] = True
                                kang1.sendMessage(msg.to,"Autoleave enable")

                        elif cmd == "autoleave off" or cmd == 'leave off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoLeave"] = False
                                kang1.sendMessage(msg.to,"Autoleave dissable")

                        elif cmd == "autoadd on" or cmd == 'add on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoAdd"] = True
                                kang1.sendMessage(msg.to,"Auto add enable")

                        elif cmd == "autoadd off" or cmd == 'add off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoAdd"] = False
                                kang1.sendMessage(msg.to,"Auto add dissable")

                        elif cmd == "jointicket on" or cmd == 'ticket on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoJoinTicket"] = True
                                kang1.sendMessage(msg.to,"Join ticket enable")

                        elif cmd == "jointicket off" or cmd == 'ticket off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoJoinTicket"] = False
                                kang1.sendMessage(msg.to,"jointicket dissable")

                        elif cmd == "invite on" or cmd == 'inv mem':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["winvite"] = True
                                kang1.sendMessage(msg.to,"Send contact")

                        elif cmd == "f1invite" or cmd == 'f1inv':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["invite1"] = True
                                fino1.sendMessage(msg.to,"Send contact")

                        elif cmd == "f2invite" or cmd == 'f2inv':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["invite2"] = True
                                fino2.sendMessage(msg.to,"Send contact")

                        elif cmd == "f3invite" or cmd == 'f3inv':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["invite3"] = True
                                fino3.sendMessage(msg.to,"Send contact")

                        elif cmd == "read on" or cmd == 'rd on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["AutoRead"] = True
                                Bot_Run["scanner"] = False
                                kang1.sendMessage(msg.to,"Message checked")

                        elif cmd == "read off" or cmd == 'rd off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["AutoRead"] = False
                                kang1.sendMessage(msg.to,"Auto read dissable")

                        elif cmd == "nyusup on" or cmd == 'nsp on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["nyusup"] = True
                                kang1.sendMessage(msg.to,"on")

                        elif cmd == "nyusup off" or cmd == 'nsp off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["nyusup"] = False
                                kang1.sendMessage(msg.to,"off")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if Bot_Run["selfbot"] == True:
                            if msg._from in Master:
                                Bot_Run["stickerOn"] = True
                                sendMentionV4(msg.to, sender, "「 Auto check Sticker 」\n", " [ 🔓 ]")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if Bot_Run["selfbot"] == True:
                            if msg._from in Master:
                                Bot_Run["stickerOn"] = False
                                kang1.sendMessage(msg.to,"「 Auto Check Sticker 」\n[ 🔒 ]")

                        elif cmd == "lock gname" or cmd == 'lgn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run['pname'][msg.to] = True
                                Bot_Run['pro_name'][msg.to] = kang.getGroup(msg.to).name
                                kang1.sendMessage(msg.to,"Group name protected")

                        elif cmd == "unlock gname" or cmd == 'ugn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del Bot_Run['pname'][msg.to]
                                kang1.sendMessage(msg.to,"Unlock pro group name")

                        elif cmd == "tagkick on" or cmd == 'notag on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["Mentionkick"] = True
                                kang1.sendMessage(msg.to,"Respon tagkick enable")

                        elif cmd == "tagkick off" or cmd == 'notag off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["MentionKick"] = False
                                kang1.sendMessage(msg.to,"Respon tagkick dissable")

                        elif cmd == "talkban add:on" or cmd == 'talkban add on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["Talkwblacklist"] = True
                                Bot_Run["Talkdblacklist"] = False
                                kang1.sendMessage(msg.to,"Send contact...")

                        elif cmd == "talkban dell:on" or cmd == 'talkban dell on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["Talkdblacklist"] = True
                                Bot_Run["Talkwblacklist"] = False
                                kang1.sendMessage(msg.to,"Send contact...")

                        elif cmd == "ban:on" or cmd == 'ban on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["wblacklist"] = True
                                Bot_Run["dblacklist"] = False
                                kang1.sendMessage(msg.to,"Send contact...")

                        elif cmd == "unban:on" or cmd == 'unban on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["dblacklist"] = True
                                Bot_Run["wblacklist"] = False
                                kang1.sendMessage(msg.to,"Send contact...")

                        elif cmd == "assist:on" or cmd == 'assist on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["assist"] = True
                                kang1.sendMessage(msg.to,"Assist enable")

                        elif cmd == "assist:off" or cmd == 'assist off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["assist"] = False
                                kang1.sendMessage(msg.to,"Assist dissable")

                        elif cmd == "block:on" or cmd == 'block on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoBlock"] = True
                                kang1.sendMessage(msg.to,"Block enable")

                        elif cmd == "block:off" or cmd == 'block off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["autoBlock"] = False
                                kang1.sendMessage(msg.to,"Block dissable")


                        elif cmd == "siri:add.backup:on" or cmd == 'backup:on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["addbackupmem"] = True
                                fino1.sendMessage(msg.to,"連絡先を送る")

                        elif cmd == "siri:delete.backup:on" or cmd == 'delete.backup:on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["dbackupmem"] = True
                                fino1.sendMessage(msg.to,"連絡先を送る")

                        elif cmd == "msg:on" or cmd == 'unsend on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["unsendMessage"] = True
                                Bot_Run["scanner"] = True
                                Bot_Run["AutoRead"] = False
                                Bot_Run['scanPoint'][msg.to] = msg_id
                                Bot_Run['scanROM'][msg.to] = {}
                                kang1.sendMessage(msg.to,"Read enable")

                        elif cmd == "msg:off" or cmd == 'unsend off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["unsendMessage"] = False
                                Bot_Run["scanner"] = False
                                kang1.sendMessage(msg.to,"Read dissable")

                        elif cmd == "rpc on" or cmd == 'cpc on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["ResponPc"] = True
                                Bot_Run["unsendMessage"] = False
                                Bot_Run["scanner"] = False
                                Bot_Run["AutoRead"] = False
                                kang1.sendMessage(msg.to,"ResponPC ON")

                        elif cmd == "rpc off" or cmd == 'cpc off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["ResponPc"] = False
                                kang1.sendMessage(msg.to,"ResponPC OFF")

                        elif cmd == "refresh" or cmd == 'fresh':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                Bot_Run["unsendMessage"] = False
                                Bot_Run["scanner"] = False
                                Bot_Run["AutoRead"] = False
                                Bot_Run["autoJoinTicket"] = False
                                Bot_Run["detectMention"] = False
                                Bot_Run["detectMention1"] = False
                                Bot_Run["MentionKick"] = False
                                Bot_Run["nyusup"] = False
                                Bot_Run["contact"] = False
                                kang1.sendMessage(msg.to,"Refresh done")

                        elif cmd == "dbn" or cmd == 'clearban':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              Bot_Run["blacklist"] = {}
                              ragets = kang1.getContacts(Bot_Run["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              kang1.sendMessage(msg.to,"Removed" +mc)

                        elif cmd == "rm backup" or cmd == 'remove backup':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              Bot_Create["backupmem"] = {}
                              ragets = kang1.getContacts(Bot_Create["backupmem"])
                              mc = "「%i」Backup User" % len(ragets)
                              kang1.sendMessage(msg.to,"Remove All" +mc)

                        elif cmd.startswith("autorestart: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Bot_Run["timeRestart"] = num
                                kang1.sendMessage(msg.to,"🄵🄸🄽 🄱🄾🅃 \nAutorestart in:『" +strnum+" Seconds』Remaining time... ")

                        elif cmd.startswith("limiter: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Bot_Run["limiter"]["members"] = num
                                kang1.sendMessage(msg.to,"Limit member switch to " +strnum)

                        elif cmd.startswith("spamtag: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Bot_Run["limitTag"] = num
                                kang1.sendMessage(msg.to,"Total Spamtag switch to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Bot_Run["limitCall"] = num
                                kang1.sendMessage(msg.to,"Total Spamcall switch to " +strnum)

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Something went wrong!")
                              else:
                                  Bot_Run["message"] = spl
                                  kang1.sendMessage(msg.to, "「PrivMsg」\nPriv Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["welcome"] = spl
                                  kang1.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set cft: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set cft: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["Responcft"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set ccft: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set ccft: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponCcft"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set cname: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set cname: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponCname"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set absen: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set absen: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponAbsen"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set wbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set wbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponWBL"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set dbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set dbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponDBL"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set wtbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set wtbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponWTBL"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set dtbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set dtbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["ResponDTBL"] = spl
                                  kang1.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["Respontag"] = spl
                                  kang1.sendMessage(msg.to, "「Respon msg」\nRespon Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["message1"] = spl
                                  kang1.sendMessage(msg.to, "「Spam Msg」\nSpam Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  kang1.sendMessage(msg.to, "Replace failed")
                              else:
                                  Bot_Run["mention"] = spl
                                  kang1.sendMessage(msg.to, "「Sider Msg」\nSider Msg switch to:\n\n「{}」".format(str(spl)))

                        elif msg.text.lower() == "cek limit":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Limit」\nMember limiter:「 " + str(Bot_Run["limiter"]["members"]) + " 」" +"\n\nSpamtag limiter:「 " + str(Bot_Run["limitTag"]) + " 」" + "\n\nSpamcall limiter:「 " + str(Bot_Run["limitCall"]) + " 」" )

                        elif msg.text.lower() == "cek pesan":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg:\n\n「 " + str(Bot_Run["message"]) + " 」")

                        elif msg.text.lower() == "cek welcome":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg:\n\n「 " + str(Bot_Run["welcome"]) + " 」")

                        elif msg.text.lower() == "cek respon":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Respon Msg」\nRespon Msg:\n\n「 " + str(Bot_Run["Respontag"]) + " 」")

                        elif msg.text.lower() == "cek spam":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Spam Msg」\nSpam Msg:\n\n「 " + str(Bot_Run["message1"]) + " 」")

                        elif msg.text.lower() == "cek sider":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Sider Msg」\nSider Msg:\n\n「 " + str(Bot_Run["mention"]) + " 」")

                        elif msg.text.lower() == "cek server":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Server」:\n\n「 " + str(Bot_Run["server"]) + " 」")

                        elif msg.text.lower() == "cek autorestart":
                            if msg._from in Master:
                               kang1.sendMessage(msg.to, "「Autorestart」:\n\nIn remaining time:「 " + str(Bot_Run["timeRestart"]) + " /scnds」")

                        elif ("siri:backup " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bot_Create["backupmem"][target] = True
                                           with open('backup.json', 'w') as fp:
                                           		json.dump(Bot_Create, fp, sort_keys=True, indent=4)
                                           fino1.sendMessage(msg.to,"ーをバックアップします。\nすべてのメンバーを復元する準備ができました。(｀・ω・´)")
                                       except:
                                           pass

                        elif cmd == "siri:backuplist" or cmd == 'backuplist':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Create["backupmem"] == {}:
                                fino1.sendMessage(msg.to,"バックアップが追加されていない(´ ・ω・`)")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Bot_Create["backupmem"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +fino1.getContact(m_id).displayName + "\n"
                                fino1.sendMessage(msg.to,"メンバーのバックアップ(｀・ω・´)\n\n"+ma+"\n合計「%s」ユーザー" %(str(len(Bot_Create["backupmem"]))))

                        elif cmd == "siri:backup.contact" or cmd == 'backup.contact':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Create["backupmem"] == {}:
                                    fino1.sendMessage(msg.to,"バックアップが追加されていない(´ ・ω・`)")
                              else:
                                    ma = ""
                                    for i in Bot_Create["backupmem"]:
                                        ma = fino1.getContact(i)
                                        fino1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif ("siri:backup.delete " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Bot_Create["backupmem"][target]
                                           fino1.sendMessage(msg.to,"バックアップを削除しました(ˋ ・ω・´)")
                                       except:
                                           pass

                        elif ("Talkban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bot_Run["Talkblacklist"][target] = True
                                           kang1.sendMessage(msg.to,"Talkblacklist user added")
                                       except:
                                           pass

                        elif ("Talkban dell " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Bot_Run["Talkblacklist"][target]
                                           kang1.sendMessage(msg.to,"Talkban user deleted")
                                       except:
                                           pass

                        elif ("Ban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bot_Run["blacklist"][target] = True
                                           kang1.sendMessage(msg.to,"Blacklist user added")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Bot_Run["blacklist"][target]
                                           kang1.sendMessage(msg.to,"User unbanned")
                                       except:
                                           pass

                        elif cmd == "banlist" or msg.text.lower() == 'banlist':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Run["blacklist"] == {}:
                                kang1.sendMessage(msg.to,"No blacklist user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Bot_Run["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "│ " +kang1.getContact(m_id).displayName + "\n"
                                kang1.sendMessage(msg.to,"╭─「 Banned List 」─\n"+ma+"\n╰──────────\nTotal「%s」Blacklist User" %(str(len(Bot_Run["blacklist"]))))

                        elif cmd == "talkbanlist" or msg.text.lower() == 'talkbanlist':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Run["Talkblacklist"] == {}:
                                kang1.sendMessage(msg.to,"No Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Bot_Run["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang1.getContact(m_id).displayName + "\n"
                                kang1.sendMessage(msg.to,"|| Talkban List\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(Bot_Run["Talkblacklist"]))))

                        elif cmd == "blc" or cmd == 'blcontact':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if Bot_Run["blacklist"] == {}:
                                    kang1.sendMessage(msg.to,"No blacklist")
                              else:
                                    ma = ""
                                    for i in Bot_Run["blacklist"]:
                                        ma = kang1.getContact(i)
                                        kang1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif "/ti/g/" in msg.text.lower():
                          if wait["finbot"] == True:
                            #if msg._from in Master:
                              if Bot_Run["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kang.findGroupByTicket(ticket_id)
                                     kang.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = fino1.findGroupByTicket(ticket_id)
                                     fino1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group2 = fino2.findGroupByTicket(ticket_id)
                                     fino2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     group3 = fino3.findGroupByTicket(ticket_id)
                                     fino3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group6 = kang1.findGroupByTicket(ticket_id)
                                     kang1.acceptGroupInvitationByTicket(group3.id,ticket_id)

    except Exception as error:
        print (error) 

while True:
    try:
        autoRestart()
        operations = oepoll.singleTrace(count=50)
        if operations is not None:
            for op in operations:
                finbot(op)
                oepoll.setRevision(op.revision)
                #_td = threading.Thread(target=finbot, args=(op))#finbot.OpInterrupt[op.type], args=(op)
                #_td.daemon = False
                #_td.start()
                #_td.join()
    except Exception as e:
        print (e)