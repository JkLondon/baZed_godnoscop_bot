def make_description(text):
	text_arr = text.split()
	if len(text_arr) > 4:
		text_arr = text_arr[:4]
	result = " ".join(text_arr)
	return result + "..."