afreeze
=======

Freeze ALSA configuration settings.

# Getting Started

afreeze may be installed via PyPi via:

```bash
pip install afreeze[daemon] --user
```

Or afreeze may be installed via git:

```bash
git clone https://github.com/Alexhuszagh/afreeze
cd afreeze
python setup.py install --user
```

Once installed, you can freeze various alsa configuration settings via various commands. For example, to force the audio to stay at 75%, you may use:

```bash
afreeze --command "'Master' 75%"
```

To list all controls available and current content settings, use:

```bash
afreeze --list-controls
afreeze --list-contents
```

afreeze supports custom devices and sound cards. To specify a custom device, use:

```bash
afreeze --device default ...
```

To specify a custom sound card, use:

```bash
afreeze --card 0 ...
```

To enable auto-mute mode (muting speakers when headphones are plugged in), use:

```bash
afreeze --card 0 "'Auto-Mute Mode' Enabled"
```

# Daemon

This script may also be run as a daemon, requiring `python-daemon`. To launch afreeze as a daemon, use:

```bash
afreeze --daemon ...
```

# Running on Startup

To run afreeze on startup for Linux distros running systemd, you can install afreeze globally:

```bash
sudo -H pip install afreeze
```

Then, add the command to `/etc/profile.d/afreeze.sh`. For example, to enable auto-mute mode, use:

```bash
# Remove a PID file that remains from a hard shutdown.
rm -f /tmp/afreeze.pid
afreeze --daemon --card 0 --command "'Auto-Mute Mode' Enabled"
```

# License

This is free and unencumbered software released into the public domain. 

# Contributing

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in afreeze by you, will be unlicensed (free and unencumbered software released into the public domain).
