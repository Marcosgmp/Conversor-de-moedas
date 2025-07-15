import customtkinter
from get_currency import * 

customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("500x600")

dic_conv_available = conv_name()
available_currencies = currency_name()

selected_origin = customtkinter.StringVar(value="Moeda de origem  ⬇")
selected_target = customtkinter.StringVar(value="Moeda de destino  ⬇")


def toggle_theme():
    if theme_switch.get() == 1:
        customtkinter.set_appearance_mode("dark")
        theme_switch.configure(text="Modo Dark")
    else:
        customtkinter.set_appearance_mode("light")
        theme_switch.configure(text="Modo Light")

def update_target_options(choice):
    destinatinations = dic_conv_available.get(choice, [])
    if destinatinations:
        selected_target.set(destinatinations[0]) 
        target_currency.configure(command=lambda: open_currency_selector(destinatinations, selected_target, "Moeda de destino"))


def open_currency_selector(currency, var_to_set, title):
    top = customtkinter.CTkToplevel(window)
    top.title(title)
    top.geometry("300x500")

    scroll = customtkinter.CTkScrollableFrame(top)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)

    def selecionar(crr):
        name = available_currencies.get(crr, "")
        var_to_set.set(f"{crr} - {name}")
        top.destroy()
        if var_to_set == selected_origin:
            update_target_options(crr)

    for coin in currency:
        btn = customtkinter.CTkButton(scroll, text=coin, width=200,command=lambda crr=coin: selecionar(crr))
        btn.pack(pady=2)

def currency_converter():
    print("Converter de:", selected_origin.get(), "para:", selected_target.get())

title = customtkinter.CTkLabel(master=window, text="Conversor de Moedas", font=("Press Start 2P", 20))
theme_switch = customtkinter.CTkSwitch(master=window, text="Modo Dark", command=toggle_theme)
theme_switch.select() 
toggle_theme()

source_currency_label = customtkinter.CTkLabel(master=window, text="selecione a moeda de origem")
target_currency_entry = customtkinter.CTkLabel(master=window, text="selecione a moeda de destino")


currency_origin = customtkinter.CTkButton(master=window,
                                          textvariable=selected_origin, 
                                          height=30,
                                          command=lambda: open_currency_selector(list(dic_conv_available.keys()), selected_origin, "Moeda de origem")
)

target_currency = customtkinter.CTkButton(master=window,
                                          textvariable=selected_target,
                                          height=30,
                                          command=lambda: open_currency_selector(["Selecione origem"], selected_target, "Moeda de destino")
)
convert_button = customtkinter.CTkButton(master=window, text='Converter', command=currency_converter)


currency_list = customtkinter.CTkScrollableFrame(master=window)

for cod_currency in available_currencies:
    curncy_name = available_currencies[cod_currency] #curncy name = currency name
    currency_text = customtkinter.CTkLabel(currency_list, text= f"{cod_currency}:{curncy_name}")
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