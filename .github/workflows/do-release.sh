#!/usr/bin/env bash

ansible-galaxy collection build
ansible-galaxy collection publish vmware-alb-*
