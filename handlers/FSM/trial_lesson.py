from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Questionnaire(StatesGroup):
    choosing_adult_ot_young = State()


