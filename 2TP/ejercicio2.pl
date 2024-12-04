%=======Hechos=====
posee_skill(marcos, uml).
posee_skill(marco, java).
posee_skill(marco, empatia_con_los_clientes).

posee_skill(maria, arquitecturas).
posee_skill(maria, gestion_de_recursos_humanos).

posee_skill(hernan, javascript).
posee_skill(hernan, php).
posee_skill(hernan, python).
posee_skill(hernan, buena_comunicación).

prefiere_rol(marco,  programador).
prefiere_rol(maria, lider).
prefiere_rol(hernan, lider).

es_para(uml, programador).
% es_para(java, programador).
es_para(python, programador).
es_para(php, programador).
es_para(buena_comunicación, lider).
es_para(javascript, programador).
es_para(empatia_con_los_clientes, lider).
es_para(empatia_con_los_clientes, analista).
es_para(empatia_con_los_clientes, diseñador).
es_para(arquitecturas, analista).
es_para(gestion_de_recursos_humanos, lider).

se_puede_trasladar(marco, capital).
se_puede_trasladar(maria, capital).
se_puede_trasladar(maria, cordoba).
se_puede_trasladar(hernan, capital).
se_puede_trasladar(hernan, mendoza).

% =======Reglas=====
es_apto(Persona, Rol) :- 
	prefiere_rol(Persona, Rol),
	posee_skill(Persona, Habilidad),
	es_para(Habilidad, Rol).

empleado_disponible(Persona, Rol, Ubicacion) :-
	se_puede_trasladar(Persona, Ubicacion),
	es_apto(Persona, Rol).