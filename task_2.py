import argparse
import csv
import logging

PATH = 'data.csv'


class Chat:
    def __init__(self, name, path):
        # create format for logger
        lg_handler = logging.FileHandler('errors_from_chat.log',mode='a',encoding='utf-8')
        formatt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
        lg_handler.setFormatter(formatt)

        # create logger's
        self.logger_about_user = logging.getLogger('info logger')
        self.logger_about_user.setLevel(logging.ERROR)
        self.logger_about_user.addHandler(lg_handler)

        self.logger_user_login = logging.getLogger('monitors user login')
        self.logger_user_login.setLevel(logging.INFO)
        self.logger_user_login.addHandler(lg_handler)

        # initializing variables
        self.name_file = path
        self.name = name
        self.main()

    def interface(self):
        while True:
            try:
                user_input = int(input(f'\n1 - Send massage\n'
                                       f'2 - Check to chat\n'
                                       f'3 - log out of this chat \n'
                                       f'{self.name} choose the command: '))
            except ValueError as e:
                self.logger_about_user.error(f'The {self.name} caused an error: {e}')
                print('You made a mistake! Please input number 1 or 2')
                continue
            else:
                if user_input not in [1, 2, 3]:
                    print('You made a mistake! Please input number 1 or 2')
                    continue
                else:
                    break
        return user_input

    def save_csv(self, data):
        with open(self.name_file, 'a', encoding='utf-8', newline='') as fl_csv:
            wr_csv = csv.writer(fl_csv)
            wr_csv.writerow([data])

    def send_message(self):
        user_message = input('Input you message: ')
        final_message = f'{self.name}: ' + user_message
        self.save_csv(final_message)
        print('Message successfully send to chat!\n')

    def check_chat(self):
        try:
            with open(self.name_file, 'r', encoding='utf-8') as fl_csv:
                rd_csv = csv.reader(fl_csv)
                for row in rd_csv:
                    str_row = ''.join(row)
                    print(str_row)
        except FileNotFoundError as e:
            self.logger_about_user.error(f'The {self.name} caused an error: {e}')
            print(f'Error: {e}')

    def main(self):
        while True:
            user_input = self.interface()
            if user_input == 1:
                self.send_message()
                self.logger_user_login.info(f'User {self.name} logged in chat')
            elif user_input == 2:
                self.check_chat()
            elif user_input == 3:
                print(f'{self.name}, you have logged out. Goodbye!')
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('name',type=str)
    parser.add_argument('--file_name', type=str, default='data.csv')
    args = parser.parse_args()

    test_chat = Chat(args.name, args.file_name)

