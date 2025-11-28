
msSrc := $(abspath $(lastword $(MAKEFILE_LIST))/../..)
msInst ?= $(abspath ${msSrc}/../..)


srcs =  globals.h  InputFile.h   SiRun.cpp   SiRun.h   typses.h  profilers.h

msCXX ?= g++

all:
	@echo linking * to ${msInst}/include/
	@(for src in ${srcs} ; do  ln -s ${msSrc}/include/$$src  ${msInst}/include/ 2>/dev/null;  done) || true


test:
	echo ${msCXX}
	${msCXX} -O2 -std=c++23 test_input.cpp -o test_input.out
	./test_input.out
	${msCXX} -O2 -std=c++23 test_sirun.cpp SiRun.cpp -o test_sirun.out
	./test_sirun.out -i "_sh_ ls -lh *.out" # show binary file sizes
	rm ./test_*.out

clean: ; @rm -f ./test
