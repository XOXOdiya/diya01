"""this program will generate a unique Id for the staff members"""
def staff_info():
    """personal information about the member """
    global staff_id,requisition_ID,staff_name,date
 
    staff_id=int(input("enter your staff id:"))
    staff_name=(input("enter your staff name:"))
    date=(input("enter date:(dd/mm/yy)"))
   
count = 10000
while count >= 10000:
    print(count)
    count += 1
    break
 
staff_info()
"""staff_id function has ender here"""
 
def requisitions_total(**kwargs):
    """input of so many items with keywords can be done thats why i have used *kwargs"""
    staff_info()
    """dictionary start """
    items_dict={}
    number_items=("enter number of requisition items")
 
    for i in range(number_items):
        item=input("enter items:")
        price=input("enter price:")
        items_dict[item]=price
        print(items_dict)
        """dictionary end"""
        global total
        total=sum(price)
       
requisitions_total()
#requisi6tion_id function end"""
 
def request_approval():
 
 """this function is to make approval decisions based on the condition"""
 
 
if total >500:
    status=print("user approved")
   
    reference_number=((staff_id[-3:])+(requisition_ID[-3:]))
    print("refrence number:",reference_number)
 
else:
    status=print("pending")
 
 
request_approval()
 
def display_requisitions():
    """this function will show all the important details of the user"""
    staff_info[staff_id,staff_name,date,requisition_ID]
    requisitions_total[total] 
    request_approval[status,reference_number]
 
 
   
 
 


