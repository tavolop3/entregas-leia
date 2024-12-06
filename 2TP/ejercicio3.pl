%          Leon
%            \
%           Franco       Magnolia   Fermin Cintia
%              \          /           /   /
%              \         /           /   /    
%                Walter         Melina
%                    \       /
%                     \     /
%               ---------------------
%               Felipe   Malena   Magali

es_hombre(felipe).
es_hombre(walter).
es_hombre(fermin).
es_hombre(franco).
es_hombre(leon).

es_mujer(malena).
es_mujer(magali).
es_mujer(magnolia).
es_mujer(melina).
es_mujer(cintia).

padre(leon, franco).
padre(fermin, melina).
padre(franco, walter).
padre(walter, felipe).
padre(walter, malena).
padre(walter, magali).

madre(cintia, melina).
madre(magnolia, walter).
madre(melina, malena).
madre(melina, magali).
madre(melina, felipe).

% Reglas para modelar las relaciones de genealogía
progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).

antepasado(X, Y) :- progenitor(X, Y).
antepasado(X, Y) :- progenitor(X, Z), antepasado(Z, Y).

hermano(X, Y) :- X \= Y, es_hombre(X), progenitor(Z, X), progenitor(Z, Y).
hermana(X, Y) :- X \= Y, es_mujer(X), progenitor(Z, X), progenitor(Z, Y).

abuelo(X, Y) :- padre(X, Z), progenitor(Z, Y).
abuela(X, Y) :- madre(X, Z), progenitor(Z, Y).
%abuelo(X, Y) :- es_hombre(X), progenitor(X, Z), progenitor(Z, Y).
%abuela(X, Y) :- es_mujer(X), progenitor(X, Z), progenitor(Z, Y).