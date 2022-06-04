from twilio.rest import Client
import time

# constants
FROM = "+15706168944"
CALLED = "+923117904818"
ACCOUNT_SID = "AC24c266cc092bc5f83e6ec5337b326495"
AUTH_TOKEN = "bac653544efe59efe1cb49d80c74b2c4"
LIMIT = 5

class Call:
    def __inti__(self):
        self.FROM = FROM
        self.CALLED = CALLED
        self.ACCOUNT_SID = ACCOUNT_SID
        self.AUTH_TOKEN = AUTH_TOKEN
        self.callCounter = 0
        self.LIMIT = LIMIT

    # def set_target(self):
    #     self.CALLED = str(input("Enter phone number of the target:"))

    def makeCall(self):
        client = Client(self.ACCOUNT_SID,self.AUTH_TOKEN)
        # call loop
        while self.callCounter < self.LIMIT:
            call = client.calls.create(
                url='http://demo.twilio.com/docs/voice.xml',
                to=self.CALLED,
                from_=self.FROM)
            self.callCounter = self.callCounter + 1
            print("Call # " + str(self.callCounter) + " Calling number: " + str(self.CALLED))
            time.sleep(3)
    

def main():
    robo = Call()
    # robo.set_target()
    robo.makeCall()


if __name__ == "__main__":
    main()



