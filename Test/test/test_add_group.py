from Test.model.group import Group
import pytest
import random
import string
# из random используем функции которые что-то случайным образом выбирают
# string содержит константы хранящие списки символов

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# генерация комбинаций
#testdata = [
    #Group(name=name, header=header, footer=footer)
    #for name in ["", random_string("name", 10)]
    #for header in ["", random_string("header", 20)]
    #for footer in ["", random_string("footer", 20)]

#]
# будет сгенерирован обьект group содерщжащий случайные данные 5 раз и еще добавится список содержищий пустые строки
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),
          footer=random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#в параметре ids указывается список с текстовым представлением тестовых данных
def test_add_group(app, group):
        old_groups = app.group.get_group_list()
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
