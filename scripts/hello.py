#!/usr/bin/env python3
from dev_aberto import hello
from babel.dates import format_datetime
import datetime
import gettext

if __name__ == '__main__':
    date, name = hello()
    date_locale = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

    gettext.install('cli', localedir='locale') 
    
    print(_('Last commit made on:'), format_datetime(date_locale), _('by'), name)
