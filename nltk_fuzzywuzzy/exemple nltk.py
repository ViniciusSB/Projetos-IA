from nltk.tokenize import sent_tokenize, word_tokenize

text = 'O tubarão-cabeça-chata, tubarão-de-cabeça-chata, ou tubarão-do-zambeze é um tubarão da ordem Carcharhiniformes, que pode viver tanto em água salgada como doce. Atinge de 2,1 a 3,5 metros de comprimento. Sua coloração do dorso vai desde marrom a cinza escuro, com o ventre branco.'


print(word_tokenize(text))

print(sent_tokenize(text))
