CC=gcc -std=gnu11 -I/usr/local/include -L/usr/local/lib

OPT=-g
CFLAGS=-Wunused -Wall $(OPT)
MTH=-lm
PNG=-lpng
LIB=$(MTH) $(PNG)
COMMON=imagelib
PROGRAMS=filter
SRCDIR=$(COMMON) $(PROGRAMS)
DEPS=$(foreach i, $(COMMON), $(wildcard code/$(i)/*.h)) Makefile
SRC=$(foreach i, $(SRCDIR), $(wildcard code/$(i)/*.c))
OBJ=$(foreach i, $(SRC), $(patsubst code/%.c, compilation/%.o, $(i)))
OBJDIR=compilation $(foreach i, $(SRCDIR), compilation/$(i))

all: $(OBJDIR) $(PROGRAMS)
	@echo "done compiling"

clean:
	@rm -fv $(PROGRAMS) && rm -rfv compilation && echo "done cleaning"

$(OBJDIR):
	@mkdir $@

.SECONDEXPANSION:

compilation/%.o: code/%.c $$(wildcard code/$$(patsubst compilation/%/,%,$(dir $$@)/*.h)) $(DEPS)
	@$(CC) $(CFLAGS) $< -c -o $@ $(LIB) && echo "compiled '$@'"

$(PROGRAMS): $$(filter compilation/$$@/% $(foreach i, $(COMMON), compilation/$(i)/%), $(OBJ))
	@$(CC) $(CFLAGS) $^ -o $@ $(LIB) && echo "compiled '$@'"
