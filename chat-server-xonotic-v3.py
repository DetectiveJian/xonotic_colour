#!/usr/bin/python3
#
# Shazza-Works did this !
# 5th Jul 2023
import re
import sys
import codecs
import random
import requests
from time import sleep
from flask import Flask, request
from duckduckgo_search import DDGS
from python_translator import Translator


"""
Usage:
	Commands: help, joke, who, search, trans, test
	
	Colours: random, white, slayer, blue, google, sunset etc
	
	Format: [command] Text or args.
	
	example: press 'o'
		type [spoon]
		hit enter
		colour codes will change to spoon
		
		press 'o'
		type [trans]:french:Your message text here
		hit enter
		TRS: is show and your message in french
"""



app = Flask(__name__)


# Global Colour Set
COLOUR = []


# set of do something commands
commands = {
	"[help]": "{help}",
	"[joke]": "say [joke] ^1COMMAND: ^2OK; defer 1.5 \"say {joke}\"",
	"[who]": "say [who] ^1COMMAND: ^2OK; say ^1Shazza^7-^4Works^7, Using a little ^xf00P^xf40y^xf70t^xfa0h^xef0o^xbf0n ^x2f03^x0f03^x0f2.^x0f91^x0fd0^x0df.^x09f6 ^7and ^6Flask",
	"[search]": "say [search] ^1COMMAND: ^2OK ; say ^2Word^7:{word} ^2Info^7: ^1{search}",
	"[trans]": "say ^1TRS: {msg}",
	"[test]": ""
	}


# colour sets for styled text. 
colours = {
	"[random]": list(),

	"[white]": ["#FFFFFF"],

	"[slayer]": ["#701000", "#702000", "#703000", "#70400", "#70500", "#70600", "#70700", "#70800", "#70900", "#80000", "#80100"],

	"[blur]": ["#0d38c0", "#460eea", "#a60ee9", "#e80ecb", "#e70e6a", "#e6110e", "#e5700e", "#e4ce0e", "#9ae30e", "#3ce20e", "#0de13c"],

	"[google]": [ "#4885ed", "#db3236", "#f4c20d", "#4885ed", "#3cba54", "#db3236", "#4885ed", "#db3236", "#f4c20d", "#4885ed", "#3cba54", "#db3236"],

	"[sunset]": ["#ff0000", "#ff2200", "#ff4400", "#ff6600", '#ff8800', '#ff9900', '#ff9922', '#ff9944', '#ff9966', '#ff9966', '#ff9988', '#ff2299', '#ff3399', '#ff4499', '#ff5599', '#ff6699', '#ff7799'],

	"[grey]": ["#010101", "#010102", "#010103", "#010104", "#010105", "#010106", "#010107", "#010108", "#010109", "#010200", "#010201", "#010202", "#010203", "#010204", "#010205", "#010206", "#010207",
		"#010208", "#010209"],	

	"[rain]": ["#ff0000", "#ff4909", "#ff7100", "#ffac00", "#eeff00", "#b1ff00", "#27ff00", "#09ff00", "#00ff21", "#00ff9b", "#00ffd8", "#00deff", "#009bff", "#0059ff", "#0016ff", "#5700ff",
		"#b100ff", "#f400ff", "#ff00c8", "#ff0085", "#ff0043"],

	"[night]": ["#5b5b5b", "#5a5a5a", "#585858", "#575757", "#565656", "#545454", "#535353", "#525252", "#515151", "#4f4f4f", "#4e4e4e", "#4d4d4d", "#4b4b4b", "#4a4a4a", "#505050", "#555555",
		"#5b5b5b", "#606060", "#666666", "#6b6b6b", "#717171", "#767676", "#7c7c7c", "#818181", "#878787", "#8c8c8c", "#929292", "#8d8d8d", "#878787", "#828282", "#7c7c7c", "#777777", "#727272",
		"#6c6c6c", "#676767", "#626262", "#5c5c5c", "#575757", "#515151", "#4c4c4c", "#4b4b4b", "#4a4a4a", "#494949", "#484848", "#474747", "#464646", "#464646", "#454545", "#444444", "#434343",
		"#424242", "#414141", "#404040", "#494949", "#515151", "#5a5a5a", "#636363", "#6b6b6b", "#747474", "#7d7d7d", "#868686", "#8e8e8e", "#979797", "#a0a0a0", "#a8a8a8", "#b1b1b1", "#a9a9a9",
		"#a1a1a1", "#999999", "#919191", "#898989", "#818181", "#7a7a7a", "#727272", "#6a6a6a", "#626262", "#5a5a5a", "#525252", "#4a4a4a"],

	"[yellow]": ["#eaff00", "#eaff18", "#ebff25", "#ebff2f", "#ebff37", "#ecff3e", "#ecff45", "#edff4b", "#edff51", "#edff57", "#eeff5c", "#eeff61", "#eeff66", "#efff6b", "#efff70", "#f0ff74",
		"#f0ff79", "#f0ff7e", "#f1ff82", "#f1ff86", "#f2ff8b", "#f2ff8f", "#f2ff93", "#f3ff97", "#f3ff9b", "#f3ff9f", "#f4ffa3", "#f4ffa7", "#f5ffab", "#f5ffaf", "#f5ffb3", "#f6ffb7", "#f6ffbb",
		"#f7ffbf", "#f7ffc3", "#f7ffc7", "#f8ffcb", "#f8ffce", "#f9ffd2", "#f9ffd6"],

	"[red]": ["#ed1616", "#e91516", "#e51516", "#e01416", "#dc1416", "#d81316", "#d41316", "#d01216", "#cc1216", "#c81116", "#c41116", "#c01116", "#bb1016", "#b71016", "#b31016", "#af1016", "#ab0f15",
		"#a70f15", "#a30f15", "#9f0f15", "#9b0e14", "#970e14", "#930e14", "#8f0e13", "#8c0d13", "#880d13", "#840d12", "#800d12", "#7c0d12", "#780c11", "#740c11", "#710c10", "#6d0c10", "#690c0f",
		"#650b0e", "#620b0e", "#5e0b0d", "#5a0b0c", "#570a0b", "#530a0a"],

	"[fire]": ["#ff0000", "#fa0702", "#f40e04", "#ef1506", "#ea1b08", "#e5210a", "#e0260c", "#db2b0d", "#d6300f", "#d13511", "#cc3912", "#c83d14", "#c34016", "#be4417", "#ba4718", "#b54a1a", "#b14c1b",
		"#ac4f1c", "#a8511d", "#a4531f", "#9f5420", "#9b5621", "#975722", "#935823", "#8f5923", "#8b5924", "#875925", "#835a26", "#7f5926", "#7b5927", "#775927", "#745828", "#705828", "#6c5729",
		"#695629", "#655529", "#62532a", "#5f522a", "#5b512a", "#584f2a"],

	"[water]": ["#2a00ff", "#2502fa", "#2104f4", "#1c06ef", "#1808ea", "#150ae5", "#110ce0", "#0e0ddb", "#0f13d6", "#1119d1", "#121fcc", "#1424c8", "#1629c3", "#172ebe", "#1832ba", "#1a36b5", "#1b3ab1",
		"#1c3dac", "#1d40a8", "#1f43a4", "#20469f", "#21489b", "#224a97", "#234c93", "#234d8f", "#244f8b", "#255087", "#265183", "#26517f", "#27527b", "#275277", "#285274", "#285270", "#29516c",
		"#295169", "#295065", "#2a4f62", "#2a4e5f", "#2a4d5b", "#2a4c58"],

	"[pink]": ["#c9389e", "#ca3ca0", "#cc41a1", "#cd45a3", "#cf48a4", "#d04ca6", "#d150a7", "#d354a9", "#d457ab", "#d55bac", "#d75eae", "#d862af", "#d965b1", "#db68b3", "#dc6cb4", "#dd6fb6", "#de72b8",
		"#e075b9", "#e178bb", "#e27cbc", "#e37fbe", "#e582c0", "#e685c1", "#e788c3", "#e88bc5", "#e98ec6", "#eb91c8", "#ec95ca", "#ed98cb", "#ee9bcd", "#ef9ecf", "#f0a1d0", "#f1a4d2", "#f3a7d4",
		"#f4aad5", "#f5add7", "#f6b0d9", "#f7b3db", "#f8b6dc", "#f9b9de"],

	"[ghost]": ["#96a2aa", "#94a0a8", "#939ea5", "#919ca3", "#909aa0", "#8e989e", "#8c959b", "#8b9399", "#899197", "#888f94", "#868d92", "#848b8f", "#83898d", "#81878a", "#808588", "#7e8386", "#7c8083",
		"#7b7e81", "#797c7e", "#787a7c", "#76787a", "#747677", "#737475", "#717272", "#707070", "#707071", "#727273", "#747475", "#767678", "#77777a", "#79797d", "#7b7b7f", "#7d7d81", "#7f7f84",
		"#808086", "#828288", "#84848b", "#86868d", "#888890", "#8a8a92", "#8b8b94", "#8d8d97", "#8f8f99", "#91919b", "#93939e", "#9494a0", "#9696a3", "#9898a5", "#9a9aa7", "#9a9aa8", "#9797a5",
		"#9595a1", "#92929e", "#8f8f9b", "#8d8d97", "#8a8a94", "#878791", "#84848e", "#82828a", "#7f7f87", "#7c7c84", "#7a7a80", "#77777d", "#74747a", "#717177", "#6f6f73", "#6c6c70", "#69696d",
		"#676769", "#646466", "#616163", "#5e5e60", "#5c5c5c", "#595959"],

	"[tree]": ["#428a24", "#448724", "#468424", "#488125", "#497e25", "#4b7b25", "#4d7825", "#4f7626", "#517326", "#537026", "#546d26", "#566a27", "#586727", "#5a6427", "#5c6127", "#5e5e28", "#605b28",
		"#615828", "#635528", "#655329", "#675029", "#694d29", "#6b4a29", "#6d472a", "#6e442a", "#71462d", "#734932", "#754d37", "#78513b", "#7a5540", "#7d5945", "#7f5c4a", "#81604e", "#846453",
		"#866858", "#886c5c", "#8b7061", "#8d7366", "#90776b", "#927b6f", "#947f74", "#978379", "#99877d", "#9b8a82", "#9e8e87", "#a0928c", "#a39690", "#a59a95", "#a79d9a", "#a89e9c", "#a59a97",
		"#a19593", "#9e918e", "#9b8c8a", "#978785", "#948381", "#917e7c", "#8e7978", "#8a7573", "#87706f", "#846b6a", "#806766", "#7d6261", "#7a5d5d", "#775958", "#735454", "#70504f", "#6d4b4b",
		"#694646", "#664242", "#633d3d", "#603839", "#5c3434", "#592f30"],

	"[ting]": ["#fb0000", "#fb0d0d", "#fb1a1a", "#fc2727", "#fc3434", "#fc4040", "#fc4d4d", "#fc5a5a", "#fd6767", "#fd7474", "#fd8181", "#fd8e8e", "#fd9b9b", "#fea7a7", "#feb4b4", "#fec1c1",
		"#fecece", "#fedbdb", "#ffe8e8", "#fff5f5", "#fefefd", "#f7fcf1", "#f0f9e5", "#eaf6da", "#e3f4ce", "#ddf1c2", "#d6eeb6", "#cfebab", "#c9e99f", "#c2e693", "#bce387", "#b5e07c", "#aede70",
		"#a8db64", "#a1d859", "#9ad64d", "#94d341", "#8dd035", "#87cd2a", "#80cb1e", "#7fca1c", "#85cd27", "#8cd033", "#92d23f", "#99d54b", "#a0d856", "#a6da62", "#addd6e", "#b4e079", "#bae385",
		"#c1e591", "#c7e89d", "#ceeba8", "#d5eeb4", "#dbf0c0", "#e2f3cb", "#e9f6d7", "#eff8e3", "#f6fbef", "#fcfefa", "#fdf8fb", "#faebf3", "#f8dfec", "#f5d2e4", "#f2c6dd", "#efbad5", "#ecadce",
		"#eaa1c6", "#e795bf", "#e488b7", "#e17cb0", "#de6fa8", "#db63a1", "#d95799", "#d64a92", "#d33e8a", "#d03283", "#cd257b", "#ca1974", "#c80c6c", "#c2146f", "#bb2074", "#b52c7a", "#ae387f",
		"#a84484", "#a25089", "#9b5c8e", "#956894", "#8e7499", "#88809e", "#818ca3", "#7b98a8", "#74a5ae", "#6eb1b3", "#67bdb8", "#61c9bd", "#5ad5c2", "#54e1c8", "#4dedcd", "#47f9d2"],

	"[spoon]": ["#50fb3b", "#52e44d", "#55cd5f", "#57b770", "#59a082", "#5b8994", "#5e72a6", "#605bb8", "#6244ca", "#642edb", "#6717ed", "#6900ff", "#7314ed", "#7c28dc", "#863bca", "#8f4fb8", "#9963a6",
		"#a27795", "#ac8b83", "#b59f71", "#bfb25f", "#c8c64e", "#d2da3c", "#cecd4e", "#cbbf5f", "#c7b271", "#c3a583", "#bf9895", "#bc8aa6", "#b87db8", "#b470ca", "#b063dc", "#ad55ed", "#a948ff",
		"#9a51ea", "#8b5ad6", "#7d63c1", "#6e6cac", "#5f7598", "#507f83", "#41886f", "#32915a", "#249a45", "#15a331", "#06ac1c", "#15a41b", "#259d1b", "#34951a", "#438e19", "#528618", "#627f18",
		"#717717", "#807016", "#8f6815", "#9f6115", "#ae5914", "#9f6716", "#907618", "#818419", "#72921b", "#63a01d", "#55af1f", "#46bd21", "#37cb23", "#28d924", "#19e826", "#0af628", "#1ae037",
		"#29cb46", "#39b555", "#49a064", "#598a73", "#687581", "#785f90", "#884a9f", "#9834ae", "#a71fbd", "#b709cc", "#a61cc1", "#962fb5", "#8541aa", "#74549f", "#646794", "#537a88", "#438d7d",
		"#32a072", "#21b267", "#11c55b", "#00d850", "#14c54a", "#28b343", "#3ca03d", "#508d37", "#647b31", "#79682a", "#8d5624", "#a1431e", "#b53018", "#c91e11", "#dd0b0b"],

	"[tango]": ["#fb5c00", "#fb5d01", "#fb5f02", "#fb6004", "#fc6105", "#fc6306", "#fc6407", "#fc6508", "#fc660a", "#fc680b", "#fc690c", "#fd6a0d", "#fd6c0e", "#fd6d10", "#fd6e11", "#fd7012", "#fd7113",
		"#fd7214", "#fe7315", "#fe7517", "#fe7618", "#fe7719", "#fe791a", "#fe7a1b", "#fe7b1d", "#ff7d1e", "#ff7e1f", "#ff7f20", "#fe8021", "#fb8021", "#f98121", "#f68121", "#f38221", "#f08221",
		"#ed8221", "#eb8321", "#e88321", "#e58321", "#e28421", "#df8421", "#dd8421", "#da8521", "#d78521", "#d48621", "#d28621", "#cf8621", "#cc8721", "#c98721", "#c68721", "#c48821", "#c18821",
		"#be8821", "#bb8921", "#b88921", "#b68a21", "#b38a21", "#b38920", "#b3871f", "#b4851e", "#b5831d", "#b6811b", "#b77f1a", "#b77d19", "#b87b18", "#b97917", "#ba7715", "#ba7614", "#bb7413",
		"#bc7212", "#bd7011", "#be6e10", "#be6c0e", "#bf6a0d", "#c0680c", "#c1660b", "#c2640a", "#c26208", "#c36007", "#c45f06", "#c55d05", "#c65b04", "#c65902", "#c75701", "#c85500"]
	}


font_list = {
	"a": "ａ", "b": "ｂ", "c": "ｃ", "d": "ｄ", "e": "ｅ", "f": "ｆ", "g": "ｇ", "h": "ｈ" ,"i": "ｉ", "j": "ｊ", "k": "ｋ", "l": "ｌ", "m": "ｍ", "n": "ｎ", "o": "ｏ", "p": "ｐ",
	"q": "ｑ", "r": "ｒ", "s": "ｓ", "t": "ｔ", "u": "ｕ", "v": "ｖ", "w": "ｗ", "x": "ｘ", "y": "ｙ", "z": "ｚ", "A": "Ａ", "B": "Ｂ", "C": "Ｃ", "D": "Ｄ", "E": "Ｅ", "F": "Ｆ",
	"G": "Ｇ", "H": "Ｈ", "I": "Ｉ", "J": "Ｊ", "K":"Ｋ", "L": "Ｌ", "M": "Ｍ", "N": "Ｎ", "O": "Ｏ", "P": "Ｐ", "Q": "Ｑ", "R": "Ｒ", "S": "Ｓ", "T": "Ｔ", "U": "Ｕ", "V": "Ｖ",
	"W": "Ｗ", "X": "Ｘ", "Y": "Ｙ", "Z": "Ｚ", " ": " "
	}


def list_all_cmds():
	"""
	Get Commands from Comands and Colours dict
	args: None
	return tuple(commands, colours)
	"""
	coms = tuple(commands.keys())
	cols = tuple(colours.keys())
	return coms, cols


def code_converter(code):
	"""
	Convert a #FF00FF hex code to #F0F hex code
	args: str(hexcode)
	return str(newcode)
	"""
	new = code[1], code[3], code[5]
	return "".join(new)


def get_joke():
	"""
	Use a joke API to get a joke
	args: None
	return str(joke)
	"""
	jokesapi = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt&type=single"
	r = requests.get(jokesapi)
	joke = r.text.replace("\n", " ")
	return joke


def duck_search(text):
	"""
	Use DuckDuckGo module to look for word
	args: str(word)
	return str(joke)
	"""
	search = DDGS()
	res = tuple(search.answers(text))
	if res == ():
		ans = "[SORRY] Could not find anything: Try a 'word' again !"
	else:
		ans = res[0]['text'][:150]
	return ans


def make_random_codes():
	"""
	Make a 30 long set of random hex codes and store them in colors dict
	args: None
	return None
	"""
	colours["[random]"] = []
	r = lambda: random.randint(0,255)
	for i in range(30):
		colours["[random]"].append("%02X%02X%02X" % (r(),r(),r()))


def get_cmd(text):
	"""
	Check the user text for a command and return it if found
	args: None
	return str(command) or str(text)
	"""
	r = r"\[(\w+)\]"
	try:
		cmd = re.search(r, text)[0]
		if cmd:
			print(f"[FOUND CMD]: Doing {cmd}")
			return cmd
	except TypeError:
		return text


def set_colour(name):
	"""
	Set the global COLOUR set
	args: str(colour_name)
	return None
	"""
	global COLOUR
	COLOUR = colours[name]


def colour_text(msg):
	"""
	Method that dose the colour of chars in message
	args: str(message)
	return str(colour_text)
	"""
	global COLOUR
	s = 0
	new = ""
	msgb = ""
	if len(msg) >= 250:
		msgb = msg[250:]
		msg = msg[:250]
	msg = list(msg)
	for char in msg:
		if char in font_list.keys():
			char = font_list[char]
		if s == len(COLOUR):
			s = 0
		if char == " ":
			new = new + " "
			s = s - 1
		else:
			code = code_converter(COLOUR[s])
			new = new + "^x" + code + char
		s = s + 1
	return new + msgb


def translate_msg(msg, lang):
	"""
	Translate the msg to another language
	args: translate_msg(message, language)
	return str(translation_results)
	"""
	translator = Translator()
	res = translator.translate(msg, lang, "english")
	return res


@app.route("/chat", methods=["GET"])
def answer_the_call():
	"""
	The request server to anser the curl get request
	args: /chat?say=input_massage
	return http.response
	"""

	data = request.args.get("say")
	clean = data.split("$", 1)[0].strip()
	cmd = get_cmd(clean)
	text = clean.split(cmd)[1].strip()
	coms, cols = list_all_cmds()
	if cmd in coms:

		if cmd == "[help]":
			return commands[cmd].format(help=f"say ^1{' '.join(coms)}; say ^1{' '.join(cols)}")

		if cmd == "[joke]":
			joke = get_joke().replace("\"", "").replace("'", "")
			return commands[cmd].format(joke=f"^5{joke}")

		if cmd == "[search]":
			info = duck_search(text)
			return commands[cmd].format(word=text, search=info)

		if cmd == "[who]":
			return commands[cmd]

		if cmd == "[trans]":
			try:
				c,l,t = clean.split(":")
				msg = translate_msg(t, l)
				code = colour_text(str(msg))
				return commands[cmd].format(msg=code)
			except ValueError:
				return "say ^1[ERROR] Try: [trans]:language:Text here..."
		if cmd == "[test]":
			#return "say [*] ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ ; say [*] ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
			# return "say 卂 乃 匚 ᗪ 乇 千 Ꮆ 卄 丨 ﾌ Ҝ ㄥ 爪 几 ㄖ 卩 Ɋ 尺 丂 ㄒ ㄩ ᐯ 山 乂 ㄚ 乙"
			st = ["^5|\---/|","^5| ^1o^6_^1o ^5|","^5 \_^6^^^5_/"]
			return f"say {st[0]} ; defer 1 \"say {st[1]}\" ; defer 4 \"say {st[2]}\""

	elif cmd in cols:
		print(f"[*] COLOUR CHANGE: {cmd}")

		if cmd == "[random]":
			make_random_codes()
			set_colour("[random]")
			return f"say {cmd} ^1COLOUR: ^2OK; say [info] 30 New Random Codes Made."

		else:
			set_colour(cmd)
			return f"say {cmd} ^1COLOUR: ^2OK"

	else:
		msg = colour_text(cmd)
		return f"say [MSG]: {msg}"


if __name__ == "__main__":
	set_colour('[rain]')
	app.run(debug=True)


# EOF
