from testfunc import test
# from pt_recursive import solve
# from pt_iteration1 import solve
# from pt_combination3 import solve
from pt_final import solve

test_data1 = [
    ((1, 1),    1),
    ((2, 1),    1),
    ((2, 2),    1),
    ((3, 1),    1),
    ((3, 2),    2),
    ((3, 3),    1),
    ((4, 2),    3),
    ((5, 2),    4),
    ((5, 3),    6),
    ((9, 5),    70)
]

# large value
test_data2 = [
    ((30, 15),          77558760),
    ((100, 50),         50445672272782096667406248628),
    ((30000, 30000),    1),
    ((30000, 29998),    449955001)
]

# illegal input
test_data3 = [
    ((1, 2),        None),
    (('1', 1),      None),
    ((1, -1),       None),
    ((1, 100000),   None)
]

test(solve, test_data1)
test(solve, test_data2)
# test(solve, test_data3)
