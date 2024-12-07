bueno(ayudar_madre).
malo(mentir).

hace(sebastian, ayudar_madre).
hace(sebastian, mentir).

es_bueno(Alguien) :- hace(Alguien, Algo), bueno(Algo).
es_malo(Alguien) :- hace(Alguien, Algo), malo(Algo).
