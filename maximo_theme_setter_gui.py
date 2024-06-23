import customtkinter as ctk
import CTkColorPicker as ctkcp

def main():
    app = ctk.CTk()
    app.title("Maximo Theme Setter")
    app.geometry("600x400")

    label_theme_colors = ctk.CTkLabel(app, text="Theme Colors")

    label_theme_primary_preview = ctk.CTkLabel(app, text="Primary")
    label_theme_secondary_preview = ctk.CTkLabel(app, text="Secondary")
    label_theme_tertiary_preview = ctk.CTkLabel(app, text="Tertiary")
    label_theme_hover_preview = ctk.CTkLabel(app, text="Hover")
    label_theme_selected_preview = ctk.CTkLabel(app, text="Selected")

    button_theme_primary = ctk.CTkButton(app, text="Primary")
    button_theme_secondary = ctk.CTkButton(app, text="Secondary")
    button_theme_tertiary = ctk.CTkButton(app, text="Tertiary")
    button_theme_onprimary = ctk.CTkButton(app, text="OnPrimary")
    button_theme_onsecondary = ctk.CTkButton(app, text="OnSecondary")
    button_theme_ontertiary = ctk.CTkButton(app, text="OnTertiary")
    button_theme_hover = ctk.CTkButton(app, text="Hover")
    button_theme_selected = ctk.CTkButton(app, text="Selected")

    entry_theme_primary = ctk.CTkEntry(app)
    entry_theme_secondary = ctk.CTkEntry(app)
    entry_theme_tertiary = ctk.CTkEntry(app)
    entry_theme_onprimary = ctk.CTkEntry(app)
    entry_theme_onsecondary = ctk.CTkEntry(app)
    entry_theme_ontertiary = ctk.CTkEntry(app)
    entry_theme_hover = ctk.CTkEntry(app)
    entry_theme_selected = ctk.CTkEntry(app)

    app.grid_rowconfigure((0, 1), weight=1)
    app.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    label_theme_primary_preview.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_secondary_preview.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_tertiary_preview.grid(row=0, column=4, columnspan=2, padx=5, pady=5, sticky='NEWS')
    label_theme_hover_preview.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='NEWS')
    label_theme_selected_preview.grid(row=1, column=3, columnspan=3, padx=5, pady=5, sticky='NEWS')

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
    
    button_theme_hover.grid(row=4, column=1, padx=5, pady=20, sticky="NEWS")
    entry_theme_hover.grid(row=4, column=2, padx=5, pady=20, sticky="NEWS")
    
    button_theme_selected.grid(row=4, column=3, padx=5, pady=20, sticky="NEWS")
    entry_theme_selected.grid(row=4, column=4, padx=5, pady=20, sticky="NEWS")

    app.mainloop()

main()