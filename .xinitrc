sxhkd &
feh --bg-center /home/niklas/wall/sorhelgoland.png 
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources
xrandr --output DP-4 --mode 1920x1080 --rate 60.00 --left-of HDMI-0
/etc/X11/xinit/xinitrc.d/50-systemd-user.sh
picom &
/home/niklas/scripts/polybar.sh & 
pcloud &
gllock &
exec bspwm
