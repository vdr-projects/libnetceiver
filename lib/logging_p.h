// Private header file! Don't ship this on "make install"!

#ifndef __NETCV_LOGGING_P_H__
#define __NETCV_LOGGING_P_H__

/* debug option */
#define DEBUG_MASK(bit, code)	if ((netcv_debugmask & bit) != 0) { code };

/* Log skip option */
#define LOGSKIP_MASK(bit, code)	if ((netcv_logskipmask & bit) == 0) { code };

#endif
