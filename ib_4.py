text = input('Введите строку: ')

keys = {
    'а': [['Q', '1', '!'], ['Ø', 'Ù', 'Ú'], ['⏩', '⏪', '⏫']],
    'б': [['W', '2', '@'], ['Û', 'Ü', 'Ý'], ['⏬', '⏭', '⏮']],
    'в': [['E', '3', '#'], ['Þ', 'ß', 'à'], ['⏯', '⏰', '⏱']],
    'г': [['R', '4', '$'], ['á', 'â', 'ã'], ['⏲', '⏳', '💼']],
    'д': [['T', '5', '%'], ['ä', 'å', 'æ'], ['📖', '💣', '💔']],
    'е': [['Y', '6', '^'], ['ç', 'è', 'é'], ['⏸', '⏹', '⏺']],
    'ё': [['U', '7', '&'], ['ê', 'ë', 'ì'], ['①', '②', '③']],
    'ж': [['I', '8', '*'], ['í', 'î', 'ï'], ['④', '⑤', '⑥']],
    'з': [['O', '9', '('], ['ð', 'ñ', 'ò'], ['⑦', '⑧', '⑨']],
    'и': [['P', '0', ')'], ['ó', 'ô', 'õ'], ['⑩', '⑪', '⑫']],
    'й': [['A', '-', '_'], ['ö', '÷', 'ø'], ['⑬', '⑭', '⑮']],
    'к': [['S', '+', '='], ['ù', 'ú', 'û'], ['⑯', '⑰', '⑱']],
    'л': [['D', '|', '/'], ['ü', 'ý', 'þ'], ['⑲', '⑳', '☎']],
    'м': [['F', '`', '~'], ['ÿ', 'Ā', 'ā'], ['☑', '☒', '☔']],
    'н': [['G', ',', '<'], ['Ă', 'ă', 'Ą'], ['☕', '☘', '☠']],
    'о': [['H', '.', '>'], ['ą', 'Ć', 'ć'], ['☢', '☣', '☭']],
    'п': [['J', ':', ':'], ['Ĉ', 'ĉ', 'Ċ'], ['☮', '☯', '☼']],
    'р': [['K', '"', '№'], ['ċ', 'Č', 'č'], ['☽', '☾', '☿']],
    'с': [['L', '?', '['], ['Ď', 'ď', 'Đ'], ['♀', '♁', '♂']],
    'т': [['Z', ']', '{'], ['đ', 'Ē', 'ē'], ['♃', '♄', '♅']],
    'у': [['X', '}', 'й'], ['Ĕ', 'ĕ', 'Ė'], ['♆', '♇', '♈']],
    'ф': [['C', 'ц', 'у'], ['ė', 'Ę', 'ę'], ['♉', '♊', '♋']],
    'х': [['V', 'к', 'е'], ['Ě', 'ě', 'Ĝ'], ['♌', '♍', '♎']],
    'ц': [['B', 'н', 'г'], ['ĝ', 'Ğ', 'ğ'], ['♏', '♐', '♑']],
    'ч': [['N', 'ш', 'щ'], ['Ġ', 'ġ', 'Ģ'], ['♒', '♓', '🕪']],
    'ш': [['M', 'з', 'х'], ['ģ', 'Ĥ', 'ĥ'], ['♔', '♕', '♘']],
    'щ': [['q', 'ъ', 'ф'], ['Ħ', 'ħ', 'Ĩ'], ['♳', '♴', '♵']],
    'ъ': [['w', 'ы', 'в'], ['ĩ', 'Ī', 'ī'], ['♶', '♷', '♸']],
    'ы': [['e', 'а', 'п'], ['Ĭ', 'ĭ', 'Į'], ['♹', '♺', '♻']],
    'ь': [['r', 'р', 'о'], ['į', 'İ', 'ı'], ['♼', '♽', '♾']],
    'э': [['t', 'л', 'д'], ['Ĳ', 'ĳ', 'Ĵ'], ['♿', '⚑', '⚒']],
    'ю': [['y', 'ж', 'э'], ['ĵ', 'Ķ', 'ķ'], ['⚐', '⚓', '⚔']],
    'я': [['u', 'я', 'ч'], ['ĸ', 'Ĺ', 'ĺ'], ['⚖', '⚠', '⚡']],
    'А': [['i', 'с', 'м'], ['Ļ', 'ļ', 'Ľ'], ['⚢', '⚣', '⚤']],
    'Б': [['o', 'и', 'т'], ['ľ', 'Ŀ', 'Ń'], ['⚥', '⚦', '⚧']],
    'В': [['p', 'ь', 'б'], ['ŀ', 'Ł', 'ł'], ['⚨', '⚩', '⚪']],
    'Г': [['a', 'ю', 'ё'], ['ń', 'Ņ', 'ņ'], ['⚫', '⚽', '⚾']],
    'Д': [['s', 'Й', 'Ц'], ['Ň', 'ň', 'ŉ'], ['⚿', '⛇', '⛈']],
    'Е': [['d', 'У', 'К'], ['Ŋ', 'ŋ', 'Ō'], ['⛎', '⛔', '⛟']],
    'Ё': [['f', 'Е', 'Н'], ['ō', 'Ŏ', 'ŏ'], ['⛢', '🔨', '🔪']],
    'Ж': [['g', 'Г', 'Ш'], ['Ő', 'ő', 'Œ'], ['⛤', '⛦', '⛧']],
    'З': [['h', 'Щ', 'З'], ['œ', 'Ŕ', 'ŕ'], ['⛪', '⛫', '⛱']],
    'И': [['j', 'Х', 'Ф'], ['Ŗ', 'ŗ', 'Ř'], ['⛲', '⛳', '⛴']],
    'Й': [['k', 'Ы', 'В'], ['ř', 'Ś', 'ś'], ['⛵', '⛶', '⛷']],
    'К': [['l', 'А', 'П'], ['Ŝ', 'ŝ', 'Ş'], ['⛸', '⛹', '⛺']],
    'Л': [['z', 'Р', 'О'], ['ş', 'Š', 'š'], ['⛻', '⛼', '⛽']],
    'М': [['x', 'Л', 'Д'], ['Ţ', 'ţ', 'Ť'], ['⛾', '⛿', '✀']],
    'Н': [['c', 'Ж', 'Э'], ['ť', 'Ŧ', 'ŧ'], ['✅', '✆', '✇']],
    'О': [['v', 'Я', 'Ч'], ['Ũ', 'ũ', 'Ū'], ['✈', '✉', '✊']],
    'П': [['b', 'С', 'М'], ['ū', 'Ŭ', 'ŭ'], ['✋', '✌', '✍']],
    'Р': [['n', 'И', 'Т'], ['Ů', 'ů', 'Ű'], ['✎', '✏', '✐']],
    'С': [['m', 'Ь', 'Б'], ['ű', 'Ų', 'ų'], ['✒', '✚', '✙']],
    'Т': [['ؠ', 'Ю', 'ء'], ['Ŵ', 'ŵ', 'Ŷ'], ['✜', '✝', '✞']],
    'У': [['آ', 'أ', 'ؤ'], ['ŷ', 'Ÿ', 'Ź'], ['✠', '✡', '✢']],
    'Ф': [['إ', 'ئ', 'ا'], ['ź', 'Ż', 'ż'], ['✣', '✤', '✥']],
    'Х': [['ب', 'ة', 'ت'], ['Ž', 'ž', 'ſ'], ['✨', '✪', '✱']],
    'Ц': [['ث', 'ج', 'ح'], ['Ɛ', 'Ƒ', 'ƒ'], ['✿', '❐', '❑']],
    'Ч': [['خ', 'د', 'ز'], ['Ɠ', 'Ɣ', 'ƕ'], ['❒', '❓', '❔']],
    'Ш': [['س', 'ش', 'ص'], ['Ɩ', 'Ɨ', 'Ƙ'], ['❕', '❖', '❗']],
    'Щ': [['ض', 'ط', 'ظ'], ['ƙ', 'ƚ', 'ƛ'], ['❘', '❙', '❚']],
    'Ъ': [['ع', 'غ', 'ػ'], ['Ɯ', 'Ɲ', 'ƞ'], ['❌', '❍', '❎']],
    'Ы': [['ؼ', 'ؽ', 'ؾ'], ['Ɵ', 'ơ', 'Ƣ'], ['❢', '❣', '❤']],
    'Ь': [['ؿ', 'ف', 'ق'], ['Ơ', 'ƣ', 'Ƥ'], ['❥', '❦', '❧']],
    'Э': [['ك', 'ل', 'م'], ['ƥ', 'Ʀ', 'Ƨ'], ['❰', '❱', '❶']],
    'Ю': [['ن', 'ه', 'و'], ['ƨ', 'Ʃ', 'ƪ'], ['❷', '❸', '❹']],
    'Я': [['ى', 'ي', 'ڀ'], ['ƫ', 'Ƭ', 'ƭ'], ['❺', '❻', '❼']],
    '0': [['א', 'ב', 'ג'], ['Ʈ', 'Ư', 'ư'], ['❽', '❾', '❿']],
    '1': [['ד', 'ה', 'ו'], ['Ʊ', 'Ʋ', 'Ƴ'], ['➔', '➕', '➖']],
    '2': [['ז', 'ח', 'ט'], ['ƴ', 'Ƶ', 'ƶ'], ['➗', '➘', '➙']],
    '3': [['י', 'ך', 'כ'], ['Ʒ', 'Ƹ', 'ƹ'], ['➚', '➛', '➜']],
    '4': [['ל', 'ם', 'מ'], ['ƺ', 'ƻ', 'Ƽ'], ['➝', '➟', '➢']],
    '5': [['ן', 'נ', 'ס'], ['ƽ', 'ƾ', 'ƿ'], ['➤', '➥', '➦']],
    '6': [['ע', 'ף', 'פ'], ['ǀ', 'ǁ', 'ǂ'], ['➧', '➨', '➩']],
    '7': [['ץ', 'צ', 'ק'], ['ǃ', 'Ǆ', 'ǅ'], ['➰', '➲', '➳']],
    '8': [['ר', 'ש', 'ת'], ['ǆ', 'Ǉ', 'ǈ'], ['➽', '➾', '➿']],
    '9': [['׆', 'Ѡ', 'ѡ'], ['ǉ', 'Ǌ', 'ǋ'], ['⟁', '⟃', '⟄']],
    '.': [['Ѣ', 'Ѥ', 'Ѧ'], ['ǌ', 'Ǎ', 'ǎ'], ['🚀', '🚁', '🚂']],
    ',': [['Ѩ', 'Ѫ', 'Ѭ'], ['Ǐ', 'Ǡ', 'ǡ'], ['🚃', '🚄', '🚅']],
    '?': [['ᕕ', 'ᕞ', 'ᕸ'], ['Ǣ', 'ǣ', 'Ǥ'], ['🚆', '🚇', '🚈']],
    '!': [['ᘦ', 'ᘫ', 'ᚸ'], ['ǥ', 'Ǧ', 'ǧ'], ['🚉', '🚊', '🚋']],
    '-': [['៖', 'ᢆ', 'ᧆ'], ['Ǩ', 'ǩ', 'Ǫ'], ['🚌', '🚍', '🚎']],
    '(': [['À', 'Á', 'Â'], ['ǫ', 'Ǭ', 'ǭ'], ['🚏', '🚐', '🚑']],
    ')': [['Ã', 'Ä', 'Å'], ['Ǯ', 'ǯ', 'ǰ'], ['🚒', '🚓', '🚔']],
    '"': [['Æ', 'Ç', 'È'], ['Ǳ', 'ǲ', 'ǳ'], ['🚕', '🚖', '🚗']],
    ':': [['É', 'Ê', 'Ë'], ['Ǵ', 'ǵ', 'Ƕ'], ['🚘', '🚙', '🚚']],
    '/': [['Ì', 'Í', 'Î'], ['Ƿ', 'Ǹ', 'ǹ'], ['🚴', '🚸', '🚧']],
    ' ': [['Ô', 'Õ', 'Ö'], ['Ǻ', 'ǻ', 'Ǽ'], ['🚤', '🚶', '🚽']],
}

crypt = ""
alp = 0
num = 0
for i in text:
    if i in keys:
        crypt += keys[i][alp][num]
        num += 1
        if num > 2:
            num = 0
        if i == ' ':
            alp += 1
            num = 0
        if alp > 2:
            alp = 0

print('Зашифрованная строка: ' + crypt)

decrypt = ""
for i in crypt:
    for j in keys:
        if i in keys[j][0] or i in keys[j][1] or i in keys[j][2]:
            decrypt += j
print('Расшифрованная строка: ' + decrypt)
