LibNetCeiver
============

LibNetCeiver provides a client side implementation of the NetCeiver protocol needed to utilize the NetCeiver hardware. It also includes basic NetCeiver maintenance tools needed to update firmware, change configuration or get status information.

Project's homepage:
https://github.com/vdr-projects/libnetceiver

Copyright (C) 2007-2010 by BayCom GmbH <info@baycom.de>

Extensions by contributors  
Copyright (C) 2020-2022 by Peter Bieringer <pb@bieringer.de>  
Copyright (C) 2013-2015 by hsteinhaus  
Copyright (C) 2014      by mhorwath  
Copyright (C) 2013      by Hoppaz  
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
