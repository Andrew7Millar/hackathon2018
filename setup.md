Conda Installation
==================

We will be using Anaconda to manage the Python environment as it 
allows you to have multiple installations of Python on you machine.

If you do not already have conda on your machine, download and 
install Anaconda from [here](https://www.anaconda.com/download/).

Environment Setup
=================

For the hackathon, we will be using Python 3.6. To setup the 
environment for the hackathon, enter the following in your 
terminal (or at the Anaconda prompt for Windows):

  `conda create -n cis python=3.6 anaconda`
  
Then activate the environment by calling:

  `source activate cis`
  
Verify that the correct version of Python is now being used.

  `python --version`
  
Install ZeroMQ C/C++ Libraries
==============================

The CiS integration framework can use either ZeroMQ or Sys V 
IPC message queues for message passing.

The ZeroMQ library is only strictly required on Windows machines 
which do not have the Sys V IPC libraries installed by default.
Although ZeroMQ is not required on Linux/OSX machines, it is
recommended as the Sys V IPC message queues do not perform as 
well for large messages.

Linux/OSX
---------

Windows
-------


