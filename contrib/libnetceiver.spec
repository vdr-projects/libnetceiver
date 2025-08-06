# Build instructions
# rpmbuild -bb --undefine=_disable_source_fetch libnetceiver.spec

%define ver	0.0.8
%define rel	1

Name:           libnetceiver
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Client side implementation for the NetCeiver hardware for VDR

License:        LGPLv2+
URL:            https://github.com/vdr-projects/libnetceiver
Source0:        https://github.com/vdr-projects/libnetceiver/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel

Requires:       libxml2
Requires:       tnftp


%description
LibNetCeiver provides a client side implementation of the
NetCeiver protocol needed to utilize the NetCeiver hardware.
It also includes basic NetCeiver maintenance tools needed to
update firmware, change configuration or get status information.


%package devel
Summary:        C header files for DVB multicast stream client 
Requires:	libnetceiver

%description devel
C header files for LibNetCeiver


%package static
Summary:        Static library for DVB multicast stream client
Requires:	libnetceiver

%description static
Static library for DVB multicast stream client


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


%post
%ldconfig_post


%postun
%ldconfig_postun


%files
%license COPYING
%doc README.md HISTORY
%{_bindir}/*
%{_libdir}/*.so*


%files devel
%{_includedir}/libnetceiver
%{_libdir}/pkgconfig/*


%files static
%{_libdir}/*.a


%changelog
* Thu Jul 31 2025 Peter Bieringer <pb@bieringer.de> - 0.0.8-1
- Add subpackage 'static'

* Tue Jun 20 2023 Peter Bieringer <pb@bieringer.de> - 0.0.7-5
- Add requirement for 'tnftp'

* Fri Jun 02 2023 Peter Bieringer <pb@bieringer.de> - 0.0.6-4
- Add missing dist to release

* Thu Jun 01 2023 Peter Bieringer <pb@bieringer.de> - 0.0.6-3
- Require libnetceiver for libnetceiver-devel

* Wed May 31 2023 Peter Bieringer <pb@bieringer.de> - 0.0.6-2
- Call ldconfig on post/postun

* Wed May 31 2023 Peter Bieringer <pb@bieringer.de> - 0.0.6-1
- Initial release based on vdr-mcli.spec 0.9.7-4
