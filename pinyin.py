# -*- coding: utf-8 -*-
import re

PINYIN_RE = re.compile(r'(([bcdfghjklmnpqrstwxyz]*)(u:an|u:|u:e|[aeiou]+)([bcdfghjklmnpqrstwxyz]*)|r)([1-5])', re.I)


TONE_MARKS = {
    'a':u'_āáǎàa',
    'e':u'_ēéěèe',
    'i':u'_īíǐìi',
    'o':u'_ōóǒòo',
    'u':u'_ūúǔùu',
    'u:':u'_ǖǘǚǜü'
}

# use upper() to get the upper case versions
TONE_MARKS['A'] = TONE_MARKS['a'].upper()
TONE_MARKS['E'] = TONE_MARKS['e'].upper()
TONE_MARKS['I'] = TONE_MARKS['i'].upper()
TONE_MARKS['O'] = TONE_MARKS['o'].upper()
TONE_MARKS['U'] = TONE_MARKS['u'].upper()
TONE_MARKS['U:'] = TONE_MARKS['u:'].upper()

ALL_SOUNDS = set(['a', 'ai', 'an', 'ang', 'ao', 'ba', 'bai', 'ban', 'bang',
    'bao', 'bei', 'ben', 'beng', 'bi', 'bian', 'biao', 'bie', 'bin', 'bing',
    'bo', 'bu', 'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng', 'cha',
    'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng', 'chi', 'chong',
    'chou', 'chu', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo', 'ci',
    'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo', 'da', 'dai', 'dan',
    'dang', 'dao', 'de', 'dei', 'den', 'deng', 'di', 'dian', 'diao', 'die',
    'ding', 'diu', 'dong', 'dou', 'du', 'duan', 'dui', 'dun', 'duo', 'e', 'en',
    'er', 'fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fo', 'fou', 'fu', 'ga',
    'gai', 'gan', 'gang', 'gao', 'ge', 'gei', 'gen', 'geng', 'gong', 'gou',
    'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo', 'ha', 'hai',
    'han', 'hang', 'hao', 'he', 'hei', 'hen', 'heng', 'hong', 'hou', 'hu',
    'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo', 'ji', 'jia', 'jian',
    'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', 'juan', 'jue',
    'jun', 'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'ken', 'keng', 'kong',
    'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo', 'la',
    'lai', 'lan', 'lang', 'lao', 'le', 'lei', 'leng', 'li', 'lia', 'lian',
    'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'long', 'lou', 'lu', 'luan',
    'lun', 'luo', 'lu:', 'lu:an', 'lu:e', 'ma', 'mai',     'man', 'mang', 'mao',
    'me', 'mei', 'men', 'meng', 'mi', 'mian', 'miao',     'mie', 'min', 'ming',
    'miou', 'mo', 'mou', 'mu', 'na', 'nai', 'nan',     'nang', 'nao', 'ne', 'nei',
    'nen', 'neng', 'ni', 'nian', 'niang', 'niao',     'nie', 'nin', 'ning', 'niu',
    'nong', 'nou', 'nu', 'nuan', 'nuo',     'nu:', 'nu:e', 'ou', 'pa', 'pai', 'pan',
    'pang', 'pao', 'pei', 'pen',     'peng', 'pi', 'pian', 'piao', 'pie', 'pin',
    'ping', 'po', 'pou', 'pu', 'qi',     'qia', 'qian', 'qiang', 'qiao', 'qie',
    'qin', 'qing', 'qiong', 'qiu', 'qu',     'quan', 'que', 'qun', 'r', 'ran',
    'rang', 'rao', 're', 'ren', 'reng', 'ri',     'rong', 'rou', 'ru', 'ruan',
    'rui', 'run', 'ruo', 'sa', 'sai', 'san',     'sang', 'sao', 'se', 'sen', 'seng',
    'sha', 'shai', 'shan', 'shang', 'shao',     'she', 'shei', 'shen', 'sheng',
    'shi', 'shou', 'shu', 'shua', 'shuai',     'shuan', 'shuang', 'shui', 'shun',
    'shuo', 'si', 'song', 'sou', 'su',     'suan', 'sui', 'sun', 'suo', 'ta', 'tai',
    'tan', 'tang', 'tao', 'te',     'teng', 'ti', 'tian', 'tiao', 'tie', 'ting',
    'tong', 'tou', 'tu', 'tuan',     'tui', 'tun', 'tuo', 'wa', 'wai', 'wan',
    'wang', 'wei', 'wen', 'weng', 'wo',     'wu', 'xi', 'xia', 'xian', 'xiang',
    'xiao', 'xie', 'xin', 'xing', 'xiong',     'xiu', 'xu', 'xuan', 'xue', 'xun',
    'ya', 'yan', 'yang', 'yao', 'ye', 'yi',     'yin', 'ying', 'yong', 'you', 'yu',
    'yuan', 'yue', 'yun', 'za', 'zai',     'zan', 'zang', 'zao', 'ze', 'zen',
    'zeng', 'zha', 'zhai', 'zhan', 'zhang',     'zhao', 'zhe', 'zhen', 'zheng',
    'zhi', 'zhong', 'zhou', 'zhu', 'zhua',     'zhuai', 'zhuan', 'zhuang', 'zhui',
    'zhun', 'zhuo', 'zi', 'zong', 'zou',     'zu', 'zuan', 'zui', 'zun', 'zuo'])



def pinyinize(src, raise_exception=False):
    "Turns a source string like 'ni3 hao3' into a utf-8 equivalent with tone marks"

    try:
        def replacer(m):
            syllable, pre, vowels, post, tone = m.groups()
            vowels = list(vowels)
            if ':' in vowels:
                dot_dot_index = vowels.index(':')
                vowels[dot_dot_index - 1] += vowels[dot_dot_index]
                del vowels[dot_dot_index]

            if syllable.lower() == 'r' and tone == '5':
                return syllable

            tone = int(tone)

            v = [c.lower() for c in vowels]
            # 3 rules
            # 1- A and E get the tone mark if either one present (they are never both present)
            # 2- in ou, o gets the tone mark
            # 3- in all other cases, last vowel gets the tone
            # see http://pinyin.info/rules/where.html

            # rule 1
            if 'a' in v:
                tindex = v.index('a')
            elif 'e' in v:
                tindex = v.index('e')
            elif 'ou' == v: # rule 2
                tindex = 0
            else: # rule 3
                tindex = len(v) - 1


            try:
                vowels = [v for v in vowels]
                vowels[tindex] = TONE_MARKS[vowels[tindex]][tone]

                vowels = [v if ':' not in v else TONE_MARKS[v][5] for v in vowels]

                vowels = u''.join(vowels)
                return "%s%s%s" % (pre, vowels, post)
            except:
#                import sys
#                import traceback
#                typ, err, tb = sys.exc_info()
#                traceback.print_tb(tb)
#                print typ, err
                if raise_exception:
                    raise
                return m.group(0)

        return PINYIN_RE.sub(replacer, src)
    except:
#        import sys
#        import traceback
#        typ, err, tb = sys.exc_info()
#        traceback.print_tb(tb)
#        print typ, err, 'src=', repr(src)
        if raise_exception:
            raise

        return src

def depinyinize(src):
    "Turns a source string like 'nǐ hǎo' into 'ni3 hao3'"

    unmarked = {}
    for k, v in TONE_MARKS.items():
        for i, c in enumerate(v[1:5]):
            unmarked[c] = (k, i+1)


    newstr = []
    lc = src.lower()
    i = 0
    while i < len(src):
        c = src[i]

        # see if this is a character with a tone mark
        if c in unmarked:
            letter, tone = unmarked[c]

            # find every sound that includes this vowel
            possible_sounds = [s for s in ALL_SOUNDS if letter.lower() in s]

            #try and match longest sounds first
            possible_sounds.sort(key=len)
            possible_sounds.reverse()

            sound = None
            so_far = u''.join(newstr).lower()
            for p in possible_sounds:
                li = p.find(letter.lower())
                before_match, after_match = p[:li], p[li+len(letter):]

                # see if this sound's spelling matches what we have...
                if ((len(before_match) == 0 # either there's nothing before the match
                    or so_far[-len(before_match):] == before_match) # or the bit before the match is in our string
                    and # ... AND
                    # the bit after the match is 0 or matches our string
                   (len(after_match) == 0 or lc[i+1:len(after_match)+i+1] == after_match)):
                    sound = p
                    break
            if sound:

                newstr.append(letter)
                # preserve case, use chars from original string
                newstr += list(src[i+1:len(after_match)+i+1])
                newstr.append(u'%d' % tone)
                i += len(after_match) + 1
            else:
                newstr.append(letter)
                i += 1

        else: # no tone mark, check for neutral tone ü
            if c == TONE_MARKS['U:'][5]:
                newstr.append('U:')
            elif c == TONE_MARKS['u:'][5]:
                newstr.append('u:')
            else:
                newstr.append(c)
            i += 1

    return u''.join(newstr)
