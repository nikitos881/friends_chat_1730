import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.create_frame as m_frame

button_width = 70
button_height = 50
margin_left = 50
button_color = "orange"


def send_message():
    button_label = ctk.CTkLabel(
        master = m_app.main_app, 
        text = m_input.text.get(),
        font = m_input.font_size

    )
    button_label.place(x = m_app.main_app.APP_WIDTH // 2, y = m_input.font_size._size // 2, anchor = ctk.CENTER)



send_button = ctk.CTkButton(
    master = m_app.main_app.FRAME3, 
    text ="->",
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    x = m_app.main_app.FRAME3._current_width // 2 + m_input.width_input // 2, 
    y = m_app.main_app.FRAME3._current_height - button_height, 
    anchor = ctk.CENTER
)