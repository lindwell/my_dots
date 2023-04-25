# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess, os, asyncio
from libqtile import hook, qtile
from libqtile.dgroups import simple_key_binder

from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

colors = [
    ["#333232", "#333232"],  # 0 background
    ["#cab0a1", "#cab0a1"],  # 1 foreground
    ["#585c69", "#585c69"],  # 2 background lighter
    ["#dd7878", "#dd7878"],  # 3 red
    ["#9f8578", "#9f8578"],  # 4 green
    ["#986c5b", "#986c5b"],  # 5 yellow
    ["#808178", "#808178"],  # 6 blue
    ["#979892", "#979892"],  # 7 magenta
    ["#dd7878", "#dd7878"],  # 8 cyan
    ["#707880", "#707880"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#c79081", "#c79081"],  # 11 orange
    ["#ea999c", "#ea999c"],  # 12 super cyan
    ["#808178", "#808178"],  # 13 super blue
    ["#444343", "#444343"],  # 14 super dark background
]


mod = "mod4"
terminal = "alacritty"
rofi_alt_tab = "rofi -show window -show-icons"
rofi_run = "rofi -show drun"
firefox = "firefox"
global_font = "agave regular Nerd Font Complete Mono"
dmenu_run = "dmenu_run -b -nb '#333232' -sf '#333232' -sb '#cab0a1' -nf '#cab0a1'"


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    #result of horrible attempts to make floating windows tile again
    
    #Key([mod], "space", lazy.toggle_focus_floating(), lazy.warp_cursor_here()),
    #Key([mod], "space", lazy.window.cmd_disable_floating()),
    Key([mod], "space", lazy.window.toggle_floating()),

    Key([mod, "shift"], "m", lazy.layout.maximize(), desc="Maximize window"),
    Key([mod], "m", lazy.layout.normalize(), desc="reset windows for columns"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "d" , lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes normalizes windows for monadtall"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # application shortcuts
    Key([mod], "r", lazy.spawn(rofi_run),
        desc="Spawn a rofi run prompt"),
    Key([mod], "w", lazy.spawn(firefox), desc="run firefox"),
    Key(["mod1"], "Tab", lazy.spawn(rofi_alt_tab), desc="rofi Alt+Tab window switcher"),
    Key([mod], "e", lazy.spawn("nemo"), desc="run nemo"),
    Key([mod, 'control'], 'l', lazy.spawn('gnome-screensaver-command -l')),
    Key([mod, 'control'], 'q', lazy.spawn('gnome-session-quit --logout --no-prompt')),
    Key([mod, 'shift', 'control'], 'q', lazy.spawn('gnome-session-quit --power-off')),
    Key([mod, "shift"], 'd', lazy.spawn(dmenu_run)),

    #toggle fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),

    #change hori/verti(not working)
    Key([mod, "shift"], "b", lazy.hide_show_bar(position='all')),

    #pavucontrol
    Key([mod], "v", lazy.spawn("pavucontrol")),

]


group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = [ "","", "", "󰙯", "", "",]
group_layouts = ["monadtall", "max", "monadtall", "monadtall", "monadtall", "monadtall",]
group_match = ["", "firefox-esr", "", "", "", "",]

groups=[
    Group(name=group_names[0],layout=group_layouts[0].lower(),label=group_labels[0]),
    Group(name=group_names[1],layout=group_layouts[1].lower(),label=group_labels[1],matches=[Match(wm_class=firefox)]),
    Group(name=group_names[2],layout=group_layouts[2].lower(),label=group_labels[2],matches=[Match(wm_class="sublime_text"), Match(wm_class="emacs")]),
    Group(name=group_names[3],layout=group_layouts[3].lower(),label=group_labels[3],matches=[Match(wm_class="discord")]),
    Group(name=group_names[4],layout=group_layouts[4].lower(),label=group_labels[4]),
    Group(name=group_names[5],layout=group_layouts[5].lower(),label=group_labels[5]),
    ]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


groups.extend([
    ScratchPad("music",[DropDown("tunes","alacritty -e ncmpcpp", x=0.18, y=0.005, width=0.6, height=0.6, on_focus_lost_hide=False)]),
    ScratchPad("logout",[DropDown("exitMenu", "alacritty -e logout", x=0.4, y=0.3, width=0.2, height=0.4, on_focus_lost_hide=False)]),
    ScratchPad("dashboard",[DropDown("dashboard", "alacritty -e wtfutil", x=0.25, y=0.2, width=0.5, height=0.6, on_focus_lost_hide=False)]),
    ])
keys.extend([
    Key([mod], "m", lazy.group['music'].dropdown_toggle('tunes')),
    Key([mod, "shift"], "e", lazy.group['logout'].dropdown_toggle('exitMenu')),
    Key([mod], "s", lazy.group['dashboard'].dropdown_toggle('dashboard')),
    ])

dgroups_key_binder = simple_key_binder(mod)

@hook.subscribe.client_new
async def move_spotify(client):
    await asyncio.sleep(0.05)
    if client.name == 'spotify':
        client.togroup(group_names[4])

def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.run([home])

def toggle_focus_floating():                                                                              
    '''Toggle focus between floating window and other windows in group'''
     
    @lazy.function
    def _toggle_focus_floating(qtile):
        group = qtile.current_group
        switch = 'non-float' if qtile.current_window.floating else 'float'
        logger.debug(f'toggle_focus_floating: switch = {switch}\t current_window: {qtile.current_window}')
        logger.debug(f'focus_history: {group.focus_history}')
         
         
        for win in reversed(group.focus_history):
            logger.debug(f'{win}: {win.floating}')
            if switch=='float' and win.floating:
                # win.focus(warp=False)
                group.focus(win)
                return
            if switch=='non-float' and not win.floating:
                # win.focus(warp=False)
                group.focus(win)
                return
    return _toggle_focus_floating

def init_layout_theme():
	return {"margin":		20,
		"border_width":		4,
		"border_focus":		colors[1],
		"border_normal":	colors[2],
		"border_single_width":	3,
        "ratio":    0.65,
		}

layout_theme = init_layout_theme()

layouts = [
    #layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.Tile(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.RatioTile(**layout_theme),
    #layout.MonadThreeCol(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Floating(**layout_theme),
    #layout.Slice(**layout_theme, fallback=layout.Columns()),
    # layout.MonadWide(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=global_font,
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

sep_defaults = dict(
linewidth=2,
padding=6,
foreground=colors[2],
background=colors[0],
)

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
}

def open_launcher():
    qtile.cmd_spawn("rofi -show drun")

def dunst():
    return subprocess.check_output(["./.config/qtile/dunst.sh"]).decode("utf-8").strip()

def toggle_dunst():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --toggle")

def toggle_notif_center():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --notif-center")

def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")

def open_pavu():
    qtile.cmd_spawn("pavucontrol")

screens = [
    Screen(
top=bar.Bar(
            [
                widget.TextBox(
                    text="󰛡",
                    foreground=colors[1],
                    background=colors[0],
                    font="Font Awesome 6 Free Solid",
                    fontsize=30,
                    padding=20,
                    mouse_callbacks={"Button1": open_launcher},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=34,
                    padding=0,
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    fontsize=30,
                    visible_groups=[""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Free Solid",
                    **group_box_settings,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=34,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=40,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[2],
                    background=colors[14],
                    padding=-10,
                    scale=0.40,
                ),
                widget.WindowCount(
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.GenPollText(
                    func=dunst,
                    update_interval=1,
                    foreground=colors[11],
                    background=colors[14],
                    padding=8,
                    mouse_callbacks={
                        "Button1": toggle_dunst,
                        "Button3": toggle_notif_center,
                    },
                ),

                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
 
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=35.4,
                    padding=0,
                ),

                widget.TaskList(
                    icon_size = 0,
                    font = "JetBrainsMono Nerd Font",
                    foreground = colors[1],
                    background = colors[14],
                    borderwidth = 0,
                    border = colors[1],
                    margin = 0,
                    padding = 11,
                    highlight_method = "block",
                    title_width_method = "uniform",
                    urgent_alert_method = "border",
                    urgent_border = colors[3],
                    rounded = True,
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=35.4,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.Systray(
                    icon_size=26,
                    background=colors[0],
                    padding=7,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[8],
                    background=colors[14],
                    font="Font Awesome 6 Free Solid",
                ),
                widget.PulseVolume(
                    foreground=colors[8],
                    background=colors[14],
                    limit_max_volume="True",
                    mouse_callbacks={"Button3": open_pavu},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[7],  # fontsize=38
                    background=colors[14],
                ),
                widget.Battery(
                    battery=0,
                    font="Font Awesome 6 Free Solid",
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                    foreground=colors[7],
                    background=colors[14],
                    padding=5,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[5],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                    format="%a, %b %d",
                    background=colors[14],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[4],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                    format="%I:%M %p",
                    foreground=colors[4],
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=30,
                    padding=0,
                ),
                widget.TextBox(
                    text="⏻",
                    background=colors[0],
                    foreground=colors[13],
                    font="Font Awesome 6 Free Solid",
                    fontsize=30,
                    padding=20,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("power")},
                ),
            ],
            40,
            margin=[20, 30, 0, 30],
            border_width=[10, 10, 10, 10],
            border_color=colors[10],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='4kvideodownloader-bin'),
    Match(wm_class='mpv'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

 
autostart()
