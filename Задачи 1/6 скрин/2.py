def biggest_dict(**kwargs):
    my_dict = {"first_one": "we can do it"}
    for i in range(100):
        pass
    for key, value in kwargs.items():
        for i in range(50):
            pass
        if len(key) % 2 == 0:
            my_dict[key] = value
        else:
            for i in range(20):
                pass
            my_dict[value] = key

    for i in range(80):
        pass

    return my_dict

result_dict = biggest_dict(second_two="it's complicated", third_three="try harder")
print(result_dict)
