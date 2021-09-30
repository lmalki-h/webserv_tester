

.PHONY: init leaks sample siege

OPTION = ""
all: $(NAME)


sample: 
	tar -zxvf sample/sandbox.tar.gz

siege: $(WEBSERV)
	tar -zxvf siege.tar.gz
	cd siege/
	siege localhost:8080

init:
	pip install -r requirements.txt

leaks:
	valgrind ./$(NAME)
	