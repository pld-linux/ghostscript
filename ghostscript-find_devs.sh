#!/bin/sh
######################################################################
# $Revision$, $Date$
######################################################################
# This scripts scans devs.mak and contrib.mak provided with
# Ghostsctipt and prints list of devices which aren't present in
# master Makefile.
# Expects two parameters: name (without path!) of makefile to scan and
# system architecture, as returned by rpm's {%_arch} macro (will work
# without second arg).
# Author:
#   Michal Kochanowicz <mkochano@pld.org.pl>
######################################################################

# BLACKLIST contains list of drivers which should *not* be activated.
BLACKLIST="ali atiw cirr tseng tvga vesa s3vga"	# MSDOS - direct hw access.
BLACKLIST="$BLACKLIST lvga256 herc ega vga svga16 pe"
BLACKLIST="$BLACKLIST att3b1"			# Console - who needs it?!
BLACKLIST="$BLACKLIST sonyfb"			# Sony Frame Buffer device.
BLACKLIST="$BLACKLIST nwp533"			# Sony NWP-533.
BLACKLIST="$BLACKLIST sunview sunhmono"		# Sun-specific.
BLACKLIST="$BLACKLIST sparc"			# Sparc printer - no headers.
BLACKLIST="$BLACKLIST cdj880"			# There is no driver in *.c?!

# Architecture-specific blacklists. These variables are included in main
# BLACKLIST if string following underscore matches first argument given
# to the script (usualy value of rpm's %{_arch} macro).
BLACKLIST_sparc="vgalib"
BLACKLIST_sparc64="vgalib"
export BLACKLIST_{sparc,sparc64}
BLACKLIST="$BLACKLIST `sh -c "echo \\$BLACKLIST_$1"`"

MAKEFILE="src/unix-gcc.mak"

is_on_blacklist() {
	DEVNAME=`echo $1 | sed -e 's/$(DD)//'`
	for X in $BLACKLIST; do
		if [ "$X.dev" = "$DEVNAME" ]; then return 1; fi
	done
	return 0
}

scan_file() {
	awk '/^\$\(DD\).*:/ { print $1 }' \
		< $1 \
		| while read DEV; do
			is_on_blacklist $DEV || continue
			# grep -q $DEV $MAKEFILE, but who needs grep?! ;)
			awk -v DEV="$DEV" '/$DEV/ { exit 1 }' < $MAKEFILE && echo -n "$DEV "
		done
}

scan_file "src/$1"
