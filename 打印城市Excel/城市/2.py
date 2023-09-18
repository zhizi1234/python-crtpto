import json
import xlwt

class Addr:
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding="utf-8")
        self.sheet = self.workbook.add_sheet("sheets")
        self.sheet.write_merge(0, 1, 0, 0, "编号")
        self.sheet.write_merge(0, 0, 1, 2, "城市")
        self.sheet.write(1, 1, "城市编码")
        self.sheet.write(1, 2, "城市名")
        self.sheet.col(1).width = 256 * 20
        self.i = 1
        self.cities = self.load_cities()

    def load_cities(self):
        with open("city.json", encoding="utf-8") as f:
            cities = json.load(f)
        return cities

    def write_city_data(self, city_id, city_name):
        self.i += 1
        self.sheet.write(self.i, 0, self.i)
        self.sheet.write(self.i, 1, city_id)
        self.sheet.write(self.i, 2, city_name)
        print("第{}行城市数据写入成功...".format(self.i))

    def process_cities(self):
        for city_data in self.cities:
            city_id = city_data["id"]
            city_name = city_data["name"]
            self.write_city_data(city_id, city_name)


    def save_to_file(self):
        self.workbook.save("cities.xls")

if __name__ == '__main__':
    addr = Addr()
    addr.process_cities()
    addr.save_to_file()
