import customtkinter
from get_currency import * 
from get_price import get_price

customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry("500x600")

dic_conv_available = conv_name()
available_currencies = currency_name()
currecy_price_text = customtkinter.CTkLabel(master=window, text="")

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
    destinations = dic_conv_available.get(choice, [])
    if destinations:
        selected_target.set(f"{destinations[0]} - {available_currencies[destinations[0]]}")
        target_currency.configure(command=lambda: open_currency_selector(destinations, selected_target, "Moeda de destino"))


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
    if " - " not in selected_origin.get() or " - " not in selected_target.get():
        currecy_price_text.configure(text="⚠️ Selecione as duas moedas.")
        return
    
    source_currency = selected_origin.get().split(" - ")[0].strip()
    dest_currency = selected_target.get().split(" - ")[0].strip()

    try:
        amount = float(amount_entry.get().replace(",", "."))
    except ValueError:
        currecy_price_text.configure(text="❌ Digite um valor numérico válido.")
        return

    price = float(get_price(source_currency, dest_currency))
    result = amount * price

    currecy_price_text.configure(
        text=f"💱 {amount} {source_currency} = {result:.2f} {dest_currency}"
    )

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

amount_label = customtkinter.CTkLabel(master=window, text="Valor a converter:")
amount_entry = customtkinter.CTkEntry(master=window, placeholder_text="Ex: 10")


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

amount_label.pack(pady=3)
amount_entry.pack(pady=3)

convert_button.pack(padx=10,pady=10)
currecy_price_text.pack(padx=10,pady=10)
currency_list.pack(padx=10,pady=10)


window.mainloop()