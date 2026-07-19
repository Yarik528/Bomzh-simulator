from ursina import *

app = Ursina()

# Настройки окна
window.title = "СИМУЛЯТОР БОМЖА - Новосибирск Edition"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

# ===== ФОНОВОЕ ИЗОБРАЖЕНИЕ =====
# Создаём затемнённый фон (позже можно заменить на текстуру двора)
bg = Entity(
    model='quad',
    scale=(20, 11.25),  # 16:9 соотношение
    color=color.rgb(20, 30, 40),  # Тёмно-синий оттенок
    z=10
)

# Затемнение фона (оверлей)
overlay = Entity(
    model='quad',
    scale=(20, 11.25),
    color=color.rgba(0, 0, 0, 150),  # Полупрозрачный чёрный
    z=9
)

# ===== ЛОГОТИП =====
title = Text(
    text='СИМУЛЯТОР БОМЖА',
    font='Vera.ttf',  # Можно заменить на свой шрифт
    origin=(0, 0),
    position=(0, 0.15),
    scale=2.5,
    color=color.rgb(100, 140, 160),  # Серо-голубой
    background=True
)

# Эффект "потёртости" для логотипа (тень)
title_shadow = Text(
    text='СИМУЛЯТОР БОМЖА',
    origin=(0, 0),
    position=(0.02, 0.13),
    scale=2.5,
    color=color.rgba(0, 0, 0, 100),
    background=False
)

# Подзаголовок
subtitle = Text(
    text='Новосибирск Edition',
    origin=(0, 0),
    position=(0, 0.02),
    scale=1.2,
    color=color.light_gray,
    background=True
)

# ===== КНОПКИ =====
button_width = 0.35
button_height = 0.08
button_y_start = -0.12
button_spacing = 0.1

# Кнопка ИГРАТЬ
play_btn = Button(
    text='ИГРАТЬ',
    scale=(button_width, button_height),
    position=(0, button_y_start),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    font='Vera.ttf',
    text_scale=0.8
)

# Кнопка НАСТРОЙКИ
settings_btn = Button(
    text='НАСТРОЙКИ',
    scale=(button_width, button_height),
    position=(0, button_y_start - button_spacing),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    font='Vera.ttf',
    text_scale=0.8
)

# Кнопка ВЫХОД
quit_btn = Button(
    text='ВЫХОД',
    scale=(button_width, button_height),
    position=(0, button_y_start - button_spacing * 2),
    color=color.rgba(60, 70, 80, 200),
    text_color=color.white,
    font='Vera.ttf',
    text_scale=0.8
)

# Эффекты при наведении на кнопки
def btn_hover(btn):
    btn.color = color.rgba(80, 90, 100, 220)
    btn.text_scale = 0.85

def btn_normal(btn):
    btn.color = color.rgba(60, 70, 80, 200)
    btn.text_scale = 0.8

play_btn.on_mouse_enter = lambda: btn_hover(play_btn)
play_btn.on_mouse_exit = lambda: btn_normal(play_btn)

settings_btn.on_mouse_enter = lambda: btn_hover(settings_btn)
settings_btn.on_mouse_exit = lambda: btn_normal(settings_btn)

quit_btn.on_mouse_enter = lambda: btn_hover(quit_btn)
quit_btn.on_mouse_exit = lambda: btn_normal(quit_btn)

# ===== ФУНКЦИИ КНОПОК =====
def play_game():
    print("Запуск игры...")
    # Здесь будет загрузка игровой сцены

def open_settings():
    print("Открытие настроек...")
    # Здесь будет меню настроек

def quit_game():
    print("Выход из игры...")
    quit()

play_btn.on_click = play_game
settings_btn.on_click = open_settings
quit_btn.on_click = quit_game

# ===== АНИМАЦИЯ ФОНА (опционально) =====
# Можно добавить лёгкое движение камеры или частицы

cursor = Entity(
    model='circle',
    color=color.white,
    scale=0.01,
    visible=True
)

def update():
    # Лёгкая анимация "дыхания" для фона
    bg.color = color.lerp(
        color.rgb(20, 30, 40),
        color.rgb(25, 35, 45),
        (time.time() % 4) / 4
    )

app.run()