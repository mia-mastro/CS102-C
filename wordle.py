import random

words = {
  "word0": "ABACK", "word1": "ABOUT", "word2": "ACORN", "word3": "ADULT", "word4": "AFIRE",
  "word5": "AGENT", "word6": "ALERT", "word7": "ALIVE", "word8": "AMAZE", "word9": "ANGER",
  "word10": "ANGLE", "word11": "ANVIL", "word12": "APPLE", "word13": "ARBOR", "word14": "ARENA",
  "word15": "ARGUE", "word16": "ARMOR", "word17": "ARRAY", "word18": "ASCOT", "word19": "ASHEN",
  "word20": "ASKEW", "word21": "ASSET", "word22": "ATOLL", "word23": "ATTIC", "word24": "AUDIO",
  "word25": "AWARD", "word26": "AWFUL", "word27": "AXIAL", "word28": "AZURE",

  "word29": "BACON", "word30": "BADGE", "word31": "BAGEL", "word32": "BASIL", "word33": "BATCH",
  "word34": "BEACH", "word35": "BEAST", "word36": "BEGIN", "word37": "BLANK", "word38": "BLEND",
  "word39": "BLOCK", "word40": "BLOOD", "word41": "BOARD", "word42": "BOOST", "word43": "BOOTH",
  "word44": "BRAIN", "word45": "BRAND", "word46": "BREAD", "word47": "BREAK", "word48": "BRIEF",
  "word49": "BRING", "word50": "BROAD", "word51": "BROWN", "word52": "BUILD", "word53": "BUILT",

  "word54": "CABIN", "word55": "CABLE", "word56": "CAIRN", "word57": "CAMEL", "word58": "CANDY",
  "word59": "CANOE", "word60": "CARGO", "word61": "CARRY", "word62": "CATCH", "word63": "CATER",
  "word64": "CAUSE", "word65": "CEASE", "word66": "CEDAR", "word67": "CELLO", "word68": "CHAIN",
  "word69": "CHAIR", "word70": "CHALK", "word71": "CHART", "word72": "CHASE", "word73": "CHEAP",
  "word74": "CHEER", "word75": "CHEST", "word76": "CHILD", "word77": "CHILL", "word78": "CHINA",
  "word79": "CHOSE", "word80": "CIDER", "word81": "CIGAR", "word82": "CINCH", "word83": "CIVIC",

  "word84": "CLAIM", "word85": "CLAMP", "word86": "CLASH", "word87": "CLASS", "word88": "CLEAN",
  "word89": "CLEAR", "word90": "CLICK", "word91": "CLOCK", "word92": "CLOUD", "word93": "CLOUT",
  "word94": "CLONE", "word95": "CLOTH", "word96": "CLOWN", "word97": "COBRA", "word98": "COAST",
  "word99": "COCOA", "word100": "COMIC", "word101": "CORAL", "word102": "COUNT", "word103": "COVER",

  "word104": "DAILY", "word105": "DAISY", "word106": "DANCE", "word107": "DANDY", "word108": "DEALT",
  "word109": "DEATH", "word110": "DEBUT", "word111": "DECAY", "word112": "DELTA", "word113": "DEMON",
  "word114": "DENIM", "word115": "DENSE", "word116": "DEPTH", "word117": "DERBY", "word118": "DEVIL",
  "word119": "DIARY", "word120": "DIGIT", "word121": "DINER", "word122": "DINGO", "word123": "DIVER",
  "word124": "DOUBT", "word125": "DOZEN", "word126": "DRAFT", "word127": "DRAIN", "word128": "DRAMA",
  "word129": "DREAR", "word130": "DRESS", "word131": "DRILL", "word132": "DRINK", "word133": "DRIVE",
  "word134": "DROVE", "word135": "DYING",

  "word136": "EAGER", "word137": "EAGLE", "word138": "EARLY", "word139": "EARTH", "word140": "EASEL",
  "word141": "EATEN", "word142": "EATER", "word143": "EBONY", "word144": "EERIE", "word145": "EGRET",
  "word146": "EIGHT", "word147": "ELATE", "word148": "ELBOW", "word149": "ELDER", "word150": "ELECT",
  "word151": "ELITE", "word152": "EMAIL", "word153": "EMBER", "word154": "EMPTY", "word155": "ENEMY",
  "word156": "ENJOY", "word157": "ENNUI", "word158": "ENTER", "word159": "ENTRY", "word160": "EQUAL",
  "word161": "ERGON", "word162": "ERASE", "word163": "ERECT", "word164": "ERROR", "word165": "EVENT",
  "word166": "EXACT", "word167": "EXALT", "word168": "EXCEL", "word169": "EXIST", "word170": "EXULT",

  "word171": "FAINT", "word172": "FAIRY", "word173": "FAITH", "word174": "FANCY", "word175": "FARCE",
  "word176": "FATAL", "word177": "FAULT", "word178": "FAVOR", "word179": "FEAST", "word180": "FEIGN",
  "word181": "FENCE", "word182": "FERAL", "word183": "FERRY", "word184": "FETCH", "word185": "FETID",
  "word186": "FETUS", "word187": "FEVER", "word188": "FIELD", "word189": "FIEND", "word190": "FIERY",
  "word191": "FIFTH", "word192": "FIGHT", "word193": "FINAL", "word194": "FINCH", "word195": "FIRST",
  "word196": "FISHY", "word197": "FIXER", "word198": "FIZZY",

  "word199": "GAFFE", "word200": "GAMER", "word201": "GAMMA", "word202": "GAUNT", "word203": "GAUZE",
  "word204": "GAVEL", "word205": "GAWKY", "word206": "GEESE", "word207": "GENIE", "word208": "GENRE",
  "word209": "GHOST", "word210": "GIANT", "word211": "GIDDY", "word212": "GIVEN", "word213": "GIVER",
  "word214": "GLADE", "word215": "GLAND", "word216": "GLARE", "word217": "GLASS", "word218": "GLEAM",
  "word219": "GLIDE", "word220": "GLINT", "word221": "GLOAT", "word222": "GLOBE", "word223": "GLOOM",
  "word224": "GLORY", "word225": "GLOSS", "word226": "GLOVE", "word227": "GNASH", "word228": "GNOME",

  "word229": "HABIT", "word230": "HAIRY", "word231": "HALVE", "word232": "HANDY", "word233": "HAPPY",
  "word234": "HASTE", "word235": "HASTY", "word236": "HATCH", "word237": "HATER", "word238": "HAUNT",
  "word239": "HAVEN", "word240": "HAVOC", "word241": "HAZEL", "word242": "HEADY", "word243": "HEART",
  "word244": "HEATH", "word245": "HEAVE", "word246": "HEAVY", "word247": "HEDGE", "word248": "HEFTY",
  "word249": "HELIX", "word250": "HELLO", "word251": "HENCE", "word252": "HYENA", "word253": "HUMOR",

  "word254": "ICING", "word255": "IDEAL", "word256": "IDIOM", "word257": "IDLER", "word258": "IMAGE",
  "word259": "IMBUE", "word260": "IMPEL", "word261": "INBOX", "word262": "INDEX", "word263": "INFER",
  "word264": "INGOT", "word265": "INLET", "word266": "INNER", "word267": "INPUT", "word268": "INTRO",
  "word269": "IONIC", "word270": "IRATE", "word271": "IRONY",

  "word272": "JAUNT", "word273": "JAZZY", "word274": "JELLY", "word275": "JERKY", "word276": "JETTY",
  "word277": "JEWEL", "word278": "JIFFY", "word279": "JOINT", "word280": "JOLLY", "word281": "JUDGE",
  "word282": "JUICE", "word283": "JUICY",

  "word284": "KARMA", "word285": "KAYAK", "word286": "KEBAB", "word287": "KIOSK", "word288": "KITTY",
  "word289": "KNACK", "word290": "KNAVE", "word291": "KNEAD", "word292": "KNEEL", "word293": "KNIFE",

  "word294": "LABEL", "word295": "LAGER", "word296": "LANCE", "word297": "LAPEL", "word298": "LARGE",
  "word299": "LASSO", "word300": "LATCH", "word301": "LAUGH", "word302": "LAYER", "word303": "LEAFY",
  "word304": "LEAPT", "word305": "LEARN", "word306": "LEASE", "word307": "LEAST", "word308": "LEAVE",
  "word309": "LEDGE", "word310": "LEGAL", "word311": "LEMON", "word312": "LEMUR", "word313": "LEPER",
  "word314": "LEVEL",

  "word315": "MACAW", "word316": "MADAM", "word317": "MADLY", "word318": "MAFIA", "word319": "MAGIC",
  "word320": "MAGMA", "word321": "MAJOR", "word322": "MAKER", "word323": "MAMBO", "word324": "MANGO",
  "word325": "MANIC", "word326": "MAPLE", "word327": "MARCH", "word328": "MARRY", "word329": "MASON",
  "word330": "MATCH", "word331": "MAYBE", "word332": "MEALY", "word333": "MEANT", "word334": "MECCA",
  "word335": "MEDAL", "word336": "MEDIA", "word337": "MELEE", "word338": "MELON", "word339": "MERGE",

  "word340": "NARLY", "word341": "NERVE", "word342": "NINTH", "word343": "NOBLE", "word344": "NURSE",
  "word345": "NYMPH", "word346": "OAKEN", "word347": "OCCUR", "word348": "OCEAN", "word349": "OCTET",
  "word350": "ODDER", "word351": "OPINE", "word352": "ORBIT", "word353": "OTHER", "word354": "OUGHT",
  "word355": "OVARY", "word356": "OVATE", "word357": "PAINT", "word358": "PANEL", "word359": "PANSY",
  "word360": "PAPER", "word361": "PENCE", "word362": "PEONY", "word363": "PERKY", "word364": "PIVOT",
  "word365": "PIXEL", "word366": "PLANT", "word367": "PLATE", "word368": "PLUMP", "word369": "POINT",
  "word370": "PRIME", "word371": "PROUD", "word372": "PROVE",

  "word373": "QUAIL", "word374": "QUARK", "word375": "QUASH",

  "word376": "RADAR", "word377": "RALLY", "word378": "RANGE", "word379": "RAPID", "word380": "RATIO",
  "word381": "RECAP", "word382": "REBAR", "word383": "RECUR", "word384": "RENAL", "word385": "RENEW",
  "word386": "REPLY", "word387": "RESET", "word388": "RIDER", "word389": "RIGID", "word390": "RIVAL",
  "word391": "RIVER", "word392": "ROAST", "word393": "ROVER", "word394": "ROWDY",

  "word395": "SALSA", "word396": "SASSY", "word397": "SAUCE", "word398": "SCAMP", "word399": "SCARF",
  "word400": "SCENE", "word401": "SCOOP", "word402": "SCOUR", "word403": "SCOWL", "word404": "SCRUB",
  "word405": "SHACK", "word406": "SHAKE", "word407": "SHARD", "word408": "SHAVE", "word409": "SHEIK",
  "word410": "SHEEP", "word411": "SHEER", "word412": "SHEET", "word413": "SHIFT", "word414": "SHOCK",
  "word415": "SHOOT", "word416": "SHORT", "word417": "SHRUB", "word418": "SIGHT", "word419": "SIGMA",

  "word420": "TABOO", "word421": "TAINT", "word422": "TALLY", "word423": "TANGO", "word424": "TAPER",
  "word425": "TEARY", "word426": "TEASE", "word427": "TENET", "word428": "TENSE", "word429": "THIRD",
  "word430": "THORN", "word431": "THOSE", "word432": "THROW", "word433": "THUMB", "word434": "TIGHT",
  "word435": "TOAST", "word436": "TOPAZ", "word437": "TOTAL", "word438": "TOXIC", "word439": "TRACE",

  "word440": "ULTRA", "word441": "UNCUT", "word442": "UNDUE", "word443": "UNITY", "word444": "UNLIT",
  "word445": "UNSET", "word446": "UNTIE", "word447": "UPPER", "word448": "UPSET", "word449": "URBAN",

  "word450": "VAGUE", "word451": "VAULT", "word452": "VAPID", "word453": "VAUNT", "word454": "VENOM",
  "word455": "VERSE", "word456": "VIGOR", "word457": "VIVID",

  "word458": "WAGON", "word459": "WAIVE", "word460": "WALTZ", "word461": "WARTY", "word462": "WASTE",
  "word463": "WATCH", "word464": "WEIRD", "word465": "WHARF", "word466": "WHEAT", "word467": "WHIFF",
  "word468": "WHITE", "word469": "WHOLE", "word470": "WIDOW", "word471": "WISPY", "word472": "WOMAN",

  "word473": "YACHT", "word474": "YEARLY", "word475": "YEAST", "word476": "YIELD", "word477": "YOUNG",

  "word478": "ZEBRA", "word479": "ZESTY", "word480": "ZONAL", "word481": "ZIPPY"
}


attempt = 1

to_guess = random.randint(0, 481)

word_to_guess = words.get(f"word{to_guess}", 0)

letters_guessed = {}

total_guessed = {}

correct_letters = {0 : word_to_guess[0], 1 : word_to_guess[1], 2 : word_to_guess[2], 3 : word_to_guess[3], 4 : word_to_guess[4]}

while attempt <= 6:
	print(f"Attempt {attempt}/6")
	guess = input("Enter your guess: ").upper()
	if guess in words.values():
		letters_guessed = {0 : guess[0], 1 : guess[1], 2 : guess[2], 3 : guess[3], 4 : guess[4]}
		display_guess = []
		for i in range(5):
			display_guess.append(letters_guessed[i])
		print("  ".join(display_guess))
		results = []
		for i in range(5):
			if(letters_guessed[i] == correct_letters[i]):
				results.append("🟩")
			elif(letters_guessed[i] in correct_letters.values()):
				results.append("🟨")
			else:
				results.append("⬜️")
		print(" ".join(results))
		attempt = attempt + 1
		print("\n\n")
		end = 0
		for i in range(5):
			if(results[i] == "🟩"):
				end = end + 1		
		if end == 5:
			print("Correct!\n")
			break
print(f"The correct word was", word_to_guess)
