CREATE DATABASE Control_Asistencia;
USE Control_Asistencia;

-- CREAMOS LOS USUARIOS
CREATE TABLE Usuarios ( 
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('alumno','administrador','docente') NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- CREAMOS LOS GRUPOS
CREATE TABLE Grupos (
    id_grupo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_docente INT NOT NULL,
    periodo_academico VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_docente) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);

-- ALUMNOS EN GRUPOS (RELACIÓN DIRECTA)
CREATE TABLE Grupo_Alumnos (
    id_grupo INT NOT NULL,
    id_alumno INT NOT NULL,
    PRIMARY KEY (id_grupo, id_alumno),
    FOREIGN KEY (id_grupo) REFERENCES Grupos(id_grupo) ON DELETE CASCADE,
    FOREIGN KEY (id_alumno) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);

-- CREAMOS LAS MATERIAS
CREATE TABLE Materias (
    id_materia INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_docente INT NOT NULL,
    id_grupo INT NOT NULL, 
    FOREIGN KEY (id_docente) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_grupo) REFERENCES Grupos(id_grupo) ON DELETE CASCADE
);

-- CREAMOS LAS ASISTENCIAS
CREATE TABLE Asistencias (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_materia INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    asistencia TINYINT NOT NULL CHECK (asistencia IN (0,1,2)),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES Materias(id_materia) ON DELETE CASCADE
);

-- CREAMOS LOS REPORTES
CREATE TABLE Reportes (
    id_reporte INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,  
    id_asistencia INT NOT NULL,
    texto_reporte VARCHAR(1000) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_asistencia) REFERENCES Asistencias(id_asistencia) ON DELETE CASCADE
);
