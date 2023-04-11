import argparse

def fill(data):
    return (8 - len(data)) * '0' + data

def send(filename, output):
    with open(output, "wt") as output:
        with open(filename, "rb") as f:
            data = f.read(1) # read one byte
            while data: # Verify if there is more data
                value = fill(str(bin(data[0]))[2:]) # convert a byte a 8 bit
                                                    # string
                output.write(value + "\n") # write to file
                
                data = f.read(1) # read next byte

def reader(filename, output):
    with open(output, "wb") as output:
        with open(filename, "rt") as f:
            for line in f:
                int_value = int(line, base=2) # convert the binary string to int
                byte_value = int_value.to_bytes(length=1, byteorder="big") # convert the int to a byte
                output.write(byte_value) # write to file

def main():
    aparse = argparse.ArgumentParser()
    aparse.add_argument("input_file", type=str, help="Digite o nome do arquivo de audio")
    aparse.add_argument("middle_file", type=str, help="Digite o nome do arquivo que representa os frames")
    aparse.add_argument("output_file", type=str, help="Digite o nome do arquivo para salvar o arquivo recebido")
    args = aparse.parse_args()
    
    data_to_send = args.input_file
    middle_file =  args.middle_file
    data_received = args.output_file

    send(data_to_send, middle_file)
    reader(middle_file, data_received)
    
    

if __name__ == "__main__":
    main()
