#!/usr/bin/python3
#
# Shazza-Works
#
# set of do something commands
commands = {
	"[help]": "say ^1COMMAND ^7[help] <> ^2OK ; say ^4{helpa} ; defer 3 \"say ^4{helpb}",
	"[joke]": "say [*]^1COMMAND ^7[joke] <> ^2OK ; say ^5{joke}",
	"[who]": "say [*]^1COMMAND ^7[who] <> ^2OK ; say ^1Shazza^7-^4Works^7, Using a little ^xf00P^xf40y^xf70t^xfa0h^xef0o^xbf0n ^x2f03^x0f03^x0f2.^x0f91^x0fd0^x0df.^x09f6 ^7and ^6Flask",
	"[search]": "say ^1COMMAND ^7[search] <> ^2OK ; say ^2Word^7:{word} ^2Info^7: ^1{search}",
	"[name]": "say [*]^1COMMAND ^7[name] {newname} <> ^2OK ; name {newname}",
	"[rname]": "{tmp}",
	#"[rname]": "say [*]^1COMMAND ^7[rname] {newname} <> ^2OK ; name {newname}",
	"[nade]": "say [*]^1COMMAND ^7[nade] {num}: {name} <> ^2OK ; cl_nade_type {num}",
	"[trans]": "say [*]^1TRS: {msg}",
	"[tell]": "say [*]^1COMMAND ^7[tell] #{num} <> ^2OK ; tell {num} {msg}",
	"[font]": "say [*]^1COMMAND ^7[font] {fc}{FONT} ^7<> ^2OK",
	"[test]": "{msg}"
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


nades = {
	"1": "Normal",
	"2": "Napalm",
	"3": "Nitro",
	"4": "Translocate",
	"5": "Spawn",
	"6": "Heal",
	"7": "PokeYaBum",
	"8": "Entrap",
	"9": "Veil",
	"10": "Ammo",
	"11": "Darkness",
	}


names = {
	1: 'shaquille.oatmeal',
	2: 'hanging_with_my_gnomies',
	3: 'hoosier-daddy',
	4: 'fast_and_the_curious',
	5: 'averagestudent',
	6: 'BadKarma',
	7: 'google_was_my_idea',
	8: 'cute.as.ducks',
	9: 'casanova',
	10: 'real_name_hidden',
	11: 'HairyPoppins',
	12: 'fedora_the_explorer',
	13: 'OP_rah',
	14: 'YellowSnowman',
	15: 'Joe Not Exotic',
	16: 'username_copied',
	17: 'whos_ur_buddha',
	18: 'unfinished_sentenc',
	19: 'AllGoodNamesRGone',
	20: 'Something',
	21: 'me_for_president',
	22: 'tinfoilhat',
	23: 'oprahwindfury',
	24: 'anonymouse',
	25: 'Definitely_not_an_athlete',
	26: 'HeartTicker',
	27: 'YESIMFUNNY',
	28: 'BenAfleckIsAnOkActor',
	29: 'magicschoolbusdropout',
	30: 'Everybody',
	31: 'regina_phalange',
	32: 'PawneeGoddess',
	33: 'pluralizes_everythings',
	34: 'chickenriceandbeans',
	35: 'test_name_please_ignore',
	36: 'IYELLALOT',
	37: 'heyyou',
	38: 'laugh_till_u_pee',
	39: 'aDistraction',
	40: 'crazy_cat_lady',
	41: 'banana_hammock',
	42: 'thegodfatherpart4',
	43: 'unfriendme',
	44: 'babydoodles',
	45: 'fluffycookie',
	46: 'buh-buh-bacon',
	47: 'ashley_said_what',
	48: 'LactoseTheIntolerant',
	49: 'ManEatsPants',
	50: 'Twentyfourhourpharmacy',
	51: 'applebottomjeans',
	52: 'Babushka',
	53: 'toastedbagelwithcreamcheese',
	54: 'baeconandeggz',
	55: 'FartinLutherKing',
	56: 'coolshirtbra',
	57: 'kentuckycriedfricken',
	58: 'REVERANDTOAST',
	59: 'kim_chi',
	60: 'idrinkchocolatemilk',
	61: 'SaintBroseph',
	62: 'chin_chillin',
	63: 'ghostfacegangsta',
	64: 'bigfootisreal',
	65: 'santas_number1_elf',
	67: 'thehornoftheunicorn',
	68: 'iNeed2p',
	69: 'abductedbyaliens',
	70: 'actuallynotchrishemsworth',
	71: 'nachocheesefries',
	72: 'personallyvictimizedbyreginageorge',
	73: 'just-a-harmless-potato',
	74: 'FrostedCupcake',
	75: 'Avocadorable',
	76: 'fatBatman',
	77: 'quailandduckeggs',
	78: 'PaniniHead',
	79: 'mandymooressingingvoice',
	80: 'catsordogs',
	81: 'FartnRoses',
	82: 'RedMonkeyButt',
	83: 'FreddyMercurysCat',
	84: 'MasterCheif',
	85: 'FreeHugz',
	86: 'ima.robot',
	87: 'actuallythedog',
	88: 'notthetigerking',
	89: 'pixie_dust',
	90: 'ChopSuey',
	91: 'turkey_sandwich',
	92: 'B.Juice',
	93: 'Chris_P_Bacon',
	94: 'LtDansLegs',
	95: 'WookiesrPpl2',
	96: 'hogwartsfailure',
	97: 'CourtesyFlush',
	98: 'MomsSpaghetti',
	99: 'spongebobspineapple',
	100: 'garythesnail',
	101: 'nothisispatrick',
	102: 'CountSwagula',
	103: 'SweetP',
	104: 'PNUT',
	105: 'Snax',
	106: 'Nuggetz',
	107: 'colonel_mustards_rope',
	108: 'baby_bugga_boo',
	109: 'joancrawfordfanclub',
	110: 'fartoolong',
	111: 'loliateyourcat',
	112: 'rawr_means_iloveyou',
	113: 'ihavethingstodo.jpg',
	114: 'heresWonderwall',
	115: 'UFO_believer',
	116: 'ihazquestion',
	117: 'SuperMagnificentExtreme',
	118: 'It’s_A _Political_ Statement',
	119: 'TheAverageForumUser',
	120: 'just_a_teen',
	121: 'OmnipotentBeing',
	122: 'GawdOfROFLS',
	123: 'loveandpoprockz',
	124: '2_lft_feet',
	125: 'Bread Pitt',
	126: 'rejectedbachelorcontestant',
	127: 'Schmoople',
	128: 'LOWERCASE GUY',
	129: 'Unnecessary',
	130: 'joan_of_arks_angel',
	131: 'InstaPrincess',
	132: 'DroolingOnU',
	133: 'Couldnt_Find_Good_Name',
	134: 'AngelWonderland',
	135: 'Born-confused',
	136: 'SargentSaltNPepa',
	137: 'DosentAnyoneCare',
	138: 'quaratineinthesejeans',
	139: 'thanoslefthand',
	140: 'ironmansnap',
	141: 'chalametbmybae',
	142: 'peterparkerspuberty',
	143: 'severusvape',
	144: 'theotherharrypotter',
	145: 'GrangerDanger',
	146: 'BlueIvysAssistant',
	147: 'Ariana_Grandes_Ponytail',
	148: 'HotButteryPopcorn',
	149: 'MelonSmasher',
	150: 'morgan_freeman_but_not',
	151: 'potatoxchipz',
	152: 'FoxtrotTangoLove',
	153: 'ElfishPresley',
	154: 'WustacheMax',
	155: 'JuliusSeizure',
	156: 'HeyYouNotYouYou',
	157: 'OneTonSoup',
	158: 'HoneyLemon',
	159: 'LoveMeKnot',
	160: 'Bud Lightyear',
	161: 'takenbyWine',
	162: 'taking0ver',
	163: 'Unic0rns',
	164: 'in_jail_out_soon',
	165: 'hotgirlbummer',
	166: 'behind_you',
	167: 'itchy_and_scratchy',
	168: 'not_james_bond',
	169: 'a_collection_of_cells',
	170: 'CowabungaDude',
	171: 'TeaBaggins',
	172: 'bill_nye_the_russian_spy',
	173: 'intelligent_zombie',
	174: 'imma_rage_quit',
	175: 'kiss-my-axe',
	176: 'king_0f_dairy_queen',
	177: 'desperate_enuf',
	178: 'AirisWindy',
	179: 'cheeseinabag',
	180: 'MakunaHatata',
	181: 'rambo_was_real',
	182: 'churros4eva',
	183: 'namenotimportant',
	184: 'i_boop_ur_nose',
	185: 'image_not_uploaded',
	186: 'suck_my_popsicle',
	187: 'sofa_king_cool',
	188: 'RootinTootinPutin',
	189: 'blousesandhouses',
	190: 'iblamejordan',
	191: 'manic_pixie_meme_ girl',
	192: 'Technophyle',
	193: 'Cuddly-Wuddly',
	194: 'JesusoChristo',
	195: 'peap0ds',
	196: 'whats_ur_sign',
	197: 'TheMilkyWeigh',
	198: 'BabyBluez',
	199: 'BarbieBreath',
	200: 'MangoGoGo',
	201: 'DirtBag',
	202: 'FurReal',
	203: 'ScoobyCute',
	204: 'YouIntradouchingMyshelf',
	205: 'IwasReloading',
	206: 'WellEndowedPenguin',
	207: 'TheAfterLife',
	208: 'PuppiesnKittens',
	209: 'WakeAwake',
	210: 'Coronacosmo',
	211: 'wherearetheavocados',
	213: 'ijustwanttobeme',
	214: 'TheKidsCallMeBoss',
	215: 'SewerSquirrel',
	216: 'because.i.like.to.like',
	217: 'notmuchtoit',
	218: 'friedchocolate',
	219: 'DonWorryItsGonBK',
	220: 'Early_Morning_Coffee',
	221: 'drunkbetch',
	222: 'strawberry_pineapple',
	223: 'MissPiggysDimples',
	224: 'chickenbaconranchpizza',
	225: 'cereal_killer',
	226: 'khaleesisfourthdragon',
	227: 'darth.daenerys',
	228: 'LeslieKnopesBinder',
	229: 'BettyBoopsBoop',
	230: 'Freddie_Not_The_Fish',
	231: 'Billys_Mullet',
	232: 'Calzone_Zone',
	233: 'ChickyChickyParmParm',
	234: 'Adobo_Ahai',
	235: 'theoldRazzleDazzle',
	236: 'Not-Insync',
	237: 'Toiletpaperman',
	238: 'Reese WitherFork',
	239: 'LizzosFlute',
	240: 'Macauliflower Culkin',
	241: 'Llama del Rey',
	242: 'Hot Name Here',
	243: 'Carmelpoptart',
	245: 'notfunnyatall',
	246: 'Mangonificent',
	247: 'toastcrunch',
	248: 'fizzysodas',
	249: 'kokonuts',
	250: 'cherry-picked',
}

woman = r"""
     z$$$$$. $$
    $$$$$$$$$$$
   $$$$$$**$$$$             eeeeer
  $$$$$%   '$$$             $$$$$F
 4$$$$P     *$$             *$$$$F
 $$$$$      '$$    .ee.      ^$$$F            ..e.
 $$$$$       ""  .$$$$$$b     $$$F 4$$$$$$   $$$$$$c
4$$$$F          4$$$""$$$$    $$$F '*$$$$*  $$$P"$$$L
4$$$$F         .$$$F  ^$$$b   $$$F  J$$$   $$$$  ^$$$.
4$$$$F         d$$$    $$$$   $$$F J$$P   .$$$F   $$$$
4$$$$F         $$$$    3$$$F  $$$FJ$$P    4$$$"   $$$$
4$$$$F        4$$$$    4$$$$  $$$$$$$r    $$$$$$$$$$$$
4$$$$$        4$$$$    4$$$$  $$$$$$$$    $$$$********
 $$$$$        4$$$$    4$$$F  $$$F4$$$b   *$$$r
 3$$$$F       d$$$$    $$$$"  $$$F *$$$F  4$$$L     .
  $$$$$.     d$$$$$.   $$$$   $$$F  $$$$.  $$$$    z$P
   $$$$$e..d$$$"$$$b  4$$$"  J$$$L  '$$$$  '$$$b..d$$
    *$$$$$$$$$  ^$$$be$$$"  $$$$$$$  3$$$$F "$$$$$$$"
     ^*$$$$P"     *$$$$*    $$$$$$$   $$$$F  ^*$$$"
"""
#EOF#
