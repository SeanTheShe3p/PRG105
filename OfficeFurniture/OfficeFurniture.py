s
class OfficeFurniture:

    def __init__(self, name, category, material, length, width, height, price, inventory):
        self.name = name
        self.category = category
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.price = float(price)
        self.inventory = int(inventory)

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_material(self, material):
        self.material = material

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_price(self, price):
        self.price = price

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_material(self):
        return self.material

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_price(self):
        return self.price

    def get_inventory(self):
        return self.inventory

    def __str__(self):
        print("item: ", str(self.get_name()), "stock:", str(self.get_inventory()), "\nc:", str(self.get_category()), "\tmaterial:", str(self.get_material()), "dimensions: l-",
              str(self.get_length()), "w-", str(self.get_width()), "h-", str(self.get_height()), "$", format(self.get_price(), " .2f"))
