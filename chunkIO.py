def koorinantit (tupla):
  HashinX = tupla[0]
  HashinY = tupla[1]
  eka = tupla[0]
  toka = tupla[1]
  eka += 2
  toka = -toka
  toka += 26
def GeditistaHashiin(tupla):
  eka = tupla[0]
  toka = tupla[1]
  eka -= 2
  toka -= 26
  toka = -toka
  return ((eka, toka)) 
class solu:
    	def __init__(self, (a, b) , c, d) :
		self.koordi = (a, b)
		self.arvo = c
		self.__onkoLaskettu = False
		self.merkki = d
	def onkoLaskettu(self) :
	  return self.__onkoLaskettu					
	def merkitseLasketuksi(self) :
		self.__onkoLaskettu = True
	def kerro_merkki(self):
		return self.merkki
	def kerro_arvo(self) :
		return self.arvo
	def kerro_koordi(self) :
		return self.koordi
	def laita_arvo(self, a) :
		self.arvo = a
	def merkitseEiLasketuksi(self) :
		self.onkoLaskettu = 0
def insertoiSolu(solu, nykyinenVektori, tulevaVektori): 
  a = len(tulevaVektori) 
  koordit = solu.kerro_koordi()
  onkoLoydettySamaa = 0 
  for i in range(a):
    if koordit == tulevaVektori[i].kerro_koordi():
	onkoLoydettySamaa = 1
  if onkoLoydettySamaa == 0 :  
  	tulevaVektori.insert((a - 1) , solu) 
	koorinantit(solu.kerro_koordi())
  return
def palautaSeuraavaSolu(nykyinenVektori, tulevaVektori):
  a = len(nykyinenVektori)
  if a == 0:
	nykyinenVektori = tulevaVektori
	tulevaVektori = []
  a = len(nykyinenVektori)
  if len(nykyinenVektori) == 0:
    return None	
  palautus = nykyinenVektori.pop()
  return palautus

class ChunkIO(object,):
    def lataa_peli(self, input , laskeVaikuttavatInputit, kaytetaankoParametreja, AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH, III, JJJ, KKK, LLL, MMM, NNN, OOO, PPP, QQQ, RRR, SSS, TTT, UUU, VVV, WWW, XXX, YYY, ZZZ):
	    TuleekoStringinNimi = 0
	    StringiVektori = []
	    StringiVektorinArvot = []
	    AlkaakouUsiStringi = 0
    	    outputteja2 = 1
    	    pientenKirjaintenEsiintyvyys = []
    	    for i in range(28):
    	      pientenKirjaintenEsiintyvyys.insert(i , 0)
	    ekaLohko = self.read_fully(3, input)
            if ekaLohko[2] == "0":
                A = 0
            else :
                A = 1
            ekaLohko = self.read_fully(1, input) 
            ekaLohko = self.read_fully(1, input) 

            if ekaLohko[0] == '\n':
            	inputteja2 = 0
            
            else:
            	inputteja2 = 1

            if inputteja2 == 1:
            	ekaLohko = self.read_fully(2, input) 	
            	if ekaLohko[1] == "0":
               	 	B = 0
		if ekaLohko[1] == "1":
		   B = 1  
	    ekaLohko = self.read_fully(2, input) 
            ekaLohko = self.read_fully(2, input) 	
	    if ekaLohko[1] == "0":
 	      C = 0
 	    if ekaLohko[1] == "1":
	      C = 1
	    ekaLohko = self.read_fully(2, input) 
            ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      D = 0
	    if ekaLohko[1] == "1":
 	      D = 1
	    ekaLohko = self.read_fully(2, input) 	
	    ekaLohko = self.read_fully(2, input) 
            if ekaLohko[1] == "0":
       	      E = 0
	    if ekaLohko[1] == "1":
	      E = 1
	    ekaLohko = self.read_fully(2, input)
	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      F = 0
	    if ekaLohko[1] == "1":
	      F = 1
	    ekaLohko = self.read_fully(2, input)
	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      G = 0
	    if ekaLohko[1] == "1":
	      G = 1
	    ekaLohko = self.read_fully(2, input)
	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      H = 0 
	    if ekaLohko[1] == "1":
	      H = 1
	    ekaLohko = self.read_fully(2, input)
	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      I = 0
	    if ekaLohko[1] == "1":
	      I = 1
	    ekaLohko = self.read_fully(2, input)
	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      J = 0
	    if ekaLohko[1] == "1":
	      J = 1
	    ekaLohko = self.read_fully(2, input)
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      K = 0
	    if ekaLohko[1] == "1":
	      K = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      L = 0
	    if ekaLohko[1] == "1":
	      L = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      M = 0
	    if ekaLohko[1] == "1":
	      M = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      N = 0
	    if ekaLohko[1] == "1":
	      N = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      O = 0
	    if ekaLohko[1] == "1":
	      O = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      P = 0
	    if ekaLohko[1] == "1":
	      P = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      Q = 0
	    if ekaLohko[1] == "1":
	      Q = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      R = 0
	    if ekaLohko[1] == "1":
	      R = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      S = 0
	    if ekaLohko[1] == "1":
	      S = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      T = 0
	    if ekaLohko[1] == "1":
	      T = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      U = 0
	    if ekaLohko[1] == "1":
	      U = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      V = 0
	    if ekaLohko[1] == "1":
	      V = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      W = 0
	    if ekaLohko[1] == "1":
	      W = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      X = 0
	    if ekaLohko[1] == "1":
	      X = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      Y = 0
	    if ekaLohko[1] == "1":
	      Y = 1
    	    ekaLohko = self.read_fully(2, input) 	
    	    ekaLohko = self.read_fully(2, input) 	
            if ekaLohko[1] == "0":
       	      Z = 0 
	    if ekaLohko[1] == "1":
	      Z = 1
	    kaavio = {}
	    x = 1
	    y = 0
            while 1:
		ekaLohko = self.read_fully(1, input)
		if ekaLohko[0] == "." : #Otapois 3.4 muutetaan lopettava . :ksi
			break
		if ekaLohko[0] == " " : # TYHJAN JALKEEN VOI OLLA JOTAIN 
			lisays = solu((x, y) , 0, ekaLohko[0]) 
			lisays.merkitseLasketuksi() 
			kaavio[(x, y)] = lisays	
			x += 1
			continue
		if ekaLohko[0] == ">" : # TYHJAN JALKEEN VOI OLLA JOTAIN 
		  lisays = solu((x, y) , 0, ekaLohko[0]) 
    		  kaavio[(x, y)] = lisays
	          x += 1
	          continue		
	        if ekaLohko[0] == "#" : # TYHJAN JALKEEN VOI OLLA JOTAIN 
		  lisays = solu((x, y) , 0, ekaLohko[0]) 
    		  kaavio[(x, y)] = lisays
	          x += 1
	          continue	
		if ekaLohko[0] == "\\" :
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			koorinantit((x, y))
			x += 1
			continue
		if ekaLohko[0] == "/" :
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			koorinantit((x, y))
			TempSolu = kaavio[ (x, y)]
			x += 1
			continue
		if ekaLohko[0] == "\n" :
			x = 0
			y -= 1
			continue
		if ekaLohko[0] == "!" :
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			x += 1
			continue
		if ekaLohko[0] == "-" :
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			koorinantit((x, y))
                        Valiaikainen504 = (x, y) 
                        GeditistaHashiin (Valiaikainen504)  
			x += 1
			continue
		if ekaLohko[0] == "|":
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			x += 1
			continue
		if ekaLohko[0] == "&":
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays
			x += 1
			continue
		if ekaLohko[0].isupper() == True:  #Muut terkit myos TODO
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays	#(x,y)]# OLI NAIN kaavio[(x,y)] =  [lisays]	
			x += 1
			continue

		if ekaLohko[0] == "(" :  #Muut terkit myos TODO
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays	#(x,y)]# OLI NAIN kaavio[(x,y)] =  [lisays]
			x += 1
			continue


		if ekaLohko[0] == ")" :  #Muut terkit myos TODO
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays	#(x,y)]# OLI NAIN kaavio[(x,y)] =  [lisays]	)]
			x += 1
			continue
		if ekaLohko[0].islower() == True:  #Muut terkit myos TODO
			lisays = solu((x, y) , 0, ekaLohko[0])  
			kaavio[(x, y)] = lisays	#(x,y)]# OLI NAIN kaavio[(x,y)] =  [lisays]	
			pientenKirjaintenEsiintyvyys[(ord(lisays.kerro_merkki()) - 97)] = 1
			x += 1
			continue

		x += 1
	    if kaytetaankoParametreja == 1:
	     A = AAA
	     B = BBB
	     C = CCC
	     D = DDD
	     E = EEE
	     F = FFF
	     G = GGG
 	     H = HHH
	     I = III
	     J = JJJ
	     K = KKK
	     L = LLL
 	     M = MMM
	     N = NNN
	     O = OOO
	     P = PPP
	     Q = QQQ
	     R = RRR
	     S = SSS
	     T = TTT
	     U = UUU
	     V = VVV
	     W = WWW
	     X = XXX
	     Y = YYY
	     Z = ZZZ
	    for i in range(1000):
	      tempsolu504 = solu ((i, 0) , 0 , " ") # Voi aiheuttaa ongelmia
	      kaavio[ (i , 0)] = tempsolu504  
	    InputB = solu ((0, -1) , A , "A")   # Ei valttamatta toimi/ voi aiheuttaa ongelmia
	    InputB.merkitseLasketuksi() # merkitaan nama alueet aina lasketuksi
	    kaavio[ ((0 , -1)) ] = InputB 
	    InputB = solu ((0, -2) , B , "B")  
	    InputB.merkitseLasketuksi() # merkitaan nama alueet aina lasketuksi
	    kaavio[ ((0, -2)) ] = InputB 
	    InputB = solu ((0, -3) , C , "C")  
	    InputB.merkitseLasketuksi()  # nama uusia 21
	    kaavio[ ((0, -3)) ] = InputB 
    	    InputB = solu ((0, -4) , D , "D")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -4)) ] = InputB 
	    InputB = solu ((0, -5) , E , "E") 
	    InputB.merkitseLasketuksi()  
	    kaavio[ ((0, -5)) ] = InputB 
	    InputB = solu ((0, -6) , F , "F")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -6)) ] = InputB 
	    InputB = solu ((0, -7) , G , "G") 
	    InputB.merkitseLasketuksi()  
	    kaavio[ ((0, -7)) ] = InputB
	    InputB = solu ((0, -8) , H , "H")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -8)) ] = InputB 
	    InputB = solu ((0, -9) , I , "I")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -9)) ] = InputB 
	    InputB = solu ((0, -10) , J , "J")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -10)) ] = InputB 
	    InputB = solu ((0, -11) , K , "K")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -11)) ] = InputB
	    InputB = solu ((0, -12) , L , "L")
	    InputB.merkitseLasketuksi()   
	    kaavio[ ((0, -12)) ] = InputB 
	    InputB = solu ((0, -13) , M , "M")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -13)) ] = InputB
	    InputB = solu ((0, -14) , N , "N")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -14)) ] = InputB    
	    InputB = solu ((0, -15) , O , "O")  
	    InputB.merkitseLasketuksi() 
            kaavio[ ((0, -15)) ] = InputB 
	    InputB = solu ((0, -16) , P , "P")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -16)) ] = InputB 
	    InputB = solu ((0, -17) , Q , "Q")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -17)) ] = InputB 
	    InputB = solu ((0, -18) , R , "R")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -18)) ] = InputB 
	    InputB = solu ((0, -19) , S , "S")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -19)) ] = InputB 
	    InputB = solu ((0, -20) , T , "T")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -20)) ] = InputB 
	    InputB = solu ((0, -21) , U , "U")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -21)) ] = InputB 
	    InputB = solu ((0, -22) , V , "V")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -22)) ] = InputB 
	    InputB = solu ((0, -23) , W , "W")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -23)) ] = InputB
	    InputB = solu ((0, -24) , X , "X")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -24)) ] = InputB 
	    InputB = solu ((0, -25) , Y , "Y")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -25)) ] = InputB
	    InputB = solu ((0, -26) , Z , "Z")  
	    InputB.merkitseLasketuksi() 
	    kaavio[ ((0, -26)) ] = InputB 
	    OvatkoInputitKaytossa = []
	    nykyinenVektori = []
	    tulevaVektori = []
	    tempAolio504 = kaavio.get((1, -1))
	    tempAolio504.laita_arvo(A)
	    if tempAolio504.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (0, 1)
	    else:
	       OvatkoInputitKaytossa.insert (0, 0)
     	    tempOlio = kaavio.get((1, -1)) 
	    nykyinenVektori.insert(0, tempOlio)
	    tempOlio = kaavio.get((1, -2))
	    if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (1, 1)
	    else:
	      OvatkoInputitKaytossa.insert (1 , 0)
	    nykyinenVektori.insert(1 , tempOlio)	
	    tempOlio = kaavio.get((1, -3))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (2, 1)
	    else:
	      OvatkoInputitKaytossa.insert (2, 0)
	    nykyinenVektori.insert(2 , tempOlio)	
	    tempOlio = kaavio.get((1, -4))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (3, 1)
	    else:
	      OvatkoInputitKaytossa.insert (3, 0)
	    nykyinenVektori.insert(3 , tempOlio)	
	    tempOlio = kaavio.get((1, -5))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (4, 1)
	    else:
	      OvatkoInputitKaytossa.insert (4, 0)
	    nykyinenVektori.insert(4 , tempOlio)	
	    tempOlio = kaavio.get((1, -6))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (5, 1)
	    else:
	      OvatkoInputitKaytossa.insert (5, 0)
	    nykyinenVektori.insert(5 , tempOlio)	
	    tempOlio = kaavio.get((1, -7))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (6, 1)
	    else:
	      OvatkoInputitKaytossa.insert (6, 0)
	    nykyinenVektori.insert(6 , tempOlio)
	    tempOlio = kaavio.get((1, -8))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (7, 1)
	    else:
	      OvatkoInputitKaytossa.insert (7, 0)

	    nykyinenVektori.insert(7 , tempOlio)	
	    tempOlio = kaavio.get((1, -9))
	    if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (8, 1)
	    else:
	      OvatkoInputitKaytossa.insert (8, 0)
	    nykyinenVektori.insert(10 , tempOlio)	
	    nykyinenVektori.insert(8 , tempOlio)
	    tempOlio = kaavio.get((1, -10))
	    if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (9, 1)
	    else:
	      OvatkoInputitKaytossa.insert (9, 0)
	    nykyinenVektori.insert(10 , tempOlio)	
	    nykyinenVektori.insert(9 , tempOlio)		

	    tempOlio = kaavio.get((1, -11))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (10, 1)
	    else:
	      OvatkoInputitKaytossa.insert (10, 0)
	    nykyinenVektori.insert(10 , tempOlio)	
	    tempOlio = kaavio.get((1, -12))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (11, 1)
	    else:
	      OvatkoInputitKaytossa.insert (11, 0)
	    nykyinenVektori.insert(11 , tempOlio)
	    tempOlio = kaavio.get((1, -13))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (12, 1)
	    else:
	      OvatkoInputitKaytossa.insert (12, 0)
	    nykyinenVektori.insert(12 , tempOlio)
	    tempOlio = kaavio.get((1, -14))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (13, 1)
	    else:
	      OvatkoInputitKaytossa.insert (13, 0)
	    nykyinenVektori.insert(13 , tempOlio)
	    tempOlio = kaavio.get((1, -15))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (14, 1)
	    else:
	      OvatkoInputitKaytossa.insert (14, 0)
	    nykyinenVektori.insert(14 , tempOlio)
	    tempOlio = kaavio.get((1, -16))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (15, 1)
	    else:
	      OvatkoInputitKaytossa.insert (15, 0)
	    nykyinenVektori.insert(15 , tempOlio)
	    tempOlio = kaavio.get((1, -17))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (16, 1)
	    else:
	      OvatkoInputitKaytossa.insert (16, 0)
	    nykyinenVektori.insert(16 , tempOlio)	
	    tempOlio = kaavio.get((1, -18))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (17, 1)
	    else:
	      OvatkoInputitKaytossa.insert (17, 0)
	    nykyinenVektori.insert(17 , tempOlio)
	    tempOlio = kaavio.get((1, -19))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (18, 1)
	    else:
	      OvatkoInputitKaytossa.insert(18, 0)
	    nykyinenVektori.insert(18 , tempOlio)
	    tempOlio = kaavio.get((1, -20))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (19, 1)
	    else:
	      OvatkoInputitKaytossa.insert (19, 0)	
	    nykyinenVektori.insert(19 , tempOlio)
	    tempOlio = kaavio.get((1, -21))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (20, 1)
	    else:
	      OvatkoInputitKaytossa.insert (20, 0)
	    nykyinenVektori.insert(20 , tempOlio)		
	    tempOlio = kaavio.get((1, -22))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (21, 1)
	    else:
	      OvatkoInputitKaytossa.insert (21, 0)
	    nykyinenVektori.insert(21 , tempOlio)		 
	    tempOlio = kaavio.get((1, -23))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (22, 1)
	    else:
	      OvatkoInputitKaytossa.insert (22, 0)
	    nykyinenVektori.insert(22 , tempOlio)	
	    tempOlio = kaavio.get((1, -24))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (23, 1)
	    else:
	      OvatkoInputitKaytossa.insert (23, 0)
	    nykyinenVektori.insert(23 , tempOlio)	
	    tempOlio = kaavio.get((1, -25))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (24, 1)
	    else:
	      OvatkoInputitKaytossa.insert (24, 0)
	    nykyinenVektori.insert(24 , tempOlio)
	    tempOlio = kaavio.get((1, -26))
            if tempOlio.kerro_merkki() != " " :
	      OvatkoInputitKaytossa.insert (25, 1)
	    else:
	      OvatkoInputitKaytossa.insert (25, 0)
	    nykyinenVektori.insert(25 , tempOlio)
            if laskeVaikuttavatInputit == 1:
	      return OvatkoInputitKaytossa
	    olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	    outputit = []
	    for  a in range(27) :
	      outputit.insert(a, 0)
	    onkoOutputtiKaytossa = []
	    for a in range(27) :
	      onkoOutputtiKaytossa.insert(a, 0)
	    TuleekoStringinNimi = 0 
	    while 1:   

	      if olio == None :
	        break
	      if  olio.kerro_merkki() == "(" :
	        TuleekoStringinNimi = 1 
	        kaksi = olio.kerro_koordi()
		eka = kaksi[0]
		toka = kaksi[1]
		koorinantit (((eka - 1) , toka)) 
		EDELLINENARVO = kaavio[ ((eka - 1) , toka) ].kerro_arvo()
		LAITETTAVAarvo = EDELLINENARVO
		olio.laita_arvo(LAITETTAVAarvo)
		PITUUS = len(StringiVektorinArvot)
		StringiVektorinArvot.insert(0, LAITETTAVAarvo)
		eka += 1
		kaksi = (eka , toka)
		olio = kaavio  [kaksi]
		olio.merkitseLasketuksi()
		insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		AlkaakouUsiStringi = 1
	        continue
	      if  olio.kerro_merkki() == ")" :
	        TuleekoStringinNimi = 0 
	        kaksi = olio.kerro_koordi()
		eka = kaksi[0]
		toka = kaksi[1]
		koorinantit(((eka - 1) , toka)) 
		EDELLINENARVO = kaavio[ ((eka - 1) , toka) ].kerro_arvo()
		LAITETTAVAarvo = EDELLINENARVO
		olio.laita_arvo(LAITETTAVAarvo)
		eka += 1
		kaksi = (eka , toka)
		koorinantit(kaksi)
		olio = kaavio  [kaksi]
		olio.merkitseLasketuksi()
		insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		AlkaakouUsiStringi = 0
	        continue

	      if TuleekoStringinNimi == 1 and olio.kerro_merkki().isupper() == True:
		kaksi = olio.kerro_koordi()
		eka = kaksi[0]
		toka = kaksi[1]
		if AlkaakouUsiStringi == 1 :
		  pituus = len(StringiVektori)
		  StringiVektori.insert(pituus, olio.kerro_merkki())
		  AlkaakouUsiStringi = 0
		else :
		  pituus = len(StringiVektori)
		  StringiVektori[ (pituus - 1) ] += (olio.kerro_merkki())
	        kaksi = olio.kerro_koordi()
		koorinantit (((eka - 1) , toka))
		EDELLINENARVO = kaavio[ ((eka - 1) , toka) ].kerro_arvo()
		LAITETTAVAarvo = EDELLINENARVO
		olio.laita_arvo(LAITETTAVAarvo)
		eka += 1
		kaksi = (eka , toka)
		olio = kaavio  [kaksi]
		koorinantit (((eka - 1) , toka))
		insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	        continue
	      if olio.kerro_merkki() == "|" :

	         tupla303 = olio.kerro_koordi()
	         vasenolio303 = kaavio[  ((tupla303[0] - 1) , tupla303[1]) ]
		 kaksi = olio.kerro_koordi()
		 koorinantit(kaksi)###print olio.kerro_koordi()
		 viivanVasenolionkoordit401 = kaksi
		 viivanVasenolionkoordit401X = viivanVasenolionkoordit401[0]
		 viivanVasenolionkoordit401X -= 1
		 viivanVasenolionkoordit401 = (viivanVasenolionkoordit401X , viivanVasenolionkoordit401[1])
		 viivanVasenolio401 = kaavio[viivanVasenolionkoordit401]
		 eka = kaksi[0]
		 toka = kaksi[1]
		 varaeka263 = eka
		 varatoka263 = toka
		 edellisenX = eka
		 edellisenX -= 1
		 VasemmanX = eka
		 VasemmanY = toka
		 VasemmanX -= 1  
		 VasenOliotuple20paiva = (VasemmanX , VasemmanY)
		 VasenOlio20Paiva = kaavio[ VasenOliotuple20paiva ] 
		 ylaX = kaksi[0]
		 ylaY = kaksi[1]
		 ylaY += 1
		 ylaTuple = (ylaX , ylaY)
		 ylaOlio20paiva = kaavio[ylaTuple]
 		 alaX = kaksi[0]
		 alaY = kaksi[1]
		 alaY -= 1
		 alaTuple = (alaX , alaY)
		 alaOlio20paiva = kaavio[alaTuple]
		 if VasenOlio20Paiva.onkoLaskettu() == False or ylaOlio20paiva.onkoLaskettu() == False or alaOlio20paiva.onkoLaskettu() == False :
		   olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		   continue
		 temp = (edellisenX, toka) 
	 	 edellisenKohdanArvo = kaavio.get(temp)
		 temppp = edellisenKohdanArvo.kerro_arvo()
		 olio.laita_arvo(temppp)
		 nykyinenArvo = temppp
	 	 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 toka += 1
		 temp = kaavio[ (eka, toka) ] 
		 ylaArvo = temp.kerro_arvo()
		 tempvaratoka263 = varatoka263
		 tempvaraeka263 = varaeka263		 
		 tempvaratoka263 -= 1
		 temp = kaavio [(tempvaraeka263, tempvaratoka263) ]		 
		 alaArvo = temp.kerro_arvo()
	         if nykyinenArvo == 0 :
		 	if ylaArvo == 1 or alaArvo == 1 :
				nykyinenArvo = 1
				olio.laita_arvo(1)
				KOORDI = olio.kerro_koordi()
				kaavio[(KOORDI[0], KOORDI[1])] = olio
		 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 eka += 1
		 kaksi = (eka , toka)
		 olio = kaavio [kaksi]
		 Merkattavaolio263 = kaavio [  (varaeka263, varatoka263) ]
		 Merkattavaolio263.merkitseLasketuksi()
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue
	      if  olio.kerro_merkki() == "!" :	 
 		 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 EDELLINENARVO = kaavio[ ((eka - 1) , toka) ].kerro_arvo()
		 if EDELLINENARVO == 0:
			LAITETTAVAarvo = 1
		 else:
		   LAITETTAVAarvo = 0
		 olio.laita_arvo(LAITETTAVAarvo)
		 olio.merkitseLasketuksi() 
		 eka += 1
		 kaksi = (eka , toka)
		 olio = kaavio  [kaksi]
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue

 	      if olio.kerro_merkki() == " " :
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue	 
	      if  olio.kerro_merkki() == "&" :
	      	 vasenkoordit303 = olio.kerro_koordi()
	      	 vasenOlio303 = kaavio [  ((vasenkoordit303[0] - 1) , vasenkoordit303[1]) ] 
		 kaksi = olio.kerro_koordi()
		 koorinantit(olio.kerro_koordi())
		 eka = kaksi[0]
		 toka = kaksi[1]
		 toka31 = toka
		 toka31 -= 1
		 koorinantit((eka, toka31))
		 olio313jaMerkki = kaavio[ ((eka, toka31)) ]
		 varaeka293 = eka 
		 varatoka293 = toka
		 varaeka263 = eka
		 varatoka263 = toka
		 varaVasenX263 = eka
		 varaVasenY263 = toka
		 varaVasenX263 -= 1
		 edellisenX = eka
		 edellisenX -= 1
		 VasemmanX = eka
		 VasemmanY = toka
		 VasemmanX -= 1  
		 VasenOliotuple20paiva = (VasemmanX , VasemmanY)
		 VasenOlio20Paiva = kaavio[ VasenOliotuple20paiva ] 
		 ylaX = kaksi[0]
		 ylaY = kaksi[1]
		 ylaY += 1
		 ylaTuple = (ylaX , ylaY)
		 ylaOlio20paiva = kaavio[ylaTuple]
 		 alaX = kaksi[0]
		 alaY = kaksi[1]
		 alaY -= 1
		 alaTuple = (alaX , alaY)
		 alaOlio20paiva = kaavio[alaTuple]
		 if VasenOlio20Paiva.onkoLaskettu() == False or ylaOlio20paiva.onkoLaskettu() == False or alaOlio20paiva.onkoLaskettu() == False :
		   olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		   continue
		 temp = (edellisenX, toka) 
	 	 edellisenKohdanArvo = kaavio.get(temp)
		 temppp = edellisenKohdanArvo.kerro_arvo()
		 olio.laita_arvo(temppp)
		 nykyinenArvo = temppp
	 	 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 toka += 1
		 temp = kaavio[ (eka, toka) ] 
		 ylaArvo = temp.kerro_arvo()
		 tempvaratoka263 = varatoka263
		 tempvaraeka263 = varaeka263		 
		 tempvaratoka263 -= 1
		 temp = kaavio [(tempvaraeka263, tempvaratoka263) ]		 
		 alaArvo = temp.kerro_arvo()
		 VasenSoluTuple263 = (varaVasenX263 , varaVasenY263)
		 VasenSoluVara263 = kaavio[VasenSoluTuple263]
		 nykyinenArvo = VasenSoluVara263.kerro_arvo()
		 varaeka293
		 vasenOlio293 = kaavio[ ((varaeka293 - 1) , varatoka293)]
		 nykyinenArvo = vasenOlio293.kerro_arvo()
		 Alateemitaan = 0
	         if nykyinenArvo != 1 or alaArvo != 1 or ylaArvo != 1 : # EROA "-":n 26.3
				varaeka303AlaviivaX = varaeka293 
				varatoka303AlaviivaY = (varatoka293 - 1)
		 		alaOlio293 = kaavio[ (varaeka303AlaviivaX, varatoka303AlaviivaY)]
				koorinantit(alaOlio293.kerro_koordi())				
		 		if alaOlio293.kerro_merkki() == " ":
					koorinantit(alaOlio293.kerro_koordi())
		 			if nykyinenArvo == 1 and ylaArvo == 1:
		 			  #print "vasemmalla ja ylhaalla arvot ovat 1 --> solun arvo 1" 
		 			  olio.laita_arvo(1)
		 			  KOORDI = olio.kerro_koordi()
		 			  kaavio[(KOORDI[0], KOORDI[1])]
		 			  Alateemitaan = 1
		 		if Alateemitaan == 0 :	  
				  nykyinenArvo = 0  #EROA "-":n 26.3
				  olio.laita_arvo(0) #EROA "-":n 26.3
				  KOORDI = olio.kerro_koordi()  #EROA "-":n 26.3
				  kaavio[(KOORDI[0], KOORDI[1])] = olio  #EROA "-":n 26.3	

		 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 eka += 1
		 kaksi = (eka , toka)
		 olio = kaavio [kaksi]
		 Merkattavaolio263 = kaavio [  (varaeka263, varatoka263) ]
		 Merkattavaolio263.merkitseLasketuksi()
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue     
	      if  olio.kerro_merkki() == "-" :     	
	         kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 if olio.kerro_arvo() == 0: # jos on 1, niin voi olla, etta joku muu solu on laittanut sen "\" tapauksessa erikoistapaus
		   olio.laita_arvo(kaavio[ ((eka - 1) , toka) ].kerro_arvo())
		 eka += 1
		 kaksi = (eka , toka)
		 olio = kaavio  [kaksi]
		 olio.merkitseLasketuksi()
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue
	      ##UUTTA 8.4
	      if olio.kerro_merkki() == ">" :	
	         kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 if olio.kerro_arvo() == 0: # jos on 1, niin voi olla, etta joku muu solu on laittanut sen "\" tapauksessa erikoistapaus
		   olio.laita_arvo(kaavio[ ((eka - 1) , toka) ].kerro_arvo())
		 eka += 1
		 kaksi = (eka , toka)
		 olio = kaavio  [(eka + 3, toka)]
		 olio.merkitseLasketuksi()
		 olio.laita_arvo(kaavio[((eka - 1) , toka) ].kerro_arvo())	
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue
	      if olio.kerro_merkki() == "#" :   	
	         kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 if olio.kerro_arvo() == 0: # jos on 1, niin voi olla, etta joku muu solu on laittanut sen "\" tapauksessa erikoistapaus
		   olio.laita_arvo(kaavio[ ((eka - 1) , toka) ].kerro_arvo())
		 olio = kaavio  [(eka, (toka - 8))]
		 olio.merkitseLasketuksi()
		 olio.laita_arvo(kaavio[((eka - 1) , toka) ].kerro_arvo())	
		 oikeallaOlevaOlio134 = kaavio [ ((eka + 1), toka) ]
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 
		 insertoiSolu(oikeallaOlevaOlio134 , nykyinenVektori, tulevaVektori) 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue
              if olio.kerro_merkki() == "\\" :
		 koorinantit (olio.kerro_koordi()) 
		 olio.kerro_koordi()
		 kaksi = olio.kerro_koordi()
		 olio304 = olio
		 olio304.merkitseLasketuksi()
 		 debugkaksi = kaksi
		 debugY = debugkaksi[1]
		 debugY += -2
		 debugX = debugkaksi[0]
		 debugX += 1
		 debugkaksi = (debugX , debugY)
		 eka = kaksi[0]
		 toka = kaksi[1]
		 if kaavio[  (eka, (toka + 1)) ].kerro_merkki() == "\\" and kaavio[  (eka, (toka - 1)) ].kerro_merkki() == "-" :
                   alaviivaolio804 = kaavio[ (eka, (toka - 1)) ]
                   ylaviivaolio804 = kaavio[ (eka, (toka + 1)) ]
		   alaviivaolio804.laita_arvo(ylaviivaolio804.kerro_arvo())
	           olio.laita_arvo(ylaviivaolio804.kerro_arvo())
		   olio.merkitseLasketuksi()
		   insertoiSolu(alaviivaolio804 , nykyinenVektori, tulevaVektori)
		   olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		   continue 
		 alaX = kaksi[0]
		 alaY = kaksi[1]
		 alaY -= 1
		 alaTuple = (alaX, alaY)
		 Varakaksi = olio.kerro_koordi() 
		 Varaeka = Varakaksi[0]
		 Varatoka = Varakaksi[1]
		 edellisenX = eka
		 edellisenX -= 1
		 ylhaallaOleva263X = eka 
		 ylhaallaOleva263Y = toka
		 ylhaallaOleva263Y += 1
		 ylaOlio263 = kaavio [ ylhaallaOleva263X , ylhaallaOleva263Y]
		 koorinantit (ylaOlio263.kerro_koordi())
		 ylaArvo263 = ylaOlio263.kerro_arvo()
		 temp = (edellisenX, toka) 
	 	 edellisenKohdanArvo = kaavio[ temp ]
		 temppp = edellisenKohdanArvo.kerro_arvo()
		 kaksi404 = olio.kerro_koordi()
		 eka404 = kaksi404[0]
		 toka404 = kaksi404[1]
		 olio404 = kaavio[ ((eka404 - 1) , toka404) ]
		 LAITETTAVAarvo = olio404.kerro_arvo()
		 if LAITETTAVAarvo == 1 or ylaArvo263 == 1 :
		   if ylaOlio263.kerro_merkki() != "-" or LAITETTAVAarvo == 1 : 
		     temppp = 1
		     olio.laita_arvo(temppp)
		     olio.merkitseLasketuksi()
		     koorinantit(olio.kerro_koordi())
		 eka += 1
		 kaksi = (eka , toka)
		 koorinantit (kaksi)
		 olio = kaavio  [kaksi]
		 olio.merkitseLasketuksi()
		 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 toka -= 1
		 toka += 2 
		 kaksi = (eka , toka)
		 olio = kaavio  [kaksi]
		 koorinantit (olio.kerro_koordi())
		 olio.merkitseLasketuksi()
		 Varatoka += 1
		 Varatoka -= 1
		 Varaeka += 1 
		 tempTuple = (Varaeka, Varatoka)
		 olio = kaavio[ (Varaeka, Varatoka) ]
		 koorinantit ((Varaeka, Varatoka))
		 alaOlio = kaavio[alaTuple]   # eroa / merkkiin
		 koorinantit (alaTuple)
		 koorinantit(alaOlio.kerro_koordi())	 
		 insertoiSolu(alaOlio , nykyinenVektori, tulevaVektori) # eroa / merkkiin
		 koorinantit(olio.kerro_koordi())		
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) 	 
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
	         continue   
       	      if olio.kerro_merkki() == "/" :
       	         GeditistaHashiin ((olio.kerro_koordi()))
  		 olio31 = olio
		 olio401Koordi = olio.kerro_koordi()	      	 
		 kaksi = olio.kerro_koordi()
		 koorinantit(kaksi)
		 eka = kaksi[0]
		 toka = kaksi[1]
		 Varakaksi = olio.kerro_koordi() 
		 Varaeka = eka
		 Varatoka = toka
		 edellisenX = eka
		 edellisenX -= 1
		 temp = (edellisenX, toka) 
		 koorinantit(temp)
	 	 edellisenKohdanArvo = kaavio[temp ]
		 temppp = edellisenKohdanArvo.kerro_arvo()
		 toka263 = toka
		 edellisenX += 1
		 toka263 -= 1
		 alhaallaTuple263 = (edellisenX, toka263)
		 alasolu263 = kaavio[alhaallaTuple263]
		 ekatemp31 = eka 
		 ekatemp31 = eka 
		 tokatemp31 = toka
		 temptuple31 = (ekatemp31, (tokatemp31))
		 koorinantit(temptuple31)
		 olioYlaviivaan30 = kaavio[temptuple31]
		 if temppp == 1 or alasolu263.kerro_arvo() == 1:
		   olioYlaviivaan30.laita_arvo(1)
		   koorinantit((olioYlaviivaan30.kerro_koordi()))
		 else:
		   olioYlaviivaan30.laita_arvo(0)
		   koorinantit(olioYlaviivaan30.kerro_koordi())
		 koorinantit ((eka, toka)) 			#VIRHE
		 eka += 1
		 kaksi = (eka , toka)
	 	 olio = kaavio  [kaksi]
		 koorinantit(olio.kerro_koordi())
		 olio.merkitseLasketuksi()
		 kaksi = olio.kerro_koordi()
		 eka = kaksi[0]
		 toka = kaksi[1]
		 toka -= 1
		 kaksi = (eka , (toka + 2))
		 tempTuple = (Varaeka, Varatoka)
		 olio = kaavio[ ((Varaeka + 1), (Varatoka)) ] #oikealla olevan solun lisaaminen
		 koorinantit (olio.kerro_koordi()) 
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) #oikealla olevan solun lisaaminen
		 olio = kaavio[ ((Varaeka), (Varatoka + 1)) ] #ylhaalla olevan solun lisaaminen
		 koorinantit (olio.kerro_koordi())
		 insertoiSolu(olio , nykyinenVektori, tulevaVektori) #ylhaalla olevan solun lisaaminen
		 olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
		 koorinantit(olio31.kerro_koordi())
		 olio401LaitettavaKaydyksi = kaavio[olio401Koordi]
		 olio401LaitettavaKaydyksi.merkitseLasketuksi()
		 kaavio[olio401Koordi] = olio401LaitettavaKaydyksi
	         continue     
              if  olio.kerro_merkki().islower() == True :
	        tupla303 = olio.kerro_koordi() 
		olio303 = kaavio [ (tupla303[0] - 1  , tupla303[1]) ]
		outputit[(ord(olio.kerro_merkki()) - 97)] = olio303.kerro_arvo()
		onkoOutputtiKaytossa[(ord(olio.kerro_merkki()) - 97)] = 1
		olio.laita_arvo(olio303.kerro_arvo())  
		olio.merkitseLasketuksi()
		olio164 = kaavio [ ((tupla303[0] + 1)  , tupla303[1]) ]
		insertoiSolu(olio164 , nykyinenVektori, tulevaVektori)
	        olio = palautaSeuraavaSolu(nykyinenVektori, tulevaVektori)
                continue
	    if onkoOutputtiKaytossa[0] == 1:
	      print "a = %d" % outputit[0]   
	    if onkoOutputtiKaytossa[1] == 1 :
	      print "b = %d" % outputit[1] 
	    if onkoOutputtiKaytossa[2] == 1 :
	      print "c = %d" % outputit[2] 
	    if onkoOutputtiKaytossa[3] == 1 :	   
	      print "d = %d" % outputit[3]
   	    if onkoOutputtiKaytossa[4] == 1 :	   
	      print "e = %d" % outputit[4]
   	    if onkoOutputtiKaytossa[5] == 1 :	   
	      print "f = %d" % outputit[5]
   	    if onkoOutputtiKaytossa[6] == 1 :	   
	      print "g = %d" % outputit[6]
   	    if onkoOutputtiKaytossa[7] == 1 :	   
	      print "h = %d" % outputit[7]
   	    if onkoOutputtiKaytossa[8] == 1 :	   
	      print "i = %d" % outputit[8]
   	    if onkoOutputtiKaytossa[9] == 1 :	   
	      print "j = %d" % outputit[9]
   	    if onkoOutputtiKaytossa[10] == 1 :	   
	      print "k = %d" % outputit[10]
   	    if onkoOutputtiKaytossa[11] == 1 :	   
	      print "l = %d" % outputit[11]
   	    if onkoOutputtiKaytossa[12] == 1 :	   
	      print "m = %d" % outputit[12]
   	    if onkoOutputtiKaytossa[13] == 1 :	   
	      print "n = %d" % outputit[13]
   	    if onkoOutputtiKaytossa[14] == 1 :	   
	      print "o = %d" % outputit[14]
   	    if onkoOutputtiKaytossa[15] == 1 :	   
	      print "p = %d" % outputit[15]
   	    if onkoOutputtiKaytossa[16] == 1 :	   
	      print "q = %d" % outputit[16]
   	    if onkoOutputtiKaytossa[17] == 1 :	   
	      print "r = %d" % outputit[17]
   	    if onkoOutputtiKaytossa[18] == 1 :	   
	      print "s = %d" % outputit[18]
   	    if onkoOutputtiKaytossa[19] == 1 :	   
	      print "t = %d" % outputit[19]
   	    if onkoOutputtiKaytossa[20] == 1 :	   
	      print "u = %d" % outputit[20]
   	    if onkoOutputtiKaytossa[21] == 1 :	   
	      print "v = %d" % outputit[21]
   	    if onkoOutputtiKaytossa[22] == 1 :	   
	      print "w = %d" % outputit[22]
   	    if onkoOutputtiKaytossa[23] == 1 :	   
	      print "x = %d" % outputit[23]
   	    if onkoOutputtiKaytossa[24] == 1 :	   
	      print "y = %d" % outputit[24]
   	    if onkoOutputtiKaytossa[25] == 1 :	   
	      print "z = %d" % outputit[25]
	    if pientenKirjaintenEsiintyvyys[0] == 1 and onkoOutputtiKaytossa[0] == 0:
	       print "a kaaviossa, mutta arvoa ei asetettu"
	    if pientenKirjaintenEsiintyvyys[1] == 1 and onkoOutputtiKaytossa[1] == 0 :
	       print "b kaaviossa, mutta arvoa ei asetettu"
	    if pientenKirjaintenEsiintyvyys[2] == 1 and onkoOutputtiKaytossa[2] == 0 :
	       print "c kaaviossa, mutta arvoa ei asetettu"
       	    if pientenKirjaintenEsiintyvyys[3] == 1 and onkoOutputtiKaytossa[3] == 0 :
	       print "d kaaviossa, mutta arvoa ei asetettu"
       	    if pientenKirjaintenEsiintyvyys[4] == 1 and onkoOutputtiKaytossa[4] == 0 :
	       print "e kaaviossa, mutta arvoa ei asetettu"
       	    if pientenKirjaintenEsiintyvyys[5] == 1 and onkoOutputtiKaytossa[5] == 0 :
	       print "f kaaviossa, mutta arvoa ei asetettu"
       	    if pientenKirjaintenEsiintyvyys[6] == 1 and onkoOutputtiKaytossa[6] == 0 :
	       print "g kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[7] == 1 and onkoOutputtiKaytossa[7] == 0 :
	       print "h kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[8] == 1 and onkoOutputtiKaytossa[8] == 0 :
	       print "i kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[9] == 1 and onkoOutputtiKaytossa[9] == 0 :
	       print "j kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[10] == 1 and onkoOutputtiKaytossa[10] == 0 :
	       print "k kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[11] == 1 and onkoOutputtiKaytossa[11] == 0 :
	       print "l kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[12] == 1 and onkoOutputtiKaytossa[12] == 0 :
	       print "m kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[13] == 1 and onkoOutputtiKaytossa[13] == 0 :
	       print "n kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[14] == 1 and onkoOutputtiKaytossa[14] == 0 :      	    
	       print "o kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[15] == 1 and onkoOutputtiKaytossa[15] == 0 :
	       print "p kaaviossa, mutta arvoa ei asetettu"
      	    if pientenKirjaintenEsiintyvyys[16] == 1 and onkoOutputtiKaytossa[16] == 0 :
	       print "q kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[17] == 1 and onkoOutputtiKaytossa[17] == 0 :
	       print "r kaaviossa, mutta arvoa ei asetettu"
 	    if pientenKirjaintenEsiintyvyys[18] == 1 and onkoOutputtiKaytossa[18] == 0 :
	       print "s kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[19] == 1 and onkoOutputtiKaytossa[19] == 0 :
	       print "t kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[20] == 1 and onkoOutputtiKaytossa[20] == 0 :
	       print "u kaaviossa, mutta arvoa ei asetettu"	       
     	    if pientenKirjaintenEsiintyvyys[21] == 1 and onkoOutputtiKaytossa[21] == 0 :
	       print "v kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[22] == 1 and onkoOutputtiKaytossa[22] == 0 :
	       print "w kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[23] == 1 and onkoOutputtiKaytossa[23] == 0 :
	       print "x kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[24] == 1 and onkoOutputtiKaytossa[24] == 0 :
	       print "y kaaviossa, mutta arvoa ei asetettu"
     	    if pientenKirjaintenEsiintyvyys[25] == 1 and onkoOutputtiKaytossa[25] == 0 :
	       print "z kaaviossa, mutta arvoa ei asetettu"
	    pituus = len(StringiVektori)
	    for i in range(pituus):
	      print "(%s)=%d" % (StringiVektori[(pituus - i - 1)], StringiVektorinArvot[i])
            return outputit       
    def read_fully(self, count, input):
        '''
        The read-method of the Reader class will occasionally read only part of
        the characters that were requested. This method will repeatedly call read
        to completely fill the given buffer. The size of the buffer tells the
        algorithm how many bytes should be read.
        
        @param count:
                   How many characters are read
        @param input:
                   The character stream to read from
        @raises: IOError
        @raises: CorruptedChessFileError
        '''
        read_chars = input.read(count)
        
        # If the file end is reached before the buffer is filled
        # an exception is thrown.    
        if len(read_chars) != count:
                print("Unexpected end of file.")

        return list(read_chars)
        

