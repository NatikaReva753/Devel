from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)
    group = Group(name="New name", header="New header", footer="New footer")
    group.id = modified_group.id
    app.group.modify_group_by_id(modified_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_name_two(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(name=""))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)