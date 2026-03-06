import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Archivos")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.root.configure(bg="#f0f0f0")
        
        # Variable para almacenar la ruta seleccionada
        self.selected_directory = tk.StringVar()
        
        # Categorías de archivos
        self.categories = {
            'Documents': ['pdf', 'docx', 'txt', 'xlsx', 'doc', 'ppt', 'pptx'],
            'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'ico'],
            'Videos': ['mp4', 'avi', 'mkv', 'mov', 'flv', 'wmv'],
            'Music': ['mp3', 'wav', 'flac', 'aac', 'm4a', 'ogg'],
            'Archives': ['zip', 'rar', '7z', 'tar', 'gz'],
            'Code': ['py', 'js', 'html', 'css', 'java', 'cpp', 'c'],
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # Título principal
        title_label = tk.Label(
            self.root, 
            text="Organizador de Archivos", 
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=15)
        
        # Marco para seleccionar directorio
        frame_dir = tk.LabelFrame(
            self.root, 
            text="Seleccionar Directorio", 
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        frame_dir.pack(padx=15, pady=10, fill="x")
        
        # Campo de texto para mostrar ruta
        self.dir_label = tk.Label(
            frame_dir, 
            text="No se ha seleccionado ningún directorio", 
            font=("Arial", 9),
            bg="white",
            fg="#666666",
            padx=10,
            pady=8
        )
        self.dir_label.pack(fill="x", pady=(0, 10))
        
        # Botón para seleccionar directorio
        btn_select = tk.Button(
            frame_dir,
            text="📁 Seleccionar Directorio",
            command=self.select_directory,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8,
            cursor="hand2"
        )
        btn_select.pack(fill="x")
        
        # Marco de categorías
        frame_categories = tk.LabelFrame(
            self.root,
            text="Categorías Configuradas",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        frame_categories.pack(padx=15, pady=10, fill="both", expand=True)
        
        # Mostrar categorías
        categories_text = "\n".join([
            f"• {category}: {', '.join(ext for ext in extensions)}"
            for category, extensions in self.categories.items()
        ])
        
        categories_label = tk.Label(
            frame_categories,
            text=categories_text,
            font=("Arial", 8),
            bg="#f0f0f0",
            fg="#333333",
            justify="left"
        )
        categories_label.pack(fill="both", expand=True)
        
        # Botones de acción
        frame_buttons = tk.Frame(self.root, bg="#f0f0f0")
        frame_buttons.pack(padx=15, pady=15, fill="x")
        
        btn_organize = tk.Button(
            frame_buttons,
            text="▶ Organizar Archivos",
            command=self.organize_files,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_organize.pack(side="left", padx=5, expand=True, fill="x")
        
        btn_exit = tk.Button(
            frame_buttons,
            text="✕ Salir",
            command=self.root.quit,
            bg="#f44336",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10,
            cursor="hand2"
        )
        btn_exit.pack(side="left", padx=5, expand=True, fill="x")
    
    def select_directory(self):
        """Permite seleccionar un directorio"""
        directory = filedialog.askdirectory(title="Selecciona el directorio a organizar")
        
        if directory:
            self.selected_directory.set(directory)
            # Mostrar solo el último nivel del directorio en la GUI
            short_path = os.path.basename(directory) or directory
            self.dir_label.config(
                text=f"✓ {short_path}\n{directory}",
                fg="#2E7D32"
            )
    
    def organize_files(self):
        """Organiza los archivos del directorio seleccionado"""
        
        if not self.selected_directory.get():
            messagebox.showwarning(
                "Advertencia",
                "Por favor, selecciona un directorio primero."
            )
            return
        
        source_folder = self.selected_directory.get()
        
        # Verificar que la carpeta exista
        if not os.path.isdir(source_folder):
            messagebox.showerror(
                "Error",
                "El directorio no existe o no es válido."
            )
            return
        
        try:
            # Contar archivos antes
            total_files = sum(
                1 for f in os.listdir(source_folder)
                if os.path.isfile(os.path.join(source_folder, f))
            )
            
            if total_files == 0:
                messagebox.showinfo(
                    "Información",
                    "El directorio no contiene archivos para organizar."
                )
                return
            
            # Organizar archivos
            moved_count = 0
            organized_files = {}
            
            for filename in os.listdir(source_folder):
                file_path = os.path.join(source_folder, filename)
                
                if os.path.isfile(file_path):
                    file_extension = filename.split('.')[-1].lower()
                    moved = False
                    
                    # Buscar categoría correspondiente
                    for category, extensions in self.categories.items():
                        if file_extension in extensions:
                            category_folder = os.path.join(source_folder, category)
                            os.makedirs(category_folder, exist_ok=True)
                            shutil.move(file_path, os.path.join(category_folder, filename))
                            moved_count += 1
                            organized_files[category] = organized_files.get(category, 0) + 1
                            moved = True
                            break
                    
                    # Si no tiene categoría, ir a "Other"
                    if not moved:
                        other_folder = os.path.join(source_folder, 'Other')
                        os.makedirs(other_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(other_folder, filename))
                        moved_count += 1
                        organized_files['Other'] = organized_files.get('Other', 0) + 1
            
            # Mostrar resultados
            result_message = "✓ ¡Archivos organizados correctamente!\n\n"
            result_message += f"Total de archivos movidos: {moved_count}\n\n"
            result_message += "Resumen por categoría:\n"
            
            for category, count in sorted(organized_files.items()):
                result_message += f"  • {category}: {count} archivo(s)\n"
            
            messagebox.showinfo(
                "Éxito",
                result_message
            )
            
        except PermissionError:
            messagebox.showerror(
                "Error de Permisos",
                "No tienes permisos para acceder a algunos archivos."
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrió un error inesperado:\n{str(e)}"
            )


def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
