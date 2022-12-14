mtr = {
    "A": "ಾ",
    "E": "ೇ",
    "E1": "ೇ",
    "I": "ೀ",
    "I1": "ೀ",
    "LR": "ೢ",
    "LRR": "ೣ",
    "O": "ೋ",
    "O1": "ೋ",
    "O2": "ೋ",
    "R": "ೃ",
    "RR": "ೄ",
    "U": "ೂ",
    "a": "",
    "ai": "ೈ",
    "ai1": "ೈ",
    "au": "ೌ",
    "e": "ೆ",
    "i": "ಿ",
    "o": "ೊ",
    "o1": "ೊ",
    "u": "ು",
}

m = {
    "range": [[0xC80, 0xCFF]],
    "sa": 1,
    # अ, आ, ऐ, औ
    "a": {
        "a": ["ಅ", "", "aiu", 0],
        "ai": ["ಐ", mtr["ai"], "", 0],
        "au": ["ಔ", mtr["au"], "", 0],
    },
    # आ, ॐ
    "A": {
        "A": ["ಆ", mtr["A"], "U", 0],
        "AU": ["", "M", 2],
        "AUM": ["ಓಂ", "", 2],
    },
    # इ, ई
    "i": {"i": ["ಇ", mtr["i"], "i", 0]},
    # ई, ऌ, ॡ
    "I": {"I": ["ಈ", mtr["I"], "", 0]},
    # उ, ऊ
    "u": {"u": ["ಉ", mtr["u"], "u", 0]},
    # ऊ
    "U": {"U": ["ಊ", mtr["U"], "", 0]},
    # ए, ऐ
    "e": {"e": ["ಎ", mtr["e"], "e", 0]},
    # ऐ
    "E": {"E": ["ಏ", mtr["E"], "", 0]},
    # ओ, औ
    "o": {"o": ["ಒ", mtr["o"], "o", 0]},
    # औ
    "O": {"O": ["ಓ", mtr["O"], "", 0]},
    # ऋ, ॠ
    "R": {
        "R": ["ಋ", mtr["R"], "R", 0],
        "RR": ["ೠ", mtr["RR"], "", 0],
    },
    # # क वर्ग
    "k": {"k": ["ಕ", "h", 1], "kh": ["ಖ", "", 1]},
    "g": {"g": ["ಗ", "h", 1], "gh": ["ಘ", "", 1]},
    "G": {"G": ["ಙ", "", 1]},
    # च वर्ग
    "C": {"C": ["ಚ", "h", 1], "Ch": ["ಛ", "", 1]},
    "j": {"j": ["ಜ", "h", 1], "jh": ["ಝ", "", 1]},
    "Y": {"Y": ["ಞ", "", 1]},
    # त वर्ग
    "t": {"t": ["ತ", "h", 1], "th": ["ಥ", "", 1]},
    "d": {"d": ["ದ", "h", 1], "dh": ["ಧ", "", 1]},
    "n": {"n": ["ನ", "", 1]},
    # ट वर्ग
    "T": {"T": ["ಟ", "h", 1], "Th": ["ಠ", "", 1]},
    "D": {
        "D": ["ಡ", "hz", 1],
        "Dz": ["ಡ಼", "", 1],
        "Dh": ["ಢ", "z", 1],
        "Dhz": ["ಢ಼", "", 1],
    },
    "N": {"N": ["ಣ", "", 1]},
    # प वर्ग
    "p": {"p": ["ಪ", "h", 1], "ph": ["ಫ", "", 1]},
    "b": {"b": ["ಬ", "h", 1], "bh": ["ಭ", "", 1]},
    "m": {"m": ["ಮ", "", 1]},
    # अन्तस्थ व्यञ्जन
    "y": {"y": ["ಯ", "", 1]},
    "v": {"v": ["ವ", "", 1]},
    "r": {
        "r": ["ರ", "2z", 1],
        "rz": ["ಱ", "", 1],
        "r2": ["ಱ", "", 1],
    },
    "l": {"l": ["ಲ", "", 1]},
    # ऊष्ण व्यञ्जन
    "h": {"h": ["ಹ", "", 1]},
    "s": {"s": ["ಸ", "h", 1], "sh": ["ಶ", "h", 1], "shh": ["ಷ", "", 1]},
    "S": {"S": ["S", "h", 2], "Sh": ["ಷ", "", 1]},
    "z": {"z": ["z", "h", 2], "zh": ["ೞ", "", 1]},
    "L": {
        "L": ["ಳ", "zR", 1],
        "Lz": ["ೞ", "", 1],
        "LR": ["ಌ", mtr["LR"], "R", 0],
        "LRR": ["ೡ", mtr["LRR"], "", 0],
    },
    "M": {"M": ["ಂ", "M", 2], "MM": ["ಁ", "", 2]},
    "H": {"H": ["ಃ", "", 2]},
    "$": {"$": ["$", "$", 2], "$$": ["₹", "", 2]},
    "Q": {"Q": ["॰", "Q", 2], "QQ": ["ಽ", "", 2]},
    "q": {"q": ["q", "q", 2], "qq": ["್", "", 2]},
    ".": {
        ".": ["।", ".1234567890zaAiIuUeEoORL", 2],
        "..": ["॥", "", 2],
        ".z": ["಼", "", 2],
        ".0": ["೦", "", 2],
        ".1": ["೧", "", 2],
        ".2": ["೨", "", 2],
        ".3": ["೩", "", 2],
        ".4": ["೪", "", 2],
        ".5": ["೫", "", 2],
        ".6": ["೬", "", 2],
        ".7": ["೭", "", 2],
        ".8": ["೮", "", 2],
        ".9": ["೯", "", 2],
        ".a": ["", "aiu", 2],
        ".i": ["", "i", 2],
        ".u": ["", "u", 2],
        ".e": ["", "e", 2],
        ".o": ["", "o", 2],
        ".L": [".L", "R", 2],
        ".LR": ["", "R", 2],
        ".R": ["", "R", 2]
    },
    "#": {
        "#": ["#", "H", 2],
        "#H": ["ೱ", "1", 2],
        "#H1": ["ೲ", "", 2],
    },
}
