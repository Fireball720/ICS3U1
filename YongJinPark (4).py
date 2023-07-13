from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import *
import datetime





#Today's Date
year = datetime.date.today().year #gets current year
month = datetime.date.today().month #gets current month
day = datetime.date.today().day#gets current day

#DATABASE--------------------------------

database=[]


#Functions
def calculatePrice(): #Calculates the price of the visit
    pass
    #TotalPrice = (days_of_visit+ sum_of_acitivites)*(1+((num_of_ppl-1)*0.5))*site_area_multiplier

def widget_reset(): #Resets widgets between frame switches
    firstnameVar.set('First Name')
    lastnameVar.set('Last Name')
    phoneVar.set('Phone #')
    emailVar.set('Email Address')
    birthdayVar.set(1)
    birthmonthVar.set('December')
    birthyearVar.set(1940)
    arrivaldayVar.set(1)
    arrivalmonthVar.set('December')
    arrivalyearVar.set(2023)
    departuredayVar.set(1)
    departuremonthVar.set('December')
    departureyearVar.set(2023)
    numofpeopleVar.set(1)
    sitenumberVar.set(1)
    sitelocationVar.set('Beach')
    medicalText.delete('1.0', END)
    canoeVar.set(0)
    treeVar.set(0)
    rockVar.set(0)
    hikingVar.set(0)
    fishingVar.set(0)
    canoeTimeVar.set(0)
    treeTimeVar.set(0)
    rockTimeVar.set(0)
    hikingTimeVar.set(0)
    fishingTimeVar.set(0)
    canoeTimeRadioButton1['state'] = DISABLED
    canoeTimeRadioButton2['state'] = DISABLED
    canoeTimeRadioButton3['state'] = DISABLED
    treeTimeRadioButton1['state'] = DISABLED
    treeTimeRadioButton2['state'] = DISABLED
    treeTimeRadioButton3['state'] = DISABLED
    rockTimeRadioButton1['state'] = DISABLED
    rockTimeRadioButton2['state'] = DISABLED
    rockTimeRadioButton3['state'] = DISABLED
    hikingTimeRadioButton1['state'] = DISABLED
    hikingTimeRadioButton2['state'] = DISABLED
    hikingTimeRadioButton3['state'] = DISABLED
    fishingTimeRadioButton1['state'] = DISABLED
    fishingTimeRadioButton2['state'] = DISABLED
    fishingTimeRadioButton3['state'] = DISABLED

def switch_frames(): #Switches between the search and the registration frame
    if switchButton['text'] == "Switch to Search":
        searchFrame.grid(row=2, column=3, columnspan=2, sticky=NSEW) #grids the search frame
        activityFrame.grid_remove()#removes the activity frame
        switchButton.configure(text="Switch to Register")
        registrationFrame.configure(text="User Information")
        widget_reset()#resets widgets
    else:
        searchFrame.grid_remove()#removes the search frame
        activityFrame.grid()#grids the activity frame
        switchButton.configure(text="Switch to Search")
        registrationFrame.configure(text="Registration")
        widget_reset() #resets widgets

def month_to_number(month): #changes the month string value into the corresponding month number
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months.index(month) + 1
                                                
def site_location_to_multiplier(site): #changes the location string into the corresponding price multiplier
    if site == "Beach":
        return 1.4
    elif site == "Field":
        return 1
    elif site == "Birch":
        return 1.2
    elif site == "Maple":
        return 1.3

def register_user(): 
    if confirmVar.get()==1: #checks if the confirm check button is checked
        #gets all the variables that go into the registration
        first_name           = firstnameVar.get()
        last_name            = lastnameVar.get()
        phone                = phoneVar.get()
        email                = emailVar.get()
        birthday             = birthdayVar.get()
        birthmonth           = birthmonthVar.get()
        birthyear            = birthyearVar.get()
        arrivalday           = arrivaldayVar.get()
        arrivalmonth         = arrivalmonthVar.get()
        arrivalyear          = arrivalyearVar.get()
        departureday         = departuredayVar.get()
        departuremonth       = departuremonthVar.get()
        departureyear        = departureyearVar.get()
        numofpeople          = numofpeopleVar.get()
        sitenumber           = sitenumberVar.get()
        sitelocation         = sitelocationVar.get()
        medicalinfo          = medicalText.get("1.0",'end-1c')
        canoeprice           = canoeVar.get()
        treeprice            = treeVar.get()
        rockprice            = rockVar.get()
        hikingprice          = hikingVar.get()
        fishingprice         = fishingVar.get()
        
        days_of_visit = abs((departureyear*365+month_to_number(departuremonth)*30+departureday)-(arrivalyear*365+month_to_number(arrivalmonth)*30+arrivalday))#subtracts the number of days of arrival from departure to find total length of stay
        sum_of_activities = canoeprice+treeprice+rockprice+hikingprice+fishingprice #adds the prices of all the activities
        
        TotalPrice = (days_of_visit*30+ sum_of_activities)*(1+((numofpeople-1)*0.5))*site_location_to_multiplier(sitelocation) #calculation for total price of user's visit
        
        result = askquestion("Price", f"The total price of your visit is: {TotalPrice:.2f}") #asks to confirm if the user 
        if result == "yes":#if the user presses yes to the question
            activities = []
            if canoeprice > 0: #Checks if the check box is checked
                if canoeTimeVar.get() == 1: #checks if the morning radio button is checked
                    time = 'Morning'
                elif canoeTimeVar.get() == 2:#checks if the noon radio button is checked
                    time = 'Noon'
                elif canoeTimeVar.get() == 3:#checks if the afternoon radio button is checked
                    time = 'Afternoon'
                activities.append(['Canoeing', time]) #appends a list to the activities list
            if treeprice > 0:
                if rockTimeVar.get() == 1:
                    time = 'Morning'
                elif rockTimeVar.get() == 2:
                    time = 'Noon'
                elif rockTimeVar.get() == 3:
                    time = 'Afternoon'
                activities.append(['Tree Trecking', time])
            if rockprice > 0:
                if treeTimeVar.get() == 1:
                    time = 'Morning'
                elif treeTimeVar.get() == 2:
                    time = 'Noon'
                elif treeTimeVar.get() == 3:
                    time = 'Afternoon'
                activities.append(['Rock Climbing', time])
            if hikingprice > 0:
                if hikingTimeVar.get() == 1:
                    time = 'Morning'
                elif hikingTimeVar.get() == 2:
                    time = 'Noon'
                elif hikingTimeVar.get() == 3:
                    time = 'Afternoon'
                activities.append(['Hiking', time])
            if fishingprice > 0:
                if fishingTimeVar.get() == 1:
                    time = 'Morning'
                elif fishingTimeVar.get() == 2:
                    time = 'Noon'
                elif fishingTimeVar.get() == 3:
                    time = 'Afternoon'
                activities.append(['Fishing', time])

                
        user_info = {'first name' : first_name, 'last name' : last_name, 'phone' : phone, \
                     'email' : email, 'day of birth' : birthday, 'month of birth' : birthmonth, \
                     'year of birth' : birthyear, 'day of arrival' : arrivalday, \
                     'month of arrival' : arrivalmonth, 'year of arrival' : arrivalyear, \
                     'day of departure' : departureday, 'month of departure' : departuremonth, \
                     'year of departure' : departureyear, 'number of people' : numofpeople, \
                     'site number' : sitenumber, 'site location' : sitelocation, 'medical info' : medicalinfo, 'activities' : activities} #creates a dictionary of the user's profile

        if user_info not in database: #checks if the user already exists
            database.append(user_info) #appends the dictionary to the database
            print(database)
        else:
            showwarning("Warning Message", "User already exists!") #shows warning message if the user already exists
    else:
        return
    confirmVar.set(0) #makes the checkbox unchecked
    widget_reset()
            
        
def delete_user():
    selected_user = eval(userListbox.get(userListbox.curselection()))
    database.remove(selected_user)
    search_user() #use this function to refresh the list box and show that the user has been deleted
def search_user(): 
    firstname = firstnameSearchVar.get()#gets the first name
    lastname = lastnameSearchVar.get()#gets the last name
    usernames.clear() #clears the usernames list so that the previous search list is removed
    for i in range(len(database)):
        if database[i]['first name'] == firstname and database[i]['last name'] == lastname: #checks for first and lastname of every registration
            usernames.append(database[i]) #adds the regustration to the username list
    usernamesVar.set(usernames) #puts the username list to the list box
            
def pick_user():
    selected_user = eval(userListbox.get(userListbox.curselection()))#the get value is a string so the eval function returns it to a dictionary
    firstnameVar.set(selected_user['first name'])
    lastnameVar.set(selected_user['last name'])
    phoneVar.set(selected_user['phone'])
    emailVar.set(selected_user['email'])
    birthdayVar.set(selected_user['day of birth'])
    birthmonthVar.set(selected_user['month of birth'])
    birthyearVar.set(selected_user['year of birth'])
    arrivaldayVar.set(selected_user['day of arrival'])
    arrivalmonthVar.set(selected_user['month of arrival'])
    arrivalyearVar.set(selected_user['year of arrival'])
    departuredayVar.set(selected_user['day of departure'])
    departuremonthVar.set(selected_user['month of departure'])
    departureyearVar.set(selected_user['year of departure'])
    numofpeopleVar.set(selected_user['number of people'])
    sitenumberVar.set(selected_user['site number'])
    sitelocationVar.set(selected_user['site location'])
    medicalText.delete('1.0', END)
    medicalText.insert('1.0', selected_user['medical info'])

def searchactivity_user():
    searchactivity = searchactivitiesVar.get() 
    searchtime = searchtimeVar.get()
    activitylist = []
    for i in range(len(database)): #iterates through the profiles
        for n in range(len(database[i]['activities'])): #iterates through the activities of profile
            if database[i]['activities'][n][0] == searchactivity and database[i]['activities'][n][1] == searchtime: #appends the profile if they registered for activity
                activitylist.append(f"{database[i]['first name']} {database[i]['last name']}")
    activityusernamesVar.set(activitylist)

def restrict_activity(searchactivity, searchtime): #returns ture or false value based on if the activity slot is full
    activitylist = 0
    for i in range(len(database)):
        for n in range(len(database[i]['activities'])):
            if database[i]['activities'][n][0] == searchactivity and database[i]['activities'][n][1] == searchtime: #checks if a profile is registered in the activity
                activitylist += 1 #adds 1 to the activitylist
    if activitylist >= 5: #if there are more than 4 users in activity, False is returned
        return False
    else:
        return True
def disable_activity1():
    if canoeVar.get() > 0: #checks if the checkbutton for the activity is checked
        if restrict_activity('Canoeing' ,'Morning'): #checks if the activity time slot is full. If not, the radio button is able to enable
            canoeTimeRadioButton1['state'] = NORMAL
        if restrict_activity('Canoeing' ,'Noon'):
            canoeTimeRadioButton2['state'] = NORMAL
        if restrict_activity('Canoeing' ,'Afternoon'):
            canoeTimeRadioButton3['state'] = NORMAL
    else:
        canoeTimeRadioButton1['state'] = DISABLED
        canoeTimeRadioButton2['state'] = DISABLED
        canoeTimeRadioButton3['state'] = DISABLED
        canoeTimeVar.set(0)
def disable_activity2():
    if treeVar.get() > 0:
        if restrict_activity('Tree Trecking' ,'Morning'):
            treeTimeRadioButton1['state'] = NORMAL
        if restrict_activity('Tree Trecking' ,'Noon'):
            treeTimeRadioButton2['state'] = NORMAL
        if restrict_activity('Tree Trecking' ,'Afternoon'):
            treeTimeRadioButton3['state'] = NORMAL
    else:
        treeTimeRadioButton1['state'] = DISABLED
        treeTimeRadioButton2['state'] = DISABLED
        treeTimeRadioButton3['state'] = DISABLED
        treeTimeVar.set(0)
def disable_activity3():
    if rockVar.get() > 0:
        if restrict_activity('Rock Climbing' ,'Morning'):
            rockTimeRadioButton1['state'] = NORMAL
        if restrict_activity('Rock Climbing' ,'Noon'):
            rockTimeRadioButton2['state'] = NORMAL
        if restrict_activity('Rock Climbing' ,'Afternoon'):
            rockTimeRadioButton3['state'] = NORMAL
    else:
        rockTimeRadioButton1['state'] = DISABLED
        rockTimeRadioButton2['state'] = DISABLED
        rockTimeRadioButton3['state'] = DISABLED
        rockTimeVar.set(0)
def disable_activity4():
    if hikingVar.get() > 0:
        if restrict_activity('Hiking' ,'Morning'):
            hikingTimeRadioButton1['state'] = NORMAL
        if restrict_activity('Hiking' ,'Noon'):
            hikingTimeRadioButton2['state'] = NORMAL
        if restrict_activity('Hiking' ,'Afternoon'):
            hikingTimeRadioButton3['state'] = NORMAL
    else:
        hikingTimeRadioButton1['state'] = DISABLED
        hikingTimeRadioButton2['state'] = DISABLED
        hikingTimeRadioButton3['state'] = DISABLED
        hikingTimeVar.set(0)
def disable_activity5():
    if fishingVar.get() > 0:
        if restrict_activity('Fishing' ,'Morning'):
            fishingTimeRadioButton1['state'] = NORMAL
        if restrict_activity('Fishing' ,'Noon'):
            fishingTimeRadioButton2['state'] = NORMAL
        if restrict_activity('Fishing' ,'Afternoon'):
            fishingTimeRadioButton3['state'] = NORMAL
    else:
        fishingTimeRadioButton1['state'] = DISABLED
        fishingTimeRadioButton2['state'] = DISABLED
        fishingTimeRadioButton3['state'] = DISABLED
        fishingTimeVar.set(0)
#MAIN   
root = Tk()
root.geometry("890x755")
root.title("Yong Jin Park Registration") #sets the window name
mainframe = Frame(root)#creates a frame within root




#Fonts
largeFont=Font(size=40, weight='bold')
mediumFont=Font(size=30)
smallFont=Font(size=16)
smallerFont=Font(size=13)
tinyFont=Font(size=10)
#CREATE THE WIDGETS************************************************************
    #Frames to group together widgets. Helpful for griding widgets that don't fit into the grid.
registrationFrame = LabelFrame(mainframe, text="Registration", font=mediumFont)
birthdateFrame = LabelFrame(registrationFrame, text="Date of Birth", font=smallFont)
sitelocationFrame = LabelFrame(registrationFrame, text="Site Number, Site Location", font=smallFont)
numofpeopleFrame = LabelFrame(registrationFrame, text="Number of People", font=smallFont)
arrivalFrame = LabelFrame(registrationFrame, text="Arrival", font=smallFont)
departureFrame = LabelFrame(registrationFrame, text="Departure", font=smallFont)
medicalFrame = LabelFrame(registrationFrame, text="Medical Information", font=mediumFont)

activityFrame = LabelFrame(mainframe, text="Activities", font=mediumFont)
activityFrame1 = Frame(activityFrame, bg="#ffffff")
activityFrame2 = Frame(activityFrame, bg="#ffffff")
activityFrame3 = Frame(activityFrame, bg="#ffffff")
activityFrame4 = Frame(activityFrame, bg="#ffffff")
activityFrame5 = Frame(activityFrame, bg="#ffffff")

searchFrame = LabelFrame(mainframe, text="Search for Registration", font=mediumFont)

listFrame = Frame(searchFrame)

activitylistFrame = LabelFrame(searchFrame, text="Search for Activity", font=mediumFont)


    #Labels
yongjinparkLabel = Label(mainframe, text="YONG JIN PARK", font=largeFont)
    #Entry
firstnameVar = StringVar()
firstnameVar.set("First Name")
firstnameEntry = Entry(registrationFrame, textvariable=firstnameVar, font=smallFont, width = 17)
lastnameVar = StringVar()
lastnameVar.set("Last Name")
lastnameEntry = Entry(registrationFrame, textvariable=lastnameVar, font=smallFont, width = 17)
phoneVar = StringVar()
phoneVar.set("Phone #")
phoneEntry = Entry(registrationFrame, textvariable=phoneVar, font=smallFont, width = 17)
emailVar = StringVar()
emailVar.set("Email Address")
emailEntry = Entry(registrationFrame, textvariable=emailVar, font=smallFont, width = 17)

firstnameSearchVar = StringVar()
firstnameSearchVar.set("First Name")
firstnameSearchEntry = Entry(searchFrame, textvariable=firstnameSearchVar, font=smallFont, width = 10)
lastnameSearchVar = StringVar()
lastnameSearchVar.set("Last Name")
lastnameSearchEntry = Entry(searchFrame, textvariable=lastnameSearchVar, font=smallFont, width = 10)
    #Text
medicalText = Text(medicalFrame, font=tinyFont, width=60, height=15)

    #Spinbox
birthyear = list(range(1940, 2025))
birthyearVar = IntVar()
birthyearVar.set(2000)
birthyearSpinbox = Spinbox(birthdateFrame, textvariable = birthyearVar, values=birthyear, font=tinyFont, width = 8)

birthmonth = ["December", "November", "October", "September", "August", "July", "June", "May", "April", "March", "February", "January"]
birthmonthVar = StringVar()
birthmonthVar.set("January")
birthmonthSpinbox = Spinbox(birthdateFrame, textvariable = birthmonthVar, values=birthmonth, font=tinyFont, width = 8)

birthday = list(range(1,32))
birthdayVar = IntVar()
birthdayVar.set(1)
birthdaySpinbox = Spinbox(birthdateFrame, textvariable = birthdayVar, values=birthday, font=tinyFont, width = 8)

arrivalyear = list(range(2023, 2030))
arrivalyearVar = IntVar()
arrivalyearVar.set(2000)
arrivalyearSpinbox = Spinbox(arrivalFrame, textvariable = arrivalyearVar, values=arrivalyear, font=tinyFont, width = 8)

arrivalmonth = ["December", "November", "October", "September", "August", "July", "June", "May", "April", "March", "February", "January"]
arrivalmonthVar = StringVar()
arrivalmonthVar.set("January")
arrivalmonthSpinbox = Spinbox(arrivalFrame, textvariable = arrivalmonthVar, values=arrivalmonth, font=tinyFont, width = 8)

arrivalday = list(range(1,32))
arrivaldayVar = IntVar()
arrivaldayVar.set(1)
arrivaldaySpinbox = Spinbox(arrivalFrame, textvariable = arrivaldayVar, values=arrivalday, font=tinyFont, width = 8)

departureyear = list(range(2023, 2030))
departureyearVar = IntVar()
departureyearVar.set(2000)
departureyearSpinbox = Spinbox(departureFrame, textvariable = departureyearVar, values=departureyear, font=tinyFont, width = 8)

departuremonth = ["December", "November", "October", "September", "August", "July", "June", "May", "April", "March", "February", "January"]
departuremonthVar = StringVar()
departuremonthVar.set("January")
departuremonthSpinbox = Spinbox(departureFrame, textvariable = departuremonthVar, values=departuremonth, font=tinyFont, width = 8)

departureday = list(range(1,32))
departuredayVar = IntVar()
departuredayVar.set(1)
departuredaySpinbox = Spinbox(departureFrame, textvariable = departuredayVar, values=departureday, font=tinyFont, width = 8)

    #Scale
numofpeopleVar = IntVar()
peopleScale=Scale(numofpeopleFrame, variable=numofpeopleVar, from_=1, to=8, orient=HORIZONTAL, length=200)
    #Option Menu
sitenumbers = list(range(1,21))
sitenumberVar = IntVar()
sitenumberVar.set(1)
sitenumberOptionMenu = OptionMenu(sitelocationFrame, sitenumberVar, *sitenumbers)
sitenumberOptionMenu.configure(width=28)

sitelocations = ["Beach", "Field", "Birch", "Maple"]
sitelocationVar = StringVar()
sitelocationVar.set("Beach")
sitelocationOptionMenu = OptionMenu(sitelocationFrame, sitelocationVar, *sitelocations)
sitelocationOptionMenu.configure(width=28)

searchactivities = ["Canoeing", "Tree Trecking", "Rock Climbing", "Hiking", "Fishing"]
searchactivitiesVar= StringVar()
searchactivitiesVar.set("Activity")
searchactivitiesOptionMenu = OptionMenu(activitylistFrame, searchactivitiesVar, *searchactivities)
searchactivitiesOptionMenu.configure(width=24)

searchtime = ["Morning", "Noon", "Afternoon"]
searchtimeVar= StringVar()
searchtimeVar.set("Time")
searchtimeOptionMenu = OptionMenu(activitylistFrame, searchtimeVar, *searchtime)
searchtimeOptionMenu.configure(width=24)
    #checkbutton
canoeVar = IntVar()
canoeVar.set(0)
canoeCheckBox= Checkbutton(activityFrame1, text="Canoeing $42", onvalue = 42, offvalue=0, variable=canoeVar, font=smallFont, bg="#ffffff", command=disable_activity1)
treeVar = IntVar()
treeVar.set(0)
treeCheckBox=Checkbutton(activityFrame2, text="Tree-Top Trecking $46", onvalue = 43, offvalue=0, variable=treeVar, font=smallFont, bg="#ffffff", command=disable_activity2)
rockVar = IntVar()
rockVar.set(0)
rockCheckBox=Checkbutton(activityFrame3, text="Rock Climbing $32", onvalue = 32 , offvalue=0, variable=rockVar, font=smallFont, bg="#ffffff", command=disable_activity3)
hikingVar = IntVar()
hikingVar.set(0)
hikingCheckBox=Checkbutton(activityFrame4, text="Hiking $5", onvalue = 5, offvalue=0, variable=hikingVar, font=smallFont, bg="#ffffff", command=disable_activity4)
fishingVar = IntVar()
fishingVar.set(0)
fishingCheckBox=Checkbutton(activityFrame5, text="Fishing $15", onvalue = 15, offvalue=0, variable=fishingVar, font=smallFont, bg="#ffffff", command=disable_activity5)

confirmVar=IntVar()
confirmVar.set(0)
confirmCheckButton=Checkbutton(activityFrame, text="The information is correct", onvalue = 1, offvalue=0, variable=confirmVar, font=tinyFont)
    #Radio button

canoeTimeVar=IntVar()
canoeTimeVar.set(0)
canoeTimeRadioButton1=Radiobutton(activityFrame1, text="Morning", value=1, variable=canoeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
canoeTimeRadioButton2=Radiobutton(activityFrame1, text="Noon", value=2, variable=canoeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
canoeTimeRadioButton3=Radiobutton(activityFrame1, text="Afternoon", value=3, variable=canoeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)

treeTimeVar=IntVar()
treeTimeVar.set(0)
treeTimeRadioButton1=Radiobutton(activityFrame2, text="Morning", value=1, variable=treeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
treeTimeRadioButton2=Radiobutton(activityFrame2, text="Noon", value=2, variable=treeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
treeTimeRadioButton3=Radiobutton(activityFrame2, text="Afternoon", value=3, variable=treeTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)

rockTimeVar=IntVar()
rockTimeVar.set(0)
rockTimeRadioButton1=Radiobutton(activityFrame3, text="Morning", value=1, variable=rockTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
rockTimeRadioButton2=Radiobutton(activityFrame3, text="Noon", value=2, variable=rockTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
rockTimeRadioButton3=Radiobutton(activityFrame3, text="Afternoon", value=3, variable=rockTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)

hikingTimeVar=IntVar()
hikingTimeVar.set(0)
hikingTimeRadioButton1=Radiobutton(activityFrame4, text="Morning", value=1, variable=hikingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
hikingTimeRadioButton2=Radiobutton(activityFrame4, text="Noon", value=2, variable=hikingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
hikingTimeRadioButton3=Radiobutton(activityFrame4, text="Afternoon", value=3, variable=hikingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)

fishingTimeVar=IntVar()
fishingTimeVar.set(0)
fishingTimeRadioButton1=Radiobutton(activityFrame5, text="Morning", value=1, variable=fishingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
fishingTimeRadioButton2=Radiobutton(activityFrame5, text="Noon", value=2, variable=fishingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)
fishingTimeRadioButton3=Radiobutton(activityFrame5, text="Afternoon", value=3, variable=fishingTimeVar, font=smallerFont, bg="#ffffff", state=DISABLED)

#Button
switchButton=Button(mainframe, text="Switch to Search", font=tinyFont, command=switch_frames)
registerButton=Button(activityFrame, text="Register User", font=smallFont, command=register_user)
searchButton=Button(searchFrame, text="Search", font=smallFont, command=search_user)
deleteButton=Button(searchFrame, text="Delete", font=smallFont, command=delete_user)
selectButton=Button(searchFrame, text="Display Selected User Info", font=smallFont, command=pick_user)
searchactivityButton=Button(activitylistFrame, text="Search", font=smallerFont, command=searchactivity_user)
#Listbox
usernames = ['Search for a user']
usernamesVar = StringVar()
usernamesVar.set(usernames)
userListbox = Listbox(listFrame, listvariable=usernamesVar, selectmode=SINGLE, font=smallerFont, height=13, width=45)

vertListScroller = Scrollbar(listFrame,command = userListbox.yview)
horizListScroller = Scrollbar(listFrame,orient=HORIZONTAL,command = userListbox.xview)

userListbox.config(yscrollcommand = vertListScroller.set,xscrollcommand = horizListScroller.set)

activityusernames = ['Search for an activity']
activityusernamesVar = StringVar()
activityusernamesVar.set(activityusernames)
activityuserListbox = Listbox(activitylistFrame, listvariable=activityusernamesVar, selectmode=SINGLE, font=smallerFont, height=9, width=25)

#GRID THE WIDGETS************************************************************************
mainframe.grid(padx=10,pady=10)
yongjinparkLabel.grid(row=1, column=1, columnspan=4)
switchButton.grid(row=1, column=4)
    #registrationFrame
registrationFrame.grid(row=2, column=1, columnspan=2)
        #information entry
firstnameEntry.grid(row=1, column=1)
lastnameEntry.grid(row=2, column=1)
phoneEntry.grid(row=1, column=2)
emailEntry.grid(row=2, column=2)

        #Date of Birth Frame
birthdateFrame.grid(row=3, column=1, pady=10)
birthyearSpinbox.grid(row=1, column=1, ipady=11)
birthmonthSpinbox.grid(row=1, column=2, ipady=11)
birthdaySpinbox.grid(row=1, column=3, ipady=11)
        #num of people Frame
numofpeopleFrame.grid(row=3, column=2, pady=10)
peopleScale.grid(row=1, column=1, columnspan=2)
        #site locaiton Frame
sitelocationFrame.grid(row=4, column=1, columnspan=2, sticky=EW)
sitenumberOptionMenu.pack(side=LEFT)
sitelocationOptionMenu.pack(side=RIGHT)
        #arrivalFrame
arrivalFrame.grid(row=5, column=1, pady=10)
arrivalyearSpinbox.grid(row=1, column=1, ipady=11)
arrivalmonthSpinbox.grid(row=1, column=2, ipady=11)
arrivaldaySpinbox.grid(row=1, column=3, ipady=11)
        #departureFrame
departureFrame.grid(row=5, column=2, pady=10)
departureyearSpinbox.grid(row=1, column=1, ipady=11)
departuremonthSpinbox.grid(row=1, column=2, ipady=11)
departuredaySpinbox.grid(row=1, column=3, ipady=11)
        #departureFrame
medicalFrame.grid(row=6, column=1, columnspan=2, pady=10)
medicalText.grid(row=1, column=1)

    #activity Frame
activityFrame.grid(row=2,column=3, columnspan=2, sticky=NS)
        #activities
activityFrame1.grid(row=1, column=1, columnspan=2, pady=20, padx=8, sticky=W)
canoeCheckBox.grid(row=1, column=1, columnspan=3, sticky=W)
activityFrame2.grid(row=2, column=1, columnspan=2, pady=20, padx=8, sticky=W)
treeCheckBox.grid(row=1, column=1, columnspan=3, sticky=W)
activityFrame3.grid(row=3, column=1, columnspan=2, pady=20, padx=8, sticky=W)
rockCheckBox.grid(row=1, column=1, columnspan=3, sticky=W)
activityFrame4.grid(row=4, column=1, columnspan=2, pady=20, padx=8, sticky=W)
hikingCheckBox.grid(row=1, column=1, columnspan=3, sticky=W)
activityFrame5.grid(row=5, column=1, columnspan=2, pady=20, padx=8, sticky=W)
fishingCheckBox.grid(row=1, column=1, columnspan=3, sticky=W)
            #activity times
canoeTimeRadioButton1.grid(row=2, column=1, padx=26)
canoeTimeRadioButton2.grid(row=2, column=2, padx=26)
canoeTimeRadioButton3.grid(row=2, column=3, padx=26)
treeTimeRadioButton1.grid(row=2, column=1, padx=26)
treeTimeRadioButton2.grid(row=2, column=2, padx=26)
treeTimeRadioButton3.grid(row=2, column=3, padx=26)
rockTimeRadioButton1.grid(row=2, column=1, padx=26)
rockTimeRadioButton2.grid(row=2, column=2, padx=26)
rockTimeRadioButton3.grid(row=2, column=3, padx=26)
hikingTimeRadioButton1.grid(row=2, column=1, padx=26)
hikingTimeRadioButton2.grid(row=2, column=2, padx=26)
hikingTimeRadioButton3.grid(row=2, column=3, padx=26)
fishingTimeRadioButton1.grid(row=2, column=1, padx=26)
fishingTimeRadioButton2.grid(row=2, column=2, padx=26)
fishingTimeRadioButton3.grid(row=2, column=3, padx=26)
    #confirm
confirmCheckButton.grid(row=6, column=1)
registerButton.grid(row=6, column=2)

#Search Frame

firstnameSearchEntry.grid(row=1, column=1, ipady=5)
lastnameSearchEntry.grid(row=1, column=2, ipady=5)
searchButton.grid(row=1, column=3)
deleteButton.grid(row=1, column=4)
listFrame.grid(row=2, column=1, columnspan=4)
userListbox.grid(row=1, column=1, sticky=NSEW)
vertListScroller.grid(row=1, column=2, sticky=NS)
horizListScroller.grid(row=2, column=1, sticky=EW)
selectButton.grid(row=3, column=1, columnspan=3, sticky=EW)

activitylistFrame.grid(row=4, column=1, columnspan=4, sticky=EW)
activityuserListbox.grid(row=1, column=2, rowspan=3, sticky=E)
searchactivitiesOptionMenu.grid(row=1, column=1, sticky=NS)
searchtimeOptionMenu.grid(row=2, column=1, sticky=NS)
searchactivityButton.grid(row=3, column=1, sticky=NSEW)

root.mainloop()


