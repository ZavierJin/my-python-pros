"""一个试验用的用户的类"""


class Users():
    """docstring for User"""
    def __init__(self, name):
        self.name = name
        self.point = 2

    def update_point(self, increment):
        if increment >= 0:
            self.point += increment
        else:
            print("Error!")


class Privileges():
    def __init__(self):
        self.privileges = (
            "can add post",
            "can delete post",
            "can ban user",
            )

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege, end='###')


class Admin(Users):
    def __init__(self, name):
        super().__init__(name)
        self.size = 70
        self.privilege = Privileges()

    def up_size(self, increment):
        self.size += increment
        print("HHH " + str(self.size))
