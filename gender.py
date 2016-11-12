import json,urllib2,re

def getGender():
	#Private Server Key					
	myKey = "AAeRoBSAaUMbRlyvKw"    		
	name=raw_input("Enter your first name :")

	#Reguler expression to satisfy the criterias of First Name	
	pattern=re.compile("^[A-Za-z]+$")		 
	try :
		if pattern.match(name):
	
	#Passing the key value and the name value through url as input and fetching the gender output in json format
			data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + myKey + "&name="+name))   
			print "Gender: " + data["gender"];
		else :
	
	#raising exception if the first name doesn't match the reguler expression pattern
			raise Exception				
	except Exception as error :	
		print "This is not a valid first name"


if __name__ == '__main__':
	getGender()  					
	
