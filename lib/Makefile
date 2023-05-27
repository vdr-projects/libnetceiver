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

BASENAME = libnetceiver.so

LIBNAME = $(BASENAME).$(VERMAJOR).$(VERMINOR).$(VERPATCH)

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
CFLAGS:= $(CFLAGS) -fPIC -fno-common -Wall -I../common -I../.. $(DEFS)
else
CFLAGS:= $(CFLAGS) -fPIC -Wall -I../common -I../.. $(DEFS)
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

lib: $(LIBNAME)

$(LIBNAME): $(MCLI_OBJS)
	$(CC) $(LDFLAGS) -shared $(MCLI_OBJS) $(LDLIBS) -Wl,-soname="$(BASENAME).$(VERMAJOR)" -o $@
	ln -sf $(LIBNAME) $(BASENAME)



api_shm_test.o: api_shm_test.c
	$(CC) -c $(CFLAGS) -DUSE_SHM_API -o $@ $<
	
api_sock_test.o:api_sock_test.c
	$(CC) -c $(CFLAGS) -DUSE_SOCK_API -o $@ $<
	
$(MCLI)-shmtest: api_shm_test.o
	$(CC) $(LDFLAGS) -o $@ api_shm_test.o $(LDLIBS) -lrt

$(MCLI)-socktest: api_sock_test.o
	$(CC) $(LDFLAGS) -o $@ api_sock_test.o 
	
install: mcli
	install -p $< /usr/sbin/$<

install-lib: libmcli.la
	libtool --mode=install install $< /usr/local/lib/	

install-shared: mcli-shared
	libtool --mode=install install $< /usr/local/bin

depend: .dependencies
	#makedepend -Y -- $(CFLAGS)  -- *c >/dev/null 2>&1

clean:
	rm -f $(MCLI) $(MCLI)-* *.elf *.gdb *.o *.lo *.la *~ *.so* *.a *.def *.dll *.dylib out.ts .dependencies

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
