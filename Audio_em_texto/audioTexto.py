import speech_recognition as sr

r = sr.Recognizer()

def audio_texto(audio):
    with sr.AudioFile(audio) as fonte:
        
        som = r.listen(fonte)
        # analiza e monta a frase com a api do google
        texto = r.recognize_google(som, language='pt-BR') 

        return print('Conteudo do audio: ' + texto)
        
def voz_texto():
    with sr.Microphone() as fonte:
        print('Diga alguma coisa: ')
        # reconhece o audio (tempo limite de 5 segundos)
        audio = r.listen(fonte, phrase_time_limit= 5)
        # analiza e monta a frase com a api do google
        texto = r.recognize_google(audio, language='pt-BR')
    
        return print('Você disse: ' + texto)
        

danca = 'danca.wav'
edu = 'brksedu.wav'

voz_texto()
audio_texto(danca)
audio_texto(edu)


