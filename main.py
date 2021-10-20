def show_menu():
    print('1. Citire multimi')
    print('2. Verificare daca cele doua liste au acelasi numar de elemente pare')
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
        print("Multimea vida")
    else:
        print(intersection)


def is_palindrome(n):
    """
    Determina daca un numar este palindrom
    :param n: numarul intreg dat spre verificare
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


def show_concatanated_palindromes(set1, set2):
    n = min(len(set1), len(set2))
    result = []
    for i in range(n):
        concat = int(str(set1[i]) + str(set2[i]))
        if is_palindrome(concat):
            result.append(concat)
    if (len(result)) == 0:
        print("Nu exista elemente care sa fie palindroame prin concatenare")
    else:
        print(f"Palindroamele rezultate sunt {result}")


def divisible_by_set3(x, set3):
    """
    Determina daca un numar este divizibil cu toate elementele dintr-o lista data
    :param x: Numarul dat spre verificare
    :param set3: Lista cu elemente date spre verificare
    :return: True, daca numarul este divizibil cu toate elementele din lista / False, in caz contrar
    """

    divisible = True
    for i in range(len(set3)):
        if x % set3[i] != 0:
            divisible = False
            break
    return divisible


def mirror_int(n):
    """
    Determina oglinditul unui numar intreg dat
    :param n: n, numar intreg
    :return: Oglinditul numarului n
    """
    mirror = 0
    while (n != 0):
        mirror = mirror * 10 + n % 10
        n = n // 10
    return mirror


def test_mirror_int():
    assert mirror_int(22) == 22
    assert mirror_int(347) == 743
    assert mirror_int(2) == 2


def show_mirrored_lists(set1, set2, set3):
    result1 = []
    result2 = []
    for i in range(len(set1)):
        if divisible_by_set3(set1[i], set3):
            result1.append(mirror_int(set1[i]))
        else:
            result1.append(set1[i])
    for i in range(len(set2)):
        if divisible_by_set3(set2[i], set3):
            result2.append(mirror_int(set2[i]))
        else:
            result2.append(set2[i])
    print(result1)
    print(result2)


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
    test_mirror_int()
    main()
