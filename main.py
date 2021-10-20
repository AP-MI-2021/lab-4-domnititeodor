def show_menu():
    print('1. Citire multimi')
    print('2. Verificare daca cele doua liste au acelasi numar de elemente pare')
    print('3. Intersectia celor doua multimi')
    print('4. Palindroamele obtinute prin concatenarea elementelor de pe aceeasi pozitie')
    print('5. ')
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


def show_check_even(set1, set2):
    if count_evens(set1) == count_evens(set2):
        print(f"Multimile {set1} si {set2} au acelasi numar de elemente pare")
    else:
        print("Multimile {set1} si {set2} nu au acelasi numar de elemente pare")


def count_evens(set):
    """
    Determina numarul elementelor pare dintr-un sir
    :param set: Lista de numere itnregi data spre verificare
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
    '''
    Determina daca un numar este palindrom(numar care scris invers este egal cu el insusi) sau nu
    Input:
    n, numar intreg, n >= 0
    Output:
    True, n palindrom
    False, n nepalindrom
    '''

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
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')


if __name__ == '__main__':
    test_count_evens()
    test_is_palindrome()
    main()
