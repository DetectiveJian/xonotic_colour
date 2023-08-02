
Python colour code for Xonotic game chat using flask.

![Project Logo From I nternet](https://github.com/shazza-works/xonotic_colour/blob/main/logo.png)


# *Ubuntu / Mint etc... Linux Mint 21.1*
<details>
<summary>How to setup...</summary>

Make sure python3, python3-venv & pip are installed on your system:
```
sudo apt install python3 python3-pip python3-venv
```

Clone the repo to your local machine:
```
git clone https://github.com/shazza-works/xonotic_colour.git
```

Move into the repo directory:
```
cd xonotic_colour
```

Setup a python virtual environment:
```
python3 -m venv .venv
```

Now activate the virtual environmet:
```
source .venv/bin/activate
```
> NOTE: to deactivate the virtual environment run:
`deactivate`

Update pip and install wheel package:
```
pip install --upgrade pip wheel
```

Now install the requirements:
```
pip install -r requirements.txt
```
Run the server with:
```
python3 chat-server.py
```

### will show Flask Running @ 127.0.0.1 port 5000 then:
__NB: move chat-server.cfg to your game Xonotic/data__

> go to Xonotic and hit ` for game console

```
exec chat-server.cfg
```

__Hit 'o' for chat in colour__

NOTE: If you want to use this app frequently, it is recommended to append "`exec chat-server.cfg`" to `autoexec.cfg` file in `~/.xonotic/data/autoexec.cfg`

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

# *ArchLinux*
<details>
<summary>How to setup...</summary>

Make sure python3 is installed on your system:
```
sudo pacman -S --needed python3
```

Clone the repo to your local machine:
```
git clone https://github.com/shazza-works/xonotic_colour.git
```

Move into the repo directory:
```
cd xonotic_colour
```

Setup a python virtual environment:
```
python3 -m venv .venv
```

Now activate the virtual environmet:
```
source .venv/bin/activate
```
> NOTE: to deactivate the virtual environment run:
`deactivate`

Update pip and install wheel package:
```
pip install --upgrade pip wheel
```

Now install the requirements:
```
pip install -r requirements.txt
```

Run the server with:
```
python3 chat-server.py
```

### will show Flask Running @ 127.0.0.1 port 5000 then:
__NB: move chat-server.cfg to your game Xonotic/data__

> go to Xonotic and hit ` for game console

```
exec chat-server.cfg
```

__Hit 'o' for chat in colour__

NOTE: If you want to use this app frequently, it is recommended to append "`exec chat-server.cfg`" to `autoexec.cfg` file in `~/.xonotic/data/autoexec.cfg`

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
| [tell]number | Tell a player a message by number `who` |
| [search]word | Search for word referance, return results. |
| [name]name | Change the player name to given string in set colour. |
| [rname] | Set a random player name from list every 60 sec. |
| [nade]number | Set Nade Type from 0-10 or show error. |
| [ids] | Show the ID's of seen API jokes. |
| [trans]:lang:msg | Translate from english to given language, TRS:message in language. |

</details>

# Colours:
<details>
<summary>Show the list of colours.</summary>

+ [random]
+ [white]
+ [slayer]
+ [blur]
+ [google]
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

__[*]You can add more sets or functions to tools.py as you like.__

</details>


[1]
__"Please note i'm still adding things to this and it will change often."__
[2]
__"Some of the functions have wait times of 1-3 sec due to chat flood filters in place and I have no way to change that!"__
