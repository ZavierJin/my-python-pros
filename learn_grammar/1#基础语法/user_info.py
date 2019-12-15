"""输入用户信息"""


def greet_user(name, **info):
    profile = {}
    profile['name'] = name
    for key, value in info.items():
        profile[key] = value
    return profile
