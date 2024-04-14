import random
import unittest
import sys
from chunkIO import ChunkIO
from unitTestSupportClass import loop
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
	  			    palautusVektori =piiri.lataa_peli(toisto_file, 0, 1, AAA, BBB, CCC, DDD,EEE,FFF,GGG,HHH, III, JJJ , KKK , LLL , MMM ,NNN ,OOO ,PPP , QQQ ,RRR ,SSS , TTT , UUU, VVV, WWW, XXX, YYY, ZZZ) # tokan laittaminen 1:seksi palauttaa muuttuvat, toisen laittaminen 1:ksi tarvoikkaa, sita, etta AAA, BBB , CCC parametreilla on
				    self.assertEqual(AAA , palautus[0],  "Perustapaus " )

class Test(unittest.TestCase):
  #def setUp(self):
   # self.load = 

  def test_given_example(self):
  
  #def load(self):    
    #self.load() = ChunkIO.lataa_peli()

    self.input_file =  open('assertiedosto1', 'r') 
    chunk_IO = ChunkIO()
    try :
      palautus = chunk_IO.lataa_peli(self.input_file , 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0)
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
	#muuta ValueError key erroriks
    





    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")

    self.input_file2 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file2 , 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")

    self.input_file3 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file3 , 0, 1, 0, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")

    self.input_file4 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file4, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")

    self.input_file5 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file5, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")


    self.input_file6 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file6, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")


    self.input_file7 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file7, 0, 1, 1, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")


    self.input_file8 =  open('assertiedosto1', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")

    self.input_file9 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file9, 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")

    self.input_file10 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file10, 0, 1, 0, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")


    self.input_file11 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file11, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")


    self.input_file12 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file12, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")

    self.input_file13 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file13, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")


    self.input_file14 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file14, 0, 1, 1, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")

    self.input_file15 =  open('assertiedosto2', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file15, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus ")

    self.input_file15 =  open('assertiedosto3', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file15, 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")

    self.input_file16 =  open('assertiedosto3', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file16, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")


    self.input_file17 =  open('assertiedosto3', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file17, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")


    self.input_file18 =  open('assertiedosto3', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file18, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus ")



    self.input_file19 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file19, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus ")

    self.input_file20 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file20, 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file21 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file21, 0, 1, 0, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file22 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file22, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )


    self.input_file22 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file22, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )


    self.input_file22 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file22, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file22 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file22, 0, 1, 1, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file22 =  open('assertiedosto4', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file22, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto5', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto5', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto5', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto5', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )


    self.input_file23 =  open('assertiedosto6', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )


    self.input_file23 =  open('assertiedosto6', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto7', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Perustapaus " )


    self.input_file23 =  open('assertiedosto7', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Perustapaus " )

    piiri = chunk_IO
    self.input_file24 =  open('assertiedosto9', 'r') 
    vaikuttavatInputit = chunk_IO.lataa_peli(self.input_file24, 1, 0, 0, 0, 0,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) 
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
			  #for NNN in range(vaikuttavatInputit[13]+1 ) :
			    #for OOO in range(vaikuttavatInputit[14]+1 ) : 
			      #for PPP in range(vaikuttavatInputit[15]+1 ) :
				#for QQQ in range(vaikuttavatInputit[16]+1 ) :
				  #for RRR in range(vaikuttavatInputit[17]+1 ) :
				    #for SSS in range(vaikuttavatInputit[18]+1 ) :
				      #for TTT in range(vaikuttavatInputit[19]+1 ) :		 
					#for UUU in range(vaikuttavatInputit[20]+1 ) :
					  #for VVV in range(vaikuttavatInputit[21]+1 ) :
					    #for WWW in range(vaikuttavatInputit[22]+1 ) :
					      #for XXX in range(vaikuttavatInputit[23]+1 ) :
						#for YYY in range(vaikuttavatInputit[24]+1 ) :
						  #for ZZZ in range(vaikuttavatInputit[25]+1 ) :
			     
			      self.input_file1000 = open('assertiedosto9' ,'r')	
			      #looppausTesti = loop()
			      palautus = chunk_IO.lataa_peli(self.input_file1000  , 0, 1, AAA, BBB, CCC ,DDD,EEE,FFF,GGG,HHH, III, JJJ ,KKK ,LLL ,MMM ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    
    
    			      self.assertEqual(AAA , palautus[0],  "Perustapaus " )
			      self.assertEqual(BBB , palautus[1],  "Perustapaus " )
			      self.assertEqual(CCC , palautus[2],  "Perustapaus " )
			      self.assertEqual(DDD , palautus[3],  "Perustapaus " )
			      self.assertEqual(EEE , palautus[4],  "Perustapaus " )
			      self.assertEqual(FFF , palautus[5],  "Perustapaus " )
			      self.assertEqual(GGG , palautus[6],  "Perustapaus " )
			      self.assertEqual(HHH , palautus[7],  "Perustapaus " )
			      self.assertEqual(III , palautus[8],  "Perustapaus " )
			      self.assertEqual(JJJ , palautus[9],  "Perustapaus " )
			      self.assertEqual(KKK , palautus[10],  "Perustapaus " )
			      self.assertEqual(LLL , palautus[11],  "Perustapaus " )
			      self.assertEqual(MMM , palautus[12],  "Perustapaus " )

    self.input_file1000 = open('assertiedosto9' ,'r')	
    vaikuttavatInputit = chunk_IO.lataa_peli(self.input_file1000, 1, 0, 0, 0, 0,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) 

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
		             self.input_file1000 = open('assertiedosto9' ,'r')	
			      #looppausTesti = loop()
		             palautus = chunk_IO.lataa_peli(self.input_file1000  , 0, 1, 0 , 0 , 0  , 0 ,0 ,0 ,0 ,0 , 0, 0 ,0 ,0 ,0 ,NNN ,OOO ,PPP , QQQ ,RRR ,SSS , TTT , UUU, VVV, WWW, XXX, YYY, ZZZ) #Laita kaikki 8 tapausta
   			     self.assertEqual(NNN , palautus[13],  "Perustapaus " )
		             self.assertEqual(OOO , palautus[14],  "Perustapaus " )
		             self.assertEqual(PPP , palautus[15],  "Perustapaus " )
		             self.assertEqual(QQQ , palautus[16],  "Perustapaus " )
		             self.assertEqual(RRR , palautus[17],  "Perustapaus " )
		             self.assertEqual(SSS , palautus[18],  "Perustapaus " )
		             self.assertEqual(TTT , palautus[19],  "Perustapaus " )
		             self.assertEqual(UUU , palautus[20],  "Perustapaus " )
		             self.assertEqual(VVV , palautus[21],  "Perustapaus " )
		             self.assertEqual(WWW , palautus[22],  "Perustapaus " )
		             self.assertEqual(XXX , palautus[23],  "Perustapaus " )
		             self.assertEqual(YYY , palautus[24],  "Perustapaus " )
			     self.assertEqual(ZZZ , palautus[25],  "Perustapaus " )

    self.input_file23 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battrey vihkoa ja toista assertiedostoa " )
    self.assertEqual(0 , palautus[1],  "Katso battrey vihkoa ja toista assertiedostoa" )
    self.input_file23 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battrey vihkoa ja toista assertiedostoa " )
    self.assertEqual(0 , palautus[1],  "Katso battrey vihkoa ja toista assertiedostoa" )

    

    self.input_file2 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file2 , 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(0 , palautus[1],  "Katso battery vihosta ")


    self.input_file3 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file3 , 0, 1, 0, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file4 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file4, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(0 , palautus[1],  "Katso battery vihosta ")

    self.input_file5 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file5, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file6 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file6, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file7 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file7, 0, 1, 1, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(0 , palautus[1],  "Katso battery vihosta ")

    self.input_file8 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")



    self.input_file23 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battrey vihkoa ja toista assertiedostoa " )
    self.assertEqual(0 , palautus[1],  "Katso battrey vihkoa ja toista assertiedostoa" )
    self.input_file23 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file23, 0, 1, 0, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battrey vihkoa ja toista assertiedostoa " )
    self.assertEqual(0 , palautus[1],  "Katso battrey vihkoa ja toista assertiedostoa" )

    
    # Alkaa tapaus, jossa X tai on aina 1 
    self.input_file2 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file2 , 0, 1, 0, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file3 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file3 , 0, 1, 0, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file4 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file4, 0, 1, 0, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")

    self.input_file5 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file5, 0, 1, 1, 0, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")


    self.input_file6 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file6, 0, 1, 1, 0, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")



    self.input_file7 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file7, 0, 1, 1, 1, 0 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(0 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")



    self.input_file8 =  open('assertiedosto10', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,0,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 1, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    self.assertEqual(1 , palautus[0],  "Katso battery vihosta ")
    self.assertEqual(1 , palautus[1],  "Katso battery vihosta ")



    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,1,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 0, 0 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 0, 0 , 1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 0, 1 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 0, 1 , 1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")


    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 1, 0 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 1, 0 , 1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 0, 1, 1 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 0, 0 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 0, 1 , 0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")


    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 0, 1 ,1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 0 ,0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
    
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 0 ,1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
 
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")

    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,0 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
 
    self.assertEqual(0 , palautus[5],  "s 59 kirja ")



    self.input_file8 =  open('assertiedosto11', 'r') 
    try :
      palautus = chunk_IO.lataa_peli(self.input_file8, 0, 1, 1, 1, 1 ,1 ,0,0,0,0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 , 0 ,0 ,0 , 0 , 0, 0, 0, 0, 0, 0) #Laita kaikki 8 tapausta
    except ValueError:
      self.fail("Loading a correctly structured file caused an exception")
 
    self.assertEqual(1 , palautus[5],  "s 59 kirja ")
    #print palautus[0]
  #inputAssert1_file = open('assertiedosto1', 'r') 
  #self.setUp()
  #Asssertpiiri1 = ChunkIO()
  
	#palautusVektori[0] = Assertpiiri1.lataa_peli( inputAssert1_file  , 0,1,1,1,1 )
  #ykkonen = []
  #ykkonen.insert( 0,0)
  #self.assertEqual( ykkonen[0] , self.setUp.lataa_peli( 'assertiedosto1' , 0, 1, 1, 1, 1 ) ,
  #"Ei toimi"  )
        #  "eka batteri kirjoitettu tapaus ei toimi")

        # WRITE MORE TESTS        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()  


