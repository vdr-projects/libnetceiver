#Comment this out to disable debugging output
#DEBUG=1
#VERBOSE_MCLI=1
#WIN32=1
#API_SOCK=1
#VERBOSE=1
#BACKTRACE=1

VERMAJOR = 1
VERMINOR = 0
VERPATCH = 0

NAME = libnetceiver

BASENAME = $(NAME).so
BASENAME_STATIC = $(NAME).a

LIBNAME = $(BASENAME).$(VERMAJOR).$(VERMINOR).$(VERPATCH)
LIBNAME_STATIC = $(BASENAME_STATIC)

HEADERS = headers.h defs.h version.h list.h satlists.h mcast.h recv_ccpp.h recv_tv.h tools.h interfaces.h mld.h api_server.h tca_handler.h tra_handler.h mld_reporter.h ciparser.h ci_handler.h mmi_handler.h logging.h

ifdef RBMINI
  ARMEL=1
endif

ARCH ?= $(shell $(CC) -dumpmachine)
APPLE_DARWIN = $(shell echo $(ARCH) | grep -q 'apple-darwin' && echo "1" || echo "0")
CYGWIN = $(shell echo $(ARCH) | grep -q 'cygwin' && echo "1" || echo "0")
MIPSEL = $(shell echo $(ARCH) | grep -q 'mipsel' && echo "1" || echo "0")

DEFS=-DCLIENT -DLIBRARY -D_REENTRANT -D_GNU_SOURCE

ifdef PLUGIN_NAME
  DEFS:= $(DEFS) -DPLUGIN_NAME=\"$(PLUGIN_NAME)\"
endif

ifeq ($(CYGWIN), 1)
WIN32=1
else
API_SOCK=1
endif

ifeq ($(APPLE_DARWIN), 1)
DEFS:=$(DEFS) -I../common/darwin/include/ -DAPPLE
APPLE=1
endif

include ../Make.config

XML_INC ?= $(shell xml2-config --cflags)
XML_LIB ?= $(shell xml2-config --libs)

ifdef ARMEL
  CROSS = arm-linux-gnueabi-
else
ifeq ($(MIPSEL),1)
DEFS:=$(DEFS) -DMIPSEL
else
LIBRARY_PATH=/usr/lib
endif
endif
ifeq ($(APPLE_DARWIN), 1)
CFLAGS:= $(CFLAGS) -fPIC -fno-common -Wall $(DEFS)
else
CFLAGS:= $(CFLAGS) -fPIC -Wall $(DEFS)
endif

ifdef BACKTRACE
CFLAGS:= $(CFLAGS) -DBACKTRACE -g
endif

ifdef API_SHM
LDFLAGS:= $(LDFLAGS) -lrt
CFLAGS:= $(CFLAGS) -DAPI_SHM
endif
ifdef API_SOCK
CFLAGS:= $(CFLAGS) -DAPI_SOCK
endif

ifdef VERBOSE_MCLI
CFLAGS:= $(CFLAGS) -DDEBUG
DEBUG=1
endif

ifdef WIN32
CFLAGS:= -Iwin32/include $(CFLAGS) -mno-cygwin -fPIC -DWIN32
LDFLAGS:= -Lwin32/lib $(LDFLAGS) -mno-cygwin
LDLIBS:= -lpthreadGC2 -lxml2 -lz -lws2_32 -liphlpapi
else
CFLAGS:= $(CFLAGS) $(XML_INC)
LDFLAGS:=$(LDFLAGS)
LDLIBS:=$(XML_LIB) -lpthread -lz -lm
endif

ifdef DEBUG
LDFLAGS:= $(LDFLAGS) -g -rdynamic
CFLAGS:= $(CFLAGS) -g -O0
else
CFLAGS:= $(CFLAGS) -O3
endif

MCLI = mcli

MCLI_OBJS= mld_common.o mld_client.o mld_reporter.o mcast.o recv_tv.o recv_ccpp.o tools.o tca_handler.o tra_handler.o satlists.o interfaces.o api_server.o ciparser.o ci_handler.o mmi_handler.o logging.o
ifdef WIN32
MCLI_OBJS := $(MCLI_OBJS) inet_pton.o inet_ntop.o inet_aton.o
else
MCLI_OBJS := $(MCLI_OBJS)
endif

all: $(LIBNAME) $(LIBNAME_STATIC)

$(LIBNAME): $(MCLI_OBJS)
	echo "Create dynamic library"
	$(CC) $(LDFLAGS) -shared $(MCLI_OBJS) $(LDLIBS) -Wl,-soname="$(BASENAME).$(VERMAJOR)" -o $@
	ln -sf $(LIBNAME) $(BASENAME)

$(LIBNAME_STATIC): $(MCLI_OBJS)
	echo "Create static library"
	$(AR) rcs $(LIBNAME_STATIC) $(MCLI_OBJS)

.PHONY: libnetceiver.pc
libnetceiver.pc:
	@echo "libdir=$(LIBDIR)" > $@
	@echo "includedir=$(INCDIR)" >> $@
	@echo "" >> $@
	@echo "Name: LibNetCeiver" >> $@
	@echo "Description: NetCeiver Client Library" >> $@
	@echo "Version: 1.0.0" >> $@
	@echo "Requires.private: libxml-2.0" >> $@
	@echo "Libs: -L\$${libdir} -lnetceiver" >> $@
	@echo "Cflags: -I\$${includedir}/libnetceiver" >> $@


api_shm_test.o: api_shm_test.c
	$(CC) -c $(CFLAGS) -DUSE_SHM_API -o $@ $<

api_sock_test.o:api_sock_test.c
	$(CC) -c $(CFLAGS) -DUSE_SOCK_API -o $@ $<

$(MCLI)-shmtest: api_shm_test.o
	$(CC) $(LDFLAGS) -o $@ api_shm_test.o $(LDLIBS) -lrt

$(MCLI)-socktest: api_sock_test.o
	$(CC) $(LDFLAGS) -o $@ api_sock_test.o

clean:
	rm -f *.o *.so* *.a libnetceiver.pc

mingw32:
	rm -rf mingw/*.c mingw/*.h mingw/win32
	cp *.c *.h mingw/
	mkdir mingw/win32
	cp -a win32/lib mingw/win32/
	cp -a win32/include mingw/win32/
	@echo "Created mingw directory - now ready to rumble... (call build.cmd)"

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $<

%.lo: %.c
	$(CC) -c $(CFLAGS) -o $@ $<

install-lib: all
	install -d $(DESTDIR)$(LIBDIR)
	install -m 755 $(LIBNAME) $(DESTDIR)$(LIBDIR)/
	install -m 755 $(LIBNAME_STATIC) $(DESTDIR)$(LIBDIR)/
	( cd $(DESTDIR)$(LIBDIR); ln -sf $(LIBNAME) $(BASENAME).$(VERMAJOR); ln -sf $(LIBNAME) $(BASENAME) )

install-includes:
	install -d $(DESTDIR)$(INCDIR)/libnetceiver/netcv/
	install -m 644 $(HEADERS) $(DESTDIR)$(INCDIR)/libnetceiver/netcv/

install-pc: libnetceiver.pc
	install -d $(DESTDIR)$(PCDIR)
	install -m 644 libnetceiver.pc $(DESTDIR)$(PCDIR)/

install-legacy:
	ln -sf $(LIBNAME) $(DESTDIR)$(LIBDIR)/libmcli.so
	install -d $(DESTDIR)$(INCDIR)/libnetceiver/mcast/
	ln -sf "../netcv" $(DESTDIR)$(INCDIR)/libnetceiver/mcast/client
	ln -sf "../netcv" $(DESTDIR)$(INCDIR)/libnetceiver/mcast/common

install: install-lib install-includes install-pc install-legacy
