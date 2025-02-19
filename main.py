from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# MySQL connection credentials
mypass = "884878"
mydatabase = "db"

# Establish MySQL connection
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Initialize the main application window
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

# Scale factor for the background image
same = True
n = 0.25

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

# Resize image according to the window size
newImageSizeWidth = int(imageSizeWidth * n)
newImageSizeHeight = int(imageSizeHeight * n) if same else int(imageSizeHeight / n)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)
img = ImageTk.PhotoImage(background_image)

# Create and set the background canvas
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

# Create a heading frame
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n LitLore Library", bg='#CDCDCD', fg='#B90504', font=('Comic Sans MS', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons for different library functions
btn1 = Button(root, text="Add Book Details", bg='#CDCDCD', fg='#B90504', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='#CDCDCD', fg='#B90504', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='#CDCDCD', fg='#B90504', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='#CDCDCD', fg='#B90504', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='#CDCDCD', fg='#B90504', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
