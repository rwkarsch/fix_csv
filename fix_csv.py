import csv


def read_lines(input_file, output_file):
    csv.register_dialect('pipes', delimiter='|')
    writer = csv.writer(output_file)
    reader = csv.reader(input_file, dialect='pipes')
    for row in reader:
        print(f'{row}. Length of line is {len(row)}')
        writer.writerow(row)
    

if __name__ == "__main__":
    input_file = open("input_file.csv")
    output_file = open("output_file.csv", 'wt')
    read_lines(input_file, output_file)
    
    