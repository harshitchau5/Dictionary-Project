import json

DEFAULT_FILE = "dictionary.json"

def load_dict(file_path=DEFAULT_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

def save_dict(data, file_path=DEFAULT_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data,file, ensure_ascii=False, indent=4)

def select_language(lang, file_path=DEFAULT_FILE):
    lang = lang.lower().strip()
    data = load_dict(file_path)

    if lang not in data:
        data[lang] = {}
        save_dict(data, file_path)

    return lang

def translate(word,lang, file_path=DEFAULT_FILE):
    data = load_dict(file_path)
    word = word.lower().strip()

    if lang not in data:
        return "Language not found"
    else:
        keys = list(data[lang].keys())
        if word in keys:
            return data[lang][word]
        else:
            return "Word not found"

def add_word(word,meaning,lang, file_path=DEFAULT_FILE):
    data = load_dict(file_path)

    word = word.lower().strip()
    meaning = meaning.strip()

    if lang not in data:
        data[lang] = {}

    if word in data[lang]:
        return "Word already exists"

    data[lang][word] = meaning
    return(data)

def list_words(lang, file_path=DEFAULT_FILE):
    data = load_dict(file_path)
    if lang not in data:
        return []
    return sorted(data[lang].keys())

def main():
    print("=== Multi-Language Dictionary Translator ===")

    lang = select_language(input("Choose language: "))

    while True:
        print(f"\n Current Language: {lang}")
        print("1. Translate a word")
        print("2. Add new word")
        print("3. List all words")
        print("4. Change language")
        print("5. Quit")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            word = input("Enter word: ")
            print("Meaning:", translate(word,lang))

        elif choice == "2":
            word = input("Enter new word: ")
            meaning = input("Enter meaning: ")
            data = add_word(word, meaning, lang)
            save_dict(data)

        elif choice == "3":
            print("Words:", list_words(lang))

        elif choice == "4":
            lang = select_language(input("New langauge: "))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input")


if __name__ == "__main__":
    main ()



