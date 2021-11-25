sudo systemctl stop serial-getty@ttyS0.service

sudo systemctl disable serial-getty@ttyS0.service

sudo nano /boot/cmdline.txt

#in the line which looks like... dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1
# remove the line: console=serial0,115200
# then save and then reboot...

sudo nano /boot/config.txt
# add the following at end of file: dtoverlay=pi3-miniuart-bt
# the above command has the effect of swapping the serial ports
# e.g. if you do ls /dev | grep serial, serial1 will now point to ttys0 instead
