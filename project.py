import csv


class Shipments:
    def __init__(self):
        self.nr_items = int(input('Type the number of your items >> '))
        self.volume = float(input('Total volume available >> '))
        self.items = []

        self.get_items()
        self.sort_list_price()
        self.items_csv()
        self.shipments()

    def get_volume(self):
        repeat = True
        while repeat:
            try:
                volume = float(input('Type its volume: '))
                repeat = False
                return volume
            except ValueError:
                print('The volume must be expressed with numbers.')

    def get_price(self):
        repeat = True
        while repeat:
            try:
                price = float(input('Type its price: '))
                repeat = False
                return price
            except ValueError:
                print('The volume and price must be expressed with numbers.')

    def get_items(self):
        for i in range(self.nr_items):
            list = []
            item = input('Type your item: ')
            volume = self.get_volume()
            price = self.get_price()

            list.append(item)
            list.append(volume)
            list.append(price)
            self.items.append(list)

    def sort_list_price(self):
        for i in range(1, len(self.items)):
            current_item = self.items[i]
            position = i

            while position > 0 and self.items[position - 1][2] > current_item[2]:
                self.items[position] = self.items[position - 1]
                position -= 1

            self.items[position] = current_item
        self.items.reverse()

        for i in range(len(self.items)):
            print(self.items[i])

    def items_csv(self):
        self.items.insert(0, ['name', 'volume', 'price'])
        with open('items.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.items)
        # self.items.pop(0)

    def shipments(self):
        list = []
        nr_shipments = 1
        counter = 1
        repeat = True

        with open('shipments.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            while repeat:

                volume = self.volume
                label = [f'Shipment {nr_shipments}']
                writer.writerow(label)

                for i in range(1, len(self.items)):

                    if self.items[i][1] <= volume and self.items[i] not in list:
                        writer.writerow(self.items[i])
                        volume = volume - self.items[i][1]
                        list.append(self.items[i])
                    elif self.items[i] in list:
                        counter += 1
                        if counter == len(self.items):
                            repeat = False

                nr_shipments += 1






if __name__ == '__main__':
    Shipments()
