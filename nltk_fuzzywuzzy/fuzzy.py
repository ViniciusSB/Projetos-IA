from fuzzywuzzy import fuzz

texto1 = 'choveu'
texto2 = 'ontem choveu muito.' 
texto3 = 'choveu muito ontem.'


print(fuzz.ratio(texto2, texto3))

print(fuzz.partial_ratio(texto1, texto2))

print(fuzz.token_sort_ratio(texto2, texto3))