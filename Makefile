@all:
	python -m main -C -i ~/Documents/sound_lines
	rm -rf ~/Music/*
	python -m main -P -i ~/Documents/sound_lines -o ~/Music
