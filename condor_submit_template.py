#!/usr/bin/env python
# encoding: utf-8
"""
condor_submit_template.py

Created by Daniel O'Donovan on 2011-02-06.
Copyright (c) 2011 Harvard University. All rights reserved.

This is a simple file that holds and produces a template of 
a submission script for condor.
"""

import string

template = """### Autogenerated Submission Script - CondorJob
### Daniel O'Donovan 2011-02-06 -> "SuperBowl Sunday" !!!
# must include "./" if script is local, not from PATH
Executable              = ${executable}

# Run time in seconds
Timeout                 = ${timeout}
X509userproxy           = ${x509userproxy}
# affects ordering relative to other jobs.  Lower is better
Priority                = ${priority}

# Options: Always, Error, Never, Complete
Notification            = ${notification}
# Uncomment and complete Notify_User if Notification != Never
Notify_User             = ${notify_user}

Universe                = ${universe}
Should_transfer_files   = ${should_transfer_files}
When_to_transfer_output = ${when_to_transfer_output}
Periodic_remove         = ${periodic_remove}
Requirements            = ${requirements}

Arguments               = ${arguments}

Output                  = ${output}
Error                   = ${error}
Log                     = ${log}

initialdir              = ${initialdir}

# these files are identical for each run
Transfer_input_files    = ${transfer_input_files}

# unique results files to be returned
Transfer_output_files   = ${transfer_output_files}

# Any additional non-templated arguments to go here
${other}

Queue
"""

def createSubmitScript( job ):

  submitTemplate = string.Template( template )

  # add any extra arguments that aren't in the template
  otherString = '\n'
  if job.c_Other:
    for key in job.c_Other.keys():
      otherString += '%s = %s' % key, job.c_Other[key]

  submitString = submitTemplate.safe_substitute( 
    executable      = job.c_Executable,
    timeout         = job.c_Timeout,
    x509userproxy   = job.c_X509userproxy,
    priority        = job.c_Priority,
    notification    = job.c_Notification,
    notify_user     = job.c_Notify_User,
    universe        = job.c_Universe,
    should_transfer_files   = job.c_Should_transfer_files,
    when_to_transfer_output = job.c_When_to_transfer_output,
    periodic_remove = job.c_Periodic_remove,
    requirements    = job.c_Requirements,
    arguments       = ' '.join( job.c_Arguments ),
    output          = job.c_Output,
    error           = job.c_Error,
    log             = job.c_Log,
    initialdir      = job.c_initialdir,
    transfer_input_files    = ', '.join(job.c_Transfer_input_files),
    transfer_output_files   = ', '.join(job.c_Transfer_output_files),
    other           = otherString, )

  return submitString

























