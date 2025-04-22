import customtkinter as ctk
from tkinter import messagebox
import clases as c
import interfaz_docente as docente
import interfaz_alumno as alumno
import interfaz_admin as admin

class InterfazLogin:
    def __init__(self, master):
        self.root = master
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        # Configuración de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Instanciamos nuestra clase usuarios 
        self.usuarios = c.usuarios()

        # Frame principal
        main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Campo para el usuario 
        self.usuario_label = ctk.CTkLabel(main_frame, text="Usuario:")
        self.usuario_label.pack(pady=5)
        self.entry_usuario = ctk.CTkEntry(main_frame, width=200)
        self.entry_usuario.pack()
        
        # Etiqueta y campo para la contraseña
        self.contraseña_label = ctk.CTkLabel(main_frame, text="contraseña:")
        self.contraseña_label.pack(pady=5)
        self.entry_contraseña = ctk.CTkEntry(main_frame, width=200, show="*")
        self.entry_contraseña.pack()
        
        # Botón de iniciar sesión
        btn_login = ctk.CTkButton(main_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        btn_login.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        
        # Validamos credenciales usando el método de la clase usuarios
        tipo_usuario = self.usuarios.validar_credenciales(usuario, contraseña)
        
        if tipo_usuario and tipo_usuario[0] == "docente":
            self.root.destroy()
            self.abrir_interfaz_docente(usuario)
        if tipo_usuario and tipo_usuario[0] == "alumno":
            self.root.destroy()
            self.abrir_interfaz_alumno(usuario)
        if tipo_usuario and tipo_usuario[0] == "administrador":
            self.root.destroy()
            self.abrir_interfaz_admin(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def abrir_interfaz_docente(self, usuario):
        root_docente = ctk.CTkToplevel()
        docente.interfaz_docente(root_docente, usuario)
        root_docente.mainloop()
    
    def abrir_interfaz_alumno(self, usuario):
        root_alumno = ctk.CTkToplevel()
        alumno.InterfazAlumno(root_alumno, usuario)
        root_alumno.mainloop()
    
    def abrir_interfaz_admin(self, usuario):
        root_admin = ctk.CTkToplevel()
        admin.InterfazAdmin(root_admin, usuario)
        root_admin.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    app = InterfazLogin(root)
    root.mainloop()
