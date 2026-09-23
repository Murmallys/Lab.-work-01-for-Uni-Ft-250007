import customtkinter as CTk
import math

#Функции задач
def Square_calculator(a: float, b: float, c: float):
    if a <= 0 or b <= 0 or c <= 0:
        return "Стороны должны быть положительными числами"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Такого треугольника не существует"
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return f"Площадь равна: {round(area, 2)}"


def convert_distance(value: float, from_unit: str, to_unit: str):
    to_meters = {
        "km": 1000.0,
        "m":  1.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "yd": 0.9144,
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result


def is_leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} — високосный год"
    else:
        return f"{year} — не високосный год"



#граф интерфейсс
class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x650")
        self.title("Лабораторная работа")
        self.resizable(False, False)

        self.tabview = CTk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        self.tabview.add("Задание 1.1")
        self.tabview.add("Задание 1.2")
        self.tabview.add("Задание 1.3")

        self._build_task1()
        self._build_task2()
        self._build_task3()

    #1.1
    def _build_task1(self):
        tab = self.tabview.tab("Задание 1.1")

        CTk.CTkLabel(tab, text="Площадь треугольника (формула Герона)",
                     font=("Arial", 22, "bold")).pack(pady=(30, 20))
        frame = CTk.CTkFrame(tab, fg_color="transparent")
        frame.pack(pady=10)

        self.a_entry = CTk.CTkEntry(frame, placeholder_text="Сторона a", width=180, height=40)
        self.a_entry.pack(side="left", padx=10)
        self.b_entry = CTk.CTkEntry(frame, placeholder_text="Сторона b", width=180, height=40)
        self.b_entry.pack(side="left", padx=10)
        self.c_entry = CTk.CTkEntry(frame, placeholder_text="Сторона c", width=180, height=40)
        self.c_entry.pack(side="left", padx=10)

        CTk.CTkButton(tab, text="Вычислить", width=200, height=40,
                      command=self._on_calc_area).pack(pady=20)

        self.area_result = CTk.CTkLabel(tab, text="", font=("Arial", 18))
        self.area_result.pack(pady=10)

    def _on_calc_area(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
        except ValueError:
            self.area_result.configure(text="Введите корректные числа")
            return

        result = Square_calculator(a, b, c)
        self.area_result.configure(text=result)

    #1.2
    def _build_task2(self):
        tab = self.tabview.tab("Задание 1.2")

        CTk.CTkLabel(tab, text="Конвертер расстояний",
                     font=("Arial", 22, "bold")).pack(pady=(30, 20))

        self.dist_value = CTk.CTkEntry(tab, placeholder_text="Значение", width=250, height=40)
        self.dist_value.pack(pady=15)

        units = ["km", "m", "cm", "mm", "mi", "yd"]

        frame = CTk.CTkFrame(tab, fg_color="transparent")
        frame.pack(pady=10)

        CTk.CTkLabel(frame, text="Из:", font=("Arial", 14)).pack(side="left", padx=10)
        self.from_unit = CTk.CTkComboBox(frame, values=units, width=120, height=35, state="readonly")
        self.from_unit.set("km")
        self.from_unit.pack(side="left", padx=10)

        CTk.CTkLabel(frame, text="В:", font=("Arial", 14)).pack(side="left", padx=10)
        self.to_unit = CTk.CTkComboBox(frame, values=units, width=120, height=35, state="readonly")
        self.to_unit.set("m")
        self.to_unit.pack(side="left", padx=10)

        CTk.CTkButton(tab, text="Конвертировать", width=200, height=40,
                      command=self._on_convert).pack(pady=20)

        self.dist_result = CTk.CTkLabel(tab, text="", font=("Arial", 18))
        self.dist_result.pack(pady=10)

    def _on_convert(self):
        try:
            value = float(self.dist_value.get())
        except ValueError:
            self.dist_result.configure(text="Введите корректное число")
            return

        from_u = self.from_unit.get()
        to_u = self.to_unit.get()

        try:
            result = convert_distance(value, from_u, to_u)
            self.dist_result.configure(text=f"{value} {from_u} = {result:.6g} {to_u}")
        except ValueError as e:
            self.dist_result.configure(text=str(e))

    #1.3
    def _build_task3(self):
        tab = self.tabview.tab("Задание 1.3")

        CTk.CTkLabel(tab, text="Определение високосного года",
                     font=("Arial", 22, "bold")).pack(pady=(30, 20))

        self.year_entry = CTk.CTkEntry(tab, placeholder_text="Введите год", width=250, height=40)
        self.year_entry.pack(pady=15)

        CTk.CTkButton(tab, text="Проверить", width=200, height=40,
                      command=self._on_check_year).pack(pady=20)

        self.year_result = CTk.CTkLabel(tab, text="", font=("Arial", 18))
        self.year_result.pack(pady=10)

    def _on_check_year(self):
        try:
            year = int(self.year_entry.get())
        except ValueError:
            self.year_result.configure(text="Введите целое число")
            return

        if year <= 0:
            self.year_result.configure(text="Год должен быть положительным")
            return

        result = is_leap_year(year)
        self.year_result.configure(text=result)


if __name__ == "__main__":
    app = App()
    app.mainloop()