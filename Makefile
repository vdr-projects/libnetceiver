#
# Makefile for libnetceiver and its corresponding tools
#

include Make.config

SOFILE = libnetceiver.so

all: lib tools

.PHONY: tools
tools: lib
	 $(MAKE) -C tools/ all

.PHONY: lib
lib:
	$(MAKE) -C lib/ all

clean:
	$(MAKE) -C lib/ clean
	$(MAKE) -C tools/ clean
