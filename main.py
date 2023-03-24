import requests
from bs4 import BeautifulSoup
import wikipedia

print("Welcome to Wikibot\nIt's not a official bot, it's just a bot wich searches wikipedia for a given word\n\nAll information is taken from wikipedia and google!\n\n")

def search_web(question):
    # Создание экземпляра UserAgent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
    
    # URL для поиска в Google
    url = 'https://www.google.com/search?q='
    
    # Запрос на поиск
    query = question
    response = requests.get(url + query, headers=headers)
    
    # Использование BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Нахождение первого результата поиска
    result = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    
    # Если ответ не найден на первой странице поиска, то возвращаем None
    if not result:
        return None
    
    # Возвращаем текст ответа
    return result.get_text()


def search_wikipedia(question):
    # Устанавливаем язык поиска
    wikipedia.set_lang('en')
    
    try:
        # Поиск статьи на Википедии
        page = wikipedia.page(question)
        return page.summary
    except:
        # Если статья не найдена, возвращаем None
        return None


def solve_math_problem(question):
    try:
        # Вычисление математической задачи с помощью функции eval()
        answer = eval(question)
        return str(answer)
    except:
        # Если задача не может быть решена, возвращаем None
        return None


def get_answer(question):
    # Сначала ищем ответ в интернете
    answer = search_web(question)
    if answer:
        return answer
    
    # Если ответ не найден в интернете, ищем на Википедии
    answer = search_wikipedia(question)
    if answer:
        return answer
    
    # Если вопрос является математической задачей, решаем ее
    answer = solve_math_problem(question)
    if answer:
        return answer
    
    # Если ответ не найден ни в одном источнике, возвращаем сообщение об ошибке
    return "Извините, я не знаю ответа на ваш вопрос."


def think():
    while True:
        # Запрос ввода вопроса
        question = input("Ваш вопрос: ")
        
        # Если введен пустой вопрос, прекращаем цикл и завершаем программу
        if not question:
            print("До свидания!")
            break
        
        # Получение ответа на вопрос
        answer = get_answer(question)
        
        # Вывод ответа на экран
        print(answer)


if __name__ == '__main__':
    think()
