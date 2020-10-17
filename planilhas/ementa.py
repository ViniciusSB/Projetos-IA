import gspread
import nltk
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

#Se autentica
gc = gspread.authorize(credentials)

#Abre a planilha
wks = gc.open_by_key('KEY')

#Seleciona a primeira página da planilha
worksheet = wks.get_worksheet(0)

#Armazenando os dados da ementa na planilha
val = worksheet.col_values(5)

#Armazenando os stop-words do nltk
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

#Método para remover stop words
def stopWord(texto):
    descricao = []
    for desc in texto:
        semstop = [p for p in desc.split() if p not in stopwordsnltk]
        descricao.append(semstop) 
    return descricao

#Removendo os stop-words da ementa
ementa = stopWord(val)
#print(ementa)

text = 'Inteligência artificial (por vezes mencionada pela sigla em português IA ou pela sigla em inglês AI - artificial intelligence) é a inteligência similar à humana exibida por mecanismos ou software, além de também ser um campo de estudo acadêmico.'
text = nltk.tokenize.word_tokenize(text)

#Removendo os stop-words do text
text = stopWord(text)
#print(text)

#Tornando a lista da ementa mais limpa
ementaLimpa = []
for i in range(0, len(ementa), 1):
    if len(ementa[i]) >= 1:
        for j in range(0, len(ementa[i]), 1):
            ementaLimpa.append(ementa[i][j])
#print(ementaLimpa)

#Tornando a lista do texto mais limpo
textoLimpo = []
for i in range(0, len(text), 1):
    if len(text[i]) == 1:
        for j in range(0, len(text[i]), 1):
            textoLimpo.append(text[i][j])

#print(TextoLimpo)

#Verificando se texto tem relação com a ementa
for i in range(0, len(textoLimpo), 1):
        if textoLimpo[i] in ementaLimpa:
            print('A palavra '+textoLimpo[i]+" está presente na ementa!")

