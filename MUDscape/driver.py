from socketserver import TCPServer, BaseRequestHandler
import signal
import sys
from colorama import init, Fore, Back, Style
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .commands import commands
from .models import *
from .exceptions import LogoutException
from .screens import welcome_message


class MUDHandler(BaseRequestHandler):
    def handle(self):
        print("{} connected".format(self.client_address[0]))

        # Connect to the database
        self.conn = sessionmaker(bind=Base.metadata.bind)()
        self.authenticated = False
        self.prompt = "{RED}> {RESET}"

        # Start user input
        self.send(welcome_message)
        self.loop()

    def loop(self):
        while True:
            data = self.require_input()

            try:
                command, *args = data.split()

                # Command handling
                try:
                    if not self.authenticated:
                        if command == 'login':
                            commands['login'].perform(self, *args)
                            continue

                        elif command == 'quit':
                            commands['quit'].perform(self, *args)
                            continue

                        else:
                            self.send('{YELLOW}You must log in first. Type "login"')
                            continue

                    message = commands[command].perform(self, *args)
                    self.send(message)
                except KeyError:  # No such command
                    self.send('{YELLOW}Invalid command!{RESET}')
                except TypeError:  # Syntax error
                    message = commands[command].help()
                    self.send(message)
                except LogoutException:  # User to be disconnected
                    break

            except ValueError:  # Client sends empty command
                self.send()

    def require_input(self, message=None):
        """Repeatedly prompt user for input until something is provided"""
        data = bytes()

        while len(data) == 0:
            if message:
                self.send(message)

            data = self.bufferInput().strip().decode('utf-8').lower()

        #log input attempt in server console
        print(self.client_address[0], "input: ", data)
        return data

    def send(self, message='', prompt=True):
        if prompt:
            # Add prompt if specified
            message = '{}\n{}'.format(message, self.prompt)
        else:
            message = '{}\n'.format(message)

        self.request.sendall(message.format(**Fore.__dict__).encode('utf-8'))

    def bufferInput(self):
        data = bytes()
        newLine = "b\'\\r\\n\'"
        backspace = "b\'\\x08\'"
        delete = "b\'\\x7f\'"
        #print(newLine, backspace, delete)

        while True:
            nextChar = self.request.recv(1024)
            if str(nextChar) == newLine:
                break
            elif str(nextChar) == (backspace or delete):
                #TODO add special character logic
                continue
            data = data + nextChar
        return data

def start_db():
    engine = create_engine('sqlite:///mudscape.sqlite')

    # Create all tables in db
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine


def main():
    HOST, PORT = "localhost", 8001
    server = TCPServer((HOST, PORT), MUDHandler)

    init()  # colorama
    start_db()

    print('Starting server at {}:{}'.format(HOST, PORT))
    server.serve_forever()


def sigint_handler(signal, frame):
    print('Shutting down')
    sys.exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()
