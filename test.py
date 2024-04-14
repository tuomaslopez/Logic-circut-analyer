import unittest
import sys
from chunkIO import ChunkIO
from optparse import OptionParser

def osa2loopista(avattavaTiedosto , piiri, vaikuttavatInputit , toisto_file, AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH, III, JJJ, KKK, LLL, MMM):
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
			      print "A= %d" % (AAA)
			    if vaikuttavatInputit[1]:
			      print "B= %d" % (BBB)
			    if vaikuttavatInputit[2]:
			      print "C= %d" %(CCC)
			    if vaikuttavatInputit[3]:
			      print "D= %d" %(DDD)
			    if vaikuttavatInputit[4]:
			      print "E= %d" %(EEE)
			    if vaikuttavatInputit[5]:
			      print "F= %d" %(FFF)
			    if vaikuttavatInputit[6]:
			      print "G= %d" %(GGG)
			    if vaikuttavatInputit[7]:
			      print "H= %d" %(HHH)
			    if vaikuttavatInputit[8]:
			      print "I= %d" %(III)
			    if vaikuttavatInputit[9]:
			      print "J= %d" %(JJJ)
			    if vaikuttavatInputit[10]:
			      print "K= %d" %(KKK)
			    if vaikuttavatInputit[11]:
			      print "L= %d" %(LLL)
  			    if vaikuttavatInputit[12]:
    			      print "M= %d" %(MMM)
 			    if vaikuttavatInputit[13]:
			      print "N= %d" %(NNN)
			    if vaikuttavatInputit[14]:
			      print "O= %d" %(OOO)
			    if vaikuttavatInputit[15]:
			      print "P= %d" %(PPP)
			    if vaikuttavatInputit[16]:
			      print "Q= %d" %(QQQ)
			    if vaikuttavatInputit[17]:
			      print "R= %d" %(RRR)
			    if vaikuttavatInputit[18]:
			      print "S= %d" %(SSS)
			    if vaikuttavatInputit[19]:
			      print "T= %d" %(TTT)
			    if vaikuttavatInputit[20]:
			      print "U= %d" %(UUU)
			    if vaikuttavatInputit[21]:
			      print "V= %d" %(VVV)
			    if vaikuttavatInputit[22]:
			      print "W= %d" %(WWW)
			    if vaikuttavatInputit[23]:
			      print "X= %d" %(XXX)
			    if vaikuttavatInputit[24]:
			      print "Y= %d" %(YYY)
			    if vaikuttavatInputit[25]:
			      print "Z= %d" %(ZZZ)
  			    toisto_file = open(avattavaTiedosto ,'r')
  			    palautusVektori = []
  			    palautusVektori =piiri.lataa_peli(toisto_file, 0, 1, AAA, BBB, CCC, DDD,EEE,FFF,GGG,HHH, III, JJJ , KKK , LLL , MMM ,NNN ,OOO ,PPP , QQQ ,RRR ,SSS , TTT , UUU, VVV, WWW, XXX, YYY, ZZZ) # tokan laittaminen 1:seksi palauttaa muuttuvat, toisen laittaminen 1:ksi tarvoikkaa, sita, etta AAA, BBB , CCC parametreilla on
                           
def main():
        firstInput = ''
	avattavaTiedosto = sys.argv[4]
	firstInputRun_file = open( avattavaTiedosto , 'r' )

	piiri = ChunkIO()
	piiri.lataa_peli(firstInputRun_file, 0, 0, 0, 0, 0,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0)
	if sys.argv[2] == "1" :
	  sys.exit()
	  exit()
	  return

        input_file = open(avattavaTiedosto, 'r')

        
        piiri = ChunkIO()      
	vaikuttavatInputit = piiri.lataa_peli(input_file, 1, 0, 0, 0, 0,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) 
	print "Onko A vaikuttava %d" %vaikuttavatInputit[0] 		 
	print "Onko B vaikuttava %d" %vaikuttavatInputit[1]
	print "Onko C vaikuttava %d" %vaikuttavatInputit[2]
	print "Onko D vaikuttava %d" %vaikuttavatInputit[3]
	print "Onko E vaikuttava %d" %vaikuttavatInputit[4]
	print "Onko F vaikuttava %d" %vaikuttavatInputit[5]
	print "Onko G vaikuttava %d" %vaikuttavatInputit[6]
	print "Onko H vaikuttava %d" %vaikuttavatInputit[7]
	print "Onko I vaikuttava %d" %vaikuttavatInputit[8]
	print "Onko J vaikuttava %d" %vaikuttavatInputit[9]
	print "Onko K vaikuttava %d" %vaikuttavatInputit[10]
	print "Onko L vaikuttava %d" %vaikuttavatInputit[11]
	print "Onko M vaikuttava %d" %vaikuttavatInputit[12]
	print "Onko N vaikuttava %d" %vaikuttavatInputit[13]
	print "Onko O vaikuttava %d" %vaikuttavatInputit[14]
	print "Onko P vaikuttava %d" %vaikuttavatInputit[15]
	print "Onko Q vaikuttava %d" %vaikuttavatInputit[16]
	print "Onko R vaikuttava %d" %vaikuttavatInputit[17]
	print "Onko S vaikuttava %d" %vaikuttavatInputit[18]
	print "Onko T vaikuttava %d" %vaikuttavatInputit[19]
	print "Onko U vaikuttava %d" %vaikuttavatInputit[20]
	print "Onko V vaikuttava %d" %vaikuttavatInputit[21]
	print "Onko W vaikuttava %d" %vaikuttavatInputit[22]
	print "Onko X vaikuttava %d" %vaikuttavatInputit[23]	 
	print "Onko Y vaikuttava %d" %vaikuttavatInputit[24]	 
	print "Onko Z vaikuttava %d" %vaikuttavatInputit[25]

        for AAA in range (vaikuttavatInputit[0]+1) :
	  for BBB in range (vaikuttavatInputit[1]+1) :
	    for  CCC in range (vaikuttavatInputit[2]+1 ) :
	      for  DDD in range (vaikuttavatInputit[3]+1 ) :
	        for EEE in range(vaikuttavatInputit[4]+1 ) :
		  for FFF in range(vaikuttavatInputit[5]+1 ) :
		    for GGG in range(vaikuttavatInputit[6]+1 ) :
		      for HHH in range(vaikuttavatInputit[7]+1 ) :
		        for III in range(vaikuttavatInputit[8]+1 ) :
			  for JJJ in range(vaikuttavatInputit[9]+1 ) :
			    for KKK in range(vaikuttavatInputit[10]+1 ) :
			      for LLL in range(vaikuttavatInputit[11]+1 ) :
			        for MMM in range(vaikuttavatInputit[12]+1 ) : 

				  toisto_file = open(avattavaTiedosto ,'r')	
				  osa2loopista(avattavaTiedosto , piiri , vaikuttavatInputit , toisto_file, AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH, III, JJJ, KKK, LLL, MMM) 

main()
