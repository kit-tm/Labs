# export pox dir
# !
# CHANGE THIS PATH ON YOUR LOCAL SYSTEM
# !
export sdn_lab_dir="/home/robert/repos/telematik/branches/hiwi/Labs/SDN/code/public/pox"

# use this alias to load the mininet scenario for aufgabe0 (sdn lab) 
alias mininet=". $sdn_lab_dir/ext/shell/run_mininet_uebungsblatt1.sh"
# same scenario as above, just a different alias (silent arp)
alias mininet1=". $sdn_lab_dir/ext/shell/run_mininet_uebungsblatt1.sh"
# and this one for aufgabe 2 (multi switch)
alias mininet2=". $sdn_lab_dir/ext/shell/run_mininet_uebungsblatt2.sh"

# controller for aufgabe0 (sdn lab)
alias controller=". $sdn_lab_dir/ext/shell/run_controller.sh"
# controller for aufgabe1 (silent arp)
alias controller1=". $sdn_lab_dir/ext/shell/run_controller_uebungsblatt1.sh"
# controller for aufgabe2 (multi switch)
alias controller2=". $sdn_lab_dir/ext/shell/run_controller_uebungsblatt2.sh"
# the same as controller2 (multi switch) but with default logging disabled
alias controller2.2=". $sdn_lab_dir/ext/shell/run_controller_uebungsblatt2_nolog.sh"
