#class is named as requisition system
class requisitionsystem:
    #some values for status like approved, pending,not approved are provided here
    global requisition_id
    approved=0
    pending=0
    not_approved=0
    counter=0
    total_submitted=0

    #function instances such as date, staff id and name are given below:
    def __init__(self,date,staff_id,staff_name,email,status):
        self.date=date
        self.staff_id=staff_id
        self.staff_name=staff_name
        self.email=email
        self.status=''
    
    def d(self):
        return self.date

    def id(self):
        return self.staff_id

    def name(self):
        return self.staff_name

    def e(self):
        return self.email
 #staff_info function created to print date, name and email of user
    def staff_info(self):
        print (f"date:{self.date}","name:{self.staff_name}","email:{self.email}")
        counter=10000
        requisition_id=1+counter

#items with its prices are asked by the user in this function:
    def requisitions_details(self):
       items,price = input("Enter items and prices: ").split()
       item=print("items: ", items)
       price=print("price ", price)
       total_price=sum(price)
#approval,pending and not approved status of staff is decided through if else statement in the request_approval function
        
    def requisition_approval(self,total_price):
        if total_price>500:
            print("approved")
            self.status="approved"
            counter+=1
            status=counter+status
            reference_number=((self.staff_id[:2])+(self.staff_name[:3]))
        elif total_price<=500:
            print("pending")
            self.status="pending"
            counter+=1
            pending=counter+pending
        
        else:
            print("not approved")
            self.status=not_approved
            not_approved+=1
#in this the pending status customers are decided by the manager if they should be set approved or not and by each approval 1 is added in the approval and each non approval 1 is added in not approved
    def respond_requisition(self,status,total_price):
        if"pending" in self.status:
            if total_price>450:
                print("approved")
                self.status="approved"
                counter+=1
                approved=counter+approved
            else:
                print("not approved")
                self.status+"not approved"
                counter+=1
                not_approved=counter+not_approved
#all the functions created are called and displayed in this
    def display_requisition():
        person1=requisitionsystem("03/04/2024",202020,"john")
        person2=requisitionsystem("05/04/2024",202021,"tracy brown")
        person3=requisitionsystem("07/05/2024",202022,"emma wellington")
        person4=requisitionsystem("03/04/2024",202023,"catlin white")
        #information of person1
        print(person1.display_requisition())
        print(person1. staff_info())
        print(person1.requisitions_details())
        print(person1. requisition_approval())
        print(person1.respond_requisition)
        #information of person 2

        print(person2.display_requisition())
        print(person2. staff_info())
        print(person2.requisitions_details())
        print(person2. requisition_approval())
        print(person2.respond_requisition)
        #information of person 3
       
        print(person3.display_requisition())
        print(person3. staff_info())
        print(person3.requisitions_details())
        print(person3. requisition_approval())
        print(person3.respond_requisition)
        #information of person 4

        print(person4.display_requisition())
        print(person4. staff_info())
        print(person4.requisitions_details())
        print(person4. requisition_approval())
        print(person4.respond_requisition)
        
    def requisition_statistic(approved,pending,submitted,not_approved):
        approval=print("enteries approved:",approved)
        total_pending=print("enteries pending:",pending)
        submitted=print("enteries submitted:",submitted)
        non_approval=print("enteries not approved:",not_approved)
   # end of the code
       
       

       
      

        
