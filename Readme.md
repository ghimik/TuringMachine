# Turing Machine Sorting

## Описание

Этот проект представляет собой реализацию машины Тьюринга, которая сортирует последовательности цифр. Машина использует методы, основанные на теории автоматов, и управляется набором состояний и переходов.

## Структура проекта

Проект включает в себя следующие модули:

### package `turingmachine`
- `Tape.py`: Определяет ленту машины Тьюринга, включая методы для чтения, записи и перемещения.
- `TuringMachine.py`: Основной класс, реализующий логику работы машины Тьюринга.
- `Alphabet.py`: Определяет алфавит, используемый машиной.
- `State.py`: Определяет состояния машины Тьюринга.
- `TransitionFunction.py`: Определяет функции перехода между состояниями.
- `configs.py`: Конфигурации, включая режим отладки.
- `selectsort.py`: Реализация сортировки, которая используется в качестве функционального элемента.
### Демонстрационный модуль
- `main.py`: Обертка для сортировки.
- `replace.py`: Пробная программа на машине тьюринга, заменяющая нули на единицы

## Установка

Для работы с проектом необходимо иметь установленный Python 3.6 или выше. Рекомендуется создать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```

## Запуск
Для запуска сортировки с помощью машины Тьюринга с последовательностью цифр можно использовать следующий скрипт:
```bash
python main.py
```
_P.S. Время конечно полиномиальное, но не гарантируется, что сортировка не займет вечность ;)_

## Пример ввода:
```commandline
Введите последовательность цифр: 112331
```
## Пример вывода:
```commandline
Отсортированная лента: 112233
Значимая часть ленты: 112233
Отсортированное питоном: 112233
NORMALNO OTSORTIROVAL?? True
```

## Функции
## Основные функции проекта:
- **Сортировка цифр:** Машина Тьюринга сортирует входные цифры и выводит отсортированную последовательность.
- **Переходы состояний:** Машина использует заранее определенные состояния и функции перехода для обработки входных данных.