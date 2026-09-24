# ==========================================
# 1. UNIVERSO DE DISCURSO Y BASE DE CONOCIMIENTO (HECHOS)
# ==========================================

# Dominios / Universos
estudiantes = ["sofia", "diego", "luis", "paula", "miguel", "elena", "carlos", "ana", "jorge", "maria"]
actividades = ["practicaLab3", "seminarioRobotica"]
grupos = ["grupoC", "grupoA"]
comites = ["comiteEtica", "comiteCurricular"]
cursos = ["Proyectos I", "programacionAvanzada"]
recursos = ["LaboratorioIA", "BibliotecaDigital"]

# Hechos (Base de conocimiento)
asiste_a_hechos = {
    "sofia": ["practicaLab3"]
}

es_tutor_de_hechos = {
    "diego": ["grupoC"]
}

tiene_creditos_hechos = {
    "luis": 78
}

es_miembro_de_hechos = {
    "paula": ["comiteEtica"]
}

solicita_extension_hechos = {
    "miguel": ["Proyectos I"]
}


# ==========================================
# 2. DEFINICIÓN DE PREDICADOS (REGLAS/FUNCIONES)
# ==========================================

def AsisteA(alumno, actividad):
    """E x Act -> 'el estudiante x asiste a la actividad a'"""
    return actividad in asiste_a_hechos.get(alumno, [])

def EsTutorDe(alumno, grupo):
    """E x G -> 'el estudiante x es tutor del grupo g'"""
    return grupo in es_tutor_de_hechos.get(alumno, [])

def TieneCreditos(alumno, cant):
    """E x N -> 'el estudiante x posee n créditos aprobados'"""
    return tiene_creditos_hechos.get(alumno) == cant

def EsMiembroDe(alumno, comite):
    """E x Cmt -> 'el estudiante x es miembro del comité c'"""
    return comite in es_miembro_de_hechos.get(alumno, [])

def SolicitaExtension(alumno, asignatura):
    """E x C -> 'el estudiante x solicita extensión para la asignatura c'"""
    return asignatura in solicita_extension_hechos.get(alumno, [])


# ==========================================
# 3. CONSULTAS (POSITIVAS Y NEGATIVAS)
# ==========================================

print("--- EVALUACIÓN DE CONSULTAS ---")

# Predicado 1: AsisteA
print("\n1. Predicado: AsisteA(alumno, actividad)")
print("Consulta Positiva: ¿Sofía asiste a practicaLab3?")
print("R:", AsisteA("sofia", "practicaLab3"))  # Esperado: True
print("Consulta Negativa: ¿Carlos asiste a practicaLab3?")
print("R:", AsisteA("carlos", "practicaLab3"))  # Esperado: False

# Predicado 2: EsTutorDe
print("\n2. Predicado: EsTutorDe(alumno, grupo)")
print("Consulta Positiva: ¿Diego es tutor del grupoC?")
print("R:", EsTutorDe("diego", "grupoC"))  # Esperado: True
print("Consulta Negativa: ¿Ana es tutora del grupoC?")
print("R:", EsTutorDe("ana", "grupoC"))  # Esperado: False

# Predicado 3: TieneCreditos
print("\n3. Predicado: TieneCreditos(alumno, cant)")
print("Consulta Positiva: ¿Luis tiene 78 créditos?")
print("R:", TieneCreditos("luis", 78))  # Esperado: True
print("Consulta Negativa: ¿Luis tiene 100 créditos?")
print("R:", TieneCreditos("luis", 100))  # Esperado: False

# Predicado 4: EsMiembroDe
print("\n4. Predicado: EsMiembroDe(alumno, comite)")
print("Consulta Positiva: ¿Paula es miembro del comiteEtica?")
print("R:", EsMiembroDe("paula", "comiteEtica"))  # Esperado: True
print("Consulta Negativa: ¿Jorge es miembro del comiteEtica?")
print("R:", EsMiembroDe("jorge", "comiteEtica"))  # Esperado: False

# Predicado 5: SolicitaExtension
print("\n5. Predicado: SolicitaExtension(alumno, asignatura)")
print("Consulta Positiva: ¿Miguel solicita extensión para Proyectos I?")
print("R:", SolicitaExtension("miguel", "Proyectos I"))  # Esperado: True
print("Consulta Negativa: ¿Elena solicita extensión para Proyectos I?")
print("R:", SolicitaExtension("elena", "Proyectos I"))  # Esperado: False