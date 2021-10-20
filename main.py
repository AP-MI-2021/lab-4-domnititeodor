def show_menu():
    print('1. Citire multimi')
    print('2. Verificare daca cele doua multimi au acelasi numar de elemente pare')
    print('3. Intersectia celor doua multimi')
    print('4. Palindroamele obtinute prin concatenarea elementelor de pe aceeasi pozitie')
    print('5. Procesarea elementelor divizibile')
    print('x. Exit')


def read_set1():
    set1_as_str = input('Dati prima multime: ')
    set1_as_list_of_str = set1_as_str.split(' ')
    set1 = []
    for set1_str in set1_as_list_of_str:
        set1.append(int(set1_str))
    return set1


def read_set2():
    set2_as_str = input('Dati a doua multime: ')
    set2_as_list_of_str = set2_as_str.split(' ')
    set2 = []
    for set2_str in set2_as_list_of_str:
        set2.append(int(set2_str))
    return set2


def read_set3():
    set3_as_str = input('Dati a treia multime: ')
    set3_as_list_of_str = set3_as_str.split(' ')
    set3 = []
    for set3_str in set3_as_list_of_str:
        set3.append(int(set3_str))
    return set3


def show_check_even(set1, set2):
    if count_evens(set1) == count_evens(set2):
        print(f"Multimile {set1} si {set2} au acelasi numar de elemente pare")
    else:
        print(f"Multimile {set1} si {set2} nu au acelasi numar de elemente pare")


def count_evens(set):
    """
    Determina numarul elementelor pare dintr-un sir
    :param set: Lista de numere intregi data spre verificare
    :return: Numarul de elemente pare din lista
    """
    e = 0
    for x in set:
        if x % 2 == 0:
            e = e + 1
    return e


def test_count_evens():
    assert count_evens([2, 3, 4, 7]) == 2
    assert count_evens([]) == 0
    assert count_evens([7, 3, 1, 5, 9]) == 0


def show_intersection_sets(set1, set2):
    intset1 = set(set1)
    intset2 = set(set2)
    intersection = intset1.intersection(intset2)
    if len(intersection) == 0:
        print(f"Intersectia multimilor {set1} si {set2} este multimea vida")
    else:
        print(f"Intersectia celor doua multimi este: {intersection}")


def is_palindrome(n):
    """
    Determina daca un numar este palindrom
    :param n: Numarul intreg dat spre verificare
    :return: True, n palindrom / False, n nepalindrom
    """
    copie = n
    oglindit = 0
    while (n != 0):
        oglindit = oglindit * 10 + n % 10
        n = n // 10
    if (copie == oglindit):
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(202) == True
    assert is_palindrome(23) == False
    assert is_palindrome(100) == False
    assert is_palindrome(7637) == False
    assert is_palindrome(1) == True


def concatanate_palindromes(set1, set2):
    """
    Determina lista de palindroame obtinuta prin concatenarea elementelor de pe pozitii egale din cele doua liste
    :param set1: Lista de numere intregi
    :param set2: Lista de umere intregi
    :return: Lista cu proprietatea data
    """
    n = min(len(set1), len(set2))
    result = []
    for i in range(n):
        concat = int(str(set1[i]) + str(set2[i]))
        if is_palindrome(concat):
            result.append(concat)
    return result


def test_concatanate_palindromes():
    assert concatanate_palindromes([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert concatanate_palindromes([1, 2, 3, 4], [1, 2, 3, 4]) == [11, 22, 33, 44]


def show_concatanated_palindromes(set1, set2):
    result = concatanate_palindromes(set1, set2)
    if (len(result)) == 0:
        print(f"Nu exista elemente in multimile {set1} si {set2} care sa fie palindroame prin concatenare")
    else:
        print(f"Palindroamele rezultate din multimile {set1} si {set2} sunt {result}")


def divisible_by_set3(x, set3):
    """
    Determina daca un numar este divizibil cu toate elementele dintr-o lista data
    :param x: Numarul intreg dat spre verificare
    :param set3: Lista cu elemente intregi date spre verificare
    :return: True, daca numarul este divizibil cu toate elementele din lista / False, in caz contrar
    """
    divisible = True
    for i in range(len(set3)):
        if x % set3[i] != 0:
            divisible = False
            break
    return divisible


def test_divisible_by_set3():
    assert divisible_by_set3(3, [1, 3]) == True
    assert divisible_by_set3(10, [3, 4, 7]) == False
    assert divisible_by_set3(12, [1, 2, 3, 4, 6, 12]) == True


def mirror_int(n):
    """
    Determina oglinditul unui numar intreg dat
    :param n: Numar intreg, n >= 0
    :return: Oglinditul numarului n
    """
    mirrored = 0
    while (n != 0):
        mirrored = mirrored * 10 + n % 10
        n = n // 10
    return mirrored


def test_mirror_int():
    assert mirror_int(22) == 22
    assert mirror_int(347) == 743
    assert mirror_int(2) == 2


def get_mirrored_lists(set1, set3):
    """
    Determina lista rezultata prin oglindirea elementelor divizibile cu toate elementele dintr-o lista data
    :param set1: Lista de nr intregi data spre modificare
    :param set3: Lista de nr intregi a carei elemente sunt date spre verificarea divizibilitatii
    :return: Lista de oglindite/neoglindite
    """
    result = []
    for i in range(len(set1)):
        if divisible_by_set3(set1[i], set3):
            result.append(mirror_int(set1[i]))
        else:
            result.append(set1[i])
    return result


def test_get_mirrored_lists():
    assert get_mirrored_lists([12, 22, 36, 363], [1, 2, 3, 4]) == [21, 22, 63, 363]
    assert get_mirrored_lists([22, 23, 36, 55, 363], [1, 2, 3, 4]) == [22, 23, 63, 55, 363]


def show_mirrored_lists(set1, set2, set3):
    result1 = get_mirrored_lists(set1, set3)
    result2 = get_mirrored_lists(set2, set3)
    print(f"Dupa procesare, prima multime devine {result1}")
    print(f"Dupa procesare, a doua multime devine {result2}")


def main():
    lst = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            set1 = read_set1()
            set2 = read_set2()
        elif option == '2':
            show_check_even(set1, set2)
        elif option == '3':
            show_intersection_sets(set1, set2)
        elif option == '4':
            show_concatanated_palindromes(set1, set2)
        elif option == '5':
            set3 = read_set3()
            show_mirrored_lists(set1, set2, set3)
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')


if __name__ == '__main__':
    test_count_evens()
    test_is_palindrome()
    test_divisible_by_set3()
    test_get_mirrored_lists()
    test_mirror_int()
    test_concatanate_palindromes()
    main()
