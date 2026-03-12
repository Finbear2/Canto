# Canto

Identify every song around you that plays viewable on a Web-UI and on the E-Ink sreen

**This project is in beta and not yet tested on hardware and support is not garunteed!**

<img src="resources/Buddy Holly-Weezer.png" width="500"/>
<img src="resources/Read My Mind-The Killers.png" width="500"/>

## What is it?

Canto is a little device designed to be ran on harware such as a Pi Zero that uses the ShazamIO python package to identify songs around you then with a 2.13 inch waveshare screen connected, it will display a black and white, pixel art version of the album art using the Deezer API and pyxelate

In it's current stage of development, it is fully coded but stl files for a case and any hardware specific features have not been made. Though, using a mock driver I was able to code a screen though the drivers need changing and maybe certain implementations will need fixing.

## Progress Report

So far it is only designed to run on a laptop and identify songs every 60 seconds with a flask web UI. It does not intergrate with the harware at the moment or probally work with it. Also it needs python3.11 because shazamIO hates me. Right now I have spotify open on my phone with a terminal open on one screen looking as it regocnises songs to test out accuracy. You can try it out if you want on a dessktop but... don't

## Vision

A e-ink keyring with an esp 32 for sound monitoring and a proper MEM mic and a sound sensor for the esp 32