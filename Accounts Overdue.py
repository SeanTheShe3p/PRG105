
def main():
    try:
        account = open('accounts.txt', 'r')
        overdue = open('over90.txt', 'r')
        account = account.readlines()
        overdue = overdue.readlines()
        overdue_list = []
        for line in overdue:
            line = line.rstrip('\n')
            for clients in account:
                clients = clients.rstrip('\n')
                # print(clients)
                if line in clients:
                    overdue_list.append(clients)
    except ImportError:
        print('the files were not fount')
    finally:
        print('these accounts are at least 90 days overdue')
        for acct in overdue_list:
            print(acct)


main()
