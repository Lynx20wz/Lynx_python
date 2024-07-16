# figd_lKa4uNZk1B1pc-AWt_YRVuC2u3iMiVk0Aup_ilgb
import os
import re
import customtkinter
import sys
from PIL import Image
from tkinter import filedialog

ico_uptade = customtkinter.CTkImage(light_image=Image.open('перезагрузка.png'),
                                    dark_image=Image.open('перезагрузка.png'), size=(30, 30))

focus_name_massiv = []
focus_dictionary = {}
tag_coutries = {
    'GER': ['germany', 'германия'],
    'ENG': ['united kingdom', 'великобритания', 'вб'],
    'SOV': ['soviet union', 'советский союз'],
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
ideologies_massiv = ['фашизм', 'комунизм', 'демокртия', 'нейтралитет']


class country_class:
    def __init__(self, tag, name, ideologies, capital=None, leader=None, create_country=None):
        self.tag = tag
        self.name = name
        self.capital = capital
        self.ideologies = ideologies
        self.leader = leader

        if create_country == 1:
            create_country(tag, name, ideologies, capital, leader)

    def create_country(self, tag, name, ideologies, capital=None, leader=None):
        with open(f"{name}.txt"):
            pass


class focus_class:
    #инициализация
    def __init__(self, id, cost, prerequisite=None, mutually_exclusive=None, create_focus=None):
        self.id = id
        self.costм = cost
        self.prerequisite = prerequisite
        self.mutually_exclusive = mutually_exclusive
        focus_name_massiv.append(self.id)
        focus_dictionary[id] = {'self': self, 'id': self.id, 'cost': self.costм, 'prerequisite': self.prerequisite,
                                'mutually_exclusive': self.mutually_exclusive}
        if create_focus == 1:
            self.focus_to_file(id, cost, prerequisite, mutually_exclusive)
        else:
            ...  #ничего не происходит

    def info(self):
        output = f'\nФокус: "{self.id}" | {self.costм}\n'
        if self.prerequisite:
            output += f'prerequisite: {self.pre}\n'
        if self.mutually_exclusive:
            output += f'mutually_exclusive: {self.muex}\n'
        return output

    @staticmethod
    def all_focus():
        output = ', '.join(focus_name_massiv)
        return output

    @staticmethod
    def clear_focus_file():  #очитска всего файла
        with open("focus.txt", "w") as file:
            file.write('')
        focus_name_massiv.clear()
        focus_dictionary.clear()
        print("Содержимое файла focus.txt было полностью удалено.")

    def search_focus_in_dictionary(id):
        for search_focus in focus_dictionary:
            if search_focus == id:
                search_focus = focus_dictionary[search_focus]['self']
                return search_focus

    # блок изменений частей
    def set_id(self, id):
        self.id = id

    def set_cost(self, cost):
        self.cost = cost

    def set_pre(self, prerequisite):
        self.pre = prerequisite

    def set_muex(self, mutually_exclusive):
        self.muex = mutually_exclusive

    def editing_focus(self):
        ...

    def focus_to_file(self, id, cost, prerequisite=None, mutually_exclusive=None):
        with open("focus.txt", 'a') as focus_file:
            focus_entry = f"focus = {{\n    id = {self.id}\n    cost = {self.costм}\n"
            focus_entry += f'}}\n\n'
            focus_file.write(focus_entry)


class App_class(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)
        self.bg_image = customtkinter.CTkImage(Image.open("bg.jpg"), size=(800, 600))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0,column=0)
        #self.iconbitmap()
        #self.attributes('-topmost', True) #закрепить наверху
        self.title("Modding manager")

        tab = customtkinter.CTkTabview(self, width=800, height=570, corner_radius=15, anchor='nw')
        tab.grid(row=0, column=0)

        tab.add('focus')
        tab.set('focus')
        tab.add('spirits')

        # кнопки

        # кнопка открыть файл
        self.btnopenfocusfile = customtkinter.CTkButton(tab.tab('focus'), height=33, width=120, fg_color='#010046',
                                                        text='открыть', command=self.open_file, corner_radius=10)
        self.btnopenfocusfile.grid(padx=5, pady=(15, 0))

        # кнопка сохранить
        self.btnsavefocusfile = customtkinter.CTkButton(tab.tab('focus'), height=33, width=120, fg_color='#010046',text='сохранить', command=self.save_file, corner_radius=10)
        self.btnsavefocusfile.grid(padx=5, pady=5)

        # кнопка обнвления
        self.updatebtn = customtkinter.CTkButton(master=tab.tab('focus'), command=self.uptadewidget(), image=ico_uptade)
        self.updatebtn.grid(padx=20, pady=30)


    def uptadewidget(self):
        app.update()

    def open_file(self):
        initial_file = filedialog.askopenfilename(title="Выберете файл содержащий фокусы",
                                                  filetypes=[("Файл с фокусами", ".txt*")])
        if initial_file != "":
            try:
                with open(initial_file, 'r') as focus_file:
                    for line in focus_file:
                        if not line.startswith("focus_tree = {"):
                            break
                        else:
                            if "focus = {" in line:
                                focus_block = True
                                while focus_block:
                                    for line in focus_file:
                                        if "id = " in line:
                                            find_id = line[line.find("id = ") + len("id = "):].strip()
                                        if "cost = " in line:
                                            find_cost = line[line.find("cost = ") + len("cost = "):].strip()
                                        if "prerequisite =" in line:
                                            find_prerequisite = line[line.find("prerequisite = ") + len(
                                                "prerequisite = "):].strip()
                                        else:
                                            find_prerequisite = None
                                        if "mutually_exclusive =" in line:
                                            find_mutually_exclusive = line[line.find("mutually_exclusive = ") + len(
                                                "mutually_exclusive = "):].strip()
                                        else:
                                            find_mutually_exclusive = None
                                        if "}" in line:
                                            focus_block = False
                                            find_id = focus_class(find_id, find_cost, find_prerequisite,
                                                                  find_mutually_exclusive)
            except FileNotFoundError:
                print("Файл с фокусами не был найден!")

            if len(focus_name_massiv) > 0:
                print(f"Всего было найдено фокусов {len(focus_name_massiv)}:")
                #print(', '.join(focus_name_massiv))
                print(focus_class.all_focus())

            else:
                print("Фокусы в файле не найдены!")
                focus_tree_quest = input("Создать новую ветку фокусов?: ")
                if focus_tree_quest == 'yes' or focus_tree_quest == 'да':
                    focus_tree_tag_quest = input("На какую страну делаем ветку фокусов?: ").lower()
                    if focus_tree_tag_quest.upper() in tag_coutries:
                        create_focus_tree(focus_tree_tag_quest)
                    else:
                        create_focus_tree(get_key(focus_tree_tag_quest))
                else:
                    ...

    def save_file(self):
        pass


def create_focus_tree(id):
    id = id.upper()
    with open("focus.txt", 'w') as focus_file:
        focus_tree = f'''focus_tree = {{
    id = {id}_focus_tree
    country = {{
        factor = 0
        modifier = {{
            add = 15
            original_tag = {id}
        }} 
    }}'''
        focus_file.write(focus_tree)


def get_key(significance):
    for k, s in tag_coutries.items():
        for s in s:
            if s == significance:
                return k
    else:
        unkown_tag_quest = input('Такого названия не найдено! Хотите создать новую страну?: ')
        if unkown_tag_quest == 'yes' or unkown_tag_quest == 'да':
            tag = input('Введите трёх-символьный тэг страны (например: "GER"): ').upper()
            if len(tag) == 3 and re.match(r'^[A-Z]+$', tag):
                name = input("Введите название страны на вашем языке: ").lower()
                ideologies_quest = input("Введите идеологию страны (фашизм, комунизм, нейтралитет, демократия, своя): ")
                #if ideologies_quest == 
                #    ideologies = input
        return 'MOD'


app = App_class()
app.mainloop()