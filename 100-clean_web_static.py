#!/usr/bin/env bash
# Bash script to delete out-of-date archives

number=$1
if [ -z "$number" ]; then
    number=0
fi

if [ $number -eq 0 ]; then
    number=1
fi

cd versions || exit
archives=($(ls -t))
for i in "${archives[@]:$number}"; do
    rm ./"$i"
done

ssh ubuntu@52.87.221.0 << EOF
    cd /data/web_static/releases || exit
    archives=(\$(ls -tr))
    for i in \${archives[@]:0:\${#archives[@]}-$number}; do
        if [[ \$i == web_static_* ]]; then
            rm -rf ./\$i
        fi
    done
EOF

ssh ubuntu@18.209.152.146 << EOF
    cd /data/web_static/releases || exit
    archives=(\$(ls -tr))
    for i in \${archives[@]:0:\${#archives[@]}-$number}; do
        if [[ \$i == web_static_* ]]; then
            rm -rf ./\$i
        fi
    done
EOF

