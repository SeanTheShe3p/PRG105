from OfficeFurnitureClasses import Cabinet, Chair, Desk


def main():

    total = 0
    dk_0001 = Desk("dk_0001", "desk", "cedar", 72, 24, 36, 149.99, 10)
    dk_0002 = Desk("dk_0002", "desk", "maple", 72, 24, 36, 124.99, 10)
    dk_0003 = Desk("dk_0002", "desk", "plastic", 72, 24, 36, 99.99, 10)
    cb_0001 = Cabinet("cb_0001", "cabinet", "aluminum", 24, 18, 60, 49.99, "center", 3, 20)
    cb_0002 = Cabinet("cb_0002", "cabinet", "plastic", 24, 18, 60, 29.99, "center", 3, 20)
    cb_0003 = Cabinet("cb_0003", "cabinet", "plastic", 24, 18, 24, 19.99, "left", 2, 20)
    cb_0004 = Cabinet("cb_0004", "cabinet", "plastic", 24, 18, 24, 19.99, "right", 2, 20)
    cr_0001 = Chair("cr_0001", "chair", "cloth/plastic", 30, 30, 60, 74.99, 20)
    cr_0002 = Chair("cr_0002", "chair", "mesh/metal", 30, 30, 60, 124.99, 20)

    desks = [dk_0001, dk_0002, dk_0003]
    cabinets = [cb_0001, cb_0002, cb_0003, cb_0004]
    chairs = [cr_0001, cr_0002]

    print("LOCAL INVENTORY")
    print("_______________")
    for desk in desks:
        desk.__str__()
    for cabinet in cabinets:
        cabinet.__str__()
    for chair in chairs:
        chair.__str__()

    print()
    print("PURCHASES")
    print("Mark")
    print("desk 0001, 6\nchair 0001, 6")
    dk_0001.set_inventory(dk_0001.get_inventory() - 6)
    cr_0001.set_inventory(cr_0001.get_inventory() - 6)
    print("cost:", str(dk_0001.get_price()), "*6 =", format(dk_0001.get_price() * 6, ".2f"))
    print("cost:", str(cr_0001.get_price()), "*6 =", format(cr_0001.get_price() * 6, ".2f"))
    mark_total = ((dk_0001.get_price() * 6) + (cr_0001.get_price() * 6))
    total += mark_total
    print("TOTAL: $", format(mark_total, ".2f"))
    print()
    print("Tim")
    print("cabinet 0002, 2\nchair 0001, 1\nchair 0002, 10")
    cb_0002.set_inventory(cb_0002.get_inventory() - 2)
    cr_0001.set_inventory(cr_0002.get_inventory() - 1)
    cr_0002.set_inventory(cr_0002.get_inventory() - 10)
    print("cost:", str(cb_0002.get_price()), "*2 =", format(cb_0002.get_price() * 2, ".2f"))
    print("cost:", str(cr_0001.get_price()), "*1 =", format(cr_0001.get_price(), ".2f"))
    print("cost:", str(cr_0002.get_price()), "*10 =", format(cr_0002.get_price() * 10, ".2f"))
    tim_total = ((cb_0002.get_price() * 2) + (cr_0001.get_price()) + (cr_0002.get_price() * 10))
    total += tim_total
    print("TOTAL: $", format(tim_total, ".2f"))
    print()
    print("NEW INVENTORIES")
    for desk in desks:
        print(str(desk.get_name()), desk.get_inventory())
    for cabinet in cabinets:
        print(str(cabinet.get_name()), cabinet.get_inventory())
    for chair in chairs:
        print(str(chair.get_name()), chair.get_inventory())
    print()
    print("Sales: $", format(total, ".2f"))


main()
