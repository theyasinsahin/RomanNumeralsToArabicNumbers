from tkinter import *
from tkinter import messagebox


def calculate_roman_numeral():
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    user_input = my_entry.get()
    input_len = len(user_input)
    for i in range(input_len):
        try:
            if i == 0:
                result += roman_dict[user_input[i]]
            elif roman_dict[user_input[i]] <= roman_dict[user_input[i-1]]:
                result += roman_dict[user_input[i]]
            elif roman_dict[user_input[i]] > roman_dict[user_input[i-1]]:
                result += ((roman_dict[user_input[i]]) - (2 * roman_dict[user_input[i-1]]))
        except:
            messagebox.askretrycancel('retry', 'Failed! want to try again?')
            break
    result_label.config(text=result)


#window
window = Tk()
window.title("Convert Roman to Arabic")
window.minsize(width=1200, height=800)

#label enter
roman_label = Label(text="Enter your roman numeral",pady=50)
roman_label.config(fg="black", font=("Arial", 15, "normal"))
roman_label.pack()

#entry
my_entry = Entry(width=30,font=("Arial", 15, "normal"))
my_entry.pack()

#label
my_label = Label(text="Conversion result to arabic",pady=50)
my_label.config(fg="black", font=("Arial", 15, "normal"))
my_label.pack()


#result label
result_label = Label(bg="blue", fg="white", width=10, height=5,font=("Arial", 20, "normal"))
result_label.pack()



#button
my_button = Button(text="Convert", command=calculate_roman_numeral)
my_button.pack()

window.mainloop()


