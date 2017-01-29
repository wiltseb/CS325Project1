The source file for the project, project1.py, is a Python 2.7.5-compatible 
script that can be run without any arguments passed to it. It was tested on
the engr server (FLIP) multiple times.

The project1.py file is setup to run the four different max subarray algorithms 
with input from 'MSS_Problems.txt' to check that they all are correctand with 
internal, semi-randomly generated arrays (with values between -1000 and 1000) of
varying sizes specified near the end of the script. The default output for these
is set to 'MSS_Results.txt' for the correctness of the algorithms and to stdout 
for the timing data from the randomly generated arrays.

When wanting to use different input to test that the algorithms are correct,
please change the argument passed in to createOutputFile or name the new input
file 'MSS_Problems.txt'. This file must be in the same formate as the original
'MSS_Problems.txt' file provided for the project.

By default, the program runs getExperimentalData for each of the functions.
This can take a few minutes for each of the algorithms, so it may be advisable
to comment these out or only do one of the functions at a time.
 
