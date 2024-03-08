import sys
import os
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from syntax_check import Tests
from customer import Customer
import adding_a_customer
import filtering_sorting
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
    csv_file = "db.csv"
    if op == "r":
        program_run(csv_file, customers)
    elif op == "a":
        write_run(csv_file, customers)


def run_options(customers, op):
    if "--from-cmd" in sys.argv:
        run_in_cmd(customers, op)
    else:
        run_in_vs(customers, op)

def write_run(csv_file, add_customer):
    with open(csv_file, "a", encoding="utf-8-sig", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerow(add_customer)

def program_run(csv_file, customers):
    if not os.path.exists(csv_file):
        while open(csv_file, "w"):
            pass
    with open(csv_file, "r", encoding="utf-8-sig", newline="") as fd:
        file = csv.reader(fd)
        for fields in file:
            if not fields:
                continue
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
                    customer.add_debt(int(fields[4]), fields[5], fields[3])
                    break
            else:
                customer = Customer(*fields)
                customers.append(customer)


def print_client(list_cus):
    output = []
    list_cus.sort(key=lambda customer: customer.debt)
    for customer in list_cus:
        output.append(str(customer))
    return "\n".join(output)


def add_new_customer(customers, new):
    first, last, id, phone, debt, data, good_custom = adding_a_customer.new_customer(
        customers, new
    )
    if good_custom == False:
        new_custom = ",".join(map(str, (first, last, id, phone, debt, data)))
        return new_custom
    # print(first, last, id, phone, debt, data)
    run_options((first, last, id, phone, debt, data), "a")
    customer = Customer(first, last, id, phone, debt, data)
    customers.append(customer)
    return "Adding a customer has been successfully completed"


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
    options_message = (
        """To print the customers according to debt,\nTo add a customer (set...)\nTo delete according to parameters (select...) or exit""")
    client_sock.sendall(options_message.encode())
    while True:
        try:
            data = client_sock.recv(2048)
        except OSError:
            if not server_quit:
                print(f"Client:{client_address} left")
                all_clients.remove(client_sock)
            break
        if "quit" in data.decode():
            continue
        if "print" in data.decode():
            data = print_client(customers)
            client_sock.sendall(data.encode())
        else:
            data = data.decode()
            if data[:3] == "set":
                add_new = add_new_customer(customers, data)
                client_sock.sendall(add_new.encode())
            if data[:6] == "select":
                filtering_sorting.select_customers(customers, data)
                
            else:
                answer = "Error! input answer will not install"
                client_sock.sendall(answer.encode())


customers_list = []
run_options(customers_list, "r")

server = ("127.0.0.1", 12345)
print(f"Statring server chat on {server}")
all_clients = []
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server)
server_socket.listen(5)
Thread(target=quit_server, args=(server_socket, all_clients)).start()


while True:
    try:
        client_socket, client_address = server_socket.accept()
    except OSError:
        break
    print(f"Client: {client_address} joined")
    all_clients.append(client_socket)
    Thread(
        target=handie_client, args=(client_socket, all_clients, customers_list)
    ).start()

print("Server leaving...")
server_quit = True
for sock in all_clients:
    sock.close()


# set first name=Moshe, second name=Berdichevsky, id=302916440, phone=0544123456, date=3/4/2022, dept=200
