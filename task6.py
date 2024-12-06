import re
text = input() # текст
words = input().split() # массив слов
pattern = r'\b(%s)\b' % '|'.join(words) # шаблон поиска
print(re.sub(pattern, lambda s: s[0].upper(), text, flags=re.IGNORECASE))
 