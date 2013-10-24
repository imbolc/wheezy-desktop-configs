alias nginx-restart='sudo /etc/init.d/nginx configtest && sudo /etc/init.d/nginx restart'
alias upgrade="sudo aptitude update; sudo aptitude upgrade"
alias chmod-standard="find ./ -type d | xargs chmod -v 755 ; find ./ -type f | xargs chmod -v 644"
alias rm-pyc-files="find . -name '*.pyc' -exec rm '{}' ';'"
alias node-prod="NODE_ENV=production node $1"

alias ab1000="sudo ab -n1000 -c10 http://127.0.0.1:8000/"

alias ssh-moon="ssh -t life-moon.pp.ru 'cd ~/life-moon.pp.ru; screen -RD'"
alias ssh-nraw="ssh -t nraw.me 'cd ~/nraw; screen -RD'"

alias weight="vim ~/gems/blog/2013-08-26.yml"
alias blogpost="vim ~/gems/blog/$(date +"%Y-%m-%d").yml"


## System updates

## Colorize the ls output ##
alias ls='ls --color=auto'
 
## Use a long listing format ##
alias ll='ls -la'

## Show hidden files ##
alias l.='ls -d .* --color=auto'

alias df='df -H'
alias du='du -cs * | sort -n'
