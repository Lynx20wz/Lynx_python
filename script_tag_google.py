from googletrans import Translator

perevodchic = Translator()

with open('tag.txt', 'r') as file:
    for line in file:
        tag = line[0:3]
        point_position = line.find('.')
        name_eng = line[17:point_position].lower()
        name_rus = str(perevodchic.translate(name_eng, dest='ru')).lower()
        with open('tag_dict_google.txt', 'a', encoding='UTF-8') as end_file:
            tag_countries = f"'{tag}': ['{name_eng}', '{name_rus}']\n"
            end_file.write(tag_countries)