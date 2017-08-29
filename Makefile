#
# Author: Samuel M.H. <samuel.mh@gmail.com>
# Description:
#    Make-based utility to manage the project.
#    Idea taken from:
#     - http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

#
### MACROS
#

LIBRARY = 'beebot'

#Don't touch
PATH_PROJECT = $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
PATH_VENV = $(PATH_PROJECT)'/venv3.5'
PATH_LIBRARY = $(PATH_PROJECT)'/'$(LIBRARY)



#
### Autodocumenting thing, don't touch
#
.PHONY: help

.DEFAULT_GOAL := help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


#
### Install the project
#

install-system_packages: ## Install Required system packages (root permissions).
	#TODO: python3, virtualenv, vlc
	@echo "Installing system packages"


install-env: ## Create a running environment (virtualenv).
	@echo "Create the environment in "$(PATH_VENV)
	@virtualenv -p python3.5 $(PATH_VENV)
	@echo "Install requirements"
	@$(PATH_VENV)'/bin/pip' install -r $(PATH_PROJECT)'/deploy/requirements.txt'
	@echo "Create symbolic links"
	# Link to project
	@ln -s $(PATH_PROJECT) $(PATH_VENV)'/'
	# Link code to project library so it is in the PYTHONPATH
	@ln -s $(PATH_LIBRARY) $(PATH_VENV)'/lib/python3.5/site-packages/'
	@echo "Done"


install-bootup: ## Create files to start beebot on bootup  (root permissions).
# TODO:
# install supervisor
#deploy supervisor deploy/beebot.conf



#
### Run different behaviors.
#

run-demo_day: ## Run the demo day
	@$(PATH_VENV)'/bin/python' beebot/beebot-demo_day.py


run-aws_iot: ## Run the Amazon Web Services IoT controller
	@$(PATH_VENV)'/bin/python' beebot/beebot-aws_iot.py
