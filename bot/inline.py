from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sal_kb = [
    [
        InlineKeyboardButton(text='от 75.000', callback_data='от 75.000'),
        InlineKeyboardButton(text='от 155.000', callback_data='от 155.000'),
    ],
    [
        InlineKeyboardButton(text='от 235.000', callback_data='от 235.000'),
        InlineKeyboardButton(text='от 315.000', callback_data='от 315.000'),
    ],
    [InlineKeyboardButton(text='от 395.000', callback_data='от 395.000')]
]

salary_kb = InlineKeyboardMarkup(inline_keyboard=sal_kb)

emp_kb = [
    [
        InlineKeyboardButton(text='Полная занятость', callback_data='Полная занятость'),
        InlineKeyboardButton(text='Частичная занятость', callback_data='Частичная занятость'),
    ],
    [
        InlineKeyboardButton(text='Стажировка', callback_data='Стажировка'),
        InlineKeyboardButton(text='Проектная работа', callback_data='Проектная работа'),
    ],
    [
        InlineKeyboardButton(text='Волонтерство', callback_data='Волонтерство'),
        InlineKeyboardButton(text='Оформление по ГПХ',
                             callback_data='Оформление по ГПХ'),
    ]
]
employment_kb = InlineKeyboardMarkup(inline_keyboard=emp_kb)

exp_kb = [
    [
        InlineKeyboardButton(text='Нет опыта', callback_data='Нет опыта'),
        InlineKeyboardButton(text='От 1 года до 3 лет', callback_data='От года 1 до 3 лет'),
    ],
    [
        InlineKeyboardButton(text='От 3 до 6 лет', callback_data='От 3 до 6 лет'),
        InlineKeyboardButton(text='Более 6 лет', callback_data='Более 6 лет'),
    ],
    [InlineKeyboardButton(text='Не важно', callback_data='Не имеет значения')]
]
experience_kb = InlineKeyboardMarkup(inline_keyboard=exp_kb)

shed_kb = [
    [
        InlineKeyboardButton(text='Полный день', callback_data='Полный день'),
        InlineKeyboardButton(text='Сменный график', callback_data='Сменный график'),
    ],
    [
        InlineKeyboardButton(text='Удаленная работа', callback_data='Удаленная работа'),
        InlineKeyboardButton(text='Гибкий график', callback_data='Гибкий график'),
    ],
    [InlineKeyboardButton(text='Вахтовый метод', callback_data='Вахтовый метод')]
]
schedule_kb = InlineKeyboardMarkup(inline_keyboard=shed_kb)

prof_roles = {'Автомобильный бизнес': ['Автомойщик', 'Автослесарь, автомеханик', 'Мастер-приемщик',
                                       'Менеджер по продажам, менеджер по работе с клиентами'],
              'Административный персонал': ['Администратор', 'Делопроизводитель, архивариус', 'Курьер',
                                            'Менеджер/руководитель АХО', 'Оператор ПК, оператор базы данных',
                                            'Офис-менеджер', 'Переводчик',
                                            'Секретарь, помощник руководителя, ассистент'],
              'Безопасность': ['Военнослужащий', 'Охранник', 'Полицейский', 'Специалист по информационной безопасности',
                               'Специалист службы безопасности'],
              'Высший и средний менеджмент': ['Генеральный директор, исполнительный директор (CEO)',
                                              'Директор по информационным технологиям (CIO)',
                                              'Директор по маркетингу и PR (CMO)', 'Директор по персоналу (HRD)',
                                              'Директор юридического департамента (CLO)', 'Коммерческий директор (CCO)',
                                              'Начальник производства', 'Операционный директор (COO)',
                                              'Руководитель отдела аналитики', 'Руководитель отдела логистики',
                                              'Руководитель отдела маркетинга и рекламы',
                                              'Руководитель отдела персонала',
                                              'Руководитель филиала', 'Технический директор (CTO)',
                                              'Финансовый директор (CFO)'],
              'Добыча сырья': ['Геодезист', 'Геолог', 'Лаборант', 'Машинист', 'Научный специалист, исследователь',
                               'Начальник смены, мастер участка', 'Технолог'],
              'Домашний, обслуживающий персонал': ['Администратор', 'Водитель', 'Воспитатель, няня', 'Дворник',
                                                   'Курьер', 'Официант, бармен, бариста', 'Охранник', 'Уборщица, уборщик'],
              'Информационные технологии': ['BI-аналитик, аналитик данных', 'DevOps-инженер', 'Аналитик',
                                            'Арт-директор, креативный директор', 'Бизнес-аналитик', 'Гейм-дизайнер',
                                            'Дата-сайентист', 'Дизайнер, художник',
                                            'Директор по информационным технологиям (CIO)', 'Менеджер продукта',
                                            'Методолог', 'Программист, разработчик', 'Продуктовый аналитик',
                                            'Руководитель группы разработки', 'Руководитель отдела аналитики',
                                            'Руководитель проектов', 'Сетевой инженер', 'Системный администратор',
                                            'Системный аналитик', 'Системный инженер',
                                            'Специалист по информационной безопасности',
                                            'Специалист технической поддержки', 'Тестировщик',
                                            'Технический директор (CTO)', 'Технический писатель'],
              'Искусство, развлечения, массмедиа': ['Арт-директор, креативный директор', 'Артист, актер, аниматор',
                                                    'Видеооператор, видеомонтажер', 'Гейм-дизайнер', 'Дизайнер, художник',
                                                    'Журналист, корреспондент', 'Копирайтер, редактор, корректор',
                                                    'Продюсер', 'Режиссер, сценарист', 'Фотограф, ретушер'],
              'Маркетинг, реклама, PR': ['Event-менеджер', 'PR-менеджер', 'SMM-менеджер, контент-менеджер', 'Аналитик',
                                         'Арт-директор, креативный директор', 'Дизайнер, художник',
                                         'Директор по маркетингу и PR (CMO)', 'Копирайтер, редактор, корректор',
                                         'Маркетолог-аналитик', 'Менеджер по маркетингу, интернет-маркетолог',
                                         'Менеджер по продажам, менеджер по работе с клиентами',
                                         'Менеджер по работе с партнерами', 'Промоутер',
                                         'Руководитель отдела маркетинга и рекламы'],
              'Медицина, фармацевтика': ['Администратор', 'Ассистент врача', 'Ветеринарный врач', 'Врач',
                                         'Главный врач, заведующий отделением', 'Заведующий аптекой', 'Лаборант',
                                         'Медицинская сестра, медицинский брат', 'Медицинский представитель',
                                         'Научный специалист, исследователь', 'Специалист по сертификации',
                                         'Фармацевт-провизор'],
              'Наука, образование': ['Бизнес-тренер', 'Воспитатель, няня', 'Лаборант', 'Методист',
                                     'Научный специалист, исследователь', 'Психолог', 'Учитель, преподаватель, педагог'],
              'Управление персоналом, тренинги': ['Бизнес-тренер', 'Директор по персоналу (HRD)',
                                                  'Менеджер по компенсациям и льготам', 'Менеджер по персоналу',
                                                  'Руководитель отдела персонала', 'Специалист по кадрам',
                                                  'Специалист по подбору персонала'],
              }

categories_kb = [
    [InlineKeyboardButton(text='Авто бизнес', callback_data='avto_kb')],
    [InlineKeyboardButton(text='Админ. персонал', callback_data='admin_kb')],
    [InlineKeyboardButton(text='Безопасность', callback_data='saf_kb')],
    [InlineKeyboardButton(text='Менеджмент', callback_data='manager_kb')],
    [InlineKeyboardButton(text='Добыча сырья', callback_data='lut_kb')],
    [InlineKeyboardButton(text='Домашний персонал', callback_data='home_kb')],
    [InlineKeyboardButton(text='ИТ', callback_data='it_kb')],
    [InlineKeyboardButton(text='Искусство, массмедиа', callback_data='art_kb')],
    [InlineKeyboardButton(text='Маркетинг, PR', callback_data='advert_kb')],
    [InlineKeyboardButton(text='Медицина', callback_data='med_kb')],
    [InlineKeyboardButton(text='Наука, образование', callback_data='edu_kb')],
    [InlineKeyboardButton(text='Тренинги', callback_data='train_kb')]
]

#{'Менеджер по продажам': ''Менеджер по продажам, менеджер по работе с клиентами', 'Автослесарь': 'Автослесарь, автомеханик',
# 'От 1 до 3':'От 1 года до 3 лет', 'Оформление по ГПХ':'Оформление по ГПХ или по совместительству',
# 'Секретарь': 'Секретарь, помощник руководителя, ассистент', 'Оператор бд': 'Оператор ПК, оператор базы данных'
# 'Менеджер АХО': 'Менеджер/руководитель АХО', 'Делопроизводитель, архивариус': 'Архивариус',
# 'Специалист по иб': 'Специалист по информационной безопасности', 'Специалист сб': 'Специалист службы безопасности',
# 'Генеральный директор': 'Генеральный директор, исполнительный директор (CEO)',
# 'Директор (CIO)': 'Директор по информационным технологиям (CIO)', 'Директор (CMO)': 'Директор по маркетингу и PR (CMO)', '': '', '': '', '': '', '': ''}
categories_name_kb = InlineKeyboardMarkup(inline_keyboard=categories_kb)

avto_start_kb = [
    [InlineKeyboardButton(text='Автомойщик', callback_data='Автомойщик')],
    [InlineKeyboardButton(text='Автомеханик', callback_data='Автослесарь')],
    [InlineKeyboardButton(text='Мастер-приемщик', callback_data='Мастер-приемщик')],
    [InlineKeyboardButton(text='Менеджер', callback_data='Менеджер по продажам')]
]

avto_kb = InlineKeyboardMarkup(inline_keyboard=avto_start_kb)

admin_start_kb = [
    [InlineKeyboardButton(text='Администратор', callback_data='Администратор')],
    [InlineKeyboardButton(text='Архивариус', callback_data='Архивариус')],
    [InlineKeyboardButton(text='Курьер', callback_data='Курьер')],
    [InlineKeyboardButton(text='Менеджер АХО', callback_data='Менеджер АХО')],
    [InlineKeyboardButton(text='Оператор бд', callback_data='Оператор бд')],
    [InlineKeyboardButton(text='Офис-менеджер', callback_data='Офис-менеджер')],
    [InlineKeyboardButton(text='Переводчик', callback_data='Переводчик')],
    [InlineKeyboardButton(text='Секретарь', callback_data='Секретарь')]
]

admin_kb = InlineKeyboardMarkup(inline_keyboard=admin_start_kb)

saf_start_kb = [
    [InlineKeyboardButton(text='Военнослужащий', callback_data='Военнослужащий')],
    [InlineKeyboardButton(text='Охранник', callback_data='Охранник')],
    [InlineKeyboardButton(text='Полицейский', callback_data='Полицейский')],
    [InlineKeyboardButton(text='Специалист по иб', callback_data='Специалист по иб')],
    [InlineKeyboardButton(text='Специалист сб', callback_data='Специалист сб')]
]

saf_kb = InlineKeyboardMarkup(inline_keyboard=saf_start_kb)

manager_start_kb = [
    [InlineKeyboardButton(text='Генеральный директор', callback_data='Генеральный директор')],
    [InlineKeyboardButton(text='Директор (CIO)', callback_data='Директор (CIO)')],
    [InlineKeyboardButton(text='Директор (CMO)', callback_data='Директор CMO)')],
    [InlineKeyboardButton(text='Директор (HRD)', callback_data='Директор (HRD)')],
    [InlineKeyboardButton(text='Директор (CLO)', callback_data='Директор (CLO)')],
    [InlineKeyboardButton(text='Директор (CCO)', callback_data='Директор (CCO)')],
    [InlineKeyboardButton(text='Начальник производ.', callback_data='Начальник производ.')],
    [InlineKeyboardButton(text='Директор (COO)', callback_data='Директор (COO)')],
    [InlineKeyboardButton(text='Рук отдела аналитики', callback_data='Рук отдела аналитики')],
    [InlineKeyboardButton(text='Рук отдела логистики', callback_data='Рук отдела логистики')],
    [InlineKeyboardButton(text='Рук отдела рекламы', callback_data='Рук отдела рекламы')],
    [InlineKeyboardButton(text='Рук отдела персонала', callback_data='Рук отдела персонала')],
    [InlineKeyboardButton(text='Рук филиала', callback_data='Рук филиала')],
    [InlineKeyboardButton(text='Директор (CTO)', callback_data='Директор (CTO)')],
    [InlineKeyboardButton(text='Директор (CFO)', callback_data='Директор (CFO)')],
]

manager_kb = InlineKeyboardMarkup(inline_keyboard=manager_start_kb)

lut_start_kb = [
    [InlineKeyboardButton(text='Геодезист', callback_data='Геодезист')],
    [InlineKeyboardButton(text='Геолог', callback_data='Геолог')],
    [InlineKeyboardButton(text='Лаборант', callback_data='Лаборант')],
    [InlineKeyboardButton(text='Машинист', callback_data='Машинист')],
    [InlineKeyboardButton(text='Научный специалист', callback_data='Научный специалист')],
    [InlineKeyboardButton(text='Начальник смены', callback_data='Начальник смены')],
    [InlineKeyboardButton(text='Технолог', callback_data='Технолог')],
]

lut_kb = InlineKeyboardMarkup(inline_keyboard=lut_start_kb)

home_start_kb = [
    [InlineKeyboardButton(text='Администратор', callback_data='Администратор')],
    [InlineKeyboardButton(text='Водитель', callback_data='Водитель')],
    [InlineKeyboardButton(text='Воспитатель, няня', callback_data='Воспитатель, няня')],
    [InlineKeyboardButton(text='Дворник', callback_data='Дворник')],
    [InlineKeyboardButton(text='Курьер', callback_data='Курьер')],
    [InlineKeyboardButton(text='Официант, бариста', callback_data='Официант, бармен')],
    [InlineKeyboardButton(text='Охранник', callback_data='Охранник')],
    [InlineKeyboardButton(text='Уборщица, уборщик', callback_data='Уборщица, уборщик')]
]

home_kb = InlineKeyboardMarkup(inline_keyboard=home_start_kb)

it_start_kb = [
    [
         InlineKeyboardButton(text='BI-аналитик', callback_data='BI-аналитик'),
         InlineKeyboardButton(text='DevOps-инженер', callback_data='DevOps-инженер')
    ],
    [
         InlineKeyboardButton(text='Аналитик', callback_data='Аналитик'),
         InlineKeyboardButton(text='Арт-директор', callback_data='Арт-директор')
    ],
    [
         InlineKeyboardButton(text='Бизнес-аналитик', callback_data='Бизнес-аналитик'),
         InlineKeyboardButton(text='Гейм-дизайнер', callback_data='Гейм-дизайнер')
    ],
    [
         InlineKeyboardButton(text='Дата-сайентист', callback_data='Дата-сайентист'),
         InlineKeyboardButton(text='Дизайнер, художник', callback_data='Дизайнер, художник')
    ],
    [
         InlineKeyboardButton(text='Директор (CIO)', callback_data='Директор (CIO)'),
         InlineKeyboardButton(text='Менеджер продукта', callback_data='Менеджер продукта')
    ],
    [
         InlineKeyboardButton(text='Методолог', callback_data='Методолог'),
         InlineKeyboardButton(text='Разработчик', callback_data='Разработчик')
    ],
    [
         InlineKeyboardButton(text='Прод аналитик', callback_data='Прод аналитик'),
         InlineKeyboardButton(text='Рук группы разработки', callback_data='Рук группы разработки')
    ],
    [
         InlineKeyboardButton(text='Рук отдела аналитики', callback_data='Рук отдела аналитики'),
         InlineKeyboardButton(text='Рук проектов', callback_data='Рук проектов')
    ],
    [
         InlineKeyboardButton(text='Сетевой инженер', callback_data='Сетевой инженер'),
         InlineKeyboardButton(text='Системный админ', callback_data='Системный админ')
    ],
    [
         InlineKeyboardButton(text='Системный аналитик', callback_data='Системный аналитик'),
         InlineKeyboardButton(text='Системный инженер', callback_data='Системный инженер')
    ],
    [
         InlineKeyboardButton(text='Специалист по иб', callback_data='Специалист по иб'),
         InlineKeyboardButton(text='Спец тех поддержки', callback_data='Спец тех поддержки')
    ],
    [
         InlineKeyboardButton(text='Тестировщик', callback_data='Тестировщик'),
         InlineKeyboardButton(text='Директор (CTO)', callback_data='Директор (CTO)')
    ],

    [InlineKeyboardButton(text='Тех писатель', callback_data='Тех писатель')]
]

it_kb = InlineKeyboardMarkup(inline_keyboard=it_start_kb)

art_start_kb = [
    [
         InlineKeyboardButton(text='Арт-директор', callback_data='Арт-директор'),
         InlineKeyboardButton(text='Артист, актер', callback_data='Артист')
    ],
    [
         InlineKeyboardButton(text='Гейм-дизайнер', callback_data='Гейм-дизайнер'),
         InlineKeyboardButton(text='Дизайнер, художник', callback_data='Дизайнер, художник')
    ],
    [
         InlineKeyboardButton(text='Журналист', callback_data='Журналист'),
         InlineKeyboardButton(text='Редактор', callback_data='Редактор')
    ],
    [
         InlineKeyboardButton(text='Продюсер', callback_data='Продюсер'),
         InlineKeyboardButton(text='Режиссер, сценарист', callback_data='Режиссер, сценарист')
    ],
    [
         InlineKeyboardButton(text='Фотограф, ретушер', callback_data='Фотограф, ретушер'),
         InlineKeyboardButton(text='Видеомонтажер', callback_data='Видеомонтажер')
    ]
]

art_kb = InlineKeyboardMarkup(inline_keyboard=art_start_kb)

advert_start_kb = [
    [
         InlineKeyboardButton(text='Event-менеджер', callback_data='Event-менеджер'),
         InlineKeyboardButton(text='PR-менеджер', callback_data='PR-менеджер')
    ],
    [
         InlineKeyboardButton(text='SMM-менеджер', callback_data='SMM-менеджер'),
         InlineKeyboardButton(text='Аналитик', callback_data='Аналитик')
    ],
    [
         InlineKeyboardButton(text='Арт-директор', callback_data='Арт-директор'),
         InlineKeyboardButton(text='Дизайнер', callback_data='Дизайнер')
    ],
    [
         InlineKeyboardButton(text='Директор (CMO)', callback_data='Директор (CMO)'),
         InlineKeyboardButton(text='Редактор', callback_data='Редактор')
    ],
    [
         InlineKeyboardButton(text='Маркетолог-аналитик', callback_data='Маркетолог-аналитик'),
         InlineKeyboardButton(text='Интернет-маркетолог', callback_data='Интернет-маркетолог')
    ],
    [
         InlineKeyboardButton(text='Менеджер по продажам', callback_data='Менеджер по продажам'),
         InlineKeyboardButton(text='Менеджер', callback_data='Менеджер')
    ],
    [
        InlineKeyboardButton(text='Промоутер', callback_data='Промоутер'),
        InlineKeyboardButton(text='Рук маркетинга', callback_data='Рук маркетинга')
    ]
]

advert_kb = InlineKeyboardMarkup(inline_keyboard=advert_start_kb)

med_start_kb = [
    [
         InlineKeyboardButton(text='Администратор', callback_data='Администратор'),
         InlineKeyboardButton(text='Ассистент врача', callback_data='Ассистент врача')
    ],
    [
         InlineKeyboardButton(text='Вет врач', callback_data='Вет врач'),
         InlineKeyboardButton(text='Врач', callback_data='Врач')
    ],
    [
         InlineKeyboardButton(text='Главный врач', callback_data='Главный врач'),
         InlineKeyboardButton(text='Заведующий аптекой', callback_data='Заведующий аптекой')
    ],
    [
         InlineKeyboardButton(text='Лаборант', callback_data='Лаборант'),
         InlineKeyboardButton(text='Медсестра, медбрат', callback_data='Мед сестра, мед брат')
    ],
    [
         InlineKeyboardButton(text='Мед представитель', callback_data='Мед представитель'),
         InlineKeyboardButton(text='Научный специалист', callback_data='Научный специалист')
    ],
    [
         InlineKeyboardButton(text='Спец по сертификации', callback_data='Спец по сертификации'),
         InlineKeyboardButton(text='Админ персонал', callback_data='Админ персонал')
    ],
    [InlineKeyboardButton(text='Фармацевт', callback_data='Фармацевт')]
]

med_kb = InlineKeyboardMarkup(inline_keyboard=med_start_kb)

edu_start_kb = [
         [InlineKeyboardButton(text='Бизнес-тренер', callback_data='Бизнес-тренер')],
         [InlineKeyboardButton(text='Воспитатель', callback_data='Воспитатель')],
         [InlineKeyboardButton(text='Лаборант', callback_data='Лаборант')],
         [InlineKeyboardButton(text='Методист', callback_data='Методист')],
         [InlineKeyboardButton(text='Исследователь', callback_data='Исследователь')],
         [InlineKeyboardButton(text='Психолог', callback_data='Психолог')],
         [InlineKeyboardButton(text='Учитель', callback_data='Учитель')]
]

edu_kb = InlineKeyboardMarkup(inline_keyboard=edu_start_kb)

train_start_kb = [
         [InlineKeyboardButton(text='Бизнес-тренер', callback_data='Бизнес-тренер')],
         [InlineKeyboardButton(text='Директор (HRD)', callback_data='Директор (HRD)')],
         [InlineKeyboardButton(text='Менеджер по льготам', callback_data='Менеджер по льготам')],
         [InlineKeyboardButton(text='Менеджер по персоналу', callback_data='Менеджер по персоналу')],
         [InlineKeyboardButton(text='Рук отдела персонала', callback_data='Рук отдела персонала')],
         [InlineKeyboardButton(text='Спец по кадрам', callback_data='Спец по кадрам')],
         [InlineKeyboardButton(text='Спец по подбору перс', callback_data='Спец по подбору перс')],
]

train_kb = InlineKeyboardMarkup(inline_keyboard=train_start_kb)