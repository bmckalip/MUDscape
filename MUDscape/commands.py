from inspect import signature
import sqlalchemy

from .models import User
from .exceptions import LogoutException


class Command():
    """The base class for all commands"""

    @classmethod
    def help(cls):
        args = list(signature(cls.perform).parameters.keys())[1:]

        return "Usage: [{}] {}".format(' | '.join(cls.tokens), ' '.join(args))


class Look(Command):
    tokens = ['l', 'map', 'm']

    @staticmethod
    def perform(session):
        # TODO: Decide on map storage method
        return """\
╔═══════════════╗
║               ║
║               ║
║       X       ║
║               ║
║               ║
╚═══════════════╝"""


class Quit(Command):
    tokens = ['quit', 'exit', 'logout', 'logoff']

    @staticmethod
    def perform(session, *args):
        session.send('{YELLOW}Goodbye!{RESET}', prompt=False)
        raise LogoutException


class Login(Command):
    tokens = ['login']

    @staticmethod
    def perform(session):

        if session.authenticated:
            return "{YELLOW}You're already logged in!"

        user = session.require_input('{YELLOW}Please enter a username')

        try:
            account = session.conn.query(User).filter(User.name == user).one()
            password = session.require_input('{YELLOW}Please enter a password')

            if password == account.password:
                session.user = account
            else:
                session.send("{RED}Login Failed! - (Password incorrect)")
                return

        except sqlalchemy.orm.exc.NoResultFound:

            if session.require_input('{YELLOW}Account not found. Create one? [y/n]')[0] == 'y':
                #Currently loops untill passwords match
                while True:
                    password = session.require_input('{YELLOW}Please enter a password')
                    password_confirmation = session.require_input('{YELLOW}Please re-enter your password')

                    if password == password_confirmation:
                        break
                    else:
                        session.send("{YELLOW}Passwords don't match, please try again", prompt=False)


                new_user = User(name=user, password=password)
                session.conn.add(new_user)
                session.conn.commit()
                session.user = new_user
            else:
                #TODO change this to prompt for next login attempt, instead of quitting. makes more sense
                session.send('{YELLOW}Alright, disconnecting you{RESET}', prompt=False)
                raise LogoutException  # Quit


        session.authenticated = True
        session.prompt = "{GREEN}" + session.user.name + "> {RESET}"
        session.send('{GREEN}Successfully logged in!')


# Create a collection of all tokens and what command they relate to
commands = {}

for cls in Command.__subclasses__():
    for token in cls.tokens:
        if token in commands.keys():
            raise RuntimeError("The token {} is used twice in the command set".format(token))

        commands[token] = cls
