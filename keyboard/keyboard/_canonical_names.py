# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import platform

# TODO: add values from https://svn.apache.org/repos/asf/xmlgraphics/commons/tags/commons-1_0/src/java/org/apache/xmlgraphics/fonts/Glyphs.java

# Defaults to Windows canonical names (platform-specific overrides below)
canonical_names = {
    'escape': 'esc',
    'return': 'enter',
    'del': 'delete',
    'control': 'ctrl',

    'left arrow': 'left',
    'up arrow': 'up',
    'down arrow': 'down',
    'right arrow': 'right',

    ' ': 'space', # Prefer to spell out keys that would be hard to read.
    '\x1b': 'esc',
    '\x08': 'backspace',
    '\n': 'enter',
    '\t': 'tab',
    '\r': 'enter',

    'scrlk': 'scroll lock',
    'prtscn': 'print screen',
    'prnt scrn': 'print screen',
    'snapshot': 'print screen',
    'ins': 'insert',
    'pause break': 'pause',
    'ctrll lock': 'caps lock',
    'capslock': 'caps lock',
    'number lock': 'num lock',
    'numlock:': 'num lock',
    'space bar': 'space',
    'spacebar': 'space',
    'linefeed': 'enter',
    'win': 'windows',

    # Mac keys
    'command': 'windows',
    'cmd': 'windows',
    'control': 'ctrl',
    'option': 'alt',

    'app': 'menu',
    'apps': 'menu',
    'application': 'menu',
    'applications': 'menu',

    'pagedown': 'page down',
    'pageup': 'page up',
    'pgdown': 'page down',
    'pgup': 'page up',
    'next': 'page down', # This looks wrong, but this is how Linux reports.
    'prior': 'page up',

    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',

    'play/pause': 'play/pause media',

    'num multiply': '*',
    'num divide': '/',
    'num add': '+',
    'num plus': '+',
    'num minus': '-',
    'num sub': '-',
    'num enter': 'enter',
    'num 0': '0',
    'num 1': '1',
    'num 2': '2',
    'num 3': '3',
    'num 4': '4',
    'num 5': '5',
    'num 6': '6',
    'num 7': '7',
    'num 8': '8',
    'num 9': '9',

    'left win': 'left windows',
    'right win': 'right windows',
    'left control': 'left ctrl',
    'right control': 'right ctrl',
    'left menu': 'left alt', # Windows...
    'altgr': 'alt gr',

    # https://www.x.org/releases/X11R7.6/doc/libX11/Compose/en_US.UTF-8.html
    "Aacute": "Á",
    "aacute": "á",
    "abovedot": "˙",
    "Abreveacute": "Ắ",
    "abreveacute": "ắ",
    "Abrevebelowdot": "Ặ",
    "abrevebelowdot": "ặ",
    "Abrevegrave": "Ằ",
    "abrevegrave": "ằ",
    "Abrevehook": "Ẳ",
    "abrevehook": "ẳ",
    "Abrevetilde": "Ẵ",
    "abrevetilde": "ẵ",
    "Acircumflex": "Â",
    "acircumflex": "â",
    "Acircumflexacute": "Ấ",
    "acircumflexacute": "ấ",
    "Acircumflexbelowdot": "Ậ",
    "acircumflexbelowdot": "ậ",
    "Acircumflexgrave": "Ầ",
    "acircumflexgrave": "ầ",
    "Acircumflexhook": "Ẩ",
    "acircumflexhook": "ẩ",
    "Acircumflextilde": "Ẫ",
    "acircumflextilde": "ẫ",
    "acute": "´",
    "add": "+",
    "Adiaeresis": "Ä",
    "adiaeresis": "ä",
    "ae": "æ",
    "AE": "Æ",
    "Agrave": "À",
    "agrave": "à",
    "agudo": "´",
    "ampersand": "&",
    "apostrophe": "'",
    "Aring": "Å",
    "aring": "å",
    "asciicircum": "^",
    "asciitilde": "~",
    "asterisk": "*",
    "at": "@",
    "Atilde": "Ã",
    "atilde": "ã",
    "backslash": "\\",
    "bar": "|",
    "braceleft": "{",
    "braceright": "}",
    "bracketleft": "[",
    "bracketright": "]",
    "breve": "˘",
    "brokenbar": "¦",
    "caron": "ˇ",
    "Ccedilla": "Ç",
    "ccedilla": "ç",
    "cedilla": "¸",
    "cent": "¢",
    "circumflex": "^",
    "colon": ":",
    "ColonSign": "₡",
    "comma": ",",
    "copyright": "©",
    "CruzeiroSign": "₢",
    "currency": "¤",
    "degree": "°",
    "diaeresis": "¨",
    "divide": "/",
    "division": "÷",
    "dollar": "$",
    "DongSign": "₫",
    "dot": ".",
    "dstroke": "đ",
    "Dstroke": "Đ",
    "Eacute": "É",
    "eacute": "é",
    "Ecircumflex": "Ê",
    "ecircumflex": "ê",
    "Ecircumflexacute": "Ế",
    "ecircumflexacute": "ế",
    "Ecircumflexbelowdot": "Ệ",
    "ecircumflexbelowdot": "ệ",
    "Ecircumflexgrave": "Ề",
    "ecircumflexgrave": "ề",
    "Ecircumflexhook": "Ể",
    "ecircumflexhook": "ể",
    "Ecircumflextilde": "Ễ",
    "ecircumflextilde": "ễ",
    "EcuSign": "₠",
    "Ediaeresis": "Ë",
    "ediaeresis": "ë",
    "Egrave": "È",
    "egrave": "è",
    "eightsubscript": "₈",
    "ellipsis": "…",
    "enfilledcircbullet": "•",
    "equal": "=",
    "ETH": "Ð",
    "eth": "ð",
    "euro": "€",
    "EuroSign": "€",
    "exclam": "!",
    "exclamdown": "¡",
    "FFrancSign": "₣",
    "fivesubscript": "₅",
    "foursubscript": "₄",
    "function": "ƒ",
    "grave": "`",
    "greater": ">",
    "guillemotleft": "«",
    "guillemotright": "»",
    "hash": "#",
    "hashtag": "#",
    "Iacute": "Í",
    "iacute": "í",
    "Icircumflex": "Î",
    "icircumflex": "î",
    "Idiaeresis": "Ï",
    "idiaeresis": "ï",
    "Igrave": "Ì",
    "igrave": "ì",
    "less": "<",
    "LiraSign": "₤",
    "macron": "¯",
    "masculine": "º",
    "MillSign": "₥",
    "minplus": "+",
    "minus": "-",
    "mu": "µ",
    "multiply": "*",
    "multiply": "×",
    "NairaSign": "₦",
    "NewSheqelSign": "₪",
    "ninesubscript": "₉",
    "nobreakspace": " ",
    "notequal": "≠",
    "notsign": "¬",
    "Ntilde": "Ñ",
    "ntilde": "ñ",
    "numbersign": "#",
    "numerosign": "№",
    "Oacute": "Ó",
    "oacute": "ó",
    "Ocircumflex": "Ô",
    "ocircumflex": "ô",
    "Ocircumflexacute": "Ố",
    "ocircumflexacute": "ố",
    "Ocircumflexbelowdot": "Ộ",
    "ocircumflexbelowdot": "ộ",
    "Ocircumflexgrave": "Ồ",
    "ocircumflexgrave": "ồ",
    "Ocircumflexhook": "Ổ",
    "ocircumflexhook": "ổ",
    "Ocircumflextilde": "Ỗ",
    "ocircumflextilde": "ỗ",
    "Odiaeresis": "Ö",
    "odiaeresis": "ö",
    "oe": "œ",
    "OE": "Œ",
    "ogonek": "˛",
    "Ograve": "Ò",
    "ograve": "ò",
    "Ohornacute": "Ớ",
    "ohornacute": "ớ",
    "Ohornbelowdot": "Ợ",
    "ohornbelowdot": "ợ",
    "Ohorngrave": "Ờ",
    "ohorngrave": "ờ",
    "Ohornhook": "Ở",
    "ohornhook": "ở",
    "Ohorntilde": "Ỡ",
    "ohorntilde": "ỡ",
    "onehalf": "½",
    "onequarter": "¼",
    "onesubscript": "₁",
    "onesuperior": "¹",
    "ordfeminine": "ª",
    "Oslash": "Ø",
    "oslash": "ø",
    "Otilde": "Õ",
    "otilde": "õ",
    "paragraph": "¶",
    "parenleft": "(",
    "parenright": ")",
    "percent": "%",
    "period": ".",
    "periodcentered": "·",
    "PesetaSign": "₧",
    "plus": "+",
    "plusminus": "±",
    "pound": "£",
    "question": "?",
    "questiondown": "¿",
    "quotedbl": "\"",
    "registered": "®",
    "RupeeSign": "₨",
    "section": "§",
    "semicolon": ";",
    "sevensubscript": "₇",
    "similarequal": "≃",
    "sixsubscript": "₆",
    "slash": "/",
    "ssharp": "§",
    "ssharp": "ß",
    "Ssharp": "ẞ",
    "sterling": "£",
    "subtract": "-",
    "Thai_baht": "฿",
    "THORN": "Þ",
    "thorn": "þ",
    "threequarters": "¾",
    "threesubscript": "₃",
    "threesuperior": "³",
    "til": "~",
    "tilde": "~",
    "twosubscript": "₂",
    "twosuperior": "²",
    "Uacute": "Ú",
    "uacute": "ú",
    "Ucircumflex": "Û",
    "ucircumflex": "û",
    "Udiaeresis": "Ü",
    "udiaeresis": "ü",
    "Ugrave": "Ù",
    "ugrave": "ù",
    "Uhornacute": "Ứ",
    "uhornacute": "ứ",
    "Uhornbelowdot": "Ự",
    "uhornbelowdot": "ự",
    "Uhorngrave": "Ừ",
    "uhorngrave": "ừ",
    "Uhornhook": "Ử",
    "uhornhook": "ử",
    "Uhorntilde": "Ữ",
    "uhorntilde": "ữ",
    "underscore": "_",
    "WonSign": "₩",
    "Yacute": "Ý",
    "yacute": "ý",
    "ydiaeresis": "ÿ",
    "yen": "¥",
    "zerosubscript": "₀",
}
sided_modifiers = {'ctrl', 'alt', 'shift', 'windows'}
all_modifiers = {'alt', 'alt gr', 'ctrl', 'shift', 'windows'} | set('left ' + n for n in sided_modifiers) | set('right ' + n for n in sided_modifiers)

# Platform-specific canonical overrides

if platform.system() == 'Darwin':
    canonical_names.update({
        "command": "command",
        "windows": "command",
        "cmd": "command",
        "win": "command",
        "backspace": "delete"
    })
    all_modifiers = {'alt', 'ctrl', 'shift', 'windows'}
if platform.system() == 'Linux':
    canonical_names.update({
        "select": "end",
        "find": "home",
    })
