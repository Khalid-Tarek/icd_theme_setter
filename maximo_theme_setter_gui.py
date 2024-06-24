import customtkinter as ctk
import CTkColorPicker as ctkcp
import maximo_theme_setter
import json
import random

theme_file_name = "theme_variables.json"

def main():
    theme = maximo_theme_setter.extract_theme(theme_file_name)
    
    app = ctk.CTk()
    app.title("Maximo Theme Setter")
    app.geometry("600x400")

    app.grid_rowconfigure((0, 1), weight=1)
    app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    
    #String Variables
    primary = ctk.StringVar(app, theme["maximo_theme"]["primary"])
    secondary = ctk.StringVar(app, theme["maximo_theme"]["secondary"])
    tertiary = ctk.StringVar(app, theme["maximo_theme"]["tertiary"])
    onprimary = ctk.StringVar(app, theme["maximo_theme"]["onPrimary"])
    onsecondary = ctk.StringVar(app, theme["maximo_theme"]["onSecondary"])
    ontertiary = ctk.StringVar(app, theme["maximo_theme"]["onTertiary"])
    hover = ctk.StringVar(app, theme["maximo_theme"]["hover"])
    selected = ctk.StringVar(app, theme["maximo_theme"]["selected"])
    maximo_path = ctk.StringVar(app, theme["file_paths"]["maximo"])
    login_path = ctk.StringVar(app, theme["file_paths"]["login"])
    deployed_maximo_path = ctk.StringVar(app, theme["file_paths"]["deployed_maximo"])
    
    #Preview Labels
    label_theme_primary_preview = ctk.CTkLabel(app, text="Primary")
    label_theme_secondary_preview = ctk.CTkLabel(app, text="Secondary")
    label_theme_tertiary_preview = ctk.CTkLabel(app, text="Tertiary")
    label_theme_hover_preview = ctk.CTkLabel(app, text="Hover")
    label_theme_selected_preview = ctk.CTkLabel(app, text="Selected")

    label_theme_primary_preview.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_secondary_preview.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_tertiary_preview.grid(row=0, column=4, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_hover_preview.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='NEWS')
    label_theme_selected_preview.grid(row=1, column=3, columnspan=3, padx=5, pady=5, sticky='NEWS')
    
    #Theme Color Selectors
    button_theme_primary = ctk.CTkButton(app, text="Primary")
    button_theme_secondary = ctk.CTkButton(app, text="Secondary")
    button_theme_tertiary = ctk.CTkButton(app, text="Tertiary")
    button_theme_onprimary = ctk.CTkButton(app, text="OnPrimary")
    button_theme_onsecondary = ctk.CTkButton(app, text="OnSecondary")
    button_theme_ontertiary = ctk.CTkButton(app, text="OnTertiary")
    button_theme_hover = ctk.CTkButton(app, text="Hover")
    button_theme_selected = ctk.CTkButton(app, text="Selected")

    entry_theme_primary = ctk.CTkEntry(app, textvariable=primary)
    entry_theme_secondary = ctk.CTkEntry(app, textvariable=secondary)
    entry_theme_tertiary = ctk.CTkEntry(app, textvariable=tertiary)
    entry_theme_onprimary = ctk.CTkEntry(app, textvariable=onprimary)
    entry_theme_onsecondary = ctk.CTkEntry(app, textvariable=onsecondary)
    entry_theme_ontertiary = ctk.CTkEntry(app, textvariable=ontertiary)
    entry_theme_hover = ctk.CTkEntry(app, textvariable=hover)
    entry_theme_selected = ctk.CTkEntry(app, textvariable=selected)

    button_theme_primary.grid(row=2, column=0, padx=5, pady=5, sticky="NEWS")
    entry_theme_primary.grid(row=2, column=1, padx=5, pady=5, sticky="NEWS")
    button_theme_onprimary.grid(row=3, column=0, padx=5, pady=5, sticky="NEWS")
    entry_theme_onprimary.grid(row=3, column=1, padx=5, pady=5, sticky="NEWS")
    button_theme_secondary.grid(row=2, column=2, padx=5, pady=5, sticky="NEWS")
    entry_theme_secondary.grid(row=2, column=3, padx=5, pady=5, sticky="NEWS")
    button_theme_onsecondary.grid(row=3, column=2, padx=5, pady=5, sticky="NEWS")
    entry_theme_onsecondary.grid(row=3, column=3, padx=5, pady=5, sticky="NEWS")
    button_theme_tertiary.grid(row=2, column=4, padx=5, pady=5, sticky="NEWS")
    entry_theme_tertiary.grid(row=2, column=5, padx=5, pady=5, sticky="NEWS")
    button_theme_ontertiary.grid(row=3, column=4, padx=5, pady=5, sticky="NEWS")
    entry_theme_ontertiary.grid(row=3, column=5, padx=5, pady=5, sticky="NEWS")
    button_theme_hover.grid(row=4, column=0, padx=5, pady=5, sticky="NEWS")
    entry_theme_hover.grid(row=4, column=1, padx=5, pady=5, sticky="NEWS")
    button_theme_selected.grid(row=4, column=4, padx=5, pady=5, sticky="NEWS")
    entry_theme_selected.grid(row=4, column=5, padx=5, pady=5, sticky="NEWS")

    #TODO: List Drives & Hard code relative paths of css files

    #File Paths
    entry_deployed_maximo_file = ctk.CTkEntry(app,textvariable=deployed_maximo_path)
    entry_maximo_file = ctk.CTkEntry(app, textvariable=maximo_path)
    entry_deployed_login_file = ctk.CTkEntry(app, textvariable=login_path)
    button_deployed_maximo_file = ctk.CTkButton(app, text="Deployed Maximo CSS", command=lambda: set_file_path_buttons(entry_deployed_maximo_file))
    button_deployed_login_file = ctk.CTkButton(app, text="Deploy Login CSS", command=lambda: set_file_path_buttons(entry_deployed_login_file))
    button_maximo_file = ctk.CTkButton(app, text="Maximo CSS", command=lambda: set_file_path_buttons(entry_maximo_file))
    
    button_deployed_maximo_file.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="NEWS")
    entry_deployed_maximo_file.grid(row=5, column=2, columnspan=4, padx=5, pady=5, sticky="NEWS")
    button_deployed_login_file.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="NEWS")
    entry_deployed_login_file.grid(row=6, column=2, columnspan=4, padx=5, pady=5, sticky="NEWS")
    button_maximo_file.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="NEWS")
    entry_maximo_file.grid(row=7, column=2, columnspan=4, padx=5, pady=5, sticky="NEWS")
    
    #Apply button
    apply_button = ctk.CTkButton(app, text="Apply Theme", command=lambda: apply(theme))
    apply_button.grid(row=8, column=0, columnspan=6, padx=5, pady=5, sticky="NEWS")
    
    primary.trace_add('write', 
                      lambda *args, 
                      theme=theme, 
                      key=('maximo_theme', 'primary'): 
                          update(theme, key, primary.get()))
    
    app.mainloop()

def set_file_path_buttons(entry: ctk.CTkEntry):
    entry.delete(0, ctk.END)
    entry.insert(0, ctk.filedialog.askopenfilename(
        filetypes=(("CSS Files", "*.css"),
                ("All Files", "*.*"))
        ))
    return

def apply(theme: dict):
    maximo_theme_setter.main(theme)
    return

def save(theme: dict):
    with open(theme_file_name, "w") as f:
        json.dump(theme, f, indent=4)
    return

def update(theme: dict, key: tuple[str, str], value: str, ):
    print(f"Log: key:{key}, value:{value}")
    theme[key[0]][key[1]] = value
    save(theme)
    return

main()