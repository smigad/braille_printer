#include <termios.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <iostream>
#include <errno.h>


int main(int argc, char **argv){

    int USB = open( "/dev/ttyACM0", O_RDWR| O_NOCTTY );
    struct termios tty;
struct termios tty_old;
memset (&tty, 0, sizeof tty);

/* Error Handling */
if ( tcgetattr ( USB, &tty ) != 0 ) {
   std::cout << "Error " << errno << " from tcgetattr: " << strerror(errno) << std::endl;
}

/* Save old tty parameters */
tty_old = tty;

/* Set Baud Rate */
cfsetospeed (&tty, (speed_t)B9600);
cfsetispeed (&tty, (speed_t)B9600);

/* Setting other Port Stuff */
tty.c_cflag     &=  ~PARENB;            // Make 8n1
tty.c_cflag     &=  ~CSTOPB;
tty.c_cflag     &=  ~CSIZE;
tty.c_cflag     |=  CS8;

tty.c_cflag     &=  ~CRTSCTS;           // no flow control
tty.c_cc[VMIN]   =  1;                  // read doesn't block
tty.c_cc[VTIME]  =  5;                  // 0.5 seconds read timeout
tty.c_cflag     |=  CREAD | CLOCAL;     // turn on READ & ignore ctrl lines

/* Make raw */
cfmakeraw(&tty);

/* Flush Port, then applies attributes */
tcflush( USB, TCIFLUSH );
if ( tcsetattr ( USB, TCSANOW, &tty ) != 0) {
   std::cout << "Error " << errno << " from tcsetattr" << std::endl;
}

unsigned char cmd[] = "h300\n";
int n_written = 0,
    spot = 0;

do {
    n_written = write( USB, &cmd[spot], 1 );
    spot += n_written;
} while (cmd[spot-1] != '\n' && n_written > 0);






    // int fd = open("/dev/ttyACM0", O_RDWR);
    // if (fd == -1) {
    //   perror("/dev/ttyACM0");
    //   return 1;
    // }
    //
    // struct termios tios;
    // tcgetattr(fd, &tios);
    // // disable flow control and all that, and ignore break and parity errors
    // tios.c_iflag = IGNBRK | IGNPAR;
    // tios.c_oflag = 0;
    // tios.c_lflag = 0;
    // cfsetspeed(&tios, B9600);
    // tcsetattr(fd, TCSAFLUSH, &tios);
    //
    // // the serial port has a brief glitch once we turn it on which generates a
    // // start bit; sleep for 1ms to let it settle
    // usleep(200000);
    //
    // // output to serial port
    // char msg[] = "h300";
    // write(fd, msg, strlen(msg));



    return 0;
}
