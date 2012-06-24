require recipes-kernel/linux-libc-headers/linux-libc-headers.inc

PR = "r0"

PROVIDES = "linux-libc-headers"
RPROVIDES_${PN}-dev = "linux-libc-headers-dev"
RPROVIDES_${PN}-dbg = "linux-libc-headers-dbg"

SRCREV = "e3a21fc997669aae744537bf69e123f88a5e69e2"
SRC_URI = "git://github.com/raspberrypi/linux.git;protocol=git"
S = "${WORKDIR}/git"
