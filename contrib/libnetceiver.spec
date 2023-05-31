# Build instructions
# rpmbuild -bb --undefine=_disable_source_fetch libnetceiver.spec

%define ver	0.0.6
%define rel	1

Name:           libnetceiver
Version:        %{ver}
Release:        %{rel}
Summary:        Client side implementation for the NetCeiver hardware for VDR

License:        LGPLv2+
URL:            https://github.com/vdr-projects/libnetceiver
Source0:        https://github.com/vdr-projects/libnetceiver/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel

Requires:       libxml2


%description
LibNetCeiver provides a client side implementation of the
NetCeiver protocol needed to utilize the NetCeiver hardware.
It also includes basic NetCeiver maintenance tools needed to
update firmware, change configuration or get status information.


%package devel
Summary:        C header files for DVB multicast stream client 


%description devel
C header files for LibNetCeiver


%prep
%setup -q -n %{name}-%{version}


%build
# enforce non-parallel build
%define _smp_mflags -j1

%make_build AUTOCONFIG=0


%install
export LIBDIR=%{_libdir}
export PREFIX=%{_usr}
export PCDIR=%{_libdir}/pkgconfig
%make_install


%files
%license COPYING
%doc README.md HISTORY
%{_bindir}/*
%{_libdir}/*.so*


%files devel
%{_includedir}/libnetceiver
%{_libdir}/pkgconfig/*


%changelog
* Wed May 31 2023 Peter Bieringer <pb@bieringer.de> - 0.0.6-1
- Initial release based on vdr-mcli.spec 0.9.7-4
