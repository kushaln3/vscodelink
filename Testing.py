import subprocess
commit_message = "link update"
token = "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"

subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git', 'push', 'https://{}@github.com/user-name/repo.git'.format(token)])