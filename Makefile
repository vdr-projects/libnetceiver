#
# Makefile for libnetceiver and its corresponding tools
#

include Make.config

SOFILE = libnetceiver.so

all: lib tools

tools: lib
	 $(MAKE) -C tool/ all

lib:
	$(MAKE) -C client/ lib

clean:
	$(MAKE) -C client/ clean
	$(MAKE) -C tool/ clean
