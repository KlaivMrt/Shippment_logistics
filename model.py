import csv
import pandas as pd
import os


class Model:
    def __init__(self):
        self.directory = None
        self.path = None
        self.shipments = None
        self.volume = 0
        self.list = []

    def set_volume(self, volume):
        self.volume = volume
        # print(self.volume)

    def items_directory(self, directory):
        self.directory = directory
        file = pd.read_csv(directory)
        sorted_file = file.sort_values(by='Price', ascending=False)
        sorted_file.to_csv(directory, index=False)

    def prepare_shipments_csv(self, file_name):
        with open(self.directory, 'r') as items:
            rdr = csv.reader(items)
            lines = 0
            for line in rdr:
                lines += 1
                self.list.append(line)
            self.list.pop(0)
            # print(self.list)

        self.path = os.path.split(self.directory)
        self.shipments = f'{self.path[0]}/{file_name}.csv'
        # print(self.directory, self.path[0])

        with open(self.shipments, 'w', newline='') as file:
            shipments = 1
            counter = 0
            header = ['Name', 'Volume', 'Price']
            writer = csv.writer(file)
            writer.writerow(header)
            repeat = True

            while repeat:
                shipped_i = []
                shipment_v = 0
                total_price = 0
                volume = self.volume
                writer.writerow([''])
                writer.writerow([f'SHIPMENT : {shipments}'])

                for row in self.list:

                    if int(row[1]) <= volume:
                        volume = volume - int(row[1])
                        shipment_v += int(row[1])
                        total_price += int(row[2])
                        writer.writerow(row)
                        shipped_i.append(row)
                        counter += 1
                writer.writerow(['==========================================='])
                writer.writerow([f'Total volume and price of the shipment nr. {shipments}:', f'{shipment_v}', f'{total_price}'])
                writer.writerow(['==========================================='])
                writer.writerow([''])

                if counter == lines - 1:
                    repeat = False

                for row in shipped_i:
                    self.list.remove(row)

                shipments += 1

    def read(self):
        with open(self.directory, 'r') as items:
            i_data = items.read()
        with open(self.shipments, 'r') as delivery:
            d_data = delivery.read()

        return i_data, d_data

    def reset(self):
        self.volume = 0
        self.directory = None
        self.path = None
        self.shipments = None
        self.list = []
