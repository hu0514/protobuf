import sys
import addressbook_pb2

address_book=addressbook_pb2.AddressBook()
with open(sys.argv[1],"rb") as f:
   address_book.ParseFromString(f.read())
for person in address_book.people:
    print("person id:",person.id)
    print("person name:",person.name)
    if person.email != "":
        print("person email:",person.email)
    for phone_number in person.phones:
        if phone_number.type==addressbook_pb2.Person.MOBILE:
            print("mobile phone:",end=" ")
        elif phone_number.type==addressbook_pb2.Person.HOME:
            print("home phone:",end=" ")
        elif phone_number.type==addressbook_pb2.Person.WORK:
            print("work phone:",end=" ")
        print(phone_number.number)
