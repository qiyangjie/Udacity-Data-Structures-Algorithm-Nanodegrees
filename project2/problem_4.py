class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return "name:{}, user:{}, group:{}".format(self.get_name(), self.get_users(), self.get_groups())


# Write a function that provides an efficient look up of whether the user is in a group.
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    if len(group.get_groups()) > 0:
        for sub_group in group.get_groups():
            if is_user_in_group(user, sub_group):
                return True
    return False


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test 1
    print(is_user_in_group(sub_child_user, parent))

    # Test 2
    print(is_user_in_group('', parent))

    # Test 3
    print(is_user_in_group('test_user', parent))

    # Test 4
    print(is_user_in_group(None, parent))