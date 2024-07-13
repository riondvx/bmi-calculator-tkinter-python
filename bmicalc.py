import tkinter as tk
from tkinter import messagebox


class BmiCalc:

  def __init__(self, root):
    font = ("Helvetica", 14)

    root.title("Kalkulator BMI")
    root.configure(padx=10, pady=10)
    root.option_add("*Dialog.msg.font", font)

    # Label Rumus BMI
    self.formula_label = tk.Label(
        root,
        text="BMI = Kg/M²",
        font=font,
    )
    self.formula_label.grid(
        row=0,
        column=0,
        pady=10,
        sticky="w",
    )

    # Inputan Berat Badan
    self.weight_label = tk.Label(
        root,
        text="Berat Badan (kg)",
        font=font,
    )
    self.weight_label.grid(
        row=1,
        column=0,
        pady=10,
        sticky="w",
    )
    self.weight_entry = tk.Entry(
        root,
        font=font,
    )
    self.weight_entry.grid(
        row=1,
        column=1,
    )

    # Inputan Tinggi Badan
    self.height_label = tk.Label(
        root,
        text="Tinggi Badan (cm)",
        font=font,
    )
    self.height_label.grid(
        row=2,
        column=0,
        pady=10,
        sticky="w",
    )
    self.height_entry = tk.Entry(
        root,
        font=font,
    )
    self.height_entry.grid(
        row=2,
        column=1,
    )

    # Tombol Hitung BMI
    self.calculate_btn = tk.Button(
        root,
        text="Hitung BMI",
        command=self.calculate_bmi,
        font=font,
    )
    self.calculate_btn.grid(
        row=3,
        column=0,
        pady=10,
        columnspan=2,
    )

  def calculate_bmi(self):
    try:
      weight = float(self.weight_entry.get())
      height = float(self.height_entry.get()) / 100
      bmi = weight / (height**2)
      bmi = round(bmi, 1)
      explanation = self.get_bmi_explanation(bmi)
      messagebox.showinfo(
          "Hasil BMI",
          f"Score BMI: {bmi}\nPenjelasan: {explanation}",
      )
    except ValueError:
      messagebox.showerror(
          "Input Error",
          "Masukkan nilai yang valid.",
      )

  def get_bmi_explanation(self, bmi):
    if bmi < 18.5:
      return "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
      return "Berat badan normal"
    elif 25 <= bmi < 29.9:
      return "Berat badan berlebih"
    else:
      return "Obesitas"


if __name__ == "__main__":
  root = tk.Tk()
  app = BmiCalc(root)
  root.mainloop()
