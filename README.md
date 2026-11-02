# Torres de Hanói 🗼

Juego interactivo de las **Torres de Hanói** desarrollado en Python con Tkinter. Incluye interfaz gráfica, movimiento manual de discos con el mouse y resolución automática mediante algoritmo recursivo.

## ✨ Características

- Interfaz gráfica desarrollada con Tkinter.
- Movimiento manual de discos mediante el mouse.
- Resolución automática utilizando recursividad.
- Animación de movimientos.
- Validación de las reglas del juego.
- Mensaje de victoria al completar el desafío.
- Interfaz visual con representación de las tres torres.

## 🛠️ Tecnologías utilizadas

- **Python 3.10 o superior**
- **Tkinter:** biblioteca para desarrollar interfaces gráficas.
- **Recursividad:** algoritmo para resolver las Torres de Hanói.

## 📋 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.
- Git (opcional, para clonar el repositorio).
- Tkinter.

Comprueba tu versión de Python:

```bash
python3 --version
```

## 📥 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/AlejandroG2310/TorresHanoi.git
```

### 2. Entrar al directorio

```bash
cd TorresHanoi
```

### 3. Crear un entorno virtual

**Windows:**

```bash
python -m venv venv
```

**Linux / Ubuntu:**

```bash
python3 -m venv venv
```

### 4. Activar el entorno virtual

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / Ubuntu:**

```bash
source venv/bin/activate
```

### 5. Instalar Tkinter

Tkinter normalmente viene incluido con Python en Windows.

En Ubuntu, si no está instalado, ejecuta:

```bash
sudo apt update
sudo apt install python3-tk
```

> **Nota:** El proyecto utiliza bibliotecas estándar de Python, por lo que no requiere instalar paquetes externos mediante `pip`.

## ▶️ Ejecutar el proyecto

Con el entorno virtual activado, ejecuta:

**Windows:**

```bash
python main.py
```

**Linux / Ubuntu:**

```bash
python3 main.py
```

Se abrirá la ventana del juego y podrás comenzar a jugar.

## 🎮 ¿Cómo jugar?

El objetivo es trasladar todos los discos desde la primera torre hasta la tercera, siguiendo estas reglas:

1. Solo puedes mover un disco a la vez.
2. Únicamente puedes mover el disco que se encuentra en la parte superior de una torre.
3. Nunca puedes colocar un disco grande sobre uno más pequeño.
4. Debes trasladar todos los discos a la torre de destino.

También puedes utilizar la resolución automática para observar cómo el algoritmo recursivo resuelve el desafío.

## 📂 Estructura del proyecto

```text
TorresHanoi/
│
├── main.py          # Código principal del juego
├── README.md        # Documentación del proyecto
├── .gitignore       # Archivos excluidos de Git
└── LICENSE          # Licencia del proyecto
```

## 🧠 Algoritmo

El solucionador automático utiliza recursividad para calcular los movimientos necesarios.

La cantidad mínima de movimientos para resolver el juego con `n` discos es:

\[
M = 2^n - 1
\]

Por ejemplo, con 5 discos se necesitan 31 movimientos.

## 👨‍💻 Autor

**AlejandroG2310**

GitHub: [@AlejandroG2310](https://github.com/AlejandroG2310)

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT. Consulta el archivo `LICENSE` para conocer sus condiciones de uso.

---

Desarrollado con Python 🐍