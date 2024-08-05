import socket
from http import HTTPStatus


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server started at localhost:4221")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        # print(f"client_socket: {client_socket}") # TODO REMOVE
        print(f"Connection from {client_address}")

        # Receive the HTTP request
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # Extract the request target
        request_line = request.split('\r\n')[0]
        request_target = request_line.split(' ')[1]
        print(f"Request target: {request_target}")

        # Extract the URL
        url = request_target
        print(f"URL: {url}")

        if url == "/":
            # Send 200 HTTP response
            response = f"HTTP/1.1 {HTTPStatus.OK.value} {HTTPStatus.OK.phrase}\r\n\r\n"
        else:
            # Send 400 HTTP response
            response = f"HTTP/1.1 {HTTPStatus.NOT_FOUND.value} {HTTPStatus.NOT_FOUND.phrase}\r\n\r\n"

        print(f"Sending response: {response}")

        client_socket.sendall(response.encode('utf-8'))

        # Close the client socket
        client_socket.close()


if __name__ == "__main__":
    main()
