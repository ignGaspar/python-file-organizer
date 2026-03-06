# 🗂️ File Organizer / Organizador de Archivos

---

## 🇺🇸 English

An automatic file organizer with a graphical interface that classifies your files by type and extension.

### ✨ Features

- **Intuitive GUI** - Easy to use without technical knowledge
- **Automatic Organization** - Classifies files by predefined categories
- **Smart Categories** - Documents, images, videos, music, compressed files, source code
- **Informative Messages** - Clear feedback during the process
- **Standalone Executable** - No Python installation required
- **Error Handling** - Permission and file validation

### 📁 File Categories

The organizer automatically classifies files into the following categories:

- **📄 Documents**: `pdf`, `docx`, `txt`, `xlsx`, `doc`, `ppt`, `pptx`
- **🖼️ Images**: `jpg`, `jpeg`, `png`, `gif`, `bmp`, `svg`, `ico`
- **🎬 Videos**: `mp4`, `avi`, `mkv`, `mov`, `flv`, `wmv`
- **🎵 Music**: `mp3`, `wav`, `flac`, `aac`, `m4a`, `ogg`
- **📦 Archives**: `zip`, `rar`, `7z`, `tar`, `gz`
- **💻 Code**: `py`, `js`, `html`, `css`, `java`, `cpp`, `c`
- **📂 Other**: Files without a defined category

### 🚀 Using the Executable

#### Download
1. Go to the `dist/` folder of the project
2. Copy the `Organizador de Archivos.exe` file

#### Installation
No installation required. Just run the `.exe` file directly.

#### How to Use
1. **Run the program**: Double-click `Organizador de Archivos.exe`
2. **Select directory**: Click "📁 Seleccionar Directorio" and choose the folder you want to organize
3. **Organize files**: Click "▶ Organizar Archivos"
4. **Review results**: The program will show a summary of organized files

#### ⚠️ Important
- The program will move files to subfolders within the selected directory
- Folders will be created automatically for each category
- Files without a category will go to the "Other" folder
- **Make a backup before using!**

### 🛠️ Development and Compilation

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

#### Clone Repository
```bash
git clone https://github.com/your-username/python-file-organizer.git
cd python-file-organizer
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Run Source Code
```bash
python file-organizer/organizer.py
```

#### Create Executable
To create a standalone executable:

1. **Install PyInstaller**:
```bash
pip install pyinstaller
```

2. **Create executable**:
```bash
pyinstaller --onefile --windowed --distpath dist file-organizer/organizer.py -n "Organizador de Archivos"
```

3. **The executable will be created in** `dist/Organizador de Archivos.exe`

#### Project Structure
```
python-file-organizer/
├── file-organizer/
│   ├── organizer.py          # Main code with GUI
│   └── __pycache__/          # Compiled files (ignore)
├── dist/
│   └── Organizador de Archivos.exe    # Generated executable
├── build/                    # PyInstaller temporary files
├── Organizador de Archivos.spec       # PyInstaller specification
├── README.md                 # This file
└── .gitignore               # Files to ignore in Git
```

### 📋 System Requirements

- **Operating System**: Windows 10/11
- **Architecture**: x64
- **Disk Space**: ~12MB for executable
- **Permissions**: Read/write access to directory to organize

### 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### 📄 License

This project is under the MIT License. See the `LICENSE` file for more details.

### 🆘 Support

If you encounter problems:
1. Check that you have write permissions in the directory
2. Make sure files are not being used by other applications
3. Check that the directory is not empty

---

## 🇪🇸 Español

Un organizador de archivos automático con interfaz gráfica que clasifica tus archivos por tipo y extensión.

### ✨ Características

- **Interfaz gráfica intuitiva** - Fácil de usar sin conocimientos técnicos
- **Organización automática** - Clasifica archivos por categorías predefinidas
- **Categorías inteligentes** - Documentos, imágenes, videos, música, archivos comprimidos, código fuente
- **Mensajes informativos** - Retroalimentación clara durante el proceso
- **Ejecutable independiente** - No requiere instalación de Python
- **Manejo de errores** - Validación de permisos y archivos

### 📁 Categorías de Archivos

El organizador clasifica automáticamente los archivos en las siguientes categorías:

- **📄 Documents**: `pdf`, `docx`, `txt`, `xlsx`, `doc`, `ppt`, `pptx`
- **🖼️ Images**: `jpg`, `jpeg`, `png`, `gif`, `bmp`, `svg`, `ico`
- **🎬 Videos**: `mp4`, `avi`, `mkv`, `mov`, `flv`, `wmv`
- **🎵 Music**: `mp3`, `wav`, `flac`, `aac`, `m4a`, `ogg`
- **📦 Archives**: `zip`, `rar`, `7z`, `tar`, `gz`
- **💻 Code**: `py`, `js`, `html`, `css`, `java`, `cpp`, `c`
- **📂 Other**: Archivos sin categoría definida

### 🚀 Uso del Ejecutable

#### Descarga
1. Ve a la carpeta `dist/` del proyecto
2. Copia el archivo `Organizador de Archivos.exe`

#### Instalación
No requiere instalación. Solo ejecuta el archivo `.exe` directamente.

#### Cómo Usar
1. **Ejecuta el programa**: Haz doble clic en `Organizador de Archivos.exe`
2. **Selecciona directorio**: Haz clic en "📁 Seleccionar Directorio" y elige la carpeta que quieres organizar
3. **Organiza archivos**: Haz clic en "▶ Organizar Archivos"
4. **Revisa resultados**: El programa mostrará un resumen de los archivos organizados

#### ⚠️ Importante
- El programa moverá los archivos a subcarpetas dentro del directorio seleccionado
- Se crearán carpetas automáticamente para cada categoría
- Los archivos sin categoría irán a la carpeta "Other"
- **¡Haz una copia de seguridad antes de usar!**

### 🛠️ Desarrollo y Compilación

#### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

#### Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/python-file-organizer.git
cd python-file-organizer
```

#### Instalar Dependencias
```bash
pip install -r requirements.txt
```

#### Ejecutar el Código Fuente
```bash
python file-organizer/organizer.py
```

#### Crear Ejecutable
Para crear un ejecutable independiente:

1. **Instalar PyInstaller**:
```bash
pip install pyinstaller
```

2. **Crear el ejecutable**:
```bash
pyinstaller --onefile --windowed --distpath dist file-organizer/organizer.py -n "Organizador de Archivos"
```

3. **El ejecutable se creará en** `dist/Organizador de Archivos.exe`

#### Estructura del Proyecto
```
python-file-organizer/
├── file-organizer/
│   ├── organizer.py          # Código principal con GUI
│   └── __pycache__/          # Archivos compilados (ignorar)
├── dist/
│   └── Organizador de Archivos.exe    # Ejecutable generado
├── build/                    # Archivos temporales de PyInstaller
├── Organizador de Archivos.spec       # Especificación de PyInstaller
├── README.md                 # Este archivo
└── .gitignore               # Archivos a ignorar en Git
```

### 📋 Requisitos del Sistema

- **Sistema Operativo**: Windows 10/11
- **Arquitectura**: x64
- **Espacio en disco**: ~12MB para el ejecutable
- **Permisos**: Lectura/escritura en el directorio a organizar

### 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

### 🆘 Soporte

Si encuentras problemas:
1. Verifica que tengas permisos de escritura en el directorio
2. Asegúrate de que los archivos no estén siendo usados por otras aplicaciones
3. Revisa que el directorio no esté vacío

---

**¡Enjoy organizing your files automatically!** 🎉 **¡Disfruta organizando tus archivos de manera automática!** 🎉