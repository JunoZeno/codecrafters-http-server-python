import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server started at localhost:4221")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"client_socket: {client_socket}")
        print(f"Connection from {client_address}")

        # Send HTTP response
        response = "HTTP/1.1 200 OK\r\n\r\n"
        client_socket.sendall(response.encode('utf-8'))

        # Close the client socket
        client_socket.close()


if __name__ == "__main__":
    main()
