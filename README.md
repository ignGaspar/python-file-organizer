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
1. Download the latest version from releases

#### Installation
No installation required. Just run the `.exe` file directly.

#### How to Use
1. **Select directory**: Click "📁 Seleccionar Directorio" and choose the folder you want to organize
2. **Organize files**: Click "▶ Organizar Archivos"
3. **Review results**: The program will show a summary of organized files

#### ⚠️ Important
- The program will move files to subfolders within the selected directory
- Folders will be created automatically for each category
- Files without a category will go to the "Other" folder
- **Make a backup before using!**

### 🛠️ Development and Compilation

#### Prerequisites
- Python 3.8 or higher

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

### 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

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
1. Descarga la última versión en la página `releases`

#### Instalación
No requiere instalación. Solo ejecuta el archivo `.exe` directamente.

#### Cómo Usar
1. **Selecciona directorio**: Haz clic en "📁 Seleccionar Directorio" y elige la carpeta que quieres organizar
2. **Organiza archivos**: Haz clic en "▶ Organizar Archivos"
3. **Revisa resultados**: El programa mostrará un resumen de los archivos organizados

#### ⚠️ Importante
- El programa moverá los archivos a subcarpetas dentro del directorio seleccionado
- Se crearán carpetas automáticamente para cada categoría
- Los archivos sin categoría irán a la carpeta "Other"
- **¡Haz una copia de seguridad antes de usar!**

### 🛠️ Desarrollo y Compilación

#### Prerrequisitos
- Python 3.8 o superior
  
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

### 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request


### 🆘 Soporte

Si encuentras problemas:
1. Verifica que tengas permisos de escritura en el directorio
2. Asegúrate de que los archivos no estén siendo usados por otras aplicaciones
3. Revisa que el directorio no esté vacío

