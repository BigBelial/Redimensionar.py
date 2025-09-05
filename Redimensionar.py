import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

class RedimensionadorImagenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Redimensionador de Imágenes")
        self.root.geometry("900x500")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.imagen_path = tk.StringVar()
        self.ancho_var = tk.IntVar(value=1920)
        self.alto_var = tk.IntVar(value=1080)
        self.imagen_original = None
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.root, text="🖼️ Redimensionador de Imágenes", 
                         font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=20)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Sección seleccionar imagen
        select_frame = tk.LabelFrame(main_frame, text="Seleccionar Imagen", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        select_frame.pack(fill='x', pady=10)
        
        # Botón seleccionar imagen
        btn_seleccionar = tk.Button(select_frame, text="📁 Seleccionar Imagen", 
                                  command=self.seleccionar_imagen, bg='#3498db', 
                                  fg='white', font=('Arial', 11), cursor='hand2',
                                  relief='flat', padx=20, pady=10)
        btn_seleccionar.pack(pady=15)
        
        # Label para mostrar ruta
        self.label_ruta = tk.Label(select_frame, textvariable=self.imagen_path, 
                                 bg='#f0f0f0', fg='#7f8c8d', font=('Arial', 9),
                                 wraplength=500)
        self.label_ruta.pack(pady=(0, 15))
        
        # Sección dimensiones
        dim_frame = tk.LabelFrame(main_frame, text="Dimensiones Deseadas", 
                                font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        dim_frame.pack(fill='x', pady=10)
        
        # Frame para dimensiones
        input_frame = tk.Frame(dim_frame, bg='#f0f0f0')
        input_frame.pack(pady=15)
        
        # Ancho
        tk.Label(input_frame, text="Ancho:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=0, column=0, padx=10, sticky='e')
        entry_ancho = tk.Entry(input_frame, textvariable=self.ancho_var, 
                              font=('Arial', 10), width=10, justify='center')
        entry_ancho.grid(row=0, column=1, padx=5)
        tk.Label(input_frame, text="px", font=('Arial', 9), 
                bg='#f0f0f0', fg='#7f8c8d').grid(row=0, column=2, padx=5)
        
        # Alto
        tk.Label(input_frame, text="Alto:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=0, column=3, padx=10, sticky='e')
        entry_alto = tk.Entry(input_frame, textvariable=self.alto_var, 
                             font=('Arial', 10), width=10, justify='center')
        entry_alto.grid(row=0, column=4, padx=5)
        tk.Label(input_frame, text="px", font=('Arial', 9), 
                bg='#f0f0f0', fg='#7f8c8d').grid(row=0, column=5, padx=5)
        
        # Botones de resoluciones predefinidas
        presets_frame = tk.Frame(dim_frame, bg='#f0f0f0')
        presets_frame.pack(pady=10)
        
        resoluciones = [
            ("Full HD", 1920, 1080),
            ("HD", 1280, 720),
            ("4K", 3840, 2160),
            ("Instagram", 1080, 1080)
        ]
        
        for texto, ancho, alto in resoluciones:
            btn = tk.Button(presets_frame, text=texto, 
                           command=lambda a=ancho, h=alto: self.set_resolution(a, h),
                           bg='#e74c3c', fg='white', font=('Arial', 9),
                           relief='flat', padx=10, pady=5, cursor='hand2')
            btn.pack(side='left', padx=5)
        
        # Preview frame (opcional)
        
        # Botón procesar
        btn_procesar = tk.Button(main_frame, text="✨ Redimensionar y Guardar", 
                               command=self.procesar_imagen, bg='#27ae60', 
                               fg='white', font=('Arial', 12, 'bold'), 
                               cursor='hand2', relief='flat', pady=15)
        btn_procesar.pack(pady=20)
        
        # Barra de progreso
        self.progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress_bar.pack(fill='x', pady=10)
        self.progress_bar.pack_forget()
        
    def seleccionar_imagen(self):
        tipos_archivo = [
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
            ("JPEG", "*.jpg *.jpeg"),
            ("PNG", "*.png"),
            ("Todos los archivos", "*.*")
        ]
        
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=tipos_archivo
        )
        
        if archivo:
            self.imagen_path.set(f"📁 {os.path.basename(archivo)}")
            self.imagen_original = archivo
            # ...vista previa eliminada...
            
    def mostrar_preview(self):
        # ...función de vista previa eliminada...
        pass
            
    def set_resolution(self, ancho, alto):
        self.ancho_var.set(ancho)
        self.alto_var.set(alto)
        
    def procesar_imagen(self):
        if not self.imagen_original:
            messagebox.showwarning("Advertencia", "Por favor selecciona una imagen primero")
            return
            
        try:
            # Mostrar barra de progreso
            self.progress_bar.pack(fill='x', pady=10)
            self.progress_bar.start()
            self.root.update()
            
            # Abrir la imagen
            imagen = Image.open(self.imagen_original)
            
            # Obtener dimensiones deseadas
            ancho_deseado = self.ancho_var.get()
            alto_deseado = self.alto_var.get()
            
            # Redimensionar
            imagen_redimensionada = imagen.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
            
            # Generar nombre de archivo de salida
            base_name = os.path.splitext(os.path.basename(self.imagen_original))[0]
            extension = os.path.splitext(self.imagen_original)[1]
            
            archivo_salida = filedialog.asksaveasfilename(
                title="Guardar imagen redimensionada",
                defaultextension=extension,
                initialfile=f"{base_name}_redimensionada{extension}",
                filetypes=[
                    ("JPEG", "*.jpg"),
                    ("PNG", "*.png"),
                    ("BMP", "*.bmp"),
                    ("TIFF", "*.tiff")
                ]
            )
            
            if archivo_salida:
                # Guardar la imagen
                if archivo_salida.lower().endswith(('.jpg', '.jpeg')):
                    imagen_redimensionada.save(archivo_salida, "JPEG", quality=95)
                else:
                    imagen_redimensionada.save(archivo_salida)
                
                # Ocultar barra de progreso
                self.progress_bar.stop()
                self.progress_bar.pack_forget()
                
                messagebox.showinfo("Éxito", 
                                  f"¡Imagen redimensionada exitosamente!\n"
                                  f"Guardada como: {os.path.basename(archivo_salida)}\n"
                                  f"Resolución: {ancho_deseado}x{alto_deseado}")
            else:
                self.progress_bar.stop()
                self.progress_bar.pack_forget()
                
        except Exception as e:
            self.progress_bar.stop()
            self.progress_bar.pack_forget()
            messagebox.showerror("Error", f"Error al procesar la imagen: {str(e)}")

def main():
    root = tk.Tk()
    app = RedimensionadorImagenes(root)
    root.mainloop()

if __name__ == "__main__":
    main()