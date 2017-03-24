def turn_red(self, event):
	event.widget["activeforeground"] = "red"

self.button.bind("<Enter>", self.turn_red)