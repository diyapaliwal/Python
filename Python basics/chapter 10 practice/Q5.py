# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random
class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def booking(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getstatus(self):
        print(f"{self.trainNo} have 123 seats")
    
    def getfare(self, fro, to ):
        print(f"Ticket fare in train no:{self.trainNo} running from {fro} to {to} is {random.randint(222,5555)}")
    
IndianRailway = train(12345)
IndianRailway.booking("udaipur","gurgaon")
IndianRailway.getstatus()
IndianRailway.getfare("udaipur","gurgaon")