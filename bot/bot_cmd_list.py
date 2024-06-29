from aiogram.types import BotCommand

private = [BotCommand(command="start", description="старт"),
           BotCommand(command="statistics", description='Посмотреть статистику'),
           BotCommand(command="vacancies", description='Поиск вакансий'),
           BotCommand(command="stop", description='Выключить бота') ]

vacancy_test_cmd = [
    BotCommand(command="salary", description="зарплата"),
    BotCommand(command="area", description="регион"),
    BotCommand(command="professional_role", description="специализация"),
    BotCommand(command="experience", description="опыт работы"),
    BotCommand(command="employment", description="тип занятости"),
    BotCommand(command="shedule", description="график работы"),
]