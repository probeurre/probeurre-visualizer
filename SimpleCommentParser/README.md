
## Output
This is an example output after calling the module with two parameters `probeurre.py` and `probeurre.py`

`{ 'probeurre.py':
   { '1':
      { begin: 1,
        end: 2,
        codeStart: 3,
        content: '!/usr/bin/env python\n-*- coding: utf-8 -*-\n',
        info: [Object],
        code: '"""' },
     '3':
      { begin: 3,
        end: 5,
        codeStart: 6,
        content: 'This file is part of Probeurre.\n',
        info: [Object],
        code: 'from argparse import ArgumentParser' },
     '12':
      { begin: 12,
        end: 12,
        codeStart: 13,
        content: 'Argument parsing\n',
        info: [Object],
        code: 'parser = ArgumentParser(' } },
  'server.py':
   { '1':
      { begin: 1,
        end: 2,
        codeStart: 3,
        content: '!/usr/bin/env python\n-*- coding: utf-8 -*-\n',
        info: [Object],
        code: '"""' },
     '3':
      { begin: 3,
        end: 5,
        codeStart: 6,
        content: 'This file is part of Probeurre.\n',
        info: [Object],
        code: 'from flask import Flask, render_template, request, current_app' },
     '12':
      { begin: 12,
        end: 12,
        codeStart: 14,
        content: 'Routes\n',
        info: [Object],
        code: '@app.route("/")' },
     '36':
      { begin: 36,
        end: 37,
        codeStart: 39,
        content: 'connection = MySQL(db_host, db_user, db_pass, \'uxie\')\nconnection.connect()\n',
        info: [Object],
        code: '    app.run(host=ip, port=port)' } } }`
