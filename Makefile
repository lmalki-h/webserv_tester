
SAMPLE_FILE_TAR= 
.PHONY: init leaks

NAME: clear init
	 	
run:

sample: $(SAMPLE_FILE_TAR)
	tar -tvzf $(SAMPLE_FILE_TAR)

clear:


init:
	pip install -r requirements.txt

leaks:
	valgrind ./$(NAME)
