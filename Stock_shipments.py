import csv

class Shipments:
    def __init__(self, volume):
        self.volume = volume
        self.list_of_items = []
        self.read_file()
        self.sort_list_price()
        self.shipments()

    def read_file(self):
        with open('list_of_items.csv', 'r', encoding='Utf-8') as file:
            rdr = csv.reader(file)
            row_counter = 0
            for row in rdr:
                if row_counter == 0:
                    pass
                else:
                    self.list_of_items.append(row)
                row_counter += 1

    def sort_list_price(self):
        for i in range(1, len(self.list_of_items)):
            current_item = self.list_of_items[i]
            position = i

            while position > 0 and int(self.list_of_items[position - 1][2]) > int(current_item[2]):
                self.list_of_items[position] = self.list_of_items[position - 1]
                position -= 1
            self.list_of_items[position] = current_item
        self.list_of_items.reverse()

        for i in self.list_of_items:
            print(i)

    def shipments(self):
        list = []
        nr_shipments = 1
        counter = 1
        repeat = True

        with open('shipments.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            info = ['Name', 'Volume', 'Price']
            writer.writerow(info)
            while repeat:

                volume = self.volume
                label = [f'Shipment {nr_shipments}']
                writer.writerow(label)

                for i in range(len(self.list_of_items)):

                    if int(self.list_of_items[i][1]) <= volume and self.list_of_items[i] not in list:
                        writer.writerow(self.list_of_items[i])
                        volume = volume - int(self.list_of_items[i][1])
                        list.append(self.list_of_items[i])
                    elif self.list_of_items[i] in list:
                        counter += 1
                        if counter == len(self.list_of_items):
                            repeat = False

                nr_shipments += 1

if __name__ == '__main__':
    Shipments(10000)