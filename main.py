from turingmachine import tm_sort

if __name__ == '__main__':
    try:
        print(tm_sort(input('Введите последовательность цифр: ')))
    except:
        print("Упс! Что-то пошло не так. Проверьте ввод еще раз!")


