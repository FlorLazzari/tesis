def fraccionar(vector):
    v_0 = len(vector)-1
    v_1 = int(v_0 * 0.75)
    v_2 = int(v_0 / 2)
    v_3 = int(v_0 / 3)
    return v_0, v_1, v_2, v_3
