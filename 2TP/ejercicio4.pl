es_bueno(Alguien) :- hace(Alguien, Algo), bueno(Algo).
es_malo(Alguien) :- hace(Alguien, Algo), malo(Algo).

hace(sebastian, ayudar_madre).
hace(sebastian, mentir).

bueno(ayudar_madre).
malo(mentir).
