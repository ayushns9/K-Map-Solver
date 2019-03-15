# CSE 101 - IP HW2
# K-Map Minimization 
# Name: AYUSH GOEL
# Roll Number: 2018029
# Section: A
# Group: 5
# Date: 17/10/2018
from copy import *

def givefinalans4(a):
	'''
		This funtion converts the essential prime implicants to their
		final answer in terms of the variables for number of variables=4.
	'''
	ans=''
	y=['w','x','y','z']
	for i in a:
		for j in range(len(i)):
			if(i[j]=='1'):
				ans=ans+y[j]
			if(i[j]=='0'):
				ans=ans+y[j]+"'"
		ans=ans+'+'
	return ans[:(len(ans)-1)]

def givefinalans3(a):
	'''
		This funtion converts the essential prime implicants to their
		final answer in terms of the variables for number of variables=3.
	'''
	ans=''
	y=['x','y','z']
	for i in a:
		for j in range(len(i)):
			if(i[j]=='1'):
				ans=ans+y[j]
			if(i[j]=='0'):
				ans=ans+y[j]+"'"
		ans=ans+'+'
	return ans[:(len(ans)-1)]

def givefinalans2(a):
	'''
		This funtion converts the essential prime implicants to their
		final answer in terms of the variables for number of variables=2.
	'''
	ans=''
	y=['y','z']
	for i in a:
		for j in range(len(i)):
			if(i[j]=='1'):
				ans=ans+y[j]
			if(i[j]=='0'):
				ans=ans+y[j]+"'"
		ans=ans+'+'
	return ans[:(len(ans)-1)]

def check(a):
	'''
		This python function checks if the given array has elements having
		_ in them.
	'''
	for i in a:
		for j in i:
			if(j=='_'):
				return False
	return True


def count1(s):
	"""
		This funtion counts and returns the number of 1's in the given string.
		Input: string
	"""
	s=str(s)
	c=0
	for i in s:
		if(i=='1'):
			c+=1
	return c

def bitcount(a,b):
	"""
		This function counts the number of bits different in two binary numbers.
		Input: 2 strings 
	"""
	count=0
	for i in range(len(a)):
		if(a[i]!=b[i]):
			count+=1
	return count
def bitchange(a,b):
	c=''
	for i in range(len(a)):
		if(a[i]!=b[i]):
			c+='_'
		else:
			c+=a[i]
	return c
def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	"""
	if(numVar==4):
		step0=[]
		step1={0:[],1:[],2:[],3:[],4:[]}
		step2={'01':[],'12':[],'23':[],'34':[]}
		step3={0:[],1:[],2:[]}
		step4={0:[],1:[]}
		step5={0:[]}
		allthemin=[]
		m={0:'0000',1:'0001',2:'0010',3:'0011',4:'0100',5:'0101',6:'0110',7:'0111',8:'1000',9:'1001',10:'1010',11:'1011',12:'1100',13:'1101',14:'1110',15:'1111'}
		n={'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':10,'1011':11,'1100':12,'1101':13,'1110':14,'1111':15}
		for i in range(len(stringIn)):
			if(stringIn[i].isdigit() and stringIn[i+1].isdigit()):
				step0.append(m[int(stringIn[i]+stringIn[i+1])])
			elif(stringIn[i].isdigit() and (stringIn[i-1]=='a' or stringIn[i-1]=='d')):
				step0.append(m[int(stringIn[i])])

		for i in step0:					#grouping the numbers
			a=count1(i)					#with the respective number of 1's
			step1[a].append(i)
		
		step1t=deepcopy(step1)							#grouping for step1
		for i in range(4):
			for j in step1[i]:
				for k in step1[i+1]:
					if(bitcount(j,k)==1):
						step2[str(i)+str(i+1)].append(bitchange(j,k))
						if j in step1t[i]:
							step1t[i].remove(j)
						if k in step1t[i+1]:
							step1t[i+1].remove(k)
						
		step2t=deepcopy(step2)
		for i in range(3):							#grouping for step2
			for j in step2[str(i)+str(i+1)]:
				for k in step2[str(i+1)+str(i+2)]:
					if(bitcount(j,k))==1:
						step3[i].append(bitchange(j,k))
						if j in step2t[str(i)+str(i+1)]:
							step2t[str(i)+str(i+1)].remove(j)
						if k in step2t[str(i+1)+str(i+2)]:
							step2t[str(i+1)+str(i+2)].remove(k)

		step3t=deepcopy(step3)

		for i in range(2):					#grouping for step3
			for j in step3[i]:
				for k in step3[i+1]:
					if(bitcount(j,k)==1):
						step4[i].append(bitchange(j,k))
						if j in step3t[i]:
							step3t[i].remove(j)
						if k in step3t[i+1]:
							step3t[i+1].remove(k) 

		step4t=deepcopy(step4)
		for i in range(1):
			for j in step4[i]:					#grouping for step4
				for k in step4[i+1]:
					if(bitcount(j,k)==1):
						step5[i].append(bitchange(j,k))
						if j in step4t[i]:
							step4t[i].remove(j)
						if k in step4t[i+1]:
							step4t[i+1].remove(k) 
		'''Grouping all the minterms in an array'''					
		for i in step1t.keys():						
			for j in step1t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step2t.keys():
			for j in step2t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step3t.keys():
			for j in step3t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step4t.keys():
			for j in step4t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step5.keys():
			for j in step5[i]:
				if(not j in allthemin):
					allthemin.append(j)

		'''Generating prime implicants'''
		prime={}
		for i in step0:
			for j in allthemin:
				flag=0
				for k in range(len(j)):
					if(j[k]!=i[k] and j[k]!='_'):
						flag=1
				if(flag==0):
					if(n[i] in prime.keys()):
						prime[n[i]].append(j)
					else:
						prime[n[i]]=[j]
		
		'''Generating essential prime implicants'''
		epi=[]
		check={}
		for i in step0:
			if(stringIn[stringIn.find(str(n[i]))-1]=='a'):
				check[n[i]]=0
		for i in prime.keys():
			if(len(prime[i])==1 and i in check.keys()):
				epi.append(prime[i][0])
				check[i]=1
		for i in epi:
			for j in prime.keys():
				if(i in prime[j] and j in check.keys()):
					check[j]=1
		

		'''Deleting duplicates'''
		fepi=[]
		for i in epi:
			if(not i in fepi):
				fepi.append(i)
		if(len(step0)==16):
			stringOut='1'
		elif(len(step0)==0):
			stringOut='0'	
		else:
			stringOut=givefinalans4(fepi)

	elif(numVar==3):
		m={0:'000',1:'001',2:'010',3:'011',4:'100',5:'101',6:'110',7:'111'}
		n={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
		step0=[]
		step1={0:[],1:[],2:[],3:[]}
		step2={'01':[],'12':[],'23':[]}
		step3={0:[],1:[]}
		step4={0:[]}
		allthemin=[]

		for i in range(len(stringIn)):
			if(stringIn[i].isdigit() and stringIn[i+1].isdigit()):
				step0.append(m[int(stringIn[i]+stringIn[i+1])])
			elif(stringIn[i].isdigit() and (stringIn[i-1]=='a' or stringIn[i-1]=='d')):
				step0.append(m[int(stringIn[i])])

		for i in step0:					#grouping the numbers
			a=count1(i)					#with the respective number of 1's
			step1[a].append(i)

		step1t=deepcopy(step1)			#grouping for step1
		for i in range(3):
			for j in step1[i]:
				for k in step1[i+1]:
					if(bitcount(j,k)==1):
						step2[str(i)+str(i+1)].append(bitchange(j,k))
						if j in step1t[i]:
							step1t[i].remove(j)
						if k in step1t[i+1]:
							step1t[i+1].remove(k)
		step2t=deepcopy(step2)
		for i in range(2):					#grouping for step2
			for j in step2[str(i)+str(i+1)]:
				for k in step2[str(i+1)+str(i+2)]:
					if(bitcount(j,k))==1:
						step3[i].append(bitchange(j,k))
						if j in step2t[str(i)+str(i+1)]:
							step2t[str(i)+str(i+1)].remove(j)
						if k in step2t[str(i+1)+str(i+2)]:
							step2t[str(i+1)+str(i+2)].remove(k)

		step3t=deepcopy(step3)

		for i in range(1):				#grouping for step1
			for j in step3[i]:
				for k in step3[i+1]:
					if(bitcount(j,k)==1):
						step4[i].append(bitchange(j,k))
						if j in step3t[i]:
							step3t[i].remove(j)
						if k in step3t[i+1]:
							step3t[i+1].remove(k) 

		'''Grouping all the minterms in an array'''
		for i in step1t.keys():
			for j in step1t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step2t.keys():
			for j in step2t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step3t.keys():
			for j in step3t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step4.keys():
			for j in step4[i]:
				if(not j in allthemin):
					allthemin.append(j)
		'''Generating prime implicants'''
		prime={}
		for i in step0:
			for j in allthemin:
				flag=0
				for k in range(len(j)):
					if(j[k]!=i[k] and j[k]!='_'):
						flag=1
				if(flag==0):
					if(n[i] in prime.keys()):
						prime[n[i]].append(j)
					else:
						prime[n[i]]=[j]

		'''Generating essential prime implicants'''				
		epi=[]
		check={}
		for i in step0:
			if(stringIn[stringIn.find(str(n[i]))-1]=='a'):
				check[n[i]]=0
		for i in prime.keys():
			if(len(prime[i])==1 and i in check.keys()):
				epi.append(prime[i][0])
				check[i]=1
		for i in epi:
			for j in prime.keys():
				if(i in prime[j] and j in check.keys()):
					check[j]=1
		'''Deleting duplicates'''
		fepi=[]
		for i in epi:
			if(not i in fepi):
				fepi.append(i)
		if(len(step0)==8):
			stringOut='1'
		elif(len(step0)==0):
			stringOut='0'
		else:
			stringOut=givefinalans3(fepi)

	elif(numVar==2):
		m={0:'00',1:'01',2:'10',3:'11'}
		n={'00':0,'01':1,'10':2,'11':3}
		step0=[]
		step1={0:[],1:[],2:[]}
		step2={'01':[],'12':[]}
		step3={0:[]}
		allthemin=[]

		for i in range(len(stringIn)):
			if(stringIn[i].isdigit() and stringIn[i+1].isdigit()):
				step0.append(m[int(stringIn[i]+stringIn[i+1])])
			elif(stringIn[i].isdigit() and (stringIn[i-1]=='a' or stringIn[i-1]=='d')):
				step0.append(m[int(stringIn[i])])

		for i in step0:					#grouping the numbers
			a=count1(i)					#with the respective number of 1's
			step1[a].append(i)

		step1t=deepcopy(step1)			#grouping for step1
		for i in range(2):
			for j in step1[i]:
				for k in step1[i+1]:
					if(bitcount(j,k)==1):
						step2[str(i)+str(i+1)].append(bitchange(j,k))
						if j in step1t[i]:
							step1t[i].remove(j)
						if k in step1t[i+1]:
							step1t[i+1].remove(k)
				step2t=deepcopy(step2)
		for i in range(1):				#grouping for step2
			for j in step2[str(i)+str(i+1)]:
				for k in step2[str(i+1)+str(i+2)]:
					if(bitcount(j,k))==1:
						step3[i].append(bitchange(j,k))
						if j in step2t[str(i)+str(i+1)]:
							step2t[str(i)+str(i+1)].remove(j)
						if k in step2t[str(i+1)+str(i+2)]:
							step2t[str(i+1)+str(i+2)].remove(k)

		'''grouping all the minterms into an array'''					
		for i in step1t.keys():
			for j in step1t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step2t.keys():
			for j in step2t[i]:
				if(not j in allthemin):
					allthemin.append(j)
		for i in step3.keys():
			for j in step3[i]:
				if(not j in allthemin):
					allthemin.append(j)
		'''Generating prime implicants'''			
		prime={}
		for i in step0:
			for j in allthemin:
				flag=0
				for k in range(len(j)):
					if(j[k]!=i[k] and j[k]!='_'):
						flag=1
				if(flag==0):
					if(n[i] in prime.keys()):
						prime[n[i]].append(j)
					else:
						prime[n[i]]=[j]

		'''Generating essential prime implicants'''
		epi=[]
		check={}
		for i in step0:
			if(stringIn[stringIn.find(str(n[i]))-1]=='a'):
				check[n[i]]=0
		for i in prime.keys():
			if(len(prime[i])==1 and i in check.keys()):
				epi.append(prime[i][0])
				check[i]=1
		for i in epi:
			for j in prime.keys():
				if(i in prime[j] and j in check.keys()):
					check[j]=1
		'''Deleting duplicates'''
		fepi=[]
		for i in epi:
			if(not i in fepi):
				fepi.append(i)
		if(len(step0)==4):
			stringOut='1'
		elif(len(step0)==0):
			stringOut='0'
		else:
			stringOut=givefinalans2(fepi)

	elif(numVar==1):
		dig=0
		for i in stringIn:
			if(i.isdigit()):
				dig+=1
		if(dig==0):
			stringOut='0'
		elif(stringIn=='(a1)'):
			stringOut='z'
		else:
			stringOut="z'"

	return stringOut
