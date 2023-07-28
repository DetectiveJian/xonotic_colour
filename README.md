
Python colour code for Xonotic game chat using flask.

![Project Logo From I nternet](https://github.com/shazza-works/xonotic_colour/blob/main/logo.png)


# *Ubuntu / Mint etc... Linux Mint 21.1*
<details>
<summary>How to setup...</summary>

```bash
	sudo apt install python3-pip
	pip3 install -r requierments.txt
	python3 chat-server.py
```

### will show Flask Running @ 127.0.0.1 port 5000 then:
__NB: move chat-server.cfg to your game Xonotic/data__

> go to Xonotic and hit ` for game console

```
exec chat-server.cfg
```

__Hit 'o' for chat in colour__

</details>

# *Fedora Linux 38 (Workstation Edition) x86_64*
<details>
<summary>How to setup...</summary>

```bash
	sudo dnf install python3-pip
	pip3 install requirements.txt
	python3 chat-server.py
```

### will show Flask Running @ 127.0.0.1 port 5000 then:
__NB: move chat-server.cfg to your game Xonotic/data__

> go to Xonotic and hit ` for game console 

```
exec chat-server.cfg
```

__Hit 'o' for chat in colour__

</details>


# Commands:
<details>
<summary>Show the list of commands and how to use them.</summary>

| Command | Description |
| ---- | ---- |
| o | KEY 'o' is bound to new colour chat command, press to speak. |
| [help] | Sow the commands and colour list. |
| [who] | Show who made this app. |
| [font] | Switch on/off toggle fancy fonts with your message. |
| [joke] | Get a random joke from an api. |
| [test] | Used to do some testing... atm prints a cat on 3 lines. |
| [search]Word | Search for word referance, return results. |
| [name]Name | Change the player name to given string in set colour. |
| [trans]:lang:msg | Translate from english to given language, TRS:message in language. |

</details>

# Colours:
<details>
<summary>Show the list of colours.</summary>

+ [random]
+ [white]
+ [slayer]
+ [blur]
+ [google]`#4885ed` `#db3236` `#f4c20d` `#4885ed` `#3cba54` `#db3236` `#4885ed` `#db3236` `#f4c20d` `#4885ed` `#3cba54` `#db3236`
+ [sunset]
+ [grey]
+ [rain]
+ [night]
+ [yellow]
+ [red]
+ [fire]
+ [water]
+ [pink]
+ [ghost]
+ [tree]
+ [ting]
+ [spoon]
+ [tango]

__[*]You can add more to tools.py as you like.__

</details>


[1]
__"Please note i'm still adding things to this and it will change often."__

