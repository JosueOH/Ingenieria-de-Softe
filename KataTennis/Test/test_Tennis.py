import sys
sys.path.insert(0, "./src")
import unittest
from Tennis import Tennis

class ProbarTennis(unittest.TestCase):

	def test_Love_All(self):
		juego=Tennis("Alan", "Kenny")
		

		self.assertEquals("love all", juego.get_Marcador())

	def test_primer_punto_j1(self):
		juego=Tennis("Alan", "Kenny")

		juego.PuntosJ1()

		self.assertEquals("Quince,love", juego.get_Marcador())

	def test_quince_all(self):
		juego=Tennis("Alan", "Kenny")
		juego.PuntosJ1()
		juego.PuntosJ2()

		self.assertEquals("Quince all", juego.get_Marcador())

	def test_J1_ganador(self):
		juego=Tennis("Alan", "Kenny")
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()


		self.assertEquals(" Gana", juego.get_Marcador())

	def test_J2_ganador(self):
		juego=Tennis("Alan", "Kenny")
		juego.PuntosJ2()
		juego.PuntosJ2()
		juego.PuntosJ2()
		juego.PuntosJ2()


		self.assertEquals(" Gana", juego.get_Marcador())

	def test_Deuce(self):
		juego=Tennis("Alan", "Kenny")
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ2()
		juego.PuntosJ2()
		juego.PuntosJ2()

		self.assertEquals("Deuce", juego.get_Marcador())	

	def test_ventaja(self):
		juego=Tennis("Alan", "Kenny")
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ1()
		juego.PuntosJ2()
		juego.PuntosJ2()
		juego.PuntosJ2()
		juego.PuntosJ2()

		self.assertEquals("Tiene ventaja ", juego.get_Marcador())	


		














		


