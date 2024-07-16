import json
import os
import sys
from tkinter import filedialog
from rich import print

tag_countries = {
    'GER': ['germany', 'германия'],
    'ENG': ['united kingdom', 'великобритания', 'вб'],
    'SOV': ['soviet union', 'советский союз', 'совок'],
    'SWE': ['sweden', 'швеция'],
    'FRA': ['france', 'франция'],
    'LUX': ['luxemburg', 'люксембург'],
    'BEL': ['belgium', 'бельгия'],
    'HOL': ['holland', 'нидерланды'],
    'CZE': ['czechoslovakia', 'чехословакия'],
    'POL': ['poland', 'польша'],
    'AUS': ['austria', 'австрия'],
    'LIT': ['lithuania', 'литва'],
    'EST': ['estonia', 'эстония'],
    'LAT': ['latvia', 'латвия'],
    'SPR': ['spain', 'испания'],
    'ITA': ['italy', 'италия'],
    'ROM': ['romania', 'румыния'],
    'YUG': ['yugoslavia', 'югославия'],
    'SER': ['serbia', 'сербия'],
    'SWI': ['switzerland', 'швейцария'],
    'TUR': ['turkey', 'турция'],
    'GRE': ['greece', 'греция'],
    'ALB': ['albania', 'албания'],
    'NOR': ['norway', 'норвегия'],
    'DEN': ['denmark', 'дания'],
    'BUL': ['bulgaria', 'болгария'],
    'POR': ['portugal', 'португалия'],
    'FIN': ['finland', 'финляндия'],
    'IRE': ['ireland', 'ирландия'],
    'HUN': ['hungary', 'венгрия'],
    'AFG': ['afghanistan', 'афганистан'],
    'ARG': ['argentina', 'аргентина'],
    'AST': ['australia', 'австралия'],
    'BHU': ['bhutan', 'бутан'],
    'BOL': ['bolivia', 'боливия'],
    'BRA': ['brazil', 'бразилия'],
    'CAN': ['canada', 'канада'],
    'CHI': ['china', 'китай'],
    'CHL': ['chile', 'чили'],
    'COL': ['colombia', 'колумбия'],
    'COS': ['costa rica', 'коста рика'],
    'ECU': ['ecuador', 'эквадор'],
    'ELS': ['el salvador', 'сальвадор'],
    'ETH': ['ethiopia', 'эфиопия'],
    'GUA': ['guatemla', 'гватемала'],
    'HON': ['honduras', 'гондурас'],
    'IRQ': ['iraq', 'ирак'],
    'JAP': ['japan', 'япония'],
    'KOR': ['korea', 'корея'],
    'LIB': ['liberia', 'либерия'],
    'MEX': ['mexico', 'мексика'],
    'MEN': ['mengkukuo', 'мэнцзян'],
    'NEP': ['nepal', 'непал'],
    'NIC': ['nicaragua', 'никарагуа'],
    'NZL': ['new zealand', 'новая зеландия'],
    'PAN': ['panama', 'панама'],
    'PER': ['persia', 'иран'],
    'PHI': ['philippines', 'филиппины'],
    'PRU': ['peru', 'перу'],
    'SAF': ['south africa', 'южная африка'],
    'SAU': ['saudi arabia', 'центральная аравия'],
    'SIA': ['siam', 'сиам'],
    'SIK': ['sinkiang', 'синьцзянь'],
    'TIB': ['tibet', 'тибет'],
    'URG': ['uruguay', 'уругвай'],
    'VEN': ['venezula', 'венесуэла'],
    'YUN': ['yunnan', 'юньнань'],
    'USA': ['usa', 'америка', 'сша'],
    'MON': ['mongolia', 'монголия'],
    'TAN': ['tannu tuva', 'танну тува'],
    'PAR': ['paraguay', 'парагвай'],
    'CUB': ['cuba', 'куба'],
    'DOM': ['dominican republic', 'доминиканская республика', 'доминиканы'],
    'HAI': ['haiti', 'гаити'],
    'YEM': ['yeman', 'йемен'],
    'OMA': ['oman', 'оман'],
    'SLO': ['slovakia', 'словакия'],
    'RAJ': ['british raj', 'индия'],
    'CRO': ['croatia', 'хорватия'],
    'GXC': ['guangxi', 'гуанси'],
    'PRC': ['comchina', 'китай'],
    'SHX': ['shanxi', 'шаньси'],
    'XSM': ['xibei san ma', 'сибэй сань ма'],
    'ICE': ['iceland', 'исландия'],
    'LEB': ['lebanon', 'ливан'],
    'JOR': ['jordan', 'иордания'],
    'SYR': ['syria', 'сирия'],
    'EGY': ['egypt', 'египет'],
    'LBA': ['libya', 'ливия'],
    'WGR': ['west germany', 'западная германия'],
    'DDR': ['east germany', 'восточная германия'],
    'PAL': ['palestine', 'палестина'],
    'ISR': ['israel', 'израиль'],
    'VIN': ['vietnam', 'вьетнам'],
    'CAM': ['cambodia', 'камбоджа'],
    'MAL': ['malaysia', 'малайзия'],
    'INS': ['indonesia', 'индонезия'],
    'LAO': ['laos', 'лаос'],
    'MNT': ['montenegro', 'черногория'],
    'UKR': ['ukraine', 'украина'],
    'GEO': ['georgia', 'грузия'],
    'KAZ': ['kazakhstan', 'казахстан'],
    'AZR': ['azerbaijan', 'азербайджан'],
    'ARM': ['armenia', 'армения'],
    'BLR': ['belarus', 'беларусь'],
    'ANG': ['angola', 'ангола'],
    'MZB': ['mozambique', 'мозамбик'],
    'ZIM': ['zimbabwe', 'зимбабве'],
    'COG': ['congo', 'заир'],
    'KEN': ['kenya', 'кения'],
    'PAK': ['pakistan', 'пакистан'],
    'BOT': ['botswana', 'ботсвана'],
    'MAN': ['manchukou', 'китай'],
    'BAH': ['bahamas', 'багамы'],
    'BAN': ['bangladesh', 'бангладеш'],
    'BLZ': ['belize', 'белиз'],
    'BRM': ['burma', 'бирма'],
    'CRC': ['curacao', 'антильские острова'],
    'GDL': ['guadeloupe', 'гваделупа'],
    'GYA': ['guyana', 'гайана'],
    'JAM': ['jamaica', 'ямайка'],
    'JAN': ['jan mayen', 'ян-майен'],
    'KYR': ['kyrgyzstan', 'киргизия'],
    'MAD': ['madagascar', 'мадагаскар'],
    'MOL': ['moldova', 'молдавия'],
    'PNG': ['papua new guinea', 'папуа'],
    'PUE': ['puerto rico', 'пуэрто-рико'],
    'QAT': ['qatar', 'катар'],
    'SCO': ['scotland', 'шотландия'],
    'SRL': ['sri lanka', 'шри-ланка'],
    'SUR': ['suriname', 'суринам'],
    'TAJ': ['tajikistan', 'таджикистан'],
    'TRI': ['trinidad and tobago', 'тринидад и тобаго'],
    'TMS': ['turkmenistan', 'туркменистан'],
    'UAE': ['united arab emirates', 'арабские эмираты'],
    'UZB': ['uzbekistan', 'узбекистан'],
    'KUW': ['kuwait', 'кувейт'],
    'CYP': ['cyprus', 'кипр'],
    'MLT': ['malta', 'мальта'],
    'ALG': ['algeria', 'алжир'],
    'MOR': ['morocco', 'марокко'],
    'TUN': ['tunisia', 'тунис'],
    'SUD': ['sudan', 'судан'],
    'ERI': ['eritrea', 'эритрея'],
    'DJI': ['djibouti', 'джибути'],
    'SOM': ['somalia', 'сомали'],
    'UGA': ['uganda', 'уганда'],
    'RWA': ['rwanda', 'руанда'],
    'BRD': ['burundi', 'бурунди'],
    'TZN': ['tanzania', 'танзания'],
    'ZAM': ['zambia', 'замбия'],
    'MLW': ['malawi', 'малави'],
    'GAB': ['gabon', 'габон'],
    'RCG': ['republic of congo', 'конго'],
    'EQG': ['equatorial guinea', 'экваториальная гвинея'],
    'CMR': ['cameroon', 'камерун'],
    'CAR': ['central african republic', 'центральноафриканская республика'],
    'CHA': ['chad', 'чад'],
    'NGA': ['nigeria', 'нигерия'],
    'DAH': ['dahomey', 'бенин'],
    'TOG': ['togo', 'того'],
    'GHA': ['ghana', 'гана'],
    'VOL': ['upper volta', 'верхняя вольта'],
    'MLI': ['mali', 'мали'],
    'SIE': ['sierra leone', 'сьерра-леоне'],
    'GNA': ['guinea', 'гвинея'],
    'GNB': ['guinea-bissau', 'гвинея-бисау'],
    'SEN': ['senegal', 'сенегал'],
    'GAM': ['gambia', 'гамбия'],
    'WLS': ['wales', 'уэльс'],
    'NGR': ['niger', 'нигер'],
    'CSA': ['csa', 'конфедерация америки'],
    'USB': ['usb', 'нейтральные штаты америки'],
    'MRT': ['mauritania', 'мавритания'],
    'NMB': ['namibia', 'намибия'],
    'WES': ['western sahara', 'западная сахара'],
    'BAS': ['british antilles', 'антильские острова'],
    'CAY': ['cayenne', 'французская гвиана'],
    'MLD': ['maldives', 'мальдивы'],
    'FIJ': ['fiji', 'фиджи'],
    'FSM': ['micronesia', 'микронезия'],
    'TAH': ['tahiti', 'таити'],
    'GUM': ['guam', 'марианские острова'],
    'SOL': ['solomon', 'соломоновы острова'],
    'SAM': ['samoa', 'самоа'],
    'HAW': ['hawaii', 'гавайи'],
    'SLV': ['slovenia', 'словения'],
    'BOS': ['bosnia', 'босния'],
    'HRZ': ['herzegovina', 'герцеговина'],
    'MAC': ['macedonia', 'македония'],
    'NIR': ['northern ireland', 'северная ирландия'],
    'BAY': ['bavaria', 'бавария'],
    'MEK': ['mecklenburg', 'мекленбург'],
    'PRE': ['prussia', 'пруссия'],
    'SAX': ['saxony', 'саксония'],
    'HAN': ['hanover', 'ганновер'],
    'WUR': ['wurtemberg', 'вюртемберг'],
    'SHL': ['schleswig-holstein', 'шлезвиг'],
    'CAT': ['catalonia', 'каталония'],
    'NAV': ['navarra', 'страна басков'],
    'GLC': ['galicia', 'галисия'],
    'ADU': ['andalusia', 'андалусия'],
    'BRI': ['brittany', 'бретань'],
    'OCC': ['occitania', 'окситания'],
    'COR': ['corsica', 'корсика'],
    'KUR': ['kurdistan', 'курдистан'],
    'TRA': ['transylvania', 'трансильвания'],
    'DNZ': ['danzig', 'данциг'],
    'SIL': ['silesia', 'силезия'],
    'KSH': ['kashubia', 'кашубия'],
    'DON': ['don republic', 'донская республика'],
    'KUB': ['kuban republic', 'кубанская республика'],
    'BUK': ['bukharan republic', 'кубанская республика'],
    'ALT': ['altay', 'кубанская республика'],
    'KAL': ['kalmykia', 'кубанская республика'],
    'KAR': ['karelia', 'кубанская республика'],
    'CRI': ['crimea', 'кубанская республика'],
    'TAT': ['tatarstan', 'кубанская республика'],
    'CIN': ['chechnya ingushetia', 'кубанская республика'],
    'DAG': ['dagestan', 'кубанская республика'],
    'BYA': ['buryatia', 'кубанская республика'],
    'CKK': ['chukotka', 'кубанская республика'],
    'FER': ['fareastern republic', 'кубанская республика'],
    'YAK': ['yakutia', 'кубанская республика'],
    'VLA': ['vladivostok', 'кубанская республика'],
    'KKP': ['karakalpakstan', 'кубанская республика'],
    'YAM': ['yamalia', 'кубанская республика'],
    'TAY': ['taymyria', 'кубанская республика'],
    'OVO': ['ostyak vogulia', 'кубанская республика'],
    'NEN': ['nenetsia', 'кубанская республика'],
    'KOM': ['komi', 'кубанская республика'],
    'ABK': ['abkhazia', 'кубанская республика'],
    'KBK': ['kabardino balkaria', 'кубанская республика'],
    'NOA': ['north ossetia', 'кубанская республика'],
    'VGE': ['volga germany', 'кубанская республика'],
    'BSK': ['bashkortostan', 'кубанская республика'],
    'KHI': ['khiva', 'кубанская республика'],
    'UDM': ['udmurtia', 'кубанская республика'],
    'CHU': ['chuvashia', 'кубанская республика'],
    'MEL': ['mariel', 'кубанская республика'],
    'RIF': ['rif', 'кубанская республика'],
    'HAR': ['harar', 'кубанская республика'],
    'TIG': ['tigray', 'кубанская республика'],
    'AFA': ['afar', 'кубанская республика'],
    'BEG': ['benishangul-gumuz', 'кубанская республика'],
    'GBA': ['gambela', 'кубанская республика'],
    'SID': ['sidamo', 'кубанская республика'],
    'ORO': ['oromo', 'кубанская республика'],
    'QEM': ['qemant', 'кубанская республика'],
    'KHA': ['khakassia', 'кубанская республика'],
    'AOI': ['italian east africa', 'итальянская восточная африка'],
    'LBV': ['lombardy venetia', 'королевство ломбардия-венеция'],
    'PAP': ['papal states', 'папские государства'],
    'TOS': ['tuscany', 'великое княжество тосканское'],
    'SPM': ['sardinia piedmont', 'сардиния-пьемонт'],
    'TTS': ['the two sicilies', 'королевство двух сицилий'],
    'SMI': ['sami', 'сапми'],
    'GRN': ['greenland', 'гренландия'],
    'RAP': ['rapa nui', 'рапа нуи'],
    'YUC': ['yucatan', 'юкатан'],
    'RIG': ['rio grande', 'республика рио гранде'],
    'QUE': ['quebec', 'квебек'],
    'WLA': ['welsh argentina', 'валлийская колония'],
    'GAR': ['guarani', 'государство гуарани'],
    'INC': ['inca', 'нео-инкское государство'],
    'MIS': ['miskito', 'москития'],
    'MAY': ['maya', 'майя'],
    'INU': ['inuit', 'инуиты'],
    'CHR': ['charrua', 'государство чарруа'],
    'ITZ': ['itza', 'государство ица'],
    'NAH': ['nahua', 'государство науа'],
    'IAS': ['isthmo amerindia', 'истмо америндия'],
}
focus_files = []

def open_file():
    while not '':
        print('Откройте папку с файлами фокусов:')
        global file_folder
        file_folder = filedialog.askdirectory(title='Открыть папку с фокусами')

        if file_folder == '':
            print("Папка не выбрана!")
            while True:
                q_exit = input('Попробовать ещё раз или выход?\n[в/п]: ')
                if q_exit == 'п':
                    break
                elif q_exit == 'в':
                    sys.exit()
                else:
                    print("Команда не найдена! Повторите попытку.")
        else:
            break

def get_key(name):
    for k, s in tag_countries.items():
        for s in s:
            if s == name:
                return k

open_file()
print("Выбранный путь к файлу: ", file_folder.replace(' ', '_'))

for files in os.listdir(file_folder):
    extension_file = files[files.find('.'):]
    if extension_file == '.txt':
        focus_files.append(files)
    else:
        print(f"В папке обнаружены посторонние файлы: [red]{files}[/red].\nПожалуйста выберете другую папку.")
        open_file()
else:
    focus_files = ', '.join(focus_files)
    print(f"Найдены следующие файлы фокусов:\n[dodger_blue2]{focus_files}[/dodger_blue2]")
    question = input("Продолжить работу с ними?\n[да/нет]: ")
    print('')
    if question == 'да' or question == 'yes':
        for files in os.listdir(file_folder):
            name_country = files[:files.find('.')]
            tag = get_key(name_country)
            print(name_country.capitalize(), ':', tag)
            with open(f'{file_folder}/{files}', 'r') as focus_file:
                focus_block = False
                focus_dict = {}
                for line in focus_file.readlines():
                    line = line.strip()
                    if line.startswith('focus = {') or focus_block is True:
                        line = line.replace('#', '')
                        prerequisite = 'None'
                        focus_block = True
                        if focus_block:
                            if line.startswith('id ='):
                                id_focus = line[len('id = '):]
                                focus_dict['id'] = id_focus
                            if line.startswith('prerequisite ='):
                                focus_count = line.count('focus =')
                                if focus_count == 1:
                                    prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1]
                                else:
                                    prerequisite = line[len('prerequisite = { focus = '):line.rfind('}') - 1].split(
                                        'focus =')
                                    prerequisite = ', '.join(i.strip() for i in prerequisite)
                                focus_dict['prerequisite'] = prerequisite

                            if line.startswith('cost ='):
                                cost = line[len('cost = '):]
                                focus_dict['cost'] = cost

                            if line.startswith('}'):
                                focus_block = False
                                print(
                                    f'[green1]Фокус: {id_focus}[/green1]\n[yellow2]{prerequisite}[/yellow2] '
                                    f'[dodger_blue2]|[/dodger_blue2] [orange1]{cost}[/orange1]\n')
                                with open('focus_json.json', 'a') as json_file:
                                    json = {tag: {id_focus: {focus_dict}}}
                                    json.dump(json, json_file, indent=2)
