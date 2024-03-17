import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo ...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo ...')
        query = r.recognize_google(audio, language='pt-br')
        print(f'Usuário disse {query}\n')

    except Exception as e:
        print('Poderia dizer novamente ...')
        return 'None'
    
    return query

def create_todo_list():
    speak('O que você quer adicionar a sua lista de tarefas?')
    task = recognize_speech()
    with open('todo.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - {task}\n')
    speak('tarefa adicionada')

def search_web():
    speak('O que você gostaria de procurar?')
    query = recognize_speech()
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)
    speak(f'Aqui está os resultados para {query}.')

def set_reminder():
    speak('O que eu devo lembrá-lo?')
    task = recognize_speech()
    speak('Em quantos minutos?')
    mins = recognize_speech()
    mins = int(mins)
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=mins)
    with open('reminders.txt', 'a') as f:
        f.write(f'{reminder_time} - {task}\n')
    speak(f'Lembrete definido para {mins} minutos a partir de agora.')

def search_for():
    speak('O que deseja saber?')
    query = recognize_speech()
    procurar = query.replace('procure por', '')
    wikipedia.set_lang('pt')
    resultado = wikipedia.summary(procurar, 2)
    speak(resultado)

def music_video():
    speak('O que deseja escutar?')
    query = recognize_speech()
    musica = query.replace('toque', '')
    pywhatkit.playonyt(musica)
    speak('Tocando Musica')

def justsu_mutiplica():
    speak('Naruaitu teskinika da multiplicassuuuuuuuuuaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiin!....... Osquei')


def main():
    speak('Olá!, me chamo Alexa. Em que posso ajudar?')
    while True:
        query = recognize_speech().lower()

        if 'criar uma lista de tarefas' in query:
            create_todo_list()

        elif 'procure na web' in query:
            search_web()

        elif 'criar um lembrete' in query:
            set_reminder()

        elif 'procure por' in query:
            search_for()
        
        elif 'toque' in query:
            music_video()

        elif 'naruto' in query:
            justsu_mutiplica()

        elif 'pare' in query or 'sair' in query:
            speak('Até logo! meu grande mestre maravilhos que tenha todos os seus dias abençoados')
            break
        else:
            speak('Desculpe, Não entendi. Poderia repetir?')
main()