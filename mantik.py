import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mantık():
    try:
        p = int(entryp.get())
        q = int(entryq.get())
        operator = mantıkchoice.get()

        if p not in (0, 1) or q not in (0, 1):
            raise ValueError("p ve q sadece 0 veya 1 olabilir.")

        # Mantık işlemleri
        if operator == "Ve (Λ)":
            result = p and q
        elif operator == "Veya (V)":
            result = p or q
        elif operator == "İse (⇒)":
            result = (not p) or q
        elif operator == "Ancak ve Ancak (⇔)":
            result = (p == q)
        elif operator == "Ya da (⊕)":
            result = (p != q)
        else:
            raise ValueError("Geçersiz bağlaç seçimi.")
        
        # Sonucu yüzdelik formatında gösterme
        result_percentage = f"{'Doğru' if result else 'Yanlış'}"
        resultlabel.config(text=f"Sonuç: {result_percentage}")
    except ValueError as e:
        messagebox.showerror("Hata", f"Geçersiz giriş: {e}")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Büyük yer
root = tk.Tk()
root.title("Mantık Bağlaçları")
root.geometry("250x350")  

# Ana frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Grid yapılandırması
root.rowconfigure(0, weight=1)  # Ana frame'in dikey olarak genişlemesi
root.columnconfigure(0, weight=1)  # Ana frame'in yatay olarak genişlemesi
frame.rowconfigure(list(range(3)), weight=1)  # Tüm satırların eşit şekilde genişlemesi
frame.columnconfigure(0, weight=1)  # İlk sütun genişlemesi
frame.columnconfigure(1, weight=2)  # İkinci sütun genişlemesi (orantılı daha fazla yer kaplar)

# 1. girdi
labelp = ttk.Label(frame, text="p (0 veya 1):")
labelp.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
entryp = ttk.Entry(frame)
entryp.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# 2. girdi
labelq = ttk.Label(frame, text="q (0 veya 1):")
labelq.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
entryq = ttk.Entry(frame)
entryq.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Mantık seçimi
mantıklabel = ttk.Label(frame, text="Bağlaç Seç:")
mantıklabel.grid(row=2, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
mantıkchoice = ttk.Combobox(frame, values=["Ve (Λ)", "Veya (V)", "İse (⇒)", "Ancak ve Ancak (⇔)", "Ya da (⊕)"], state="readonly")
mantıkchoice.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
mantıkchoice.current(0)

# Hesapla butonu
hesaplabutton = ttk.Button(frame, text="Hesapla", command=mantık)
hesaplabutton.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

# Sonuç etiketi
resultlabel = ttk.Label(frame, text="Sonuç: ")
resultlabel.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

root.mainloop()
