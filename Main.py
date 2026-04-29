class Servermy:
    """Simulates a UDP server for the Pinger application."""

    def __init__(self, domainnumber=4, typenumber=1, protocolnum=1, ipnumber="10.0.0.1"):
        self.domainnumber = domainnumber
        self.typenumber = typenumber
        self.protocolnum = protocolnum
        self.ipnumber = ipnumber

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
        print("Server: Server is listening")
        return 1

    def ServerPinger(self, domainnumber, typenumber, protocolnum, ipnumber, portnumber):
        result = self.ServerCont(domainnumber, typenumber, protocolnum)
        if result == 1:
            print("Server: The IP address is being checked.")
            if ipnumber != "10.0.0.1":
                print("Server: Access denied.")
                return
            # Check port number
            if portnumber == 3306:
                print("Server: Port 3306 is occupied by MySQL server.")
                print("Server: Access denied.")
                return
            elif portnumber != 5000 and portnumber != 9000:
                print("Server: Access denied.")
                return
            # RTT Calculation
            X = portnumber / 1000
            RoundTripTime = 10000 / (X ** 2 + 3 * X)
            if RoundTripTime < 100:
                print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is acceptable.")
            else:
                print("Server: Round Trip Time is=" + str(RoundTripTime) + " The value is too high.")


class Clientmy:
    """Simulates a UDP client for the Pinger application."""

    def __init__(self, domainnumber, typenumber, protocolnum):
        self.domainnumber = domainnumber
        self.typenumber = typenumber
        self.protocolnum = protocolnum

    def Clientcreat(self, domainnumber, typenumber, protocolnum, clientip):

        if domainnumber != 4:
            print("Client: domain number is not true")
            return 0
        if typenumber != 1:
            print("Client: type number is not true")
            return 0
        if protocolnum != 1:
            print("Client: protocol number is not true")
            return 0
        if clientip != "10.0.0.6":
            print("Client: The device is busy")
            return 0
        print("Client: Client is created")
        print("Client: Client is ready to connection")
        self.Pingrequest()
        return 1

    def Pingrequest(self):
        clientport = int(input("Client: Enter Client port number:"))
        if clientport != 9000:
            print("Client: Error is occurred.")
            return
        serverip = input("Client: Enter Server IP:")
        destport = int(input("Client: Enter Destination Port Number:"))
        server = Servermy()
        server.ServerPinger(self.domainnumber, self.typenumber, self.protocolnum, serverip, destport)


# ======================== MAIN ========================
domainnumber = int(input("Enter domain number:"))
typenumber = int(input("Enter type number:"))
protocolnum = int(input("Enter protocol number:"))
clientip = input("Enter Client IP number:")

client = Clientmy(domainnumber, typenumber, protocolnum)
client.Clientcreat(domainnumber, typenumber, protocolnum, clientip)

print("Program closed.")
