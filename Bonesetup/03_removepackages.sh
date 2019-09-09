#!/bin/bash

# Removes unnecessary packages from the Bone
sudo apt-get remove apache2 avahi-daemon bison colord flex manpages-dev notification-daemon pastebinit
sudo apt-get autoremove

# autoremove will remove the following packages:
# acl adwaita-icon-theme at-spi2-core colord-data dconf-gsettings-backend dconf-service glib-networking glib-networking-common glib-networking-services
# gsettings-desktop-schemas humanity-icon-theme libatk-bridge2.0-0 libatspi2.0-0 libbison-dev libcairo-gobject2 libcapnp-0.5.3 libcolord2 libcolorhug2
# libdconf1 libegl1-mesa libepoxy0 libexif12 libfl-dev libgbm1 libgphoto2-6 libgphoto2-l10n libgphoto2-port12 libgtk-3-0 libgtk-3-bin libgtk-3-common
# libgudev-1.0-0 libgusb2 libieee1284-3 libjson-glib-1.0-0 libjson-glib-1.0-common libmirclient9 libmircommon7 libmircore1 libmirprotobuf3
# libpolkit-agent-1-0 libpolkit-backend-1-0 libpolkit-gobject-1-0 libprotobuf-lite9v5 libproxy1v5 librest-0.7-0 libsane libsane-common libsigsegv2
# libsoup-gnome2.4-1 libsoup2.4-1 libwayland-client0 libwayland-cursor0 libwayland-egl1-mesa libwayland-server0 libxcb-xfixes0 libxkbcommon0 libxtst6
# m4 policykit-1 ssl-cert ubuntu-mono

# Remark: This frees 7703kb (first command) + 66.2mb (2nd command) of disk space