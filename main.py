import customtkinter

customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x600")

def toggle_theme():
    if theme_switch.get() == 1:
        customtkinter.set_appearance_mode("dark")
        theme_switch.configure(text="Modo Dark")
    else:
        customtkinter.set_appearance_mode("light")
        theme_switch.configure(text="Modo Light")


title = customtkinter.CTkLabel(master=window, text="Conversor de Moedas", font=("Press Start 2P", 20))
theme_switch = customtkinter.CTkSwitch(master=window, text="Modo Dark", command=toggle_theme)
theme_switch.select() 
toggle_theme()

source_currency_label = customtkinter.CTkLabel(master=window, text="selecione a moeda de origem")
target_currency_entry = customtkinter.CTkLabel(master=window, text="selecione a moeda de destino")

currency_origin = customtkinter.CTkOptionMenu(master=window, values=["USD","BRL","EUR","BTC"])
target_currency = customtkinter.CTkOptionMenu(master=window, values=["USD","BRL","EUR","BTC"])

def currency_converter():
    print("converter moeda")
convert_button = customtkinter.CTkButton(master=window, text='converter', command=currency_converter)

currency_list = customtkinter.CTkScrollableFrame(master=window)
available_currencies = ["USD: DOLAR AMERICANO", "BRL: Real brasileiro"]
for currency in available_currencies:
    currency_text = customtkinter.CTkLabel(currency_list, text= currency)
    currency_text.pack()


title.pack(padx=10,pady=10)
theme_switch.pack(padx=10, pady=5)
source_currency_label.pack(padx=10,pady=3)
currency_origin.pack(padx=10)
target_currency_entry.pack(padx=10,pady=3)
target_currency.pack(padx=10)
convert_button.pack(padx=10,pady=10)
currency_list.pack(padx=10,pady=10)


window.mainloop()