def true_or_false():
    list_true = [True] * 5
    list_false = [False] * 5
    list_one_true = list_false.copy()
    list_one_true[4] = True
    list_one_false = list_true.copy()
    list_one_false[4] = False
    list_void = []
    list_all = [list_true, list_false,
                list_one_true, list_one_false, list_void]

    for case in list_all:
        print(case)
        print("All: ", all(case))
        print("Any: ", any(case))


true_or_false()
