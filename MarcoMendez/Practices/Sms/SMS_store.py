class SMS_store:
    mySmsStore={}

    # my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
    def add_new_arrival(self,from_number,time_arrived,text_of_SMS):
        aux = self.mySmsStore.get(from_number)
        resultIsExisteElement = aux
        if(str(resultIsExisteElement) != str('None')):
            list = []
            list = aux
            message = time_arrived + " : " + text_of_SMS +":Status : False "
            list.append(str(message))
            self.mySmsStore[from_number] = list
        else:
            list = []
            message = time_arrived + " : " + text_of_SMS + ":Status : True "
            list.append(str(message))
            self.mySmsStore[from_number] = list

    def message_count(self):
        print("The amount message are : ", str(self.mySmsStore.__len__()))


    def get_unread_indexes(self):
        print("======================================")
        print("Message unread")
        for i in self.mySmsStore:
            list = []
            list = self.mySmsStore.get(i)
            index = 0
            for keys in list:
                arrayMessage = keys.split(":")
                index += 1
                if(arrayMessage[4] == " False "):
                    print("This message unread of:", keys, " message # : ", str(index))
        print("======================================")

    def get_message(self,index):
        print("======================================")
        print("Get Message ")
        result ="None"
        count = 1
        for i in self.mySmsStore:
            list = []
            list = self.mySmsStore.get(i)
            for keys in list:
                cad = keys.split(":")
                if (cad[4] == " False "):
                    list[count] = cad[0]+cad[1]+cad[2]+cad[3]+ " True "
                    self.mySmsStore[i] = cad
                if index == count:
                    result = "This is the message : " + str(cad[0]+cad[1]+cad[2]+cad[3])
            count += 1
            return result
        print("======================================")

    def delete(self,index):
        count = 1
        key = ""
        for i in self.mySmsStore:
            if count == index:
                key = i
            count += 1
        self.mySmsStore.pop(key)
    def clear(self):
        self.mySmsStore.clear()



my_inbox = SMS_store()

my_inbox.add_new_arrival("77884632","1/16/18:10-12 AM","hola marco")
my_inbox.add_new_arrival("77884632","1/16/18:10-13 AM","hola como estas")

my_inbox.add_new_arrival("72282814","1/16/18:10-13 AM","hola que tal??")

print(my_inbox.mySmsStore)
my_inbox.message_count()

my_inbox.get_unread_indexes()

print(my_inbox.get_message(1))
print(my_inbox.mySmsStore)


my_inbox.delete(1)

my_inbox.clear()
print(my_inbox.mySmsStore)
