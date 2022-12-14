mtr = {}

m = {
    "sa": 0,
    "a": {
        "a": ["a", "aui1", 2],
        "a1": ["ạ", "5", 2],
        "a15": ["Ạ", "", 2],
        "aa": ["", "5", 2],
        "ai": ["ai", "I", 2],
        "au": ["au", "U1", 2],
        "au1": ["ọ", "5", 2],
        "au15": ["Ọ", "", 2],
        "aiI": ["ê", "5", 2],
        "auU": ["ô", "5", 2],
        "aa5": ["Ā", "", 2],
        "auU5": ["Ô", "", 2],
        "aiI5": ["Ê", "", 2],
    },
    "A": {
        "A": ["ā", "125U", 2],
        "A1": ["A", "", 2],
        "A2": ["ạ̄", "5", 2],
        "A5": ["Ā", "", 2],
        "A25": ["Ạ̄", "", 2],
        "AU": ["", "M", 2],
        "AUM": ["ॐ", "", 2],
    },
    "O": {"O": ["ō", "15", 2], "O1": ["O", "", 2], "O5": ["Ō", "", 2]},
    "E": {"E": ["ē", "15", 2], "E1": ["E", "", 2], "E5": ["Ē", "", 2]},
    "i": {"i": ["i", "i", 2], "ii": ["", "5", 2], "ii5": ["Ī", "", 2]},
    "e": {"e": ["e", "e", 2], "ee": ["", "5", 2], "ee5": ["Ī", "", 2]},
    "I": {"I": ["ī", "15", 2], "I1": ["I", "", 2], "I5": ["Ī", "", 2]},
    "u": {
        "u": ["u", "u1", 2],
        "u1": ["ü", "5", 2],
        "u15": ["Ü", "", 2],
        "uu": ["", "15", 2],
        "uu1": ["ǖ", "5", 2],
        "uu15": ["Ǖ", "", 2],
        "uu5": ["Ū", "", 2],
    },
    "o": {"o": ["o", "o", 2], "oo": ["", "5", 2], "oo5": ["Ū", "", 2]},
    "U": {"U": ["ū", "15", 2], "U1": ["U", "", 2], "U5": ["Ū", "", 2]},
    "r": {
        "r": ["r", "z1", 2],
        "r1": ["ṟ", "", 2],
        "rz": ["ṟ", "5", 2],
        "rz5": ["Ṟ", "", 2],
    },
    "R": {
        "R": ["r̥", "R15", 2],
        "R1": ["R", "", 2],
        "RR": ["r̥̄", "5", 2],
        "R5": ["R̥", "", 2],
        "RR5": ["R̥̄", "", 2],
    },
    "g": {"g": ["g", "", 2]},
    "G": {"G": ["ṅ", "15", 2], "G1": ["G", "", 2], "G5": ["Ṅ", "", 2]},
    "j": {"j": ["j", "z", 2], "jz": ["z", "", 2]},
    "J": {"J": ["ñ", "15", 2], "J1": ["J", "", 2], "J5": ["Ñ", "", 2]},
    "y": {"y": ["y", "z1", 2], "yz": ["ẏ", "", 2], "y1": ["ẏ", "", 2]},
    "Y": {"Y": ["ñ", "15", 2], "Y1": ["Y", "", 2], "Y5": ["Ñ", "", 2]},
    "t": {"t": ["t", "", 2]},
    "T": {"T": ["ṭ", "15", 2], "T1": ["T", "", 2], "T5": ["Ṭ", "", 2]},
    "d": {"d": ["d", "", 2]},
    "D": {
        "D": ["ḍ", "1hz5", 2],
        "D1": ["D", "", 2],
        "Dz": ["ṛ", "5", 2],
        "Dh": ["ḍh", "z", 2],
        "Dhz": ["ṛh", "5", 2],
        "D5": ["Ḍ", "", 2],
        "Dz5": ["Ṛ", "", 2],
        "Dhz5": ["Ṛh", "", 2],
    },
    "n": {"n": ["n", "z5", 2], "nz": ["ṉ", "", 2], "n5": ["ṉ", "", 2]},
    "N": {"N": ["ṇ", "15", 2], "N1": ["N", "", 2], "N5": ["Ṇ", "", 2]},
    "s": {"s": ["s", "h", 2], "sh": ["ś", "h", 2], "shh": ["ṣ", "", 2]},
    "S": {"S": ["S", "h", 2], "Sh": ["ṣ", "", 2]},
    "x": {"x": ["kṣ", "", 2]},
    "l": {"l": ["l", "", 2]},
    "L": {
        "L": ["ḷ", "zR15", 2],
        "LR": ["l̥", "R5", 2],
        "LRR": ["l̥̄", "5", 2],
        "Lz": ["ḻ", "5", 2],
        "L1": ["L", "", 2],
        "Lz5": ["Ḻ", "", 2],
        "L5": ["Ḷ", "", 2],
        "LR5": ["L̥", "", 2],
        "LRR5": ["L̥̄", "", 2],
    },
    "m": {"m": ["m", "", 2]},
    "q": {"q": ["q", "", 2]},
    "$": {"$": ["$", "$", 2], "$$": ["₹", "", 2]},
    "M": {
        "M": ["ṁ", "M235", 2],
        "MM": ["m̐", "5", 2],
        "M2": ["ṃ", "5", 2],
        "M3": ["M", "", 2],
        "MM5": ["M̐", "", 2],
        "M25": ["Ṃ", "", 2],
        "M5": ["Ṁ", "", 2],
    },
    "h": {"h": ["h", "", 2]},
    "H": {"H": ["ḥ", "15", 2], "H1": ["H", "", 2], "H5": ["Ḥ", "", 2]},
    "z": {"z": ["z", "h", 2], "zh": ["ḻ", "", 2]},
    ".": {
        ".": [".", "auAOEUIRLGJNTDMHY", 2],
        ".A": ["Ā", "1IU", 2],
        ".a": ["a", "aiu1", 2],
        ".a1": ["Ạ", "", 2],
        ".A1": ["Ạ̄", "", 2],
        ".AI": ["Ê", "", 2],
        ".AU": ["Ô", "", 2],
        ".O": ["Ō", "", 2],
        ".E": ["Ē", "", 2],
        ".I": ["Ī", "", 2],
        ".u": ["ü", "1u", 2],
        ".u1": ["Ü", "", 2],
        ".U": ["Ū", "1", 2],
        ".U1": ["Ǖ", "", 2],
        ".R": ["R̥", "Rz", 2],
        ".Rz": ["Ṟ", "", 2],
        ".RR": ["R̥̄", "", 2],
        ".G": ["Ṅ", "", 2],
        ".J": ["Ñ", "", 2],
        ".Y": ["Ñ", "", 2],
        ".N": ["Ṇ", "", 2],
        ".T": ["Ṭ", "", 2],
        ".D": ["Ḍ", "hz", 2],
        ".Dz": ["Ṛ", "", 2],
        ".Dh": ["Ḍh", "z", 2],
        ".Dhz": ["Ṛh", "", 2],
        ".L": ["Ḷ", "Rz", 2],
        ".LR": ["L̥", "R", 2],
        ".LRR": ["L̥̄", "", 2],
        ".Lz": ["Ḻ", "", 2],
        ".M": ["Ṁ", "M1", 2],
        ".MM": ["M̐", "", 2],
        ".M1": ["Ṃ", "", 2],
        ".H": ["Ḥ", "", 2],
        ".au": ["", "1", 2],
        ".au1": ["Ọ", "", 2],
    },
}
