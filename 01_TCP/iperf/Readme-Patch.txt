### Introduction ###

This iperf patch enables us to view the tcp-info data out of an iperf connection.
The data is given in csv format. The first line shows all field-names.

This patch was created with version 2.0.5 of iperf. 
It only changes client code, so this version can run against an unpatched server.

Unless there are no huge changes in the code, it should work also with newer versions.

This patch adds two new command-line parameters:

-Q, --tcp-info           write tcp-info data to stdout
    --tcp-info=filename  write tcp-info data to file/pipe

-Y, --tcp-info-time #    time in milliseconds of update (default 500)

### Example ###
A typical run looks like this:
Terminal 1: iperf -s 
Terminal 2: iperf -c localhost -i 1 --tcp-info=out.csv --tcp-info-time=100

The -i switch prints bandwith reports every second.

Interesting fields in the tcpi csv output are:
	tcpi_snd_ssthresh
	tcpi_snd_cwnd
	tcpi_unacked
	tcpi_retransmits


### How to compile ###

The patched version is located in iperf-2.0.5-patched. 
But you can also use the official source and patch it 
with the "iperf-TcpInfo_2.0.5.patch" file.

1) first get the "original" iperf-2.0.5.tar.gz
2) extract it 
   -> tar xvf iperf-2.0.5.tar.gz

3) get the patch and place it in the new directory iperf-2.0.5

4) move to the iperf directory
   -> cd iperf-2.0.5

5) now patch with the following command
   -> patch -p1 -i iperf-TcpInfo_2.0.5.patch

6) compile iperf
   -> ./configure
   -> make

7) the binary can be found in folder "src" named "iperf" 
   -> cd src
   -> ./iperf

### How to run with pipes ###

1) first run a server
  -> iperf -s

2) in a new terminal, create a pipe
  -> mkfifo testpipe

3) start the client
  -> iperf -c localhost --tcp-info=testpipe --tcp-info-time=100
  Alternative (parameters must be given without whitespaces)
  -> iperf -c localhost -Qtestpipe -Y100

4) in a new terminal, read the pipe
  -> cat testpipe


### Plotting ###

The data can be plottet e.g. with the "Live Graph" tool: http://www.live-graph.org/

