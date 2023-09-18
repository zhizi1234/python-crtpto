import json
import xlwt

class Addr:
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding="utf-8")
        self.sheet = self.workbook.add_sheet("sheets")
        self.sheet.write_merge(0, 1, 0, 0, "编号")
        self.sheet.write_merge(0, 0, 1, 2, "省份")
        self.sheet.write_merge(0, 0, 3, 4, "城市")
        self.sheet.write_merge(0, 0, 5, 6, "区/县")
        self.sheet.write_merge(0, 0, 7, 8, "乡/镇")
        self.sheet.write(1, 1, "省编码")
        self.sheet.write(1, 2, "省名")
        self.sheet.write(1, 3, "市编码")
        self.sheet.write(1, 4, "市名")
        self.sheet.write(1, 5, "区/县编码")
        self.sheet.write(1, 6, "区/县名")
        self.sheet.write(1, 7, "乡/镇编码")
        self.sheet.write(1, 8, "乡/镇名")
        self.sheet.col(1).width = 256 * 20
        self.sheet.col(3).width = 256 * 20
        self.sheet.col(5).width = 256 * 20
        self.sheet.col(7).width = 256 * 20
        self.sheet.col(8).width = 256 * 20
        self.i = 1
        self.addr = self.load_data()

    def load_data(self):
        with open("province.json", encoding="utf-8") as f:
            provinces = json.load(f)
        return provinces

    def write_data(self, pro_id, pro_name, city_id, city_name, county_id, county_name, town_id, town_name):
        self.i += 1
        self.sheet.write(self.i, 0, self.i)
        self.sheet.write(self.i, 1, pro_id)
        self.sheet.write(self.i, 2, pro_name)
        self.sheet.write(self.i, 3, city_id)
        self.sheet.write(self.i, 4, city_name)
        self.sheet.write(self.i, 5, county_id)
        self.sheet.write(self.i, 6, county_name)
        self.sheet.write(self.i, 7, town_id)
        self.sheet.write(self.i, 8, town_name)
        print("第{}行数据写入成功...".format(self.i))

    def process_data(self):
        for pro_data in self.addr:
            pro_id = pro_data.get("id")
            pro_name = pro_data.get("name")
            for city_data in self.city(pro_id):
                city_id = city_data.get("id")
                city_name = city_data.get("name")
                if self.county(city_id):
                    for county_data in self.county(city_id):
                        county_id = county_data.get("id")
                        county_name = county_data.get("name")
                        if self.town(county_id):
                            for town_data in self.town(county_id):
                                town_id = town_data.get("id")
                                town_name = town_data.get("name")
                                self.write_data(pro_id, pro_name, city_id, city_name, county_id, county_name, town_id, town_name)
                        else:
                            self.write_data(pro_id, pro_name, city_id, city_name, county_id, county_name, "NON", "NON")
                else:
                    self.write_data(pro_id, pro_name, city_id, city_name, "NON", "NON", "NON", "NON")

    def province(self):
        return self.addr

    def city(self, id):
        with open("city.json", encoding="utf-8") as f:
            cities = json.load(f)
        return cities[str(id)]

    def county(self, id):
        with open("county.json", encoding="utf-8") as f:
            counties = json.load(f)
        try:
            return counties[str(id)]
        except:
            return []

    def town(self, id):
        with open("town.json", encoding="utf-8") as f:
            towns = json.load(f)
        try:
            return towns[str(id)]
        except:
            return []

    def save_to_file(self):
        self.workbook.save("test.xls")

if __name__ == '__main__':
    addr = Addr()
    addr.process_data()
    addr.save_to_file()
