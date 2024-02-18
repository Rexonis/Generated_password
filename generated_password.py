import tkinter as tk
import random
import string

def generate_password():
    # Получаем выбранные пользователем настройки
    password_length = length_scale.get()
    use_characters = [var.get() for var in vars_list]

    # Создаем строку символов на основе выбранных настроек
    characters = ''
    for i, option in enumerate(use_characters):
        if option:
            characters += CHARACTERS_SET[i]

    # Если не выбран ни один тип символов, выводим сообщение об ошибке
    if not characters:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Выберите хотя бы один тип символов")
        return

    # Генерируем пароль и выводим его
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")

# Поле для отображения пароля
password_entry = tk.Entry(root, width=50, justify="center")
password_entry.pack(pady=10)

# Символьные наборы
CHARACTERS_SET = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

# Создание фрейма для настроек пароля
settings_frame = tk.Frame(root, padx=20, pady=20)
settings_frame.pack()

# Длина пароля
length_label = tk.Label(settings_frame, text="Длина пароля:")
length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_scale = tk.Scale(settings_frame, from_=4, to=32, orient=tk.HORIZONTAL, length=200)
length_scale.grid(row=0, column=1, padx=10, pady=5)

# Тумблеры для выбора типов символов
labels = ["Строчные буквы", "Заглавные буквы", "Цифры", "Специальные символы"]
vars_list = []

# Создаем тумблеры и добавляем их в список для дальнейшего использования
for i, label_text in enumerate(labels):
    var = tk.BooleanVar()
    var.set(True)
    vars_list.append(var)
    check = tk.Checkbutton(settings_frame, text=label_text, variable=var)
    check.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

# Кнопка для генерации пароля
generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password, width=20)
generate_button.pack(pady=10)

# Запуск главного цикла программы
root.mainloop()