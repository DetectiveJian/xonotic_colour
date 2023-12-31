#!/usr/bin/python3
#
# Shazza-Works did this !
# 5th Jul 2023
import re
import sys
import json
import codecs
import random
import requests
from time import sleep
from flask import Flask, request
from duckduckgo_search import DDGS
from python_translator import Translator
from tools import commands, colours, font_list, nades, names, woman


"""
Usage:
	Commands: help, joke, who, search, trans, test, name. font, etc

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
# Global Font Setting
FONT = False
# Global Jokes Seen
JOKES = []


def toggle_font():
	global FONT
	if FONT is False:
		FONT = True
	else:
		FONT = False


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
	global JOKES

	try:
		if len(JOKES) <= 0:
			url = "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,racist,sexist,explicit&type=single&amount=10"
			JOKES = list(json.loads(requests.get(url).content)["jokes"])
	finally:
		joke = JOKES.pop()
		joke, iid =  joke["joke"].replace("\n", " "), joke['id']
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


def colour_text(msg, colour=COLOUR):
	"""
	Method that dose the colour of chars in message
	args: str(message)
	return str(colour_text)
	"""
	#global COLOUR
	global FONT
	s = 0
	new = ""
	msgb = ""
	if len(msg) >= 160:
		msgb = msg[160:]
		msg = msg[:160]
	msg = list(msg)
	for char in msg:
		if FONT is True:
			if char in font_list.keys():
				char = font_list[char]
		if s == len(colour):
			s = 0
		if char == " ":
			new = new + " "
			s = s - 1
		else:
			code = code_converter(colour[s])
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
			# show the commands and colours
			return commands[cmd].format(helpa=f"{''.join(coms)}", helpb=f"{''.join(cols)}")

		if cmd == "[joke]":
			# grab a joke from the api
			joke = get_joke()
			return commands[cmd].format(joke=joke)

		if cmd == "[search]":
			# search online for a word
			info = duck_search(text)
			return commands[cmd].format(word=text, search=info)

		if cmd == "[who]":
			# show who made this
			return commands[cmd]

		if cmd == "[nade]":
			# Set the player nade type from 0-10
			# will make a list for these to convert num to names
			num = text.strip()
			if num in nades.keys():
				return commands[cmd].format(num=num, name=nades[num])
			else:
				return f"say [!] Sorry {num} is not a nade type (1-11) !"

		if cmd == "[tell]":
			# Tell a user a message by their number.
			num = text.split(" ")[0].strip()
			print(f"NUM: {num}")
			msg = " ".join(text.split(" ")[1:])
			print(f"MSG: {msg}")
			return commands[cmd].format(num=num, msg=msg)

		if cmd == "[name]":
			# set the player name
			# N.B: CHAR cap seems to be 160 chars
			code = colour_text(text)
			return commands[cmd].format(newname=code)

		if cmd == "[rname]":
			# set the player name from random list
			# NB: Your name is longer than 127 chars! It has been truncated issue.
			time = 10
			out = []
			l = list(names.values())
			random.shuffle(l)
			for name in l:
				key = random.choice(list(colours.keys()))
				code = colour_text(name, colour=colours[key])
				out.append(f"defer {str(time)} \"say [*]New Name: {name} ; name {code}\";")
				time += 30
			done = " ".join(out)
			return commands[cmd].format(tmp=done)

		if cmd == "[kname]":
			# Stop all defers to name changes, needed on exit
			# add finally block for that.
			return commands[cmd]

		if cmd == "[trans]":
			# translate a message
			try:
				c,l,t = clean.split(":")
				msg = translate_msg(t, l)
				code = colour_text(str(msg))
				return commands[cmd].format(msg=code)
			except ValueError:
				return "say ^1[ERROR] Try: [trans]:language:Text here..."

		if cmd == "[test]":
			# few bits for testing
			# return "say 卂 乃 匚 ᗪ 乇 千 Ꮆ 卄 丨 ﾌ Ҝ ㄥ 爪 几 ㄖ 卩 Ɋ 尺 丂 ㄒ ㄩ ᐯ 山 乂 ㄚ 乙"
			st = ["^5|\---/|","^5| ^1o^6_^1o ^5|","^5 \_^6^^^5_/"]
			return commands[cmd].format(msg=f"say {st[0]} ; defer 1 \"say {st[1]}\" ; defer 4 \"say {st[2]}\"")

		if cmd == "[font]":
			toggle_font()
			fc = ""
			if FONT is True:
				fc = "^2"
			else:
				fc = "^1"
			return commands[cmd].format(fc=fc, FONT=FONT)

		if cmd == "[random]":
			make_random_codes()
			set_colour("[random]")
			return f"say {cmd} ^1COLOUR: ^2OK; say [info] 30 New Random Codes Made."

	if cmd in cols:
		set_colour(cmd)
		return f"say {cmd} ^1COLOUR: ^2OK"

	else:
		msg = colour_text(cmd)
		return f"say [MSG]: {msg}"


if __name__ == "__main__":
	set_colour('[rain]')
	app.run(debug=True)


# EOF
