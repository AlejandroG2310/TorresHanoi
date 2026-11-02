
import tkinter as tk
from tkinter import messagebox


class TorresHanoi:
    MARCA = "DEVLAB"
    COPYRIGHT = "© 2026 DEVLAB | Todos los derechos reservados"

    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanói | DEVLAB")
        self.root.geometry("750x590")
        self.root.resizable(False, False)
        self.root.configure(bg="#172033")

        self.num_discos = 5
        self.torres = [list(range(self.num_discos, 0, -1)), [], []]
        self.movimientos = 0
        self.dragging = None
        self.drag_origin = None
        self.drag_x = 0
        self.drag_y = 0
        self.auto_moves = []
        self.auto_running = False
        self.after_id = None
        self.colores = ["#EF4444", "#F97316", "#EAB308", "#22C55E", "#3B82F6", "#A855F7", "#EC4899"]
        self.posiciones = [120, 350, 580]

        self.crear_interfaz()
        self.dibujar()

    def crear_interfaz(self):
        tk.Label(self.root, text="TORRES DE HANÓI", font=("Arial", 25, "bold"), bg="#172033", fg="white").pack(pady=(15, 3))

        tk.Label(self.root, text=self.MARCA, font=("Arial", 10, "bold"), bg="#172033", fg="#38BDF8").pack(pady=(0, 10))

        self.info = tk.Label(self.root, text="Movimientos: 0", font=("Arial", 14, "bold"), bg="#172033", fg="#38BDF8")
        self.info.pack()

        self.canvas = tk.Canvas(self.root, width=700, height=350, bg="#263449", highlightthickness=0)
        self.canvas.pack(pady=15)
        self.canvas.bind("<ButtonPress-1>", self.iniciar_arrastre)
        self.canvas.bind("<B1-Motion>", self.arrastrar)
        self.canvas.bind("<ButtonRelease-1>", self.soltar)

        botones = tk.Frame(self.root, bg="#172033")
        botones.pack(pady=5)

        tk.Button(botones, text="Reiniciar", command=self.reiniciar, font=("Arial", 12, "bold"), bg="#2563EB", fg="white", padx=20, pady=8, relief="flat", cursor="hand2").pack(side="left", padx=10)

        tk.Button(botones, text="Resolver automáticamente", command=self.resolver, font=("Arial", 12, "bold"), bg="#16A34A", fg="white", padx=20, pady=8, relief="flat", cursor="hand2").pack(side="left", padx=10)

        self.mensaje = tk.Label(self.root, text="Arrastra un disco hacia otra torre.", font=("Arial", 11), bg="#172033", fg="white")
        self.mensaje.pack(pady=8)

        tk.Label(self.root, text=self.COPYRIGHT, font=("Arial", 9, "bold"), bg="#172033", fg="#94A3B8").pack(side="bottom", pady=12)

    def dibujar_disco(self, x, y, disco):
        ancho = 35 + disco * 22
        color = self.colores[(disco - 1) % len(self.colores)]
        self.canvas.create_rectangle(x - ancho, y, x + ancho, y + 25, fill=color, outline="white", width=2)

    def dibujar(self):
        self.canvas.delete("all")

        for i, x in enumerate(self.posiciones):
            self.canvas.create_rectangle(x - 5, 100, x + 5, 300, fill="#CBD5E1", outline="")
            self.canvas.create_rectangle(x - 95, 300, x + 95, 312, fill="#CBD5E1", outline="")
            self.canvas.create_text(x, 330, text=f"Torre {i + 1}", fill="white", font=("Arial", 12, "bold"))

            for nivel, disco in enumerate(self.torres[i]):
                if self.dragging is not None and i == self.drag_origin and nivel == len(self.torres[i]) - 1:
                    continue
                y = 300 - (nivel + 1) * 28
                self.dibujar_disco(x, y, disco)

        if self.dragging is not None:
            self.dibujar_disco(self.drag_x, self.drag_y - 12, self.dragging)

        # Marca de agua permanente dentro del área de juego
        self.canvas.create_text(690, 342, text="DEVLAB", anchor="se", fill="#64748B", font=("Arial", 10, "bold"))

        self.info.config(text=f"Movimientos: {self.movimientos}")

    def obtener_torre(self, x):
        return min(range(3), key=lambda i: abs(x - self.posiciones[i]))

    def iniciar_arrastre(self, evento):
        if self.auto_running:
            return

        torre = self.obtener_torre(evento.x)

        if not self.torres[torre]:
            self.mensaje.config(text="Esta torre está vacía.")
            return

        disco = self.torres[torre][-1]
        ancho = 35 + disco * 22
        centro = self.posiciones[torre]
        y = 300 - len(self.torres[torre]) * 28

        if centro - ancho <= evento.x <= centro + ancho and y <= evento.y <= y + 25:
            self.dragging = disco
            self.drag_origin = torre
            self.drag_x = evento.x
            self.drag_y = evento.y + 12
            self.dibujar()
        else:
            self.mensaje.config(text="Selecciona el disco superior.")

    def arrastrar(self, evento):
        if self.dragging is None:
            return

        self.drag_x = evento.x
        self.drag_y = evento.y + 12
        self.dibujar()

    def soltar(self, evento):
        if self.dragging is None:
            return

        origen = self.drag_origin
        destino = self.obtener_torre(evento.x)
        disco = self.dragging

        self.dragging = None
        self.drag_origin = None

        if origen == destino:
            self.mensaje.config(text="Movimiento cancelado.")
            self.dibujar()
            return

        if not self.torres[destino] or disco < self.torres[destino][-1]:
            self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos += 1
            self.mensaje.config(text="¡Movimiento realizado!")
            self.dibujar()
            self.verificar_victoria()
        else:
            self.mensaje.config(text="¡No puedes colocar un disco grande sobre uno pequeño!")
            self.dibujar()

    def verificar_victoria(self):
        if len(self.torres[2]) == self.num_discos:
            minimo = 2 ** self.num_discos - 1
            self.auto_running = False
            messagebox.showinfo("¡Felicidades!", f"¡Resolviste las Torres de Hanói!\n\nMovimientos: {self.movimientos}\nMínimo posible: {minimo}\n\nDesarrollado por DEVLAB")

    def reiniciar(self):
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.auto_running = False
        self.auto_moves.clear()
        self.torres = [list(range(self.num_discos, 0, -1)), [], []]
        self.movimientos = 0
        self.dragging = None
        self.drag_origin = None
        self.mensaje.config(text="Juego reiniciado.")
        self.dibujar()

    def generar_movimientos(self, n, origen, destino, auxiliar):
        if n == 0:
            return

        self.generar_movimientos(n - 1, origen, auxiliar, destino)
        self.auto_moves.append((origen, destino))
        self.generar_movimientos(n - 1, auxiliar, destino, origen)

    def resolver(self):
        self.reiniciar()
        self.generar_movimientos(self.num_discos, 0, 2, 1)
        self.auto_running = True
        self.mensaje.config(text="Resolviendo automáticamente...")
        self.after_id = self.root.after(500, self.ejecutar_siguiente)

    def ejecutar_siguiente(self):
        self.after_id = None

        if not self.auto_moves:
            self.auto_running = False
            self.mensaje.config(text="¡Resolución automática completada!")
            self.verificar_victoria()
            return

        origen, destino = self.auto_moves.pop(0)
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1
        self.dibujar()
        self.after_id = self.root.after(400, self.ejecutar_siguiente)


if __name__ == "__main__":
    root = tk.Tk()
    app = TorresHanoi(root)
    root.mainloop()
