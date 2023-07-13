from tkinter import *
from tkinter.messagebox import *
from tkinter import font
from tkinter.messagebox import *

database = []

def registerperson():
    # Get the values from the input fields
    global activitieslist
    name = name_var.get()
    age = age_var.get()
    day = day_var.get()
    month = month_var.get()
    year = year_var.get()
    activities = activity_var.get()
    medical_records = medical_var.get()
    site_number = site_var.get()
    email = email_var.get()
    phone_number = phone_var.get()

    
    if restrict_activity('Hiking') == False and activities == 'Hiking':
        showwarning('Warning', 'This activity is full')
        return
    if restrict_activity('Swimming') == False and activities == 'Swimming':
        showwarning('Warning', 'This activity is full')
        return
    if restrict_activity('Tennis') == False and activities == 'Tennis':
        showwarning('Warning', 'This activity is full')
        return
    if restrict_activity('Canoeing') == False and activities == 'Canoeing':
        showwarning('Warning', 'This activity is full')
        return

    
    # Create a formatted string with the data and labels
    data = {'name':name, 'age':age, 'day':day, 'month':month, 'year':year, 'activities':activities, 'medical_records':medical_records, 'site_number':site_number, 'email':email, 'phone_number':phone_number}
    
    # Append the data to the listbox
    database.append(data)
    person_var.set(database)
    
def filter_people():
    people = ''
    activity = filter_var.get()
    for i in range(len(database)):
        if database[i]['activities'] == activity:
            people = people + f'{database[i]["name"]}\n'
    showinfo('people', people)

def restrict_activity(searchactivity): 
    activitylist = 0
    for i in range(len(database)):
         if database[i]['activities'] == searchactivity:
                activitylist += 1 
    if activitylist >= 5: 
        return False
    else:
        return True

def search_person():
    query = search_var.get()
    matching_people = []

    for person in database:
        if person['name'].lower() == query.lower():
            matching_people.append(person)

    if matching_people:
        results = ""
        for person in matching_people:
            results += f"Name: {person['name']}\n"
            results += f"Age: {person['age']}\n"
            results += f"Activities: {person['activities']}\n"
            results += f"Medical Records: {person['medical_records']}\n"
            results += f"Site Number: {person['site_number']}\n"
            results += f"Email: {person['email']}\n"
            results += f"Phone Number: {person['phone_number']}\n\n"
        showinfo("Search Results", results)
    else:
        showinfo("Search Results", "No matching person found.")



root = Tk()
root.geometry("1200x800")

mainframe = Frame(root)
mainframe.grid(padx=50, pady=50)

person_list = []

nameFrame = Frame(mainframe)
ageFrame = Frame(mainframe)
monthFrame = Frame(mainframe)
yearFrame = Frame(mainframe)
activityFrame = Frame(mainframe)
medicalFrame = Frame(mainframe)
siteFrame = Frame(mainframe)
emailFrame = Frame(mainframe)
phoneFrame = Frame(mainframe)

# Title
titlelabel = Label(mainframe, text="Campsite Booking Manager", font=("Cooper", 20, "bold"))

# Register New user instruction
registerlabel = Label(mainframe, text="Register New User", font=("Cooper", 12, "bold"))

# Enter Name
full_name_label = Label(nameFrame, text="Full Name:")
name_var = StringVar()
full_name_entry = Entry(nameFrame, textvariable=name_var)

# Age
age_label = Label(mainframe, text="Age:")
age_var = IntVar()
age_spinbox = Spinbox(mainframe, from_=0, to=150, textvariable=age_var)

# Day
day_label = Label(mainframe, text="Day:")
day_var = IntVar()
day_spinbox = Spinbox(mainframe, from_=0, to=31, textvariable=day_var)

# Month
month_label = Label(mainframe, text="Month:")
month_var = DoubleVar()
month_slider = Scale(mainframe, variable=month_var, from_=1, to=12, orient=HORIZONTAL)

# Year
year_label = Label(mainframe, text="Year:")
year_var = IntVar()
year_slider = Scale(mainframe, variable=year_var, from_=1900, to=2100, orient=HORIZONTAL)

# Activities
activity_label = Label(mainframe, text="Activities:")
activitieslist = ["Hiking", "Swimming", "Tennis", "Canoeing"]
activity_var = StringVar()
activity_dropdown = OptionMenu(mainframe, activity_var, *activitieslist)

# Medical Records
medical_label = Label(mainframe, text="Medical Records:")
medical_var = StringVar()
medical_entry = Entry(mainframe, textvariable=medical_var)

# Site Number
site_label = Label(mainframe, text="Site Number:")
site_var = StringVar()
site_entry = Entry(mainframe, textvariable=site_var)

# Email
email_label = Label(mainframe, text="Email:")
email_var = StringVar()
email_entry = Entry(mainframe, textvariable=email_var)

# Phone Number
phone_label = Label(mainframe, text="Phone Number:")
phone_var = StringVar()
phone_entry = Entry(mainframe, textvariable=phone_var)

# Listbox
person_var = StringVar()
person_listbox = Listbox(mainframe, listvariable=person_var, width=120, selectmode=SINGLE)
scrollbar_y = Scrollbar(mainframe, orient=VERTICAL)
scrollbar_x = Scrollbar(mainframe, orient=HORIZONTAL)

# Filter Dropdown
filter_var = StringVar()
filter_var.set("All")
filter_dropdown = OptionMenu(mainframe, filter_var, "All", "Hiking", "Swimming", "Tennis", "Canoeing")
filter_button = Button(mainframe, text="Filter", command=filter_people)

# Register Button
add_button = Button(mainframe, text="Insert", command=registerperson)

#Search
search_var = StringVar()

# Search Label
search_label = Label(mainframe, text="Search:")

# Search Entry
search_entry = Entry(mainframe, textvariable=search_var)

# Search Button
search_button = Button(mainframe, text="Search", command=search_person)

# Grid the Widgets
titlelabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)
registerlabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W)

#search
search_button.grid(row=15, column=2, padx=10, pady=10)
search_label.grid(row=15, column=0, padx=10, pady=10, sticky=W)
search_entry.grid(row=15, column=1, padx=10, pady=10, sticky=W)


# Name
full_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
full_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)
nameFrame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky=W)

# Age
age_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
age_spinbox.grid(row=3, column=1, padx=10, pady=10, sticky=W)

# Day
day_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
day_spinbox.grid(row=4, column=1, padx=10, pady=10, sticky=W)

# Month
month_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
month_slider.grid(row=5, column=1, padx=10, pady=10, sticky=W)

# Year
year_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
year_slider.grid(row=6, column=1, padx=10, pady=10, sticky=W)

# Activities
activity_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)
activity_dropdown.grid(row=7, column=1, padx=10, pady=10, sticky=W)


# Medical Records
medical_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
medical_entry.grid(row=8, column=1, padx=10, pady=10, sticky=W)

# Site Number
site_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
site_entry.grid(row=9, column=1, padx=10, pady=10, sticky=W)

# Email
email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
email_entry.grid(row=10, column=1, padx=10, pady=10, sticky=W)

# Phone Number
phone_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
phone_entry.grid(row=11, column=1, padx=10, pady=10, sticky=W)

# Listbox
person_listbox.grid(row=0, column=2, rowspan=12, padx=10, pady=10, sticky=N+S+E)
scrollbar_y.grid(row=0, column=3, rowspan=12, sticky=N+S)
scrollbar_x.grid(row=12, column=2, padx=10, sticky=W+E)

# Filter Dropdown
filter_dropdown.grid(row=13, column=2, padx=10, pady=10, sticky=W)
filter_button.grid(row=13, column=2, padx=10, pady=10, sticky=E)

# Register Button
add_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

# Configure Scrollbars
scrollbar_y.config(command=person_listbox.yview)
scrollbar_x.config(command=person_listbox.xview)

root.mainloop()
