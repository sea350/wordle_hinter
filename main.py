from curses import nl
import json
import time

# with open('words_dictionary.json') as f1:
# 	words = json.load(f1)
# 	five_letter_words = {}
# 	for key in words:
# 		if len(key) == 5:
# 			five_letter_words[key] = 1
# 	f2 = io.open('five_letter_words.json', 'w', encoding='utf-8')
# 	json.dump(five_letter_words,f2)




def main():
	print("Okay u lazy POS let's do this")
	only_five_letters = False
	letters = []
	not_letters = ""

	#get letters that aren't part of the word
	while True:
		print()
		print("Enter all the letters that are NOT in the word as a single block of text (ex: qwertyuiop)")
		not_letters = input().lower()
		if not_letters.isalpha():
			break
		if not_letters == "":
			print("If you havent found any wrong letters then you obviously found the right answer")
			print("aren't you a little smarty pants getting it on you first try")
			for i in range(3):
				time.sleep(4)
				print(".")
			print()
			print("why in the every living FUCK are you still here?????")
		else:
			print("*Trump voice* WRONG. LETTERS ONLY")
		print("we go again")

	#get letters that ARE part of the word
	while not only_five_letters:
		print()
		print("Enter what letters are in your word seperated by a comma (ex: a,b or a)")
		letters = input().split(',')
		if len(letters) == 0:
			print("Seriously? Just put the phucking letters in the script")
			print("we go again")
			continue
		go_again = False
		for letter in letters:
			if len(letter) != 1:
				print("What??? What are you typing into my script right now?")
				print("It's just Letter Comma Letter Comma Letter Comma, how hard is that?!")
				print("we go again")
				go_again = True
				break
			if letter.isdigit():
				print("*sigh*", end="")
				for i in range(3):
					time.sleep(0.5)
					print(".")
				print()
				print("You can't have a number in a word...")
				print("we go again")
				go_again = True
				break
			if not letter.isalpha():
				print("Why? Just ... why? ONLY LETTERS! DO YOU KNOW WHAT LETTERS ARE???")
				print("we go again")
				go_again = True
				break
		if go_again:
			continue
		if len(letters) > 5:
			print("How does a 5 letter word have more than 5 letters?")
			print("no wonder you need a script to solve your puzzles for you")
			print("we go again")
			continue
		only_five_letters = True
		
	print("")
	print("OK don't mess this part up")
	print("I need you to mark the positions that the letters AREN'T in with an x")
	print("Like this _,x,_,_,x this means the letter cannot be the 2nd or 5th letter in the word")
	print("")
	print("OR you can mark where the letter is with an o")
	print("Like this _,_,o,_,_ this means the letter MUST be the 3rd of the word")
	print("you don't need the underscores but you do need the commas")
	letter_map = {}
	for letter in letters:
		is_five_letters = False
		while not is_five_letters:
			print("")
			print("what is the postion information for the letter '" + letter +"':" )
			pos = input().split(',')
			if len(pos) != 5:
				print("YOU FUCKED IT UP, make sure you have 5 and ONLY 5 letter positions")
				print("we go again")
				continue
			correct_letter_found = False
			incorrect_letter_found = False
			for p in pos:
				if p.lower() == "x" or p.lower() == "o" or  p == "":
					correct_letter_found = True
					break
				if len(p) != 1 or not p.isalpha():
					print("What??? What are you typing into my script right now?")
					print("It's just a SINGULAR x or a SINGULAR o at a time and then some commas")
					print("we go again")
					incorrect_letter_found = True
					break
			if not correct_letter_found:
				print("Not an x or an o to be seen")
				print("boy you sure are great at following instructions")
				print("we go again")
				continue
			if incorrect_letter_found:
				continue
			letter_map[letter] = pos
			is_five_letters = True

	print("Ok this is where the magic happens")

	words = json.load(open('five_letter_words.json'))
	possible_words = []
	for word in words:
		continue_word = False
		letter_included = {}
		for letter in letter_map:
			letter_included[letter] = False
		for i in range(5):
			for n_l in not_letters:
				if n_l == word[i]:
					continue_word = True
					break
			if continue_word:
				break
			for letter in letter_map:
				if letter_map[letter][i].lower() == 'x' and letter.lower() == word[i]:
					continue_word = True
					break
				if letter_map[letter][i].lower() == 'o' and letter.lower() != word[i]:
					continue_word = True
					break
				if letter.lower() == word[i]:
					letter_included[letter] = True
			if continue_word:
				break
		if continue_word:
			continue
		for l_i in letter_included:
			if not letter_included[l_i]:
				continue_word = True
				break
		if continue_word:
			continue
		possible_words.append(word)

	print()
	print("alright if i did this right your list of possible words are:")
	for word in possible_words:
		print(word)


main()