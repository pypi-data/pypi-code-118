from .base import Encoding

class WinAnsiEncoding(Encoding):
    def __init__(self):
        super().__init__()
        self.encoding_name = "WinAnsiEncoding"
        self.code_to_name = {
            0o101: "A",
            0o306: "AE",
            0o301: "Aacute",
            0o302: "Acircumflex",
            0o304: "Adieresis",
            0o300: "Agrave",
            0o305: "Aring",
            0o303: "Atilde",
            0o102: "B",
            0o103: "C",
            0o307: "Ccedilla",
            0o104: "D",
            0o105: "E",
            0o311: "Eacute",
            0o312: "Ecircumflex",
            0o313: "Edieresis",
            0o310: "Egrave",
            0o320: "Eth",
            0o200: "Euro",
            0o106: "F",
            0o107: "G",
            0o110: "H",
            0o111: "I",
            0o315: "Iacute",
            0o316: "Icircumflex",
            0o317: "Idieresis",
            0o314: "Igrave",
            0o112: "J",
            0o113: "K",
            0o114: "L",
            0o115: "M",
            0o116: "N",
            0o321: "Ntilde",
            0o117: "O",
            0o214: "OE",
            0o323: "Oacute",
            0o324: "Ocircumflex",
            0o326: "Odieresis",
            0o322: "Ograve",
            0o330: "Oslash",
            0o325: "Otilde",
            0o120: "P",
            0o121: "Q",
            0o122: "R",
            0o123: "S",
            0o212: "Scaron",
            0o124: "T",
            0o336: "Thorn",
            0o125: "U",
            0o332: "Uacute",
            0o333: "Ucircumflex",
            0o334: "Udieresis",
            0o331: "Ugrave",
            0o126: "V",
            0o127: "W",
            0o130: "X",
            0o131: "Y",
            0o335: "Yacute",
            0o237: "Ydieresis",
            0o132: "Z",
            0o216: "Zcaron",
            0o141: "a",
            0o341: "aacute",
            0o342: "acircumflex",
            0o264: "acute",
            0o344: "adieresis",
            0o346: "ae",
            0o340: "agrave",
            0o046: "ampersand",
            0o345: "aring",
            0o136: "asciicircum",
            0o176: "asciitilde",
            0o052: "asterisk",
            0o100: "at",
            0o343: "atilde",
            0o142: "b",
            0o134: "backslash",
            0o174: "bar",
            0o173: "braceleft",
            0o175: "braceright",
            0o133: "bracketleft",
            0o135: "bracketright",
            0o246: "brokenbar",
            0o225: "bullet",
            0o143: "c",
            0o347: "ccedilla",
            0o270: "cedilla",
            0o242: "cent",
            0o210: "circumflex",
            0o072: "colon",
            0o054: "comma",
            0o251: "copyright",
            0o244: "currency",
            0o144: "d",
            0o206: "dagger",
            0o207: "daggerdbl",
            0o260: "degree",
            0o250: "dieresis",
            0o367: "divide",
            0o044: "dollar",
            0o145: "e",
            0o351: "eacute",
            0o352: "ecircumflex",
            0o353: "edieresis",
            0o350: "egrave",
            0o070: "eight",
            0o205: "ellipsis",
            0o227: "emdash",
            0o226: "endash",
            0o075: "equal",
            0o360: "eth",
            0o041: "exclam",
            0o241: "exclamdown",
            0o146: "f",
            0o065: "five",
            0o203: "florin",
            0o064: "four",
            0o147: "g",
            0o337: "germandbls",
            0o140: "grave",
            0o076: "greater",
            0o253: "guillemotleft",
            0o273: "guillemotright",
            0o213: "guilsinglleft",
            0o233: "guilsinglright",
            0o150: "h",
            0o055: "hyphen",
            0o151: "i",
            0o355: "iacute",
            0o356: "icircumflex",
            0o357: "idieresis",
            0o354: "igrave",
            0o152: "j",
            0o153: "k",
            0o154: "l",
            0o074: "less",
            0o254: "logicalnot",
            0o155: "m",
            0o257: "macron",
            0o265: "mu",
            0o327: "multiply",
            0o156: "n",
            0o071: "nine",
            0o361: "ntilde",
            0o043: "numbersign",
            0o157: "o",
            0o363: "oacute",
            0o364: "ocircumflex",
            0o366: "odieresis",
            0o234: "oe",
            0o362: "ograve",
            0o061: "one",
            0o275: "onehalf",
            0o274: "onequarter",
            0o271: "onesuperior",
            0o252: "ordfeminine",
            0o272: "ordmasculine",
            0o370: "oslash",
            0o365: "otilde",
            0o160: "p",
            0o266: "paragraph",
            0o050: "parenleft",
            0o051: "parenright",
            0o045: "percent",
            0o056: "period",
            0o267: "periodcentered",
            0o211: "perthousand",
            0o053: "plus",
            0o261: "plusminus",
            0o161: "q",
            0o077: "question",
            0o277: "questiondown",
            0o042: "quotedbl",
            0o204: "quotedblbase",
            0o223: "quotedblleft",
            0o224: "quotedblright",
            0o221: "quoteleft",
            0o222: "quoteright",
            0o202: "quotesinglbase",
            0o047: "quotesingle",
            0o162: "r",
            0o256: "registered",
            0o163: "s",
            0o232: "scaron",
            0o247: "section",
            0o073: "semicolon",
            0o067: "seven",
            0o066: "six",
            0o057: "slash",
            0o040: "space",
            0o243: "sterling",
            0o164: "t",
            0o376: "thorn",
            0o063: "three",
            0o276: "threequarters",
            0o263: "threesuperior",
            0o230: "tilde",
            0o231: "trademark",
            0o062: "two",
            0o262: "twosuperior",
            0o165: "u",
            0o372: "uacute",
            0o373: "ucircumflex",
            0o374: "udieresis",
            0o371: "ugrave",
            0o137: "underscore",
            0o166: "v",
            0o167: "w",
            0o170: "x",
            0o171: "y",
            0o375: "yacute",
            0o377: "ydieresis",
            0o245: "yen",
            0o172: "z",
            0o236: "zcaron",
            0o060: "zero",
            # additions due to PDF1.7 sD.2 footnote 5,6
            0o240: "space",
            0o255: "hyphen",
        }
        # additions due to PDF1.7 sD.2 footnote 3
        for i in range(0o41, 256):
            if i not in self.code_to_name:
                self.code_to_name[i] = "bullet"
