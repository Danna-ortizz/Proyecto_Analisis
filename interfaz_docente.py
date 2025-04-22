from datetime import datetime
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import clases as c

class interfaz_docente:
    def __init__(self, root, usuario):
        self.root = root
        self.root.title("Sistema docente")
        self.root.geometry("650x450")
        self.root.resizable(True, True)

        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Instanciamos las clases que necesitamos
        self.usuarios = c.usuarios()
        self.asistencia = c.asistencias()
        self.materias = c.materias()
        self.alumno = c.alumno()
        
        # Guardamos el usuario
        self.usuario = usuario
        self.nombre_usuario = self.usuarios.obtener_usuarios_nombre_id(usuario)

        self._construir_interfaz_docente()

    def regresar_button(self):
        self.frame_docente.destroy()
        self._construir_interfaz_docente()

    def escoger_alumno(self):
        alumno_selec = self.combobox_alumnos.get()
        return alumno_selec

    def _construir_interfaz_docente(self):
        self.frame_docente = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_docente.pack(fill='both', expand=True, padx=10, pady=10)

        def limpiar_frame_docente():
            for widget in self.frame_docente.winfo_children():
                widget.destroy()

        def construir_tab_ver_alumnos():
            limpiar_frame_docente()
            self._construir_tab_alumnos(self.frame_docente)

        def construir_tab_reg_asistencias():
            limpiar_frame_docente()
            self._construir_registrar_asistencias(self.frame_docente)

        # Botones en la interfaz principal
        self.button_ver_alumnos = ctk.CTkButton( self.frame_docente,  text="Ver Alumnos",  command=construir_tab_ver_alumnos)
        self.button_ver_alumnos.pack(pady=10)

        self.button_reg_asistencias = ctk.CTkButton( self.frame_docente,  text="Registrar Asistencias",  command=construir_tab_reg_asistencias)
        self.button_reg_asistencias.pack(pady=10)

    def _construir_tab_alumnos(self, parent):
        self.frame_alumnos = ctk.CTkFrame(parent, corner_radius=10)
        self.frame_alumnos.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_usuario = ctk.CTkLabel(self.frame_alumnos, text=f"Bienvenido {self.nombre_usuario}")
        self.label_usuario.pack(pady=10)

        # Frame scrollable para mostrar la lista de alumnos
        self.scrollableframe_alumnos = ctk.CTkScrollableFrame(self.frame_alumnos, width=250, height=200)
        self.scrollableframe_alumnos.pack(pady=10)

        # Encabezados de columna
        id_alumno_label = ctk.CTkLabel(self.scrollableframe_alumnos, text="ID")
        id_alumno_label.grid(row=0, column=0, padx=20)

        nombre_alumno_label = ctk.CTkLabel(self.scrollableframe_alumnos, text="Alumno")
        nombre_alumno_label.grid(row=0, column=1, padx=20)

        usuario_alumno_label = ctk.CTkLabel(self.scrollableframe_alumnos, text="Usuario")
        usuario_alumno_label.grid(row=0, column=2, padx=20)

        # Obtenemos todos los registros de alumnos
        registros = self.alumno.obtener_alumno()

        for i, fila in enumerate(registros, start=1):
  
            lbl_id = ctk.CTkLabel(self.scrollableframe_alumnos, text=str(fila[0]))
            lbl_id.grid(row=i, column=0, padx=20)

            lbl_nombre = ctk.CTkLabel(self.scrollableframe_alumnos, text=fila[3])
            lbl_nombre.grid(row=i, column=1, padx=20)

            lbl_usuario = ctk.CTkLabel(self.scrollableframe_alumnos, text=fila[1])
            lbl_usuario.grid(row=i, column=2, padx=20)

        self.regresar_button_alumnos = ctk.CTkButton(self.frame_alumnos, text="Regresar", command=self.regresar_button)
        self.regresar_button_alumnos.pack(pady=10)

    def _construir_registrar_asistencias(self, parent):
        self.frame_asistencias = ctk.CTkFrame(parent, corner_radius=10)
        self.frame_asistencias.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_alumno = ctk.CTkLabel(self.frame_asistencias, text="Selecciona el alumno")
        self.label_alumno.pack(pady=10)

        self.alumnos = self.alumno.obtener_alumno_nombre()
        self.combobox_alumnos = ctk.CTkComboBox(self.frame_asistencias, values=self.alumnos, width=200)
        self.combobox_alumnos.pack(pady=5)

        self.label_materias = ctk.CTkLabel(self.frame_asistencias, text="Escoge la materia")
        self.label_materias.pack(pady=10)

        self.materia = self.materias.obtener_materias_nombre()
        self.combobox_materia = ctk.CTkComboBox(self.frame_asistencias, values=self.materia, width=200)
        self.combobox_materia.pack(pady=10)

        self.frame_botones_asistecias = ctk.CTkFrame(self.frame_asistencias, corner_radius=10)
        self.frame_botones_asistecias.pack(pady=20, padx=20, fill="both", expand=True)

        def registrar_asistencia():
            alumno_selec = self.combobox_alumnos.get()
            id_alumno = self.alumno.obtener_alumno_id_nombre(alumno_selec)
            materia_selec = self.combobox_materia.get()
            id_materia = self.materias.obtener_materias_id_nombre(materia_selec)
            self.asistencia.registrar_asistencia(id_alumno, id_materia, None, None, 1)
            messagebox.showinfo("Aviso", "Asistencia Registrada")

        def registrar_falta():
            alumno_selec = self.combobox_alumnos.get()
            id_alumno = self.alumno.obtener_alumno_id_nombre(alumno_selec)
            materia_selec = self.combobox_materia.get()
            id_materia = self.materias.obtener_materias_id_nombre(materia_selec)
            self.asistencia.registrar_asistencia(id_alumno, id_materia, None, None, 0)
            messagebox.showinfo("Aviso", "Falta Registrada")

        def registrar_retardo():
            alumno_selec = self.combobox_alumnos.get()
            id_alumno = self.alumno.obtener_alumno_id_nombre(alumno_selec)
            materia_selec = self.combobox_materia.get()
            id_materia = self.materias.obtener_materias_id_nombre(materia_selec)
            self.asistencia.registrar_asistencia(id_alumno, id_materia, None, None, 2)
            messagebox.showinfo("Aviso", "Retardo Registrado")

        button_asistencia = ctk.CTkButton(self.frame_botones_asistecias, text="Registrar asistencia", command=registrar_asistencia)
        button_asistencia.pack(pady=10, padx=10, side="left")

        button_falta = ctk.CTkButton(self.frame_botones_asistecias, text="Registrar Falta", command=registrar_falta)
        button_falta.pack(pady=10, padx=10, side="left")

        button_retardo = ctk.CTkButton(self.frame_botones_asistecias, text="Registrar Retardo", command=registrar_retardo)
        button_retardo.pack(pady=10, padx=10, side="left")

        self.regresar_button_reg = ctk.CTkButton(self.frame_asistencias, text="Regresar", command=self.regresar_button)
        self.regresar_button_reg.pack(pady=10)
