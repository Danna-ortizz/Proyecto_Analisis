# Importa librerías necesarias
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import clases as c

# Clase principal de la interfaz de administrador
class InterfazAdmin:
    def __init__(self, root, usuario):
        # Configura la ventana
        self.root = root
        self.root.title("Interfaz Administrador")
        self.root.geometry("700x650")
        self.root.resizable(False, False)

        # Configura el tema de la interfaz
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Crea instancias de las clases necesarias
        self.admin = c.admin()
        self.usuarios = c.usuarios()
        self.materias = c.materias()
        self.grupos = c.grupos()

        self.usuario = usuario  # Guarda el nombre del usuario

        # Construye el menú principal
        self._construir_menu_principal()

    # Construye el menú principal
    def _construir_menu_principal(self):
        self.frame_menu = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_menu.pack(fill='both', expand=True, padx=10, pady=10)

        label_bienvenida = ctk.CTkLabel(self.frame_menu, text=f"Bienvenido, administrador {self.usuario}")
        label_bienvenida.pack(pady=10)

        # Botones del menú
        btn_usuarios = ctk.CTkButton(self.frame_menu, text="Gestionar Usuarios", command=self._abrir_tab_usuarios)
        btn_usuarios.pack(pady=5)

        btn_grupos = ctk.CTkButton(self.frame_menu, text="Gestionar Grupos", command=self._abrir_tab_grupos)
        btn_grupos.pack(pady=5)

        btn_materias = ctk.CTkButton(self.frame_menu, text="Gestionar Materias", command=self._abrir_tab_materias)
        btn_materias.pack(pady=5)

    # Abre la sección de usuarios
    def _abrir_tab_usuarios(self):
        self.frame_menu.destroy()
        self._construir_tab_usuarios()

    # Abre la sección de grupos
    def _abrir_tab_grupos(self):
        self.frame_menu.destroy()
        self._construir_tab_grupos()

    # Abre la sección de materias
    def _abrir_tab_materias(self):
        self.frame_menu.destroy()
        self._construir_tab_materias()

    # Volver al menú principal desde cualquier sección
    def _volver_menu_principal(self, frame_actual):
        frame_actual.destroy()
        self._construir_menu_principal()

    def _volver_menu_principal_usuarios(self):
        self._volver_menu_principal(self.frame_usuarios)

    def _volver_menu_principal_grupos(self):
        self._volver_menu_principal(self.frame_grupos)

    def _volver_menu_principal_materias(self):
        self._volver_menu_principal(self.frame_materias)

    # ================== USUARIOS ==================
    def _construir_tab_usuarios(self):
        self.frame_usuarios = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_usuarios.pack(fill='both', expand=True, padx=10, pady=10)

        label_title = ctk.CTkLabel(self.frame_usuarios, text="GESTIÓN DE USUARIOS", font=("Arial", 18))
        label_title.pack(pady=10)

        # Área para mostrar todos los usuarios
        self.scrollableframe_usuarios = ctk.CTkScrollableFrame(self.frame_usuarios, width=600, height=200)
        self.scrollableframe_usuarios.pack(pady=10)

        # Encabezados de la tabla
        lbl_id = ctk.CTkLabel(self.scrollableframe_usuarios, text="ID")
        lbl_id.grid(row=0, column=0, padx=10)

        lbl_usuario = ctk.CTkLabel(self.scrollableframe_usuarios, text="Usuario")
        lbl_usuario.grid(row=0, column=1, padx=10)

        lbl_nombre = ctk.CTkLabel(self.scrollableframe_usuarios, text="Nombre")
        lbl_nombre.grid(row=0, column=2, padx=10)

        lbl_contraseña = ctk.CTkLabel(self.scrollableframe_usuarios, text="contraseña")
        lbl_contraseña.grid(row=0, column=3, padx=10)

        lbl_tipo = ctk.CTkLabel(self.scrollableframe_usuarios, text="Tipo")
        lbl_tipo.grid(row=0, column=4, padx=10)

        # Muestra todos los usuarios en la tabla
        todos_usuarios = self.usuarios.obtener_todos_usuarios()

        for fila, usuario in enumerate(todos_usuarios, start=1):
            ctk.CTkLabel(self.scrollableframe_usuarios, text=str(usuario[0])).grid(row=fila, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_usuarios, text=str(usuario[1])).grid(row=fila, column=1, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_usuarios, text=str(usuario[2])).grid(row=fila, column=2, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_usuarios, text=str(usuario[3])).grid(row=fila, column=3, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_usuarios, text=str(usuario[4])).grid(row=fila, column=4, padx=10, pady=5)

        # Formulario para crear, editar o eliminar un usuario
        form_frame = ctk.CTkFrame(self.frame_usuarios)
        form_frame.pack(pady=10)

        # Campos del formulario
        lbl_idusuario = ctk.CTkLabel(form_frame, text="ID (para editar/eliminar)")
        lbl_idusuario.grid(row=0, column=0, padx=5, pady=5)
        self.entry_idusuario = ctk.CTkEntry(form_frame, width=150)
        self.entry_idusuario.grid(row=0, column=1, padx=5, pady=5)

        lbl_usuario = ctk.CTkLabel(form_frame, text="Usuario:")
        lbl_usuario.grid(row=1, column=0, padx=5, pady=5)
        self.entry_usuario = ctk.CTkEntry(form_frame, width=150)
        self.entry_usuario.grid(row=1, column=1, padx=5, pady=5)

        lbl_contraseña = ctk.CTkLabel(form_frame, text="contraseña:")
        lbl_contraseña.grid(row=2, column=0, padx=5, pady=5)
        self.entry_contraseña = ctk.CTkEntry(form_frame, width=150)
        self.entry_contraseña.grid(row=2, column=1, padx=5, pady=5)

        lbl_nombre_ = ctk.CTkLabel(form_frame, text="Nombre:")
        lbl_nombre_.grid(row=3, column=0, padx=5, pady=5)
        self.entry_nombre = ctk.CTkEntry(form_frame, width=150)
        self.entry_nombre.grid(row=3, column=1, padx=5, pady=5)

        lbl_tipo_ = ctk.CTkLabel(form_frame, text="Tipo:")
        lbl_tipo_.grid(row=4, column=0, padx=5, pady=5)
        self.combobox_tipo = ctk.CTkComboBox(form_frame, width=150, values=["administrador", "docente", "alumno"])
        self.combobox_tipo.grid(row=4, column=1, padx=5, pady=5)

        # Botones de acción (crear, modificar, eliminar)
        btn_frame = ctk.CTkFrame(self.frame_usuarios)
        btn_frame.pack(pady=10)

        # Funciones para crear, modificar y eliminar usuarios
        def crear_usuario():
            usuario = self.entry_usuario.get()
            contraseña = self.entry_contraseña.get()
            nombre = self.entry_nombre.get()
            tipo = self.combobox_tipo.get()
            c.admin.crear_usuario(self, usuario, contraseña, nombre, tipo)
            messagebox.showinfo("Éxito", "Usuario creado satisfactoriamente.")
            self.frame_usuarios.destroy()
            self._construir_tab_usuarios()

        def modificar_usuario():
            id = self.entry_idusuario.get()
            usuario = self.entry_usuario.get()
            contraseña = self.entry_contraseña.get()
            nombre = self.entry_nombre.get()
            tipo = self.combobox_tipo.get()
            c.admin.modificar_usuario(self, id,usuario, contraseña, nombre, tipo)
            messagebox.showinfo("Éxito", "Usuario modificado satisfactoriamente.")
            self.frame_usuarios.destroy()
            self._construir_tab_usuarios()

        def eliminar_usuario():
            id = self.entry_idusuario.get()
            c.admin.eliminar_usuario(self,id)
            messagebox.showinfo("Éxito", "Usuario eliminado satisfactoriamente.")
            self.frame_usuarios.destroy()
            self._construir_tab_usuarios()

        # Botones
        btn_crear = ctk.CTkButton(btn_frame, text="Crear Usuario", command=crear_usuario)
        btn_crear.grid(row=0, column=0, padx=5, pady=5)

        btn_modificar = ctk.CTkButton(btn_frame, text="Modificar Usuario", command=modificar_usuario)
        btn_modificar.grid(row=0, column=1, padx=5, pady=5)

        btn_eliminar = ctk.CTkButton(btn_frame, text="Eliminar Usuario", command=eliminar_usuario)
        btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

        # Botón para volver al menú
        btn_volver = ctk.CTkButton(self.frame_usuarios, text="Volver al Menú", command=self._volver_menu_principal_usuarios)
        btn_volver.pack(pady=10)

    # ================== GRUPOS ==================
    def _construir_tab_grupos(self):
        self.frame_grupos = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_grupos.pack(fill='both', expand=True, padx=10, pady=10)

        label_title = ctk.CTkLabel(self.frame_grupos, text="GESTIÓN DE GRUPOS", font=("Arial", 18))
        label_title.pack(pady=10)

        # Muestra los grupos en un scroll
        self.scrollableframe_grupos = ctk.CTkScrollableFrame(self.frame_grupos, width=600, height=200)
        self.scrollableframe_grupos.pack(pady=10)

        # Encabezados de columna
        lbl_id = ctk.CTkLabel(self.scrollableframe_grupos, text="ID Grupo")
        lbl_id.grid(row=0, column=0, padx=10)
        lbl_nombre = ctk.CTkLabel(self.scrollableframe_grupos, text="Nombre de Grupo")
        lbl_nombre.grid(row=0, column=1, padx=10)
        lbl_iddocente = ctk.CTkLabel(self.scrollableframe_grupos, text="ID Docente")
        lbl_iddocente.grid(row=0, column=2, padx=10)
        lbl_periodo = ctk.CTkLabel(self.scrollableframe_grupos, text="Periodo Académico")
        lbl_periodo.grid(row=0, column=3, padx=10)


        # Obtiene todos los grupos
        grupos = self.grupos.obtener_grupo()

        # Muestra cada grupo en una fila
        for columna, grupo in enumerate(grupos, start=1):
            ctk.CTkLabel(self.scrollableframe_grupos, text=str(grupo[0])).grid(row=columna, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_grupos, text=str(grupo[1])).grid(row=columna, column=1, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_grupos, text=str(grupo[2])).grid(row=columna, column=2, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_grupos, text=str(grupo[3])).grid(row=columna, column=3, padx=10, pady=5)

        # Formulario para crear, modificar y eliminar grupo
        form_frame = ctk.CTkFrame(self.frame_grupos)
        form_frame.pack(pady=10)

        # Entradas del formulario
        lbl_id_grupo = ctk.CTkLabel(form_frame, text="ID Grupo")
        lbl_id_grupo.grid(row=0, column=0, padx=5, pady=5)
        self.entry_id_grupo = ctk.CTkEntry(form_frame, width=150)
        self.entry_id_grupo.grid(row=0, column=1, padx=5, pady=5)

        lbl_nombre_grupo = ctk.CTkLabel(form_frame, text="Nombre del Grupo:")
        lbl_nombre_grupo.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre_grupo = ctk.CTkEntry(form_frame, width=150)
        self.entry_nombre_grupo.grid(row=1, column=1, padx=5, pady=5)

        lbl_periodo = ctk.CTkLabel(form_frame, text="Periodo Académico:")
        lbl_periodo.grid(row=2, column=0, padx=5, pady=5)
        self.entry_periodo = ctk.CTkEntry(form_frame, width=150)
        self.entry_periodo.grid(row=2, column=1, padx=5, pady=5)

        lbl_id_docente = ctk.CTkLabel(form_frame, text="ID Docente:")
        lbl_id_docente.grid(row=3, column=0, padx=5, pady=5)
        self.entry_docente = ctk.CTkEntry(form_frame, width=150)
        self.entry_docente.grid(row=3, column=1, padx=5, pady=5)

        # Botones para acciones
        btn_frame = ctk.CTkFrame(self.frame_grupos)
        btn_frame.pack(pady=10)

        # Función para crear grupo
        def crear_grupo():
            id_grupo = self.entry_id_grupo.get()
            nombre = self.entry_nombre_grupo.get()
            periodo = self.entry_periodo.get()
            id_docente = self.entry_docente.get()
            c.admin.crear_grupo(self, id_grupo, nombre, periodo, id_docente)
            messagebox.showinfo("Éxito", "Grupo creado satisfactoriamente.")
            self.frame_grupos.destroy()
            self._construir_tab_grupos()

        # Función para modificar grupo
        def modificar_grupo():
            id_grupo = self.entry_id_grupo.get()
            nombre = self.entry_nombre_grupo.get()
            periodo = self.entry_periodo.get()
            id_docente = self.entry_docente.get()
            c.admin.modificar_grupo(self, id_grupo, nombre, periodo, id_docente)
            messagebox.showinfo("Éxito", "Grupo modificado satisfactoriamente.")
            self.frame_grupos.destroy()
            self._construir_tab_grupos()

        # Función para eliminar grupo
        def eliminar_grupo():
            id_grupo = self.entry_id_grupo.get()
            c.admin.eliminar_grupo(self, id_grupo)
            messagebox.showinfo("Éxito", "Grupo eliminado satisfactoriamente.")
            self.frame_grupos.destroy()
            self._construir_tab_grupos()

        # Botones para crear, modificar y eliminar
        btn_crear = ctk.CTkButton(btn_frame, text="Crear Grupo", command=crear_grupo)
        btn_crear.grid(row=0, column=0, padx=5, pady=5)

        btn_modificar = ctk.CTkButton(btn_frame, text="Modificar Grupo", command=modificar_grupo)
        btn_modificar.grid(row=0, column=1, padx=5, pady=5)

        btn_eliminar = ctk.CTkButton(btn_frame, text="Eliminar Grupo", command=eliminar_grupo)
        btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

        # Botón para volver al menú
        btn_volver = ctk.CTkButton(self.frame_grupos, text="Volver al Menú", command=self._volver_menu_principal_grupos)
        btn_volver.pack(pady=10)

    # ================== MATERIAS ==================
    def _construir_tab_materias(self):
        self.frame_materias = ctk.CTkFrame(self.root, corner_radius=10)
        self.frame_materias.pack(fill='both', expand=True, padx=10, pady=10)

        label_title = ctk.CTkLabel(self.frame_materias, text="GESTIÓN DE MATERIAS", font=("Arial", 18))
        label_title.pack(pady=10)

        # Muestra lista de materias en scroll
        self.scrollableframe_materias = ctk.CTkScrollableFrame(self.frame_materias, width=600, height=200)
        self.scrollableframe_materias.pack(pady=10)

        # Encabezados
        lbl_id_materia = ctk.CTkLabel(self.scrollableframe_materias, text="ID Materia")
        lbl_id_materia.grid(row=0, column=0, padx=10)
        lbl_nombre = ctk.CTkLabel(self.scrollableframe_materias, text="Nombre")
        lbl_nombre.grid(row=0, column=1, padx=10)
        lbl_id_docente = ctk.CTkLabel(self.scrollableframe_materias, text="ID docente")
        lbl_id_docente.grid(row=0, column=2, padx=10)
        lbl_id_grupo = ctk.CTkLabel(self.scrollableframe_materias, text="ID Grupo")
        lbl_id_grupo.grid(row=0, column=3, padx=10)

        # Muestra cada materia
        materias = self.materias.obtener_materias()
        for fila, materia in enumerate(materias, start=1):
            ctk.CTkLabel(self.scrollableframe_materias, text=str(materia[0])).grid(row=fila, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_materias, text=str(materia[1])).grid(row=fila, column=1, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_materias, text=str(materia[2])).grid(row=fila, column=2, padx=10, pady=5)
            ctk.CTkLabel(self.scrollableframe_materias, text=str(materia[3])).grid(row=fila, column=3, padx=10, pady=5)

        # Formulario para materias
        form_frame = ctk.CTkFrame(self.frame_materias)
        form_frame.pack(pady=10)

        # Entradas del formulario
        lbl_id_materia = ctk.CTkLabel(form_frame, text="ID Materia (para editar/eliminar)")
        lbl_id_materia.grid(row=0, column=0, padx=5, pady=5)
        self.entry_id_materia = ctk.CTkEntry(form_frame, width=150)
        self.entry_id_materia.grid(row=0, column=1, padx=5, pady=5)

        lbl_nombre = ctk.CTkLabel(form_frame, text="Nombre de Materia:")
        lbl_nombre.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre_materia = ctk.CTkEntry(form_frame, width=150)
        self.entry_nombre_materia.grid(row=1, column=1, padx=5, pady=5)

        lbl_id_grupo = ctk.CTkLabel(form_frame, text="ID Grupo:")
        lbl_id_grupo.grid(row=2, column=0, padx=5, pady=5)
        self.entry_id_grupo_materia = ctk.CTkEntry(form_frame, width=150)
        self.entry_id_grupo_materia.grid(row=2, column=1, padx=5, pady=5)

        lbl_id_docente = ctk.CTkLabel(form_frame, text="ID docente:")
        lbl_id_docente.grid(row=3, column=0, padx=5, pady=5)
        self.entry_id_docente_materia = ctk.CTkEntry(form_frame, width=150)
        self.entry_id_docente_materia.grid(row=3, column=1, padx=5, pady=5)

        # Botones para acciones
        btn_frame = ctk.CTkFrame(self.frame_materias)
        btn_frame.pack(pady=10)

        # Funciones para crear, modificar, eliminar materias
        def crear_materia():
            nombre = self.entry_nombre_materia.get()
            id_grupo = self.entry_id_grupo_materia.get()
            id_docente = self.entry_id_docente_materia.get()
            c.admin.crear_materia(self, nombre, id_grupo, id_docente)
            messagebox.showinfo("Éxito", "Materia creada satisfactoriamente.")
            self.frame_materias.destroy()
            self._construir_tab_materias()

        def modificar_materia():
            id_matera = self.entry_id_materia.get()
            nombre = self.entry_nombre_materia.get()
            id_grupo = self.entry_id_grupo_materia.get()
            id_docente = self.entry_id_docente_materia.get()
            c.admin.modificar_materia(self, id_matera, nombre, id_grupo, id_docente)
            messagebox.showinfo("Éxito", "Materia modificada satisfactoriamente.")
            self.frame_materias.destroy()
            self._construir_tab_materias()

        def eliminar_materia():
            id_materia = self.entry_id_materia.get()
            c.admin.eliminar_materia(self, id_materia)
            messagebox.showinfo("Éxito", "Materia eliminada satisfactoriamente.")
            self.frame_materias.destroy()
            self._construir_tab_materias()

        # Botones finales
        btn_crear = ctk.CTkButton(btn_frame, text="Crear Materia", command=crear_materia)
        btn_crear.grid(row=0, column=0, padx=5, pady=5)

        btn_modificar = ctk.CTkButton(btn_frame, text="Modificar Materia", command=modificar_materia)
        btn_modificar.grid(row=0, column=1, padx=5, pady=5)

        btn_eliminar = ctk.CTkButton(btn_frame, text="Eliminar Materia", command=eliminar_materia)
        btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

        # Botón para volver
        btn_volver = ctk.CTkButton(self.frame_materias, text="Volver al Menú", command=self._volver_menu_principal_materias)
        btn_volver.pack(pady=10)
