def show_menu():
    print('1. Citire multimi')
    print('2. Verificare daca cele doua liste au acelasi numar de elemente pare')
    print('3. Intersectia celor doua multimi')
    print('4. ')
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

def show_check_even(set1,set2):
    if count_evens(set1)==count_evens(set2):
        print(f"Multimile {set1} si {set2} au acelasi numar de elemente pare")
    else:
        print("Multimile {set1} si {set2} nu au acelasi numar de elemente pare")

def count_evens(set):
    """
    Determina numarul elementelor pare dintr-un sir
    :param set: Lista de numere itnregi data spre verificare
    :return: Numarul de elemente pare din lista
    """
    e=0
    for x in set:
        if x%2==0:
            e=e+1
    return e

def test_count_evens():
    assert count_evens([2,3,4,7])==2
    assert count_evens([])==0
    assert count_evens([7,3,1,5,9])==0

def show_intersection_sets(set1,set2):
    intset1=set(set1)
    intset2=set(set2)
    intersection = intset1.intersection(intset2)
    if len(intersection)==0:
        print("Multimea vida")
    else:
        print(intersection)

def main():
    lst = []
    while True:
        show_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            set1=read_set1()
            set2=read_set2()
        elif option == '2':
            show_check_even(set1,set2)
        elif option == '3':
            show_intersection_sets(set1,set2)
        elif option == '4':
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')

if __name__ == '__main__':
    test_count_evens()
    main()