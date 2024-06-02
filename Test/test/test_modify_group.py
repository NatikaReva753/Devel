from Test.model.group import Group
import random


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    old_groups = db.get_group_list()
    group = Group(name="New name", header="New header", footer="New footer")
    group.id = random.choice(old_groups).id
    new_groups = db.get_group_list()
    group.id = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

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