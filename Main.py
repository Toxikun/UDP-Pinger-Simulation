class Servermy:

    #default values for server: IPv4, SOCK_STREAM, TCP, and server IP
    def __init__(self, domainnumber=4, typenumber=1, protocolnum=1, ipnumber="10.0.0.1"):
        self.domainnumber = domainnumber
        self.typenumber = typenumber
        self.protocolnum = protocolnum
        self.ipnumber = ipnumber

    #this method checks if the given parameters match the expected values
    def ServerCont(self, domainnumber, typenumber, protocolnum):
        print("Server: Server take the request.")
        if domainnumber != 4:
            print("Server: domain number is not true")
            return 0
        if typenumber != 1:
            print("Server: type number is not true")
            return 0
        if protocolnum != 1:
            print("Server: protocol number is not true")
            return 0
        #if all parameters are correct server starts listening
        print("Server: Server is listening")
        return 1

    #main method that handles the ping process
    def ServerPinger(self, domainnumber, typenumber, protocolnum, ipnumber, portnumber):
        #first check the parameters using ServerCont
        result = self.ServerCont(domainnumber, typenumber, protocolnum)
        if result == 1:
            print("Server: The IP address is being checked.")
            #ip must be 10.0.0.1 otherwise deny access
            if ipnumber != "10.0.0.1":
                print("Server: Access denied.")
                return
            #check port number - only 5000 and 9000 are available
            if portnumber == 3306:
                #3306 is used by MySQL so its not available
                print("Server: Port 3306 is occupied by MySQL server.")
                print("Server: Access denied.")
                return
            elif portnumber != 5000 and portnumber != 9000:
                #any other port is also not available
                print("Server: Access denied.")
                return
            #calculate RTT using the formula from the assignment
            #X = portnumber / 1000
            #RTT = 10000 / (X^2 + 3*X)
            X = portnumber / 1000
            RoundTripTime = 10000 / (X ** 2 + 3 * X)
            #if RTT is less than 100ms its acceptable, otherwise too high
            if RoundTripTime < 100:
                print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is acceptable.")
            else:
                print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is too high.")


#Client class - sends ping requests to the server
class Clientmy:

    def __init__(self, domainnumber, typenumber, protocolnum):
        self.domainnumber = domainnumber
        self.typenumber = typenumber
        self.protocolnum = protocolnum

    #checks client parameters and creates the client if valid
    def Clientcreat(self, domainnumber, typenumber, protocolnum, clientip):
        #same checks as ServerCont but for the client side
        if domainnumber != 4:
            print("Client: domain number is not true")
            return 0
        if typenumber != 1:
            print("Client: type number is not true")
            return 0
        if protocolnum != 1:
            print("Client: protocol number is not true")
            return 0
        #only 10.0.0.6 is available for the client, others are busy
        if clientip != "10.0.0.6":
            print("Client: The device is busy")
            return 0
        print("Client: Client is created")
        print("Client: Client is ready to connection")
        #after client is created, start the ping request process
        self.Pingrequest()
        return 1

    #takes input from user and sends ping to the server
    def Pingrequest(self):
        #client port must be 9000
        clientport = int(input("Client: Enter Client port number:"))
        if clientport != 9000:
            print("Client: Error is occurred.")
            return
        #get server ip and destination port from user
        serverip = input("Client: Enter Server IP:")
        destport = int(input("Client: Enter Destination Port Number:"))
        #create a server object and call ServerPinger with the parameters
        server = Servermy()
        server.ServerPinger(self.domainnumber, self.typenumber, self.protocolnum, serverip, destport)


#Main part - program starts here
#get connection parameters from user
domainnumber = int(input("Enter domain number:"))
typenumber = int(input("Enter type number:"))
protocolnum = int(input("Enter protocol number:"))
clientip = input("Enter Client IP number:")

#create client object and try to establish connection
client = Clientmy(domainnumber, typenumber, protocolnum)
client.Clientcreat(domainnumber, typenumber, protocolnum, clientip)

print("Program closed.")
