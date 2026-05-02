LANGS := en uk ru it
DOMAIN := this_project
POT := transl.pot

PYFILES := $(shell find . -name "*.py")

.PHONY: pot
pot:
	echo "start searching translations"
	xgettext -o $(POT) -d $(DOMAIN) $(PYFILES)
	echo "finish searching translations"

.PHONY: lang-structure
lang-structure:
	@echo 'Creating locale structure...'
	@for lang in $(LANGS); do \
		mkdir -p locale/$$lang/LC_MESSAGES; \
	done

.PHONY: lang-po
lang-po: lang-structure pot
	@for lang in $(LANGS); do \
		if [ ! -f locale/$$lang/LC_MESSAGES/$(DOMAIN).po ]; then \
			msginit --no-translator -i $(POT) -o locale/$$lang/LC_MESSAGES/$(DOMAIN).po -l $$lang; \
		else \
			echo "locale/$$lang/LC_MESSAGES/$(DOMAIN).po already exists"; \
		fi \
	done

.PHONY: lang-mo
lang-mo:
	@for lang in $(LANGS); do \
		msgfmt locale/$$lang/LC_MESSAGES/$(DOMAIN).po -o locale/$$lang/LC_MESSAGES/$(DOMAIN).mo; \
	done

.PHONY: merge-po
merge-po: pot
	@for lang in $(LANGS); do \
		msgmerge --update locale/$$lang/LC_MESSAGES/$(DOMAIN).po $(POT); \
	done