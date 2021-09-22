

.PHONY: init leaks test siege

all : $(NAME)


test: $(SAMPLE_FILE_TAR)
	tar -tvzf $(SAMPLE_FILE_TAR)

clear:

siege:
	tar -zxvf siege.tar.gz
	cd siege/
	siege localhost:8080

init:
	pip install -r requirements.txt

leaks:
	valgrind ./$(NAME)
