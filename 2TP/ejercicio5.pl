% Hechos de las vacunas
edad_minima(sinopharm, 3).
edad_minima(pfizer, 12).
edad_minima(moderna, 0.5).

contraindicacion(sinopharm, hipersensibilidad).
contraindicacion(sinopharm, enfermedades_cronicas).
contraindicacion(sinopharm, trombocitopenia).
contraindicacion(sinopharm, trastornos_coagulacion).
contraindicacion(sinopharm, epilepsia).
contraindicacion(moderna, enfermedades_cronicas).
contraindicacion(moderna, anafilaxia).
contraindicacion(moderna, trombocitopenia).
contraindicacion(pfizer, enfermedades_agudas_graves).
contraindicacion(pfizer, enfermedades_cronicas).
contraindicacion(pfizer, anafilaxia).
contraindicacion(pfizer, trombocitopenia).

% Hechos sobre las personas
edad(matias, 63).
edad(jorge, 7).
edad(josefina, 21).

padece(matias, epilepsia).
padece(jorge, anafilaxia).

% Declaracion de las reglas
tiene_contraindicacion(Persona, Vacuna) :-
    padece(Persona, Enfermedad),
    contraindicacion(Vacuna, Enfermedad).

puede_vacunarse(Persona, Vacuna) :-
    edad_minima(Vacuna, EdadMinima),
    edad(Persona, Edad),
    Edad >= EdadMinima,
    not(tiene_contraindicacion(Persona, Vacuna)).