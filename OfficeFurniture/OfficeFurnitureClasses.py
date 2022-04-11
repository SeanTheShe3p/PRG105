from OfficeFurniture import OfficeFurniture


class Cabinet(OfficeFurniture):

    def __init__(self, name, category, material, length, width, height, price, drawer_location, number_of_drawers, inventory):
        OfficeFurniture.__init__(self, name, category, material, length, width, height, price, inventory)
        self.drawer_location = drawer_location
        self.number_of_drawers = number_of_drawers

    def set_drawer_location(self, drawer_location):
        self.drawer_location = drawer_location

    def set_number_of_drawers(self, number_of_drawers):
        self.number_of_drawers = number_of_drawers

    def get_drawer_location(self):
        return self.drawer_location

    def get_number_of_drawers(self):
        return self.number_of_drawers

    def __str__(self):
        print("item: ", str(self.get_name()), "stock:", str(self.get_inventory()), "\nc:", str(self.get_category()),
              "\tmaterial:", str(self.get_material()), "dimensions: l-", str(self.get_length()), "w-", str(self.get_width()),
              "h-", str(self.get_height()), "drawer count:", str(self.get_number_of_drawers()), ", location:",
              str(self.get_drawer_location()), "$", format(self.get_price(), " .2f"))


class Desk(OfficeFurniture):

    def __init__(self, name, category, material, length, width, height, price, inventory):
        OfficeFurniture.__init__(self, name, category, material, length, width, height, price, inventory)


class Chair(OfficeFurniture):

    def __init__(self, name, category, material, length, width, height, price, inventory):
        OfficeFurniture.__init__(self, name, category, material, length, width, height, price, inventory)
