#!/bin/sh
######################################################################
# $Revision$, $Date$
######################################################################
# This scripts scans devs.mak and contrib.mak provided with
# Ghostsctipt and prints list of devices which aren't present in
# master Makefile.
# Expects parameters: name (without path!) of makefile to scan and
# additional list of drivers that won't be built.
# 
# Authors:
#   Michal Kochanowicz <mkochano@pld.org.pl>
#   Sebastian Zagrodzki <zagrodzki@pld.org.pl>
######################################################################

# MAKENAME is a name of makefile to scan
MAKENAME="$1"
shift

# BLACKLIST contains list of drivers which should *not* be activated.
BLACKLIST="$@"
BLACKLIST="$BLACKLIST ali atiw cirr tseng tvga" # MSDOS - direct hw access.
BLACKLIST="$BLACKLIST vesa s3vga"
BLACKLIST="$BLACKLIST herc ega vga svga16 pe"
BLACKLIST="$BLACKLIST att3b1"			# Console - who needs it?!
BLACKLIST="$BLACKLIST sonyfb"			# Sony Frame Buffer device.
BLACKLIST="$BLACKLIST nwp533"			# Sony NWP-533.
BLACKLIST="$BLACKLIST sunview sunhmono"		# Sun-specific.
BLACKLIST="$BLACKLIST sparc"			# Sparc printer - no headers.
BLACKLIST="$BLACKLIST omni"			# omni - no source in 7.00
# BLACKLIST="$BLACKLIST cdj880"			# There is no driver in *.c?!

MAKEFILE="src/unix-gcc.mak"

is_on_blacklist() {
	DEVNAME=`echo $1 | sed -e 's/$(DD)//'`
	for X in $BLACKLIST; do
		if [ "$X.dev" = "$DEVNAME" ]; then return 1; fi
	done
	return 0
}

scan_file() {
	awk 'BEGIN { FS="[: ]+" } /^\$\(DD\).*:/ { print $1 }' \
		< $1 \
		| while read DEV; do
			is_on_blacklist $DEV || continue
			# grep -q $DEV $MAKEFILE, but who needs grep?! ;)
			awk -v DEV="$DEV" '/^DEVICE_DEVS/ { if(index($0, DEV) > 0) exit 1 }' < $MAKEFILE && echo -n "$DEV "
		done
}

scan_file "src/$MAKENAME"
