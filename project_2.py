import csv
import pandas as pd

class Shipments:
    def __init__(self):
        self.list_of_items = []
        self.read_file()
        self.sort_list_price()

    def read_file(self):
        with open('list_of_items_1.csv', 'r', encoding='Utf-8', errors='ignore') as file:
            rdr = csv.reader(file)
            for row in rdr:
                self.list_of_items.append(row)
                # print(row)

    def sort_list_price(self):
        for i in range(len(self.list_of_items)):
            current_item = self.list_of_items[i]
            position = i

            while position > 0 and self.list_of_items[position - 1][2] > current_item[2]:
                self.list_of_items[position] = self.list_of_items[position - 1]
                position -= 1
            self.list_of_items[position] = current_item
        self.list_of_items.reverse()

        for i in self.list_of_items:
            print(i)

if __name__ == '__main__':
    Shipments()