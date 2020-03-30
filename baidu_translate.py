import requests
import json
import re
from bs4 import BeautifulSoup
import lxml
import js2py

#不同语言的标志值 常量
language_dict={'阿拉伯语': 'ara', '爱沙尼亚语': 'est', '保加利亚语': 'bul',
               '波兰语': 'pl', '丹麦语': 'dan', '德语': 'de', '俄语': 'ru',
               '法语': 'fra', '芬兰语': 'fin', '韩语': 'kor', '荷兰语': 'nl',
               '捷克语': 'cs', '罗马尼亚语': 'rom', '葡萄牙语': 'pt', '日语': 'jp',
               '瑞典语': 'swe', '斯洛文尼亚语': 'slo', '泰语': 'th', '文言文': 'wyw',
               '西班牙语': 'spa', '希腊语': 'el', '匈牙利语': 'hu', '中文': 'zh', '英语': 'en',
               '意大利语': 'it', '越南语': 'vie', '粤语': 'yue', '中文繁体': 'cht'}


#翻译,默认中译英
def translate(word,sign,token,BAIDUID,fro='zh',to='en'):
    url='https://fanyi.baidu.com/v2transapi'
    headers={
        'cookie':BAIDUID,
    }
    data={
        'from':fro,
        'to':to,
        'query':word,
        'transtype':'translang',
        'simple_means_flag':'3',
        'sign':sign,
        'token':token

    }

    res=requests.post(url=url,data=data,headers=headers)
    result_dict = json.loads(res.text)
    result=result_dict.get('trans_result').get('data')[0].get('dst')
    return result

#破解token参数
def token_parser(BAIDUID):
    html=requests.get('https://fanyi.baidu.com',
                      headers={'cookie':BAIDUID,}).text
    token=re.findall(r"token: '(.*?)'",html)[0]
    return token

#破解sign参数 未完成
def sign_parser(word):
    session = requests.Session()
    headers= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    session.headers = headers
    response = session.get("http://fanyi.baidu.com/")
    gtk = re.findall(";window.gtk = ('.*?');",response.content.decode())[0]

    context = js2py.EvalJs()
    js = r'''
    function a(r) {
            if (Array.isArray(r)) {
                for (var o = 0, t = Array(r.length); o < r.length; o++)
                    t[o] = r[o];
                return t
            }
            return Array.from(r)
        }
        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
            return r
        }
        function e(r) {
            var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === o) {
                var t = r.length;
                t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
            } else {
                for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                    "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                    C !== h - 1 && f.push(o[C]);
                var g = f.length;
                g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
            }
            var u = void 0
                , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
            u = 'null !== i ? i : (i = window[l] || "") || ""';
            for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                var A = r.charCodeAt(v);
                128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                    S[c++] = A >> 18 | 240,
                    S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                    S[c++] = A >> 6 & 63 | 128),
                    S[c++] = 63 & A | 128)
            }
            for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                p += S[b],
                    p = n(p, F);
            return p = n(p, D),
                p ^= s,
            0 > p && (p = (2147483647 & p) + 2147483648),
                p %= 1e6,
            p.toString() + "." + (p ^ m)
        }
    '''
    #js中添加一行gtk
    js = js.replace('\'null !== i ? i : (i = window[l] || "") || ""\'',gtk)
    # print(js)
    #执行js
    context.execute(js)
    #调用函数得到sign
    sign = context.e(word)
    return sign



#获取不同语言的标志值
def get_language_value(BAIDUID):
    res = requests.get('https://fanyi.baidu.com',
                        headers={'cookie': BAIDUID, })
    res.encoding=res.apparent_encoding
    html=res.text
    soup=BeautifulSoup(html,'lxml')
    language_list=soup.find('div',class_='language-list clearfix').find_all('a')
    language_dict={}
    for language in language_list:
        k=language.text.strip()
        v=language['value'].strip()
        language_dict[k]=v
    return language_dict




if __name__=='__main__':
    #BAIDUID是固定参数，随着时间可能会变化
    BAIDUID='BAIDUID=20BCEF784EBA1C91FF03146E4E126F4F:FG=1;'
    # 获取不同语言的标志值
    # language_dict = get_language_value(BAIDUID)
    # print(language_dict )
    #获取token参数
    token=token_parser(BAIDUID)
    languages=input('请输入语种(比如“中文 英语”):').split(' ')
    fro,to=language_dict.get(languages[0]),language_dict.get(languages[1])
    word=input('请输入要翻译的单词：')
    sign=sign_parser(word)
    print(translate(word,sign,fro=fro,to=to,token=token,BAIDUID=BAIDUID))


