import socket

def server():
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 9999        # Port to bind to

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)  # Listen for a connection

    print(f"Listening on {host}:{port}...")
    conn, addr = s.accept()
    print(f"Connection established from {addr}")

    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            conn.send(b"exit")
            break

        conn.send(command.encode())
        response = conn.recv(1024).decode()

        print(f"Response: {response}")

    conn.close()

if __name__ == "__main__":
    server()
