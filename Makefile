WGET := $(shell command -v wget2 2> /dev/null)

ifeq ($(WGET),)
WGET := $(shell command -v wget 2> /dev/null)
endif

ifeq ($(WGET),)
$(error either wget or wget2 are required)
endif

http-status-codes.json: http-status-codes.csv
	cat $< | ./to-json.py > $@

http-status-codes.csv:
	$(WGET) -O $@ \
		https://www.iana.org/assignments/http-status-codes/http-status-codes-1.csv
