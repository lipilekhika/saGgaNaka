mtr = {
    "A": "ා",
    "E": "ේ",
    "I": "ී",
    "LR": "ෟ",
    "LRR": "ෳ",
    "O": "ෝ",
    "O1": "ෝ",
    "O2": "ෝ",
    "R": "ෘ",
    "RR": "ෲ",
    "U": "ූ",
    "a": "",
    "ai": "ෛ",
    "aiI": "ැ",
    "au": "ෞ",
    "au1": "ෞ",
    "auU": "ෑ",
    "e": "ෙ",
    "i": "ි",
    "o": "ො",
    "o1": "ො",
    "u": "ු",
}

m = {
    "range": [[0xD80, 0xDFF]],
    "sa": 1,
    # अ, आ, ऐ, औ
    "a": {
        "a": ["අ", "", "aiu", 0],
        "ai": ["ඓ", mtr["ai"], "I", 0],
        "au": ["ඖ", mtr["au"], "U", 0],
        "aiI": ["ඇ", mtr["aiI"], "", 0],
        "auU": ["ඈ", mtr["auU"], "", 0],
    },
    # आ, ॐ
    "A": {
        "A": ["ආ", mtr["A"], "U", 0],
        "AU": ["", "M", 2],
        "AUM": ["ॐ", "", 2],
    },
    # इ, ई
    "i": {"i": ["ඉ", mtr["i"], "i", 0]},
    # ई, ऌ, ॡ
    "I": {"I": ["ඊ", mtr["I"], "", 0]},
    # उ, ऊ
    "u": {"u": ["උ", mtr["u"], "u", 0]},
    # ऊ
    "U": {"U": ["ඌ", mtr["U"], "", 0]},
    # ए, ऐ
    "e": {"e": ["එ", mtr["e"], "e", 0]},
    # ऐ
    "E": {"E": ["ඒ", mtr["E"], "", 0]},
    # ओ, औ
    "o": {"o": ["ඔ", mtr["o"], "o", 0]},
    # औ
    "O": {"O": ["ඕ", mtr["O"], "", 0]},
    # ऋ, ॠ
    "R": {
        "R": ["ඍ", mtr["R"], "R", 0],
        "RR": ["ඎ", mtr["RR"], "", 0],
    },
    # # क वर्ग
    "k": {"k": ["ක", "h", 1], "kh": ["ඛ", "", 1]},
    "g": {"g": ["ග", "h", 1], "gh": ["ඝ", "", 1]},
    "G": {"G": ["ඞ", "1", 1], "G1": ["ඟ", "", 1]},
    # # च वर्ग
    "C": {"C": ["ච", "h", 1], "Ch": ["ඡ", "", 1]},
    "j": {"j": ["ජ", "1h", 1], "jh": ["ඣ", "", 1], "j1": ["ඥ", "", 1]},
    "J": {"J": ["ඤ", "1", 1], "J1": ["ඦ", "", 1]},
    "Y": {"Y": ["ඤ", "1", 1], "Y1": ["ඦ", "", 1]},
    # त वर्ग
    "t": {"t": ["ත", "h", 1], "th": ["ථ", "", 1]},
    "d": {"d": ["ද", "h", 1], "dh": ["ධ", "", 1]},
    "n": {"n": ["න", "z", 1], "nz": ["ඳ", "", 1]},
    # ट वर्ग
    "T": {"T": ["ට", "h", 1], "Th": ["ඨ", "", 1]},
    "D": {"D": ["ඩ", "h", 1], "Dh": ["ඪ", "", 1]},
    "N": {"N": ["ණ", "z", 1], "Nz": ["ඬ", "", 1]},
    # प वर्ग
    "p": {"p": ["ප", "h", 1], "ph": ["ඵ", "z", 1], "phz": ["ෆ", "", 1]},
    "b": {"b": ["බ", "h", 1], "bh": ["භ", "", 1]},
    "f": {"f": ["", "z", 1], "fz": ["ෆ", "", 1]},
    "m": {"m": ["ම", "z", 1], "mz": ["ඹ", "", 1]},
    # अन्तस्थ व्यञ्जन
    "y": {"y": ["ය", "", 1]},
    "v": {"v": ["ව", "", 1]},
    "r": {"r": ["ර", "", 1]},
    "l": {"l": ["ල", "", 1]},
    # ऊष्ण व्यञ्जन
    "h": {"h": ["හ", "", 1]},
    "s": {"s": ["ස", "h", 1], "sh": ["ශ", "h", 1], "shh": ["ෂ", "", 1]},
    "S": {"S": ["S", "h", 2], "Sh": ["ෂ", "", 1]},
    "L": {
        "L": ["ළ", "R", 1],
        "LR": ["ඏ", mtr["LR"], "R", 0],
        "LRR": ["ඐ", mtr["LRR"], "", 0],
    },
    "M": {"M": ["ං", "M", 2], "MM": ["ઁ", "", 2]},
    "H": {"H": ["ඃ", "", 2]},
    "$": {"$": ["$", "$", 2], "$$": ["₹", "", 2]},
    "Q": {"Q": ["॰", "Q", 2], "QQ": ["ಽ", "", 2]},
    "q": {"q": ["q", "q", 2], "qq": ["්", "", 2]},
    ".": {
        ".": ["।", ".1234567890aAiIuUeEoORL", 2],
        "..": ["॥", "", 2],
        ".0": ["෦", "", 2],
        ".1": ["෧", "", 2],
        ".2": ["෨", "", 2],
        ".3": ["෩", "", 2],
        ".4": ["෪", "", 2],
        ".5": ["෫", "", 2],
        ".6": ["෬", "", 2],
        ".7": ["෭", "", 2],
        ".8": ["෮", "", 2],
        ".9": ["෯", "", 2],
        ".a": ["", "aiu", 2],
        ".i": ["", "i", 2],
        ".u": ["", "u", 2],
        ".e": ["", "e", 2],
        ".o": ["", "o", 2],
        ".ai": ["", "I", 2],
        ".aiI": [mtr["aiI"], "", 2],
        ".au": ["", "U", 2],
        ".auU": [mtr["auU"], "", 2],
        ".L": [".L", "R", 2],
        ".LR": ["", "R", 2],
        ".R": ["", "R", 2],
    },
}
