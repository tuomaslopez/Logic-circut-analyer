import random
import unittest
import sys
from chunkIO import ChunkIO
class loop(unittest.TestCase):
	def osa2loopista(piiri, vaikuttavatInputit , toisto_file, AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH, III, JJJ, KKK, LLL, MMM):
	  for NNN in range(vaikuttavatInputit[13]+1 ) :
	    for OOO in range(vaikuttavatInputit[14]+1 ) : 
	      for PPP in range(vaikuttavatInputit[15]+1 ) :
		for QQQ in range(vaikuttavatInputit[16]+1 ) :
		  for RRR in range(vaikuttavatInputit[17]+1 ) :
		    for SSS in range(vaikuttavatInputit[18]+1 ) :
		      for TTT in range(vaikuttavatInputit[19]+1 ) :		 
			for UUU in range(vaikuttavatInputit[20]+1 ) :
			  for VVV in range(vaikuttavatInputit[21]+1 ) :
			    for WWW in range(vaikuttavatInputit[22]+1 ) :
			      for XXX in range(vaikuttavatInputit[23]+1 ) :
				for YYY in range(vaikuttavatInputit[24]+1 ) :
				  for ZZZ in range(vaikuttavatInputit[25]+1 ) :
				    if vaikuttavatInputit[0]:
				      print "AAA="
				      print AAA
				    if vaikuttavatInputit[1]:
				      print "BBB="
				      print BBB
				    if vaikuttavatInputit[2]:
				      print "CCC="
				      print CCC
				    if vaikuttavatInputit[3]:
				      print "DDD="
				      print DDD
				    if vaikuttavatInputit[4]:
				      print "EEE="
				      print EEE
				    if vaikuttavatInputit[5]:
				      print "FFF="
				      print FFF
				    if vaikuttavatInputit[6]:
				      print "GGG="
				      print GGG
				    if vaikuttavatInputit[7]:
				      print "HHH="
				      print HHH
				    if vaikuttavatInputit[8]:
				      print "III="
				      print III
				    if vaikuttavatInputit[9]:
				      print "JJJ="
				      print JJJ
				    if vaikuttavatInputit[10]:
				      print "KKK="
				      print KKK
				    if vaikuttavatInputit[11]:
				      print "LLL="
				      print LLL
	  			    if vaikuttavatInputit[12]:
	    			      print "MMM="
	   			      print MMM
	 			    if vaikuttavatInputit[13]:
				      print "NNN="
				      print NNN
				    if vaikuttavatInputit[14]:
				      print "OOO="
				      print OOO
				    if vaikuttavatInputit[15]:
				      print "PPP="
				      print PPP
				    if vaikuttavatInputit[16]:
				      print "QQQ="
				      print QQQ
				    if vaikuttavatInputit[17]:
				      print "RRR="
				      print RRR
				    if vaikuttavatInputit[18]:
				      print "SSS="
				      print SSS
				    if vaikuttavatInputit[19]:
				      print "TTT="
				      print TTT
				    if vaikuttavatInputit[20]:
				      print "UUU="
				      print UUU
				    if vaikuttavatInputit[21]:
				      print "VVV="
				      print VVV
				    if vaikuttavatInputit[22]:
				      print "WWW="
				      print WWW
				    if vaikuttavatInputit[23]:
				      print "XXX="
				      print XXX
				    if vaikuttavatInputit[24]:
				      print "YYY="
				      print YYY
				    if vaikuttavatInputit[25]:
				      print "ZZZ="
				      print ZZZ
	  			    toisto_file = open('assertiedosto9' ,'r')
	  			    palautusVektori = []
	  			    palautusVektori =piiri.load_game(toisto_file, 0, 1, AAA, BBB, CCC, DDD,EEE,FFF,GGG,HHH, III, JJJ , KKK , LLL , MMM ,NNN ,OOO ,PPP , QQQ ,RRR ,SSS , TTT , UUU, VVV, WWW, XXX, YYY, ZZZ) # tokan laittaminen 1:seksi palauttaa muuttuvat, toisen laittaminen 1:ksi tarvoikkaa, sita, etta AAA, BBB , CCC parametreilla on
				    self.assertEqual(AAA , palautusVektori[0],  "Perustapaus " )
