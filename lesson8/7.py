"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""


def analyze_text(text):
    if not isinstance(text, str):
        return None

    characters = len(text)

    lines = text.splitlines()
    num_lines = len(lines)

    words = text.split()
    num_words = len(words)

    sentences = text.replace("!", ".").replace("?", ".").split(".")
    num_sentences = len([s for s in sentences if s.strip()])

    return {
        'characters': characters,
        'words': num_words,
        'lines': num_lines,
        'sentences': num_sentences
    }

def display_analysis(analysis):
    if not isinstance(analysis, dict):
        print("Ошибка: Некорректный формат данных для анализа.")
        return

    print("--- Анализ Текста ---")
    print(f"Символов:   {analysis['characters']}")
    print(f"Слов:       {analysis['words']}")
    print(f"Строк:      {analysis['lines']}")
    print(f"Предложений: {analysis['sentences']}")
    print("-----------------------")

# пример использования
text = """Это пример текста.
Он состоит из нескольких строк. И предложений!
Сколько тут слов?"""

analysis_result = analyze_text(text)

if analysis_result:
    display_analysis(analysis_result)
else:
    print("Ошибка: Входные данные должны быть строкой.")
