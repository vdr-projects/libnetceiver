#
# Makefile for libnetceiver and its corresponding tools
#

include Make.config

SOFILE = libnetceiver.so

all: lib tools

tools: lib
	 $(MAKE) -C tool/ all

lib:
	$(MAKE) libmcli.so

libmcli.a libmcli.so:
	$(MAKE) -C client/ libmcli

clean:
	$(MAKE) -C client/ clean
	$(MAKE) -C tool/ clean
