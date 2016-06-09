# ddBackup — prevent accidental timeboard/screenboard modifications
Ever delete a dashboard accidentally? Or change one and wish you hadn't? We all do. This tool is to help get out of a sticky situation.

## Pre-setup
[Get your Datadog API and APP keys][dd-keys]  

## Setup
In a shell:  
`pip install datadog`  
`export DD_API=<your API key>`  
`export DD_APP=<your APP key>`  
(optionally, add the exports to your `.bashrc` or `.bash_profile`)

## Run
Download all screenboards and timeboards: `python ddBackup.py`  
Restore a particular screenboard/timeboard: `python putBoard.py <board id>`  

## Recurring task
Setup a cronjob to download your boards nightly. Set another cronjob to commit to git. Boom, version-controlled time/screenboards.

## Issues
Saves to local directory  
Barebones 

## More info
DD API: http://docs.datadoghq.com/api/

[dd-keys]: https://app.datadoghq.com/account/settings#api
