print("hello everyone")
print("welcome to KBC")
print("very good luck for your game")
print("so lets play the game")
question_list = [
"What is the capital of India?", "how many colours in rainbow?",
"NG mei kaun se course padhaya jaata hai?","how many girls live one room of ng?"
]

options_list = [
["Chandigarh", "Bhopal", "Chennai", "Delhi"],["7","8","6","5"],

["Software Engineering", "Counseling", "Tourism", "Agriculture"],["9","8","5","10"]
]

solution_list = ["d","a","a","d"]

i=0
while i<len(question_list):
	print(i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j]),
		j=j+1
	n=(input("enter option"))
	if n==solution_list[i]:
		print("wow!!,congrats")
	else:
		print("oops!,better luck for the next time")
		break
	i=i+1           
