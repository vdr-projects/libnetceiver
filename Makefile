#
# Makefile for libnetceiver and its corresponding tools
#

include Make.config

all: lib tools

.PHONY: tools
tools: lib
	 $(MAKE) -C tools/ all

.PHONY: lib
lib:
	$(MAKE) -C lib/ all

install:
	$(MAKE) -C lib/ install
	$(MAKE) -C tools/ install

clean:
	$(MAKE) -C lib/ clean
	$(MAKE) -C tools/ clean
