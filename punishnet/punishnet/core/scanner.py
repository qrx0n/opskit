import socket
import threading



class Scanner:
    def __init__(
            self, target, ports):
        self.target = target
        self.ports = ports

        self.db = []


    def scan_port(
            self, host, port,
            timeout):
        scanner = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        scanner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        scanner.settimeout(timeout)

        try:
            scanner.connect((host, port))
            self.db.append(port)

        except:
            pass


    def scan_ports(
            self, host):
        tmp_threads = [

        ]

        for threadnum in range(self.ports):
            thread = threading.Thread(
                target=self.scan_port, args=(host, threadnum, 0.5))
            tmp_threads.append(thread)

        for threadnum in range(self.ports):
            tmp_threads[threadnum].start()

        for threadnum in range(self.ports):
            tmp_threads[threadnum].join()

        return self.db
