import tkinter as tk
from tkinter import filedialog, CENTER
from PyPDF2 import PdfMerger

class PDFCombinerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Combiner")

        # Lista para almacenar los archivos PDF seleccionados
        self.pdf_files = []

        # Ajustar el tamaño de la ventana y centrarla
        window_width = 500
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        self.root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Crear y configurar elementos de la GUI
        font_size = 16  # Tamaño de fuente personalizado

        self.select_button = tk.Button(root, text="Seleccionar archivos", font=("Arial", font_size), command=self.select_files)
        self.select_button.pack(side="top", pady=10)

        self.combine_button = tk.Button(root, text="Combinar archivos", font=("Arial", font_size), command=self.combine_pdfs, state=tk.DISABLED)
        self.combine_button.pack(side="top", pady=10)

        # Etiqueta con tu frase
        self.label = tk.Label(root, text="Programa desarrollado por Luis David Castañeda Jimenez", font=("Arial", 12))
        self.label.pack(side="bottom")

        # Centrar los elementos en la ventana
        self.label.config(anchor=CENTER)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if file_paths:
            self.pdf_files = file_paths
            self.combine_button.config(state=tk.NORMAL)
            print("Archivos seleccionados:")
            for file_path in self.pdf_files:
                print(file_path)

    def combine_pdfs(self):
        if self.pdf_files:
            merger = PdfMerger()
            for pdf_file in self.pdf_files:
                merger.append(pdf_file)
            output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output_file:
                merger.write(output_file)
                merger.close()
                print(f"Archivos combinados y guardados como: {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFCombinerApp(root)
    root.mainloop()
