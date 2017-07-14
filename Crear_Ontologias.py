from owlready import *
import types
onto=0

class Crear_Ontologia:
	def __init__(self,nombre):
		self.nombre="file://"+nombre+".owl"
	
	def crear(self):
		onto = Ontology(self.nombre)
		print (type(onto))
		onto.save()
		return onto
	
	def abrir(self):
		onto = Ontology(self.nombre)
		onto.load(self.nombre)
		return onto
	
	def crear_clase(self,onto,clase_padre,clase):
		onto2=onto
#		print (onto)
		if(clase_padre=="Thing"):
			#temporal = types.new_class(clase_padre,(Thing,),kwds={"ontology":onto})
			temporal = types.new_class(clase,(Thing,),kwds={"ontology":onto})
			print (temporal)
		else:
			temporal=types.new_class(clase_padre,(Thing,),kwds={"ontology":onto})
			newClass = types.new_class(clase,(temporal,),kwds={"ontology":onto})
			print (newClass)
		#temporal = types.new_class(clase_padre,(Thing),kwds={"ontology":onto2})
		
		#print (newClass)	
		onto.save()
		return onto
