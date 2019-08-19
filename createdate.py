import sys
import addressbook_pb2
address_book=addressbook_pb2.AddressBook()
person=address_book.people.add()
person.id=int(input("enter person id number:"))
person.name=input("enter person name:")
email=input("enter email address(blank for none):")
if email!="":
   person.email=email
while True:
   number=input("input a phone number(or leave blank to finish)")
   if number=="":
       break
   phone_number=person.phones.add()
   phone_number.number=number
   type=input("is this a mobile,home,or work phone?")
   if type=="mobile":
       phone_number.type=addressbook_pb2.Person.MOBILE
   elif type=="home":
       phone_number.type=addressbook_pb2.Person.HOME
   elif type=="work":
       phone_number.type=addressbook_pb2.Person.WORK
   else:
       print("unknown phone type; leaving as default value")

with open(sys.argv[1],"wb") as f:
   f.write(address_book.SerializeToString())


