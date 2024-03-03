import sys
import os
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from syntax_check import Tests
from customer import Customer
import adding_a_customer
import csv

def run_in_cmd(customers, op):
    if len(sys.argv) < 2:
        print("Error missing csv file name!")
        quit()
    csv_file = sys.argv[1]
    if op == "r":
        program_run(csv_file, customers)
    elif op == "a":
        write_run(csv_file, customers)

def run_in_vs(customers, op):
    csv_file = "db - copy.csv"
    if op == "r":
        program_run(csv_file, customers)
    elif op == "a":
        write_run(csv_file, customers)

def run_options(customers, op):
    if '--from-cmd' in sys.argv:
        run_in_cmd(customers, op)
    else:
        run_in_vs(customers, op)

def program_run(csv_file, customers):
    if not os.path.exists(csv_file):
        while open(csv_file, "w"):
            pass
    with open(csv_file, "r", encoding='utf-8-sig', newline='') as fd:
        file = csv.reader(fd)
        for fields in file:
            first = Tests.check_names(fields[0])
            if first == False:
                fields[0] = f"Error invalid: {fields[0]}"
            else:
                fields[0] = first

            last = Tests.check_names(fields[1])
            if not last:
                fields[1] = f"Error invalid: {fields[1]}"
            else:
                fields[1] = last

            id = Tests.check_id(fields[2])
            if not id:
                fields[2] = f"Invalid id:{fields[2]}"
            else:
                id = fields[2]

            phone = Tests.check_phone(fields[3])
            if not phone:
                fields[3] = f"Error invalid: {fields[3]}"

            debt = Tests.check_debt(fields[4])
            if not debt:
                fields[4] = f"Error invalid:{fields[4]}"

            data = Tests.check_data(fields[5])
            if not data:
                fields[5] = f"Error invalid: {fields[5]}"
            else:
                fields[5] = data

            for customer in customers:
                if customer.id == id:
                    customer.add_debt(int(fields[4]),fields[5],fields[3])
                    break
            else:
                print(*fields)
                customer = Customer(*fields)
                customers.append(customer)
    
def printed(list_cus):
    list_cus.sort(key=lambda customer: customer.debt)
    for customer in list_cus:
        print(customer)

def write_run(csv_file, add_customer):
    with open(csv_file, "a", encoding='utf-8-sig', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow(add_customer)

def add_new_customer(customers):
    add_customer = adding_a_customer.new_customer(customers)
    print(add_customer)
    first, last, id, phone, debt, data = add_customer
    customer = Customer(first, last, id, phone, debt, data)
    customers.append(customer)
    run_options(add_customer, "a")

def client_requests(data):
    data.split()
    print(data)

def quit_server(server_socket, all_clients):
    while True:
        e = input("")
        if e == "quit":
            for sock in all_clients:
                sock.sendall(e.encode()) 
            server_socket.close()
            break

server_quit = False
def handie_client(client_sock, all_clients, customers):
    while True:
        try:
            data = client_sock.recv(2048)
        except OSError:
            if not server_quit:
                print(f"Client:{client_address} left")
                all_clients.remove(client_sock)
            break
        if "quit" in data.decode():
            client_sock.sendall(data)
            continue
        if "print" in data.decode():
            msg = customers
            msg = program_run(customers)
        else:
            client_requests(data.decode())
        sock.sendall(msg.encode())


server = ('127.0.0.1', 12345)
print(f"Statring server chat on {server}")
all_clients = []
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server)
server_socket.listen(5)
Thread(target=quit_server, args=(server_socket, all_clients)).start()


customers_list  = []

while True:
    run_options(customers_list, "r")
    try:
        client_socket, client_address = server_socket.accept()
    except OSError:
        break
    print(f"Client: {client_address} joined")
    all_clients.append(client_socket)
    Thread(target=handie_client, args=(client_socket, all_clients, customers_list)).start()

print("Server leaving...")
server_exit = True
for sock in all_clients:
    sock.close()
    



