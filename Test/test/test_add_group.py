from Test.model.group import Group


def test_add_group(app):
    app.group.create(Group("New", "test", "test"))

def test_add_group_two(app):
    app.group.create(Group("", "", ""))