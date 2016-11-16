#!/bin/bash
subscription-manager list --available
subscription-manager repos --enable=rhel-7-server-extras-rpms
subscription-manager repos --enable=rhel-7-server-optional-rpms
yum docker install device-mapper-libs device-mapper-event-libs
systemctl start docker.service
systemctl enable docker.service
systemctl status docker.service