phrase_to_guess = raw_input('enter a word:')

word_length = len(phrase_to_guess)

guess = word_length*'_'
guess_list = list(guess)
allguess = []

j = 6
updated_word = guess

while (j > 0): 
	your_guess = raw_input('enter a letter:')
	if your_guess in allguess:
		print "You already guessed that."
	for i in range(0, word_length):
		if your_guess == phrase_to_guess[i]:
			guess_list[i] = your_guess
	if your_guess not in phrase_to_guess and your_guess not in allguess:
		j = j - 1
	updated_word = ''.join(guess_list)
	allguess.append(your_guess)
	if updated_word == phrase_to_guess:
		print "You guessed the word!"
		break
	print updated_word
	chances_remaining = j
	print chances_remaining
