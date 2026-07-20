from ursina import *

app = Ursina()

window.title = "СИМУЛЯТОР БОМЖА - Новосибирск Edition"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

# ФОН
bg = Entity(
    model='quad',
    scale=(20, 11.25),
    color=color.rgb(20, 30, 40),
    z=10
)

overlay = Entity(
    model='quad',
    scale=(20, 11.25),
    color=color.rgba(0, 0, 0, 150),
    z=9
)

# ЛОГОТИП
title = Text(
    text='СИМУЛЯТОР БОМЖА',
    origin=(0, 0),
    position=(0, 0.15),
    scale=2.5,
    color=color.rgb(100, 140, 160),
    background=True
)

subtitle = Text(
    text='Новосибирск Edition',
    origin=(0, 0),
    position=(0, 0.02),
    scale=1.2,
    color=color.light_gray,
    background=True
)

# КНОПКИ
play_btn = Button(
    text='ИГРАТЬ',
    scale=(0.35, 0.08),
    position=(0, -0.12),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    text_scale=0.8
)

settings_btn = Button(
    text='НАСТРОЙКИ',
    scale=(0.35, 0.08),
    position=(0, -0.22),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    text_scale=0.8
)

quit_btn = Button(
    text='ВЫХОД',
    scale=(0.35, 0.08),
    position=(0, -0.32),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    text_scale=0.8
)

# Эффекты при наведении
def btn_hover(btn):
    btn.color = color.rgba(80, 90, 100, 220)

def btn_normal(btn):
    btn.color = color.rgba(60, 70, 80, 200)

play_btn.on_mouse_enter = lambda: btn_hover(play_btn)
play_btn.on_mouse_exit = lambda: btn_normal(play_btn)

settings_btn.on_mouse_enter = lambda: btn_hover(settings_btn)
settings_btn.on_mouse_exit = lambda: btn_normal(settings_btn)

quit_btn.on_mouse_enter = lambda: btn_hover(quit_btn)
quit_btn.on_mouse_exit = lambda: btn_normal(quit_btn)

# Функции кнопок
def play_game():
    print("Запуск игры...")

def open_settings():
    print("Настройки...")

def quit_game():
    quit()

play_btn.on_click = play_game
settings_btn.on_click = open_settings
quit_btn.on_click = quit_game

app.run()