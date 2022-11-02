mtr = {
    "A": "ા",
    "I": "ી",
    "LR": "ૢ",
    "LRR": "ૣ",
    "R": "ૃ",
    "RR": "ૄ",
    "U": "ૂ",
    "a": "",
    "ai": "ૈ",
    "aiI": "ૅ",
    "au": "ૌ",
    "auU": "ૉ",
    "e": "ે",
    "i": "િ",
    "o": "ો",
    "u": "ુ",
}

m = {
    "range": [[0xA80, 0xAFF]],
    "sa": 0,
    # अ, आ, ऐ, औ
    "a": {
        "a": ["અ", "", "aiu", 0],
        "ai": ["ઐ", mtr["ai"], "I", 0],
        "aiI": ["ઍ", mtr["aiI"], "", 0],
        "au": ["ઔ", mtr["au"], "U", 0],
        "auU": ["ઑ", mtr["auU"], "", 0],
    },
    # आ, ॐ
    "A": {
        "A": ["આ", mtr["A"], "U", 0],
        "AU": ["", "M", 2],
        "AUM": ["ૐ", "", 2],
    },
    # इ, ई
    "i": {"i": ["ઇ", mtr["i"], "i", 0]},
    # ई, ऌ, ॡ
    "I": {"I": ["ઈ", mtr["I"], "", 0]},
    # उ, ऊ
    "u": {"u": ["ઉ", mtr["u"], "u", 0]},
    # ऊ
    "U": {"U": ["ઊ", mtr["U"], "", 0]},
    # ए, ऐ
    "e": {"e": ["એ", mtr["e"], "e", 0]},
    # ओ, औ
    "o": {"o": ["ઓ", mtr["o"], "o", 0]},
    # ऋ, ॠ
    "R": {
        "R": ["ઋ", mtr["R"], "R", 0],
        "RR": ["ૠ", mtr["RR"], "", 0],
    },
    # # क वर्ग
    "k": {"k": ["ક", "h", 1], "kh": ["ખ", "", 1]},
    "g": {"g": ["ગ", "h", 1], "gh": ["ઘ", "", 1]},
    "G": {"G": ["ઙ", "", 1]},
    # च वर्ग
    "C": {"C": ["ચ", "h", 1], "Ch": ["છ", "", 1]},
    "j": {"j": ["જ", "h", 1], "jh": ["ઝ", "", 1]},
    "Y": {"Y": ["ઞ", "", 1]},
    # त वर्ग
    "t": {"t": ["ત", "h", 1], "th": ["થ", "", 1]},
    "d": {"d": ["દ", "h", 1], "dh": ["ધ", "", 1]},
    "n": {"n": ["ન", "", 1]},
    # ट वर्ग
    "T": {"T": ["ટ", "h", 1], "Th": ["ઠ", "", 1]},
    "D": {"D": ["ડ", "h", 1], "Dh": ["ઢ", "", 1]},
    "N": {"N": ["ણ", "", 1]},
    # प वर्ग
    "p": {"p": ["પ", "h", 1], "ph": ["ફ", "", 1]},
    "b": {"b": ["બ", "h", 1], "bh": ["ભ", "", 1]},
    "m": {"m": ["મ", "", 1]},
    # अन्तस्थ व्यञ्जन
    "y": {"y": ["ય", "", 1]},
    "v": {"v": ["વ", "", 1]},
    "r": {"r": ["ર", "", 1]},
    "l": {"l": ["લ", "", 1]},
    # ऊष्ण व्यञ्जन
    "h": {"h": ["હ", "", 1]},
    "s": {"s": ["સ", "h", 1], "sh": ["શ", "h", 1], "shh": ["ષ", "", 1]},
    "S": {"S": ["S", "h", 2], "Sh": ["ષ", "", 1]},
    # अन्योविशिष्टश्च
    "L": {
        "L": ["ળ", "R", 1],
        "LR": ["ઌ", mtr["LR"], "R", 0],
        "LRR": ["ૡ", mtr["LRR"], "", 0],
    },
    "M": {"M": ["ં", "M", 2], "MM": ["ઁ", "", 2]},
    "H": {"H": ["ઃ", "", 2]},
    "$": {"$": ["$", "$", 2], "$$": ["₹", "", 2]},
    "Q": {"Q": ["॰", "Q", 2], "QQ": ["ઽ", "", 2]},
    "q": {"q": ["q", "q", 2], "qq": ["્", "", 2]},
    ".": {
        ".": ["।", ".1234567890azAiIuUeoRL", 2],
        "..": ["॥", "", 2],
        ".0": ["০", "", 2],
        ".z": ["઼", "", 2],
        ".1": ["૧", "", 2],
        ".2": ["૨", "", 2],
        ".3": ["૩", "", 2],
        ".4": ["૪", "", 2],
        ".5": ["૫", "", 2],
        ".6": ["૬", "", 2],
        ".7": ["૭", "", 2],
        ".8": ["૮", "", 2],
        ".9": ["૯", "", 2],
        ".a": ["", "aiu", 2],
        ".i": ["", "i", 2],
        ".ai": ["", "I", 2],
        ".aiI": [mtr["aiI"], "", 2],
        ".au": ["", "U", 2],
        ".auU": [mtr["auU"], "", 2],
        ".u": ["", "u", 2],
        ".e": ["", "e", 2],
        ".o": ["", "o", 2],
        ".L": [".L", "R", 2],
        ".LR": ["", "R", 2],
        ".R": ["", "R", 2],
    },
}