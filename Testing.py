import subprocess
commit_message = "link update"
token = "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"

subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git', 'push', 'https://{}@github.com/kushaln3/vscodelink.git'.format(token)])