import sys, getopt, requests

def main(argv):
    username = ''
    try:
        opts, args = getopt.getopt(argv, "hu:")
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-u":
            username = arg
            if username == "":
                sys.exit(2)
            user = {"userName" : username}
            r = requests.post('http://localhost:3000/api/incrementBeverage', json = user)
            print r.text
        elif opt == "-h":
            print "Usage: <script> -u <UserName>"
        else:
            print "Usage only with arguments!"

if __name__ == "__main__":
    main(sys.argv[1:])