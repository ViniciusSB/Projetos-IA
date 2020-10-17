import gspread
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

#Atualiza celula
# worksheet.update_acell('A1', 'OLÁ')

worksheet.update_cell(4,2,'Nome')
worksheet.update_cell(4,3,'Ordem')

#Dicionario com os nomes e as ordens dos animais
animais = {'Onça-pintada': 'Carnívora', 'Tubarão-tigre': 'Carcharhiniformes', 'Jabuti' : 'Testudinata' }

#Contador de colunas e celulas
col = 2
lin = 5

for nome, ordem in animais.items():
    #Atualizando o nome do animal da linha 5 coluna 2
    worksheet.update_cell(lin, col, nome)
    #Atualizando a col para 3
    col = 3
    #Atualizando a ordem do animal da linha 5 coluna 3
    worksheet.update_cell(lin, col, ordem)
    #Retorna a coluna para 2
    col = 2
    #Icrementando o valor da linha    
    lin += 1



