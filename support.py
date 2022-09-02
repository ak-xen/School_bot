import time
import json


def on_startup():
    print('Bot started!')


async def write_form(all_records: dict):
    path = f'data/forms/{time.strftime("%d.%m.%Y")}.json'
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(all_records, file, ensure_ascii=False, indent=4)
    return path
