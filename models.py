from datetime import datetime


class Task:

    counter = 0
    bad_data = 0
    all_data = 0

    @staticmethod
    def _logic_function(task):
        pass

    @classmethod
    def check(cls, task):
        try:
            if cls._logic_function(task):
                cls.counter += 1
        # не очень хорошая практика, но пока задача не стоит
        except Exception:
            cls.bad_data += 1
        finally:
            cls.all_data += 1

    @classmethod
    def info(cls):
        print('--------------------------------------')
        print(f'{cls.__name__}: ')
        print(f'верных ответов: {cls.counter}')
        print(f'не прошли проверку: {cls.bad_data}')
        print(f'проанализировано данных: {cls.all_data}')


class Task1(Task):

    @staticmethod
    def _logic_function(task):
        return False if int(task) % 2 else True


class Task2(Task):

    @staticmethod
    def _logic_function(number):
        k = 0
        for i in range(2, int(number) // 2 + 1):
            if number % i == 0:
                k += 1
        return True if k <= 0 else False


class Task3mod(Task):

    # проверим данные
    @staticmethod
    def _logic_function(task):
        result = float(task.replace(' ', '').replace(',', '.'))
        return True if result < 0.5 else False


class Task3(Task):

    @staticmethod
    def _logic_function(task):
        # приводим число в нужный вид
        # да я знаю, что скорее всего хотелось бы обработать все данные :), а не выбросить лишнее
        return True if float(task) < 0.5 else False


class Task4(Task):

    @staticmethod
    # конечно, тут можно написать проверки, или перевести в datetime, но пока не нужно
    def _logic_function(date_str: str):
        result = date_str.split()[0]
        return True if result == 'Tue' else False


class Task5(Task):

    @staticmethod
    # а вот тут придется :)
    def _logic_function(date_str: str):
        result = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        dt_result = result.strftime("%w")
        return True if dt_result == '2' else False


class Task6(Task):

    year_dict = {'01': 31, '02': 28, '03': 31,
                 '04': 30, '05': 31, '06': 30,
                 '07': 31, '08': 31, '09': 30,
                 '10': 31, '11': 30, '12': 31
                 }

    @classmethod
    # не реализовываю високосный год:)
    def _logic_function(cls, date_str: str):
        result = datetime.strptime(date_str, "%m-%d-%Y")
        dt_result = result.strftime("%w")
        month = result.strftime("%m")
        day = result.strftime('%d')
        if dt_result == '2' and int(day) in range(cls.year_dict[month] - 7, cls.year_dict[month]):
            return True
        return False
