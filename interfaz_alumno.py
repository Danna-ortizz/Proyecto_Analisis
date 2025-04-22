from datetime import datetime
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import clases as c

class InterfazAlumno:
    def __init__(self, root, usuario):
        # Configuración de la ventana
        self.root = root
        self.root.title("Interfaz Alumno")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # Guardamos el nombre del alumno (usuario)
        self.usuario = usuario
        
        # Instanciamos las clases que necesitamos
        self.asistencia = c.asistencias()
        self.materias = c.materias()
        self.alumno = c.alumno()

        # Obtenemos el ID del usuario a partir de su nombre
        self.id_alumno = self.alumno.obtener_alumno_id_nombre(usuario)

        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")  # Tema oscuro
        ctk.set_default_color_theme("blue")  # Tema de color azul

        # Inicializamos la tab de asistencia
        self._construir_tab_asistencia()

    def regresar_button(self):
        self.frame_asistencia.destroy()
        self._construir_tab_asistencia()

    def _construir_tab_reg_asistencia(self, parent):
        # Creación del marco principal
        main_frame = ctk.CTkFrame(parent, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Etiqueta de bienvenida
        label_usuario = ctk.CTkLabel(main_frame, text=f"Bienvenido {self.usuario}", font=("Arial", 16))
        label_usuario.pack(pady=10)

        # Etiqueta y combobox para seleccionar materia
        materias_label = ctk.CTkLabel(main_frame, text="Seleccione la materia:")
        materias_label.pack(pady=5)
        self.materia = self.materias.obtener_materias_nombre()
        self.combobox_materias = ctk.CTkComboBox(main_frame, values=self.materia, width=200)
        self.combobox_materias.pack(pady=5)

        # Botón para marcar asistencia
        btn_asistir = ctk.CTkButton(main_frame, text="Marcar Asistencia", command=self.marcar_asistencia)
        btn_asistir.pack(pady=10)

        # Botón para regresar
        self.button_regresar = ctk.CTkButton(parent, text="Regresar", command=self.regresar_button)
        self.button_regresar.pack(pady=10)

    def _construir_tab_ver_asistencias(self, parent):
        main_frame_ver_asistencia = ctk.CTkFrame(parent, corner_radius=10)
        main_frame_ver_asistencia.pack(pady=20, padx=20, fill="both", expand=True)

        label_asistencias = ctk.CTkLabel(main_frame_ver_asistencia, text="Asistencias")
        label_asistencias.pack(pady=10)

        # Frame scrollable
        self.scrollableframe_asistencias = ctk.CTkScrollableFrame(main_frame_ver_asistencia, width=400, height=200)
        self.scrollableframe_asistencias.pack(pady=10)

        # Encabezados de columnas
        nombre_materias_label = ctk.CTkLabel(self.scrollableframe_asistencias, text="Materia")
        nombre_materias_label.grid(row=0, column=0, padx=20)

        asistencias_label = ctk.CTkLabel(self.scrollableframe_asistencias, text="Asistencia")
        asistencias_label.grid(row=0, column=1, padx=20)

        fechas_label = ctk.CTkLabel(self.scrollableframe_asistencias, text="Fecha")
        fechas_label.grid(row=0, column=2, padx=20)

        horas_label = ctk.CTkLabel(self.scrollableframe_asistencias, text="Hora")
        horas_label.grid(row=0, column=3, padx=20)

        # Obtenemos las asistencias del alumno
        registros = self.asistencia.obtener_asistencias_alumno_id(self.id_alumno)

        # Función para convertir el código de asistencia en texto
        def asistencia_a_texto(codigo):
            if codigo == 0:
                return "Falta"
            elif codigo == 1:
                return "Asistencia"
            elif codigo == 2:
                return "Retardo"
            return "Desconocido"

        # Insertamos los datos en el scrollableframe 
        for i, fila in enumerate(registros, start=1):
            # fila = (id_usuario, usuario_nombre, id_materia, materia_nombre, fecha, hora, asistencia)
            materia_id = fila[2]
            fecha = str(fila[3])
            hora = str(fila[4])
            codigo_asistencia = fila[5]
            asistencia_texto = asistencia_a_texto(codigo_asistencia)

            lbl_materia = ctk.CTkLabel(self.scrollableframe_asistencias, text=materia_id)
            lbl_materia.grid(row=i, column=0, padx=20)

            lbl_fecha = ctk.CTkLabel(self.scrollableframe_asistencias, text=fecha)
            lbl_fecha.grid(row=i, column=1, padx=20)

            lb_hora = ctk.CTkLabel(self.scrollableframe_asistencias, text=hora)
            lb_hora.grid(row=i, column=2, padx=20)

            label_asistencia = ctk.CTkLabel(self.scrollableframe_asistencias, text=asistencia_texto)
            label_asistencia.grid(row=i, column=3, padx=20)

        # Botón para regresar
        self.button_regresar = ctk.CTkButton(main_frame_ver_asistencia, text="Regresar", command=self.regresar_button)
        self.button_regresar.pack(pady=10)

    def marcar_asistencia(self):
        # Damos valores a la variables usando la información del usuario y del combobox
        nombre_alumno = self.usuario
        usuario_id = self.alumno.obtener_alumno_id_nombre(nombre_alumno)
        materia_seleccionada = self.combobox_materias.get()
        id_materia = self.materias.obtener_materias_id_nombre(materia_seleccionada)

        # Establecemos la fecha y hora del sistema   
        fecha = datetime.now().date()
        hora = datetime.now().time()

        # Marcamos la asistencia como 1
        asistencia = 1
        self.asistencia.registrar_asistencia(usuario_id, id_materia, fecha, hora, asistencia)
        messagebox.showinfo("Asistencia", "¡Asistencia marcada con éxito!")

    def _construir_tab_asistencia(self):
        self.frame_asistencia = ctk.CTkFrame(self.root)
        self.frame_asistencia.pack(fill='both', expand=True, padx=10, pady=10)

        def limpiar_frame_asistencia():
            for widget in self.frame_asistencia.winfo_children():
                widget.destroy()
        
        def construir_tab_reg_asistencia():
            limpiar_frame_asistencia()
            self._construir_tab_reg_asistencia(self.frame_asistencia)

        def construir_tab_ver_asistencia():
            limpiar_frame_asistencia()
            self._construir_tab_ver_asistencias(self.frame_asistencia)

        # Botones para seleccionar la ventana a abrir
        self.button_reg_asistencia = ctk.CTkButton( self.frame_asistencia,  text="Registrar Asistencia",  command=construir_tab_reg_asistencia)
        self.button_reg_asistencia.pack(pady=10)

        self.button_ver_asistencias = ctk.CTkButton( self.frame_asistencia,  text="Ver Asistencias",  command=construir_tab_ver_asistencia)
        self.button_ver_asistencias.pack(pady=10)
