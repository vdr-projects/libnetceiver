#Comment this out to disable debugging output
#DEBUG = 1
API_SOCK=1

ifdef RBMINI
  ARMEL=1
endif

APPLE_DARWIN = $(shell gcc -dumpmachine | grep -q 'apple-darwin' && echo "1" || echo "0")
CYGWIN = $(shell gcc -dumpmachine | grep -q 'cygwin' && echo "1" || echo "0")

DEFINES = -DCLIENT -D_REENTRANT -D_GNU_SOURCE

ifeq ($(CYGWIN), 1)
WIN32=1
else
API_SOCK=1
endif

ifeq ($(APPLE_DARWIN), 1)
INCLUDES += -I../common/darwin/include/
DEFINES  += -DAPPLE
APPLE=1
endif

include ../Make.config

XML_INC ?= $(shell xml2-config --cflags)

ifndef ARMEL
  LIBRARY_PATH = /usr/lib
endif

CFLAGS ?= -Os -Wall -pthread

INCLUDES += $(XML_INC) -I../lib/

LDFLAGS:= -L../lib -lnetceiver -pthread

ifdef API_SHM
LDFLAGS:= $(LDFLAGS) -lrt
CFLAGS:= $(CFLAGS) -DAPI_SHM
endif

ifdef API_SOCK
CFLAGS:= $(CFLAGS) -DAPI_SOCK
endif

ifdef DEBUG
LDFLAGS:= $(LDFLAGS) -g
CFLAGS:= $(CFLAGS) -g -DDEBUG
endif

ifdef WIN32
CFLAGS:= $(CFLAGS) -DWIN32
endif



NETCVDIAG = netcvdiag
NETCVDIAG_OBJS = netcvdiag.o

NETCVUPDATE = netcvupdate
NETCVUPDATE_OBJS = netcvupdate.o

NETCVLOGVIEW = netcvlogview
NETCVLOGVIEW_OBJS = netcvlogview.o


all: $(NETCVDIAG) $(NETCVUPDATE) $(NETCVLOGVIEW)


$(NETCVDIAG): $(NETCVDIAG_OBJS)
	$(CC) $(LDFLAGS) $(NETCVDIAG_OBJS) -o $@
ifndef DEBUG
ifndef WIN32
	strip $(NETCVDIAG)
endif
endif

$(NETCVUPDATE): $(NETCVUPDATE_OBJS)
	$(CC) $(LDFLAGS) $(NETCVUPDATE_OBJS) -o $@
ifndef DEBUG
ifndef WIN32
	strip $(NETCVUPDATE)
endif
endif

$(NETCVLOGVIEW): $(NETCVLOGVIEW_OBJS)
	$(CC) $(LDFLAGS) $(NETCVLOGVIEW_OBJS) -o $@
ifndef DEBUG
ifndef WIN32
	strip $(NETCVLOGVIEW)
endif
endif

install: $(NETCVDIAG) $(NETCVUPDATE) $(NETCVLOGVIEW)
	install -d $(DESTDIR)$(BINDIR)
	install -p $(NETCVDIAG) $(DESTDIR)$(BINDIR)/$(NETCVDIAG)
	install -p $(NETCVUPDATE) $(DESTDIR)$(BINDIR)/$(NETCVUPDATE)
	install -p $(NETCVLOGVIEW) $(DESTDIR)$(BINDIR)/$(NETCVLOGVIEW)

clean:
	rm -f $(NETCVDIAG) $(NETCVUPDATE) $(NETCVLOGVIEW) *.elf *.gdb *.o *~ .dependencies

%.o: %.c
	$(CC) -c $(CFLAGS) $(INCLUDES) $(DEFINES) -o $@ $<
