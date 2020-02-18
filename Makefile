#!/bin/make -f

VERSION = $(shell git describe --tags)

all: config.cfg

config.cfg: config.cfg.template
	sed 's|@CACHEDIR@|/var/cache/koschei|g; s|@DATADIR@|/usr/share/koschei|g; s|@VERSION@|$(VERSION)|g; s|@CONFDIR@|/etc/koschei|g; s|@STATEDIR@|/var/lib/koschei|g' config.cfg.template >$@

.ONESHELL:
.PHONY: all
