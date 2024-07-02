from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import CallbackQuery

import reply
import inline
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Product
users_router = Router()


class vacance_info(StatesGroup):
    area = State()
    prof_category = State()
    prof_role = State()
    salary = State()
    schedule = State()
    experience = State()
    employment = State()


@users_router.message(or_f(CommandStart(), Command('start')))
async def start(message: types.Message):
    await message.answer('Здравствуйте! Что Вы хотите посмотреть?', reply_markup=reply.start_keyboard)


@users_router.message(or_f(F.text.lower() == 'статистика', Command('statistics')))
async def statistics_cmd(message: types.Message):
    await message.answer('Общая статистика на сегодня', reply_markup=reply.del_kbd)


@users_router.message(or_f(F.text.lower() == 'вакансии', Command('vacancies')))
async def vacancies_cmd(message: types.Message, state: FSMContext):
    await message.answer('Пожалуйста, ответьте на следующие вопросы', reply_markup=reply.del_kbd)
    await state.set_state(vacance_info.area)
    await message.answer('Введите Ваш регион проживания')


@users_router.message(vacance_info.area)
async def area_input(message: types.Message, state: FSMContext):
    await state.update_data(area=message.text)
    await state.set_state(vacance_info.prof_category)
    await message.answer(text='Выберите одну из категорий', reply_markup=inline.categories_name_kb)


@users_router.callback_query(vacance_info.prof_category)
async def prof_category_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(prof_category=callback.data)
    await callback.answer('Вы выбрали категорию')
    await state.set_state(vacance_info.prof_role)
    if callback.data == 'avto_kb':
        await callback.message.answer(text='Специализация', reply_markup=inline.avto_kb)
    elif callback.data == 'admin_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.admin_kb)
    elif callback.data == 'saf_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.saf_kb)
    elif callback.data == 'manager_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.manager_kb)
    elif callback.data == 'lut_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.lut_kb)
    elif callback.data == 'home_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.home_kb)
    elif callback.data == 'it_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.it_kb)
    elif callback.data == 'art_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.art_kb)
    elif callback.data == 'advert_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.advert_kb)
    elif callback.data == 'med_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.med_kb)
    elif callback.data == 'edu_kb':
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.edu_kb)
    else:
        await callback.message.answer(text='Выберите специализацию', reply_markup=inline.train_kb)


@users_router.callback_query(vacance_info.prof_role)
async def prof_role_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(prof_role=callback.data)
    await callback.answer(f'Вы выбрали специализацию {callback.data}')
    await state.set_state(vacance_info.salary)
    await callback.message.answer('Пожалуйста укажите желаемый уровень дохода:', reply_markup=inline.salary_kb)


@users_router.callback_query(vacance_info.salary)
async def salary_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(salary=callback.data)
    await callback.answer('Вы выбрали уровень дохода')
    await state.set_state(vacance_info.schedule)
    await callback.message.answer(text="Укажите график работы", reply_markup=inline.schedule_kb)


@users_router.callback_query(vacance_info.schedule)
async def schedule_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(schedule=callback.data)
    await callback.answer('Вы выбрали график работы')
    await state.set_state(vacance_info.experience)
    await callback.message.answer(text="Укажите опыт работы", reply_markup=inline.experience_kb)


@users_router.callback_query(vacance_info.experience)
async def experience_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(experience=callback.data)
    await callback.answer('Вы выбрали опыт работы')
    await state.set_state(vacance_info.employment)
    await callback.message.answer(text="Укажите тип занятости", reply_markup=inline.employment_kb)


@users_router.callback_query(vacance_info.employment)
async def employment_input(callback: CallbackQuery, state: FSMContext, session: AsyncSession):
    await state.update_data(employment=callback.data)
    await callback.answer('Вы выбрали тип занятости')
    data = await state.get_data()
    await callback.message.answer(f'Регион: {data["area"]}\nСпециализация: {data["prof_role"]}\n'
                                  f'Уровень дохода: {data["salary"]}\nГрафик работы: {data["schedule"]}\n'
                                  f'Опыт работы: {data["experience"]}\nТип занятости: {data["employment"]}')
    if data["employment"] in inline.check:
        data["employment"] = inline.check[data["employment"]]
    if data["prof_role"] in inline.check:
        data["prof_role"] = inline.check[data["prof_role"]]

    session.add(Product(
        area=data["area"],
        prof_role=data["prof_role"],
        salary=data["salary"],
        schedule=data["schedule"],
        experience=data["experience"],
        employment=data["employment"]
    ))

    await session.commit()
    await callback.message.answer('Подтвердите, что данные указаны верно', reply_markup=reply.get_keyboard)
    await state.clear()

#@users_router.message(or_f(F.text.lower() == 'стоп', Command('stop'))
#async def stop_cmd(message: types.Message):
#    await message.answer('Была введена команда "stop"', reply_markup=reply.del_kbd)

#Inline_Keyboard
