import json
from datetime import datetime
import customtkinter as ctk
import os
import sys

# ===============================
# إعدادات النافذة
# ===============================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.iconbitmap(resource_path("icon.ico"))
app.title("Expense Tracker v2")
app.geometry("900x700")

# ===============================
# قاعدة البيانات
# ===============================

try:
    with open("expense.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []

# ===============================
# حفظ البيانات
# ===============================

def save_data():
    with open("expense.json", "w") as file:
        json.dump(expenses, file, indent=4)

# ===============================
# العنوان
# ===============================

title = ctk.CTkLabel(
    app,
    text="Expense Tracker",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)


# ===============================
# الإدخالات
# ===============================

name_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Expense Name"
)

name_entry.pack(pady=5)

price_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Price"
)

price_entry.pack(pady=5)

category_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Category"
)

category_entry.pack(pady=5)


# ===============================
# صندوق عرض البيانات
# ===============================

text_box = ctk.CTkTextbox(
    app,
    width=700,
    height=300
)

text_box.pack(pady=20)
text_box.configure(state="disabled")

# ===============================
# إضافة مصروف
# ===============================

def add_expense():

    name = name_entry.get()
    price = price_entry.get()
    category = category_entry.get()
    if name == "" or price == "" or category == "":
     return

    today = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "name": name,
        "price": price,
        "category": category,
        "today": today
    }

    expenses.append(expense)

    save_data()

    name_entry.delete(0, "end")
    price_entry.delete(0, "end")
    category_entry.delete(0, "end")
    show_expenses()

# ===============================
# عرض المصروفات
# ===============================

def show_expenses():
    text_box.configure(state="normal")
    
    text_box.delete("1.0", "end")

    for item in expenses:

        text_box.insert(
            "end",
            f"Name : {item['name']}\n"
            f"Price : {item['price']}\n"
            f"Category : {item['category']}\n"
            f"Date : {item['today']}\n"
            "------------------------------------\n"
        )
    text_box.configure(state="disabled")


# ===============================
# البحث
# ===============================

def search_expense():
    text_box.configure(state="normal")
    
    text_box.delete("1.0", "end")

    keyword = name_entry.get().lower()

    for item in expenses:

        if keyword in item["name"].lower():

            text_box.insert(
                "end",
                f"Name : {item['name']}\n"
                f"Price : {item['price']}\n"
                f"Category : {item['category']}\n"
                f"Date : {item['today']}\n"
                "------------------------------------\n"
            )
    text_box.configure(state="disabled")

# ===============================
# إجمالي المصروفات
# ===============================

def total_expense():
    text_box.configure(state="normal")
    
    total = 0

    for item in expenses:

        total += float(item["price"])

    text_box.delete("1.0", "end")

    text_box.insert(
        "end",
        f"Total Expense : {total}"
    )
    text_box.configure(state="disabled")


# ===============================
# حذف مصروف
# ===============================

def delete_expense():

    keyword = name_entry.get()

    for item in expenses:

        if item["name"] == keyword:

            expenses.remove(item)

            save_data()

            break

    show_expenses()


# ===============================
# تعديل مصروف
# ===============================

def edit_expense():

    keyword = name_entry.get()

    for item in expenses:

        if item["name"] == keyword:

            item["name"] = name_entry.get()

            item["price"] = price_entry.get()
            item["category"] = category_entry.get()

            save_data()

            break

    show_expenses() 

#====ازرار====#

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

add_button = ctk.CTkButton(
    button_frame,
    text="Add",
    command=add_expense,
    width=100
)
add_button.grid(row=0, column=0, padx=5)

show_button = ctk.CTkButton(
    button_frame,
    text="Show",
    command=show_expenses,
    width=100
)
show_button.grid(row=0, column=1, padx=5)

search_button = ctk.CTkButton(
    button_frame,
    text="Search",
    command=search_expense,
    width=100
)
search_button.grid(row=0, column=2, padx=5)

edit_button = ctk.CTkButton(
    button_frame,
    text="Edit",
    command=edit_expense,
    width=100
)
edit_button.grid(row=0, column=3, padx=5)

delete_button = ctk.CTkButton(
    button_frame,
    text="Delete",
    command=delete_expense,
    width=100
)
delete_button.grid(row=0, column=4, padx=5)

total_button = ctk.CTkButton(
    button_frame,
    text="Total",
    command=total_expense,
    width=100
)
total_button.grid(row=0, column=5, padx=5)




footer = ctk.CTkFrame(app, height=40)

footer.pack(fill="x", side="bottom")

developer = ctk.CTkLabel(
    footer,
    text="Expense Tracker v2.0 | Developed by Youssef Sheeba (CodeSniper)",
    font=("Segoe UI", 13)
)

developer.pack(pady=8)

app.mainloop()