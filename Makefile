UI_RESOURCES_DIR := ui
UI_BUILD_DIR := src/main/python/nc2dt/gui/generated

UI_RESOURCES := $(wildcard $(UI_RESOURCES_DIR)/*.ui)
UI_OBJECTS := $(patsubst $(UI_RESOURCES_DIR)/%.ui, $(UI_BUILD_DIR)/%.py, $(UI_RESOURCES))

PYTHON := python
UIC := $(PYTHON) -m PyQt5.uic.pyuic

.PHONY: all test

all: $(UI_OBJECTS)

$(UI_BUILD_DIR)/%.py: $(UI_RESOURCES_DIR)/%.ui
	$(UIC) $< -o $@

test:
	$(PYTHON) -m unittest discover -s src/main/python/tests -t src/main/python
