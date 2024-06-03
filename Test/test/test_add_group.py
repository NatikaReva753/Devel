from Test.model.group import Group


# из random используем функции которые что-то случайным образом выбирают
# string содержит константы хранящие списки символов

# генерация комбинаций
#testdata = [
#Group(name=name, header=header, footer=footer)
#for name in ["", random_string("name", 10)]
#for header in ["", random_string("header", 20)]
#for footer in ["", random_string("footer", 20)]

#]
# будет сгенерирован обьект group содерщжащий случайные данные 5 раз и еще добавится список содержищий пустые строки


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
