/* 
GazeTrack: Basic demo
-
In this demo, the user's gaze is represented
by a white circle.
-

Before you run this demo, make sure the
Tobii eye-tracker (EyeX, 4C) is connected
to the computer, and that the Tobii software 
is running and calibrated to your eyes.

Finally, make sure the 'TobiiStream.exe' is 
running and displaying gaze data. You can
download this application from:
http://hci.soc.napier.ac.uk/GazeTrack/TobiiStream.zip

by Augusto Esteves
http://hci.soc.napier.ac.uk
https://github.com/AugustoEst/gazetrack
*/

import gazetrack.*;

GazeTrack gazeTrack;

int cnt;
int showFlag = 1;
double[][] data = new double[9999][4];

void setup() 
{
  fullScreen();
  
  // Gaze cursor param.
  noFill();
  stroke(50, 100);
  strokeWeight(4);
  
  gazeTrack = new GazeTrack(this);
  
  // If the TobiiStream.exe asked you to use a 
  // different socket port (e.g., 5656), use this instead:
  // gazeTrack = new GazeTrack(this, "5656");
  
  cnt = 0;
}

void draw() 
{
  background(255);
  
  if (gazeTrack.gazePresent())
  {
    ellipse(gazeTrack.getGazeX(), gazeTrack.getGazeY(), 80, 80);
    
    // Print the tracker's timestamp for the gaze cursor above
    println("Latest gaze data at: " + gazeTrack.getTimestamp());
    
    data[cnt][0] = gazeTrack.getTimestamp();
    data[cnt][1] = gazeTrack.getGazeX();
    data[cnt][2] = gazeTrack.getGazeY();
    
    // showFlag =  
    //            0 show all of 1,3,5 and waiting (10s)      : 60fps x 10s = 600 samples
    //            1 show 'target string'                     : 60fps x  7s = 420 samples     1111
    //            2 key input detected, a.k.a. the end of '2':                 1 samples     222222    with key hit message
    //            3 show question about where did you see?   : 60fps x 10s = 600 samples     33333333
    //            4 key input detected, a.k.a. the end of '4':                 1 samples
    //            5 blank                                    : 60fps x  3s = 180 samples
    // showQuestion = 1 or 0

    data[cnt][3] = showFlag;
    cnt++;
  }
}
