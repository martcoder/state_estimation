#!/bin/sh
for v in {1..5}; do awk -F, '{print $3}' A_log$v.data >> A_z-axis_concat.data; done
