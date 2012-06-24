# Base this image on core-image-sato
include recipes-sato/images/core-image-sato.bb

# Inherit sdcard creation bbclass
inherit sdcard-rpi

# Include modules in rootfs
IMAGE_INSTALL += " \
	kernel-modules \
	"
