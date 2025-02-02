# -*- coding: cp1252 -*-
import re
 
def cut_repeat(text, threshold):
	"""
	Reduce a character until threshold if it repeats more than threshold
	"""
	text = list(text)
	result = ''
	count = 0
	for i in xrange(len(text)-1):
		if text[i] == text[i+1]:
			count += 1
			if count < threshold:
				result += text[i]
		else:
			count = 0
			result += text[i]
	return result+text[-1]
 
re_symbol = re.compile('[^@][^a-z][^A-Z][^0-9]+$')
def normalize_word(word):
	"""
	Normalize repeat expression for English
	"""
	word = cut_repeat(word, 2)
	suffix_symbol = re_symbol.findall(word)
	word = re_symbol.sub('',word)
	word = converttable.get(word, word)
	return word+cut_repeat(suffix_symbol[0],1) if suffix_symbol else word
 
def normalize_sentence(sentence):
	"""
	Normalize for each word
	"""
	words = sentence.split(' ')
	return ' '.join([normalize_word(word) for word in words])
 
converttable = {
'aa':'aaa',
'againn':'again',
'aghh':'agh',
'aah':'ah',
'aahh':'ah',
'ahh':'ah',
'ahaa':'aha',
'ahha':'aha',
'al':'all',
'alonee':'alone',
'alreadyy':'already',
'allways':'always',
'alwayss':'always',
'amm':'am',
'amazingg':'amazing',
'aand':'and',
'andd':'and',
'annd':'and',
'aree':'are',
'ass':'as',
'aaw':'aww',
'aaww':'aww',
'aw':'aww',
'awayy':'away',
'awee':'awe',
'awwe':'awe',
'awesomee':'awesome',
'awhh':'awh',
'awwh':'awh',
'awwhh':'awh',
'ayy':'ay',
'ayee':'aye',
'ayye':'aye',
'ayyee':'aye',
'ayoo':'ayo',
'babby':'baby',
'babyy':'baby',
'baack':'back',
'backk':'back',
'badd':'bad',
'bee':'be',
'bedd':'bed',
'ben':'been',
'bestt':'best',
'beter':'better',
'bihh':'bih',
'birthdayy':'birthday',
'bitchh':'bitch',
'bitchess':'bitches',
'blahh':'blah',
'bo':'boo',
'boii':'boi',
'boredd':'bored',
'boyy':'boy',
'broo':'bro',
'bruhh':'bruh',
'bur':'burr',
'butt':'but',
'buut':'but',
'byee':'bye',
'cal':'call',
'chil':'chill',
'chilin':'chillin',
'col':'cool',
'coll':'cool',
'cooll':'cool',
'cooll!!':'cool!',
'comee':'come',
'comme':'come',
'craazy':'crazy',
'crazyy':'crazy',
'crazzy':'crazy',
'ctfuu':'ctfu',
'ctfupp':'ctfup',
'ctfuup':'ctfup',
'cutee':'cute',
'cuzz':'cuz',
'damm':'dam',
'daamn':'damn',
'dammn':'damn',
'damnn':'damn',
'dangg':'dang',
'dawgg':'dawg',
'dayy':'day',
'dayss':'days',
'deff':'def',
'doo':'do',
'doee':'doe',
'donee':'done',
'downn':'down',
'dudee':'dude',
'duhh':'duh',
'dyingg':'dying',
'earlyy':'early',
'ef':'eff',
'ehh':'eh',
'ek':'eek',
'eem':'em',
'emm':'em',
'eep':'ep',
'err':'er',
'erbody':'errbody',
'everr':'ever',
'everyonee':'everyone',
'eew':'ew',
'eww':'ew',
'excitedd':'excited',
'facee':'face',
'farr':'far',
'fel':'feel',
'fell':'feel',
'finaly':'finally',
'finee':'fine',
'fol':'fool',
'foll':'fool',
'followw':'follow',
'folow':'follow',
'followerss':'followers',
'folowers':'followers',
'fre':'free',
'fridayy':'friday',
'fuckk':'fuck',
'fuuck':'fuck',
'fukk':'fuk',
'funn':'fun',
'funnyy':'funny',
'gahh':'gah',
'gamee':'game',
'ge':'gee',
'geting':'getting',
'girll':'girl',
'girrl':'girl',
'girlss':'girls',
'goo':'go',
'god':'good',
'godd':'good',
'goodd':'good',
'goodmorningg':'goodmorning',
'goodnightt':'goodnight',
'gona':'gonna',
'goona':'gonna',
'goshh':'gosh',
'gota':'gotta',
'grr':'gr',
'greatt':'great',
'gues':'guess',
'guhh':'guh',
'gurll':'gurl',
'guyss':'guys',
'haa':'ha',
'hha':'ha',
'haaha':'haha',
'hahaa':'haha',
'hahha':'haha',
'hahhaa':'haha',
'hhaha':'haha',
'hahaaha':'hahaha',
'hahahaa':'hahaha',
'hahahha':'hahaha',
'hahahhaa':'hahaha',
'hahhaha':'hahaha',
'hhahaha':'hahaha',
'happyy':'happy',
'hardd':'hard',
'hatee':'hate',
'haave':'have',
'havee':'have',
'heel':'hell',
'hel':'hell',
'heello':'hello',
'helloo':'hello',
'helo':'hello',
'herr':'her',
'heree':'here',
'herre':'here',
'heey':'hey',
'heeyy':'hey',
'heyy':'hey',
'hii':'hi',
'himm':'him',
'hhmm':'hmm',
'hm':'hmm',
'hoo':'ho',
'homee':'home',
'homme':'home',
'hoot':'hot',
'hott':'hot',
'housee':'house',
'huhh':'huh',
'humm':'hum',
'hungryy':'hungry',
'hur':'hurr',
'idkk':'idk',
'ight':'iight',
'ightt':'iight',
'il':'ill',
'iim':'im',
'imm':'im',
'iin':'in',
'inn':'in',
'iis':'is',
'iss':'is',
'ishh':'ish',
'issh':'ish',
'iit':'it',
'itt':'it',
'itss':'its',
'juss':'jus',
'kil':'kill',
'knoo':'kno',
'knoow':'know',
'knoww':'know',
'latee':'late',
'latte':'late',
'laterr':'later',
'latter':'later',
'lawdd':'lawd',
'leggo':'lego',
'leggoo':'lego',
'legoo':'lego',
'lifee':'life',
'liike':'like',
'likee':'like',
'llike':'like',
'livee':'live',
'lmaao':'lmao',
'lmaaoo':'lmao',
'lmaoo':'lmao',
'lmboo':'lmbo',
'lmfaao':'lmfao',
'lmfaaoo':'lmfao',
'lmfaoo':'lmfao',
'lmmfao':'lmfao',
'lok':'look',
'llol':'lol',
'loll':'lol',
'lool':'lol',
'longg':'long',
'loove':'love',
'lovee':'love',
'llss':'lls',
'ls':'lls',
'luckyy':'lucky',
'madd':'mad',
'maan':'man',
'mann':'man',
'manee':'mane',
'mee':'me',
'meann':'mean',
'meeh':'meh',
'mehh':'meh',
'mhmm':'mhm',
'mmhm':'mhm',
'mmhmm':'mhm',
'mindd':'mind',
'mis':'miss',
'moneyy':'money',
'mooney':'money',
'moore':'more',
'moree':'more',
'morningg':'morning',
'moviee':'movie',
'muahh':'muah',
'muchh':'much',
'mmy':'my',
'myy':'my',
'naa':'na',
'naah':'nah',
'naahh':'nah',
'nahh':'nah',
'naww':'naw',
'ned':'need',
'neverr':'never',
'nicee':'nice',
'niice':'nice',
'niga':'nigga',
'niggaa':'nigga',
'niggass':'niggas',
'nightt':'night',
'noo':'no',
'nopee':'nope',
'nott':'not',
'nothingg':'nothing',
'noww':'now',
'oo':'ooo',
'ode':'odee',
'off':'of',
'oof':'of',
'ohh':'oh',
'ooh':'oh',
'oohh':'oh',
'okk':'ok',
'ook':'ok',
'okaay':'okay',
'okayy':'okay',
'okkay':'okay',
'omfgg':'omfg',
'omgg':'omg',
'onn':'on',
'oon':'on',
'onee':'one',
'oop':'op',
'opp':'op',
'opps':'oops',
'ops':'oops',
'orr':'or',
'ouu':'ou',
'outt':'out',
'overr':'over',
'oww':'ow',
'partyy':'party',
'peoplee':'people',
'pff':'pf',
'pft':'pfft',
'phonee':'phone',
'pleasee':'please',
'plzz':'plz',
'pplz':'plz',
'prettyy':'pretty',
'pshh':'psh',
'pssh':'psh',
'psst':'pst',
'pur':'purr',
'qq':'qqq',
'readyy':'ready',
'reall':'real',
'reallyy':'really',
'realy':'really',
'rightt':'right',
'riight':'right',
'rom':'room',
'samee':'same',
'sayy':'say',
'se':'see',
'sse':'see',
'sexxy':'sexy',
'sexyy':'sexy',
'shh':'sh',
'ssh':'sh',
'sheeshh':'sheesh',
'shii':'shi',
'shidd':'shid',
'shiid':'shid',
'shiit':'shit',
'shitt':'shit',
'shoo':'sho',
'shoree':'shore',
'shoot':'shot',
'showw':'show',
'showerr':'shower',
'sickk':'sick',
'sighh':'sigh',
'sleepp':'sleep',
'sloww':'slow',
'smhh':'smh',
'soo':'so',
'sso':'so',
'son':'soon',
'sonn':'soon',
'songg':'song',
'sorryy':'sorry',
'stil':'still',
'stoop':'stop',
'stopp':'stop',
'stuf':'stuff',
'suckss':'sucks',
'suree':'sure',
'swagg':'swag',
'swearr':'swear',
'tel':'tell',
'thankk':'thank',
'thankss':'thanks',
'thanxx':'thanx',
'thaat':'that',
'thatt':'that',
'tthat':'that',
'thatss':'thats',
'thee':'the',
'tthe':'the',
'themm':'them',
'thenn':'then',
'theree':'there',
'thingg':'thing',
'thiis':'this',
'thiss':'this',
'thoo':'tho',
'thoughh':'though',
'timee':'time',
'tiredd':'tired',
'too':'to',
'tto':'to',
'todaay':'today',
'todayy':'today',
'tommorow':'tomorrow',
'tommorrow':'tomorrow',
'tomorow':'tomorrow',
'tonightt':'tonight',
'truu':'tru',
'truee':'true',
'twiiter':'twitter',
'twiter':'twitter',
'twitterr':'twitter',
'ug':'ugg',
'uggh':'ugh',
'ugghh':'ugh',
'ughh':'ugh',
'uugghh':'ugh',
'uhh':'uh',
'uhmm':'uhm',
'umm':'um',
'upp':'up',
'uss':'us',
'vv':'vvv',
'veryy':'very',
'ww':'www',
'wackk':'wack',
'waah':'wah',
'wahh':'wah',
'waitt':'wait',
'wana':'wanna',
'wannaa':'wanna',
'waas':'was',
'wass':'was',
'wassupp':'wassup',
'wasup':'wassup',
'waay':'way',
'wayy':'way',
'wee':'we',
'wwe':'we',
'wel':'well',
'welcomee':'welcome',
'whaa':'wha',
'whaat':'what',
'whatt':'what',
'wheree':'where',
'wheww':'whew',
'whoo':'who',
'whoaa':'whoa',
'whop':'whoop',
'whyy':'why',
'wif':'wiff',
'wil':'will',
'wo':'woo',
'woahh':'woah',
'wooah':'woah',
'wohoo':'woohoo',
'wop':'woop',
'wordd':'word',
'workk':'work',
'worldd':'world',
'wot':'woot',
'woow':'wow',
'woww':'wow',
'wtff':'wtf',
'xdd':'xd',
'xii':'xi',
'yaa':'ya',
'yahh':'yah',
'yal':'yall',
'yass':'yas',
'yaay':'yay',
'yayy':'yay',
'yee':'ye',
'yeaa':'yea',
'yeeaa':'yea',
'yeaah':'yeah',
'yeaahh':'yeah',
'yeahh':'yeah',
'yeeah':'yeah',
'yepp':'yep',
'yess':'yes',
'yoo':'yo',
'yoou':'you',
'youu':'you',
'yuu':'yu',
'yumm':'yum',
'yupp':'yup',
'yuup':'yup',
'zz':'zzz'
}
 
if __name__ == '__main__':
##	print "normalize_word('thanxxxx') ->",
	print normalize_word('@bcci')
##	print "normalize_sentence('you are cooooooooooooooollllllllllllll!!!!!!!!!!!!!!') ->",
	print normalize_sentence('you are cooooooooooooooollllllllllllll!!!!!!!!!!!!!')
