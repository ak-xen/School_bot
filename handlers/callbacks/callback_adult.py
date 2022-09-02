from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from support import write_form

router = Router()


class Form(StatesGroup):
    get_name = State()
    get_telephone_number = State()
    get_age = State()
    get_addr = State()
    get_lang = State()
    get_skill = State()
    get_format_learning = State()
    get_days_learning = State()
    get_time_learnings = State()
    get_how_find_us = State()
    get_another = State()


FORM_LIST = {}


@router.callback_query(text='adult')
async def adult_trial_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Сперва нужно познакомиться!\n'
                                  'Напишите имя, фамилию и отчество человека, '
                                  'который будет записан.\n'
                                  'Пример : Иванов Иван Иванович\n\n'
                                  'Вы в любой момент можете прекратить'
                                  'заполнение заявки написав сообщение'
                                  '"STOP". (Ваша заявка не будет отправлена!)')
    await state.set_state(Form.get_name)
    await callback.answer()


@router.message(Form.get_name)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['name'] = message.text
    await message.answer("Отлично!\nА теперь введите, свой номер телефона: ")
    await state.set_state(Form.get_telephone_number)


@router.message(Form.get_telephone_number)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['telephone'] = message.text
    await message.answer("Отлично!\nТеперь введите свой адрес: ")
    await state.set_state(Form.get_addr)


@router.message(Form.get_addr)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['address'] = message.text
    await message.answer("Супер!\nНапишите, через запятую какими языками"
                         "вы уже владеете! ")
    await state.set_state(Form.get_lang)


@router.message(Form.get_lang)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['list languages'] = message.text
    await message.answer("Пожалуйста, кратко опишите ваш уровень владения языком!")
    await state.set_state(Form.get_skill)


@router.message(Form.get_skill)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['description skills'] = message.text
    await message.answer("Это очень важно!\nПожалуйста, напишите какие форматы"
                         "обучения Вам более подходят\n"
                         "Групповые занятия или индивидуальные?\n"
                         "Офлайн или Онлайн формата?")

    await state.set_state(Form.get_format_learning)


@router.message(Form.get_format_learning)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['training format'] = message.text
    await message.answer("Это очень важно!\nПожалуйста, напишите в какие дни"
                         "недели, Вам удобнее заниматься!")

    await state.set_state(Form.get_days_learning)


@router.message(Form.get_days_learning)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['possible training days'] = message.text
    await message.answer("Это очень важно!\nПожалуйста, напишите в какие часы"
                         ", Вам удобнее заниматься!")

    await state.set_state(Form.get_time_learnings)


@router.message(Form.get_time_learnings)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['possible training time'] = message.text
    await message.answer("Пожалуйста, укажите как вы о нас узнали!")
    await state.set_state(Form.get_how_find_us)


@router.message(Form.get_how_find_us)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['How they find us'] = message.text
    await message.answer("Если у вас есть дополнительная информация!"
                         "\nВы можете указать ее в этом сообщении!")

    await state.set_state(Form.get_another)


@router.message(Form.get_another)
async def get_name(message: types.Message, state: FSMContext):
    if message.text == 'STOP':
        await stop_fsm(message, state)
        return
    FORM_LIST['another information'] = message.text
    await message.answer("Спасибо, что заполнили заявку!\n"
                         "Менеджер в скором времени свяжется с Вами!")

    path = await write_form(FORM_LIST)
    file = types.FSInputFile(path)
    await message.answer_document(file)
    await state.clear()
    return


async def stop_fsm(message: types.Message, state: FSMContext):
    await message.answer("Режим заполнения заявки завершен!")
    await state.clear()
