Provincia = {'Bocas del Toro': ['Bocas del Toro', 'Changuinola', 'Chiriquí Grande'],
			 'Coclé':['Aguadulce','Antón','La Pintada','Natá','Olá','Penonomé'],
			 'Colón':['Colón','Chagres','Donoso','Portobelo','Santa Isabel'],
			 'Chiriquí':['Alanje','Barú','Boquerón','Boquete','Bugaba','David','Dolega','Gualaca','Remedios','San Felíx','San Lorenzo','Tolé'],
			 'Darién':['Chepigana','Pinogana'],
			 'Herrera':['Chitré','Las Minas','Los Pozos','Ocú','Parita','Pesé','Santa María','Los Santos','Guararé','Macaracas','Pedasí','Pocrí','Tonosí'],
			 'Panamá':['Balboa','Chepo','Chimán','Panamá','San Miguelito','Taboga','Panamá Oeste','Arraiján','Capira','La Chorrera','San Carlos',''],
			 'Veraguas':['Atalaya','Calobre','Cañazas','La Mesa','Las Palmas','Montijo','Río de Jesús','San Francisco','Santa Fe','Soná','Mariato',''],
			 'Kuna Yala':['Kuna Yala'],
			 'Emberá':['Cémaco','Sambú'],
			 'Ngäbe Buglé':['Besiko','Mironó','Müna','Nole Duima','Ñürüm','Kankintú','Kusapín']
			 }
			 
print("***************************************************")
NombreProvincia =input('Buscar Distritos en Provincia de: ')
print("***************************************************")
NomProv =Provincia.keys()
try:
	Valor = Provincia.get(NombreProvincia)
	for k in Valor:
		print("DISTRITO: " + k )	
except:
	print (" ERROR ERROR ERROR: verifique la ortografia de la provincia")
	NomProv =Provincia.keys()
	for i in NomProv:
		print("Provincia: " + i ) 

