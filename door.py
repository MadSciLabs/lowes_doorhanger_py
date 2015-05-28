from twilio.rest import TwilioRestClient

# put your own credentials here 
ACCOUNT_SID = "ACdfe9efe2ba27cf4cec7539813935c656" 
AUTH_TOKEN = "754f1063d616f4691ca1248abb4644b7" 

CLIENT_TAG = "20801160"
HOUSEKEEPING_TAG = "3687842952"

HOTEL_NUMBER = "9172078398"
 
#get rfid from hid

while (True):
  _rfid = input("rfid:");
  print(_rfid);

  if str(_rfid) == CLIENT_TAG:

    print("RFID: please clean");
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

    client.messages.create(
      to=HOTEL_NUMBER, 
      from_="+12015499399", 
      body="Please clean room",  
    )

  if str(_rfid) == HOUSEKEEPING_TAG:

    print("RFID: done cleaning");

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

    client.messages.create(
      to=HOTEL_NUMBER, 
      from_="+12015499399", 
      body="We have cleaned room",  
    )
