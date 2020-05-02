pids=$(xdotool search --class "gvim")
for pid in $pids; do
    name=$(xdotool getwindowname $pid)
    if [[ $name == *"TODO"* ]]; then
        #Do what you want, $pid is your sought for PID,
        #matching both class gvim and TODO in title
    fi
done
