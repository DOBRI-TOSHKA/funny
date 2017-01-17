"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:
Yes
Yes
Yes
No

"""

class_tree = dict()
parent_set = set()


def check_parent(parent, child):
    if parent not in parent_set:
        if parent == child:
            return True
        return False
    child_list = get_list_by_val(class_tree, parent)
    if child not in child_list:
        for node in child_list:
            result = check_parent(node, child)
            if result:
                return True
    else:
        return True
    return False


def get_list_by_val(dict_foo, val):
    ret = list()
    for key, value in dict_foo.items():
        if val in value:
            ret.append(key)
    return ret

insert_count = int(input())

for i in range(insert_count):
    data = input().split()
    if ':' not in data:
        class_tree.update({data[0]: ['OBJECT']})
    else:
        class_tree.update({data[0]: set()})
        for j in range(2, len(data)):
            class_tree[data[0]].add(data[j])
            parent_set.add(data[j])

get_count = int(input())

for i in range(get_count):
    data = input().split()
    if data[0] == data[1]:
        print('Yes')
    else:
        if check_parent(data[0], data[1]):
            print('Yes')
        else:
            print('No')
