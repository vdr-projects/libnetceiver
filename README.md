LibNetCeiver
============

LibNetCeiver provides a client side implementation of the NetCeiver protocol needed to utilize the NetCeiver hardware. It also includes basic NetCeiver maintenance tools needed to update firmware, change configuration or get status information.

Project's homepage:
https://github.com/vdr-projects/libnetceiver

Copyright (C) 2007-2010 by BayCom GmbH <info@baycom.de>

Extensions by contributors<br/>
Copyright (C) 2020-2022 by Peter Bieringer <pb@bieringer.de><br/>
Copyright (C) 2013-2015 by hsteinhaus<br/>
Copyright (C) 2014      by mhorwath<br/>
Copyright (C) 2013      by Hoppaz<br/>
Copyright (C) 2023      by Manuel Reimer <manuel.reimer@gmx.de>

Usage notes
-----------

When using the LibNetCeiver includes, please use the "netcv/" include prefix path only. The paths below "mcast" are there for legacy reasons only and will be removed in future versions.

Example:
```
#include "netcv/mcast.h"
```

Contributor notes
-----------------

The NetCeiver is old, outdated hardware and only a few projects cover it. To make it as easy as possible for existing projects with NetCeiver support, please follow these rules:

- Do not break or change existing interfaces. Best case the current interface is stable forever.
- If new interfaces are added, then prefix them with "netcv_" or "NETCV_" to reduce the risk of conflicts with other functions in a project. Example for this is the recently added ["log masking" feature](https://github.com/vdr-projects/libnetceiver/blob/master/lib/logging.h).

NetCeiver Clients based on LibNetCeiver
---------------------------------------

LibNetCeiver itself does not provide a usable client to receive a TV signal from a NetCeiver. But it is used by the following projects to provide NetCeiver client functionality:

- [vdr-plugin-mcli](https://github.com/vdr-projects/vdr-plugin-mcli/)
- [minisatip](https://minisatip.org/) if built with `./configure --with-mcli=/usr/include/libnetceiver`
- [netcv2dvbip](https://github.com/vdr-projects/netcv2dvbip)

Packages
--------

* RPM (Fedora): until included in upstream available via COPR: https://copr.fedorainfracloud.org/coprs/pbiering/vdr_extensions/packages/
* Arch Linux (AUR): [libnetceiver](https://aur.archlinux.org/packages/libnetceiver) and [libnetceiver-tools](https://aur.archlinux.org/packages/libnetceiver-tools)
