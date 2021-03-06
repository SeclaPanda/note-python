line = input('Введите строку: ') #input text

key = { #tuple for key
	'а': ['Q', '1', '!'],
	'б': ['W', '2', '@'],
	'в': ['E', '3', '#'],
	'г': ['R', '4', '$'],
	'д': ['T', '5', '%'],
	'е': ['Y', '6', '^'],
	'ё': ['U', '7', '&'],
	'ж': ['I', '8', '*'],
	'з': ['O', '9', '('],
	'и': ['P', '0', ')'],
	'й': ['A', '-', '_'],
	'к': ['S', '+', '='],
	'л': ['D', '|', '/'],
	'м': ['F', '`', '~'],
	'н': ['G', ',', '<'],
	'о': ['H', '.', '>'],
	'п': ['J', ':', ':'],
	'р': ['K', '"', '№'],
	'с': ['L', '?', '['],
	'т': ['Z', ']', '{'],
	'у': ['X', '}', 'й'],
	'ф': ['C', 'ц', 'у'],
	'х': ['V', 'к', 'е'],
	'ц': ['B', 'н', 'г'],
	'ч': ['N', 'ш', 'щ'],
	'ш': ['M', 'з', 'х'],
	'щ': ['q', 'ъ', 'ф'],
	'ъ': ['w', 'ы', 'в'],
	'ы': ['e', 'а', 'п'],
	'ь': ['r', 'р', 'о'],
	'э': ['t', 'л', 'д'],
	'ю': ['y', 'ж', 'э'],
	'я': ['u', 'я', 'ч'],
	'А': ['i', 'с', 'м'],
	'Б': ['o', 'и', 'т'],
	'В': ['p', 'ь', 'б'],
	'Г': ['a', 'ю', 'ё'],
	'Д': ['s', 'Й', 'Ц'],
	'Е': ['d', 'У', 'К'],
	'Ё': ['f', 'Е', 'Н'],
	'Ж': ['g', 'Г', 'Ш'],
	'З': ['h', 'Щ', 'З'],
	'И': ['j', 'Х', 'Ф'],
	'Й': ['k', 'Ы', 'В'],
	'К': ['l', 'А', 'П'],
	'Л': ['z', 'Р', 'О'],
	'М': ['x', 'Л', 'Д'],
	'Н': ['c', 'Ж', 'Э'],
	'О': ['v', 'Я', 'Ч'],
	'П': ['b', 'С', 'М'],
	'Р': ['n', 'И', 'Т'],
	'С': ['m', 'Ь', 'Б'],
	'Т': ['ؠ', 'Ю', 'ء'],
	'У': ['آ', 'أ', 'ؤ'],
	'Ф': ['إ', 'ئ', 'ا'],
	'Х': ['ب', 'ة', 'ت'],
	'Ц': ['ث', 'ج', 'ح'],
	'Ч': ['خ', 'د', 'ز'],
	'Ш': ['س', 'ش', 'ص'],
	'Щ': ['ض', 'ط', 'ظ'],
	'Ъ': ['ع', 'غ', 'ػ'],
	'Ы': ['ؼ', 'ؽ', 'ؾ'],
	'Ь': ['ؿ', 'ف', 'ق'],
	'Э': ['ك', 'ل', 'م'],
	'Ю': ['ن', 'ه', 'و'],
	'Я': ['ى', 'ي', 'ڀ'],
	'0': ['א', 'ב', 'ג'],
	'1': ['ד', 'ה', 'ו'],
	'2': ['ז', 'ח', 'ט'],
	'3': ['י', 'ך', 'כ'],
	'4': ['ל', 'ם', 'מ'],
	'5': ['ן', 'נ', 'ס'],
	'6': ['ע', 'ף', 'פ'],
	'7': ['ץ', 'צ', 'ק'],
	'8': ['ר', 'ש', 'ת'],
	'9': ['׆', 'Ѡ', 'ѡ'],
	'.': ['Ѣ', 'Ѥ', 'Ѧ'],
	',': ['Ѩ', 'Ѫ', 'Ѭ'],
	'?': ['ᕕ', 'ᕞ', 'ᕸ'],
	'!': ['ᘦ', 'ᘫ', 'ᚸ'],
	'-': ['៖', 'ᢆ', 'ᧆ'],
	'(': ['À', 'Á', 'Â'],
	')': ['Ã', 'Ä', 'Å'],
	'"': ['Æ', 'Ç', 'È'],
	':': ['É', 'Ê', 'Ë'],
	'/': ['Ì', 'Í', 'Î'],
	' ': ['Ô', 'Õ', 'Ö']
}

crypted = "" #crypted line 
num = 0 #counter for shift
for i in line: #take number from line
	if i in key: #if symbol from line in key
		crypted += key[i][num] #crypted line = key[i][num]
		num += 1 #counter update
		if num > 2: #if counter bigger then key 
			num = 0 #upd counter
		pare = key.get(i) #here and next - shift upd
		copy_pare = pare.copy()
		copy_pare[2] = pare[0]
		copy_pare[0] = pare[1]
		copy_pare[1] = pare[2]
		upd = {i: copy_pare}
		key.update(upd)
print('Зашифрованная строка: ' + crypted) #output

decrypted = "" #decrypted line
for i in crypted: #take a num from crypted line
	for j in key: #find symbol in key
		if i in key[j]: #if find 
			decrypted += j #decrypt
print('Расшифрованная строка: ' + decrypted) #output
