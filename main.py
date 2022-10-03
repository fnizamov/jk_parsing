from parser1 import Parser
from models import Deputat, db


def check_connection(func):
    def wrapper(*args, **kwargs):
        try:
            db.connect()
            func(*args, **kwargs)
        finally:
            db.close()
    return wrapper

@check_connection
def insert_data():
    db.create_tables([Deputat])
    objs = Parser().data
    with db.atomic():
        Deputat.insert_many(objs).execute()
    # for deputat in objs:
    #     Deputat.create(**deputat)

# TODO: Создать класс CRUD, который будет содержать методы для:
    # 1) Создания записей,
    # 2) Удаления записей,
    # 3) Обновления записей,
    # 4) Получения записей.


if __name__ == '__main__':
    insert_data()