from owlready import *
import types
onto = get_ontology("file://kike.owl").load()

#class Alumno(Thing):
#	ontology = onto
	
#class Alumno1(Alumno):
#	ontology = onto	


newClass = types.new_class("Carpintero",(Thing,),kwds={"ontology":onto})



newClass2 = types.new_class("kike",(newClass,),kwds={"ontology":onto})

#is_a = [newClass & newClass2]

#newClass.equivalent_to(newClass2)
#newClass.equivalent_to.append(newClass2)
#print (is_a)
onto.save()
