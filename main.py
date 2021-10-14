import time
from typing import List, Any, Union

import pyaudio
import speech_recognition as sr
import pyttsx3
from falas import *
from random import choice
import wikipedia
from datetime import datetime
import pywhatkit

wikipedia.set_lang('pt')
engine = pyttsx3.init()
engine.setProperty('rate', 120)

voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)

def reproduz_voz(frase):
    engine.say(frase)
    engine.runAndWait()

#funcao que vai processar a voz
def processar_voz():
    rec = sr.Recognizer() # cria um reconhecedor de voz

    # serve para abrir o microfone para captura
    with sr.Microphone() as s:
        while True:
            rec.adjust_for_ambient_noise(s)
            while True:
                try:
                    voz = rec.listen(s)
                    entrada = rec.recognize_google(voz, language='pt')
                    bd_falas = [entrada]
                    print(f'Você disse: {entrada}')
                    entrada = entrada.lower()

                    if entrada == 'oi' or entrada == 'olá':
                        resposta = choice(cumprimentar)
                        print(resposta)
                        reproduz_voz(resposta)

                    elif entrada == 'como vai' or entrada == 'como você está' or entrada == 'tudo numa boa':
                        resposta = choice(como_esta)
                        print(resposta)
                        reproduz_voz(resposta)

                    elif entrada == 'sim estou bem' or entrada == 'estou bem' or entrada == 'bem' or entrada == 'sim' or entrada == 'estou indo':
                        resposta = choice(humano_bem)
                        print(resposta)
                        reproduz_voz(resposta)

                    elif entrada == 'que horas são' or entrada == 'quais são as horas' or entrada == 'me informe as horas' or entrada == 'me fala as horas' or entrada == 'me informa que horas são agora' or entrada == 'me informa que horas são':
                        now = datetime.now()
                        hora_de_agora = (f'{now.hour} hora : {now.minute} minutos : {now.second} segundos')
                        reproduz_voz(hora_de_agora)
                        print(hora_de_agora)

                    elif entrada == 'que dia é hoje' or entrada == 'qual o dia de hoje' or entrada == 'qual a data de hoje':
                        now = datetime.now()
                        data_de_hoje = (f'{now.day} de {now.month} de {now.year}')
                        reproduz_voz(data_de_hoje)
                        print(data_de_hoje)

                    elif 'wikipédia' in entrada:
                        termo = entrada.split('wikipédia')
                        termo_da_pesquisa = termo[1]
                        reproduz_voz(f'Pesquisando por {termo[1]} no wikipédia')
                        pesquisa = wikipedia.page(termo_da_pesquisa)
                        try:
                            wikipedia.exceptions.PageError("Não foi encontrado!")
                        except:
                            reproduz_voz(f'Achamos a pagina {pesquisa.title} no wikipédia')
                            reproduz_voz('Agora estamos buscando o conteúdo dela')
                            print(f'Fonte: {pesquisa.url}')
                            reproduz_voz(pesquisa.content)
                            print(f'Conteúdo da Pagina:\n {pesquisa.content}')

                    elif 'youtube' in entrada:
                        termo = entrada.split('youtube')
                        termo_da_pesquisa = termo[1]
                        pywhatkit.playonyt(termo_da_pesquisa)

                    elif 'pesquise por' in entrada:
                        termo = entrada.split('pesquisar por')
                        termo_da_pesquisa = termo[1]
                        pywhatkit.search(termo_da_pesquisa)

                except sr.UnknownValueError:
                    reproduz_voz('Não entendi o que foi dito')
                    print('R414NNY: Não entendi o que foi dito')

assistente_virtual = processar_voz()