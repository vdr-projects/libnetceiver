#ifndef __NETCV_LOGGING_H__
#define __NETCV_LOGGING_H__

/* debug option */
#define NETCV_DEBUG_BIT_PIDS	 	0x01
#define NETCV_DEBUG_BIT_recv_ts_func_NO_LOGRATELIMIT 0x02  // disable rate limiter Mcli::recv_ts_func

// NOTE: Do not use this global variable for your own logging bits!
//       This is exclusive for communication with this library!
extern int netcv_debugmask;

/* Log skip option */
#define NETCV_LOGSKIP_BIT_recv_ts_func_pid_Data	0x01	// skip log of issues with Data pids (16-18) like Mcli::recv_ts_func: Discontinuity on receiver 0x559f735c7e00 for pid 18: 5->7 at pos 0/7

// NOTE: Do not use this global variable for your own logging bits!
//       This is exclusive for communication with this library!
extern int netcv_logskipmask;

#endif
