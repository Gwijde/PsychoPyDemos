#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Mar 23 17:17:23 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SoundTaskDemo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/gwijde/Library/CloudStorage/OneDrive-UniversityCollegeLondon/Experimental Officer/Teaching_and_Training/PsychoPyDemos/SoundTaskDemo/SoundTaskDemo_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro_routine"
intro_routineClock = core.Clock()
intro_slide = visual.TextStim(win=win, name='intro_slide',
    text='Get ready to start the experiment…',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
press_key = visual.TextStim(win=win, name='press_key',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
tone = sound.Sound('377', secs=0.5, stereo=True, hamming=True,
    name='tone')
tone.setVolume(0.5)

# Initialize components for Routine "outro_routine"
outro_routineClock = core.Clock()
outro_slide = visual.TextStim(win=win, name='outro_slide',
    text='Thanks!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro_routine"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
intro_routineComponents = [intro_slide]
for thisComponent in intro_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_routine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intro_routineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_routineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_slide* updates
    if intro_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_slide.frameNStart = frameN  # exact frame index
        intro_slide.tStart = t  # local t and not account for scr refresh
        intro_slide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_slide, 'tStartRefresh')  # time at next scr refresh
        intro_slide.setAutoDraw(True)
    if intro_slide.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > intro_slide.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            intro_slide.tStop = t  # not accounting for scr refresh
            intro_slide.frameNStop = frameN  # exact frame index
            win.timeOnFlip(intro_slide, 'tStopRefresh')  # time at next scr refresh
            intro_slide.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_routine"-------
for thisComponent in intro_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_slide.started', intro_slide.tStartRefresh)
thisExp.addData('intro_slide.stopped', intro_slide.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials_loop')
thisExp.addLoop(trials_loop)  # add the loop to the experiment
thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
if thisTrials_loop != None:
    for paramName in thisTrials_loop:
        exec('{} = thisTrials_loop[paramName]'.format(paramName))

for thisTrials_loop in trials_loop:
    currentLoop = trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    press_key.setText('Press space when you hear a tone')
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    tone.setSound('377', secs=0.5, hamming=True)
    tone.setVolume(0.5, log=False)
    # keep track of which components have finished
    trialComponents = [press_key, key_resp, tone]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *press_key* updates
        if press_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            press_key.frameNStart = frameN  # exact frame index
            press_key.tStart = t  # local t and not account for scr refresh
            press_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(press_key, 'tStartRefresh')  # time at next scr refresh
            press_key.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        # start/stop tone
        if tone.status == NOT_STARTED and tThisFlip >= sound_start-frameTolerance:
            # keep track of start time/frame for later
            tone.frameNStart = frameN  # exact frame index
            tone.tStart = t  # local t and not account for scr refresh
            tone.tStartRefresh = tThisFlipGlobal  # on global time
            tone.play(when=win)  # sync with win flip
        if tone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tone.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                tone.tStop = t  # not accounting for scr refresh
                tone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tone, 'tStopRefresh')  # time at next scr refresh
                tone.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_loop.addData('press_key.started', press_key.tStartRefresh)
    trials_loop.addData('press_key.stopped', press_key.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_loop.addData('key_resp.rt', key_resp.rt)
    trials_loop.addData('key_resp.started', key_resp.tStartRefresh)
    trials_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    tone.stop()  # ensure sound has stopped at end of routine
    trials_loop.addData('tone.started', tone.tStartRefresh)
    trials_loop.addData('tone.stopped', tone.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_loop'


# ------Prepare to start Routine "outro_routine"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
outro_routineComponents = [outro_slide]
for thisComponent in outro_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outro_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "outro_routine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = outro_routineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outro_routineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *outro_slide* updates
    if outro_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        outro_slide.frameNStart = frameN  # exact frame index
        outro_slide.tStart = t  # local t and not account for scr refresh
        outro_slide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outro_slide, 'tStartRefresh')  # time at next scr refresh
        outro_slide.setAutoDraw(True)
    if outro_slide.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > outro_slide.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            outro_slide.tStop = t  # not accounting for scr refresh
            outro_slide.frameNStop = frameN  # exact frame index
            win.timeOnFlip(outro_slide, 'tStopRefresh')  # time at next scr refresh
            outro_slide.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outro_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "outro_routine"-------
for thisComponent in outro_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('outro_slide.started', outro_slide.tStartRefresh)
thisExp.addData('outro_slide.stopped', outro_slide.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
