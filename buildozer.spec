[app]

title = Car Racing Game
package.name = carracing
package.domain = org.saledra

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,pygame-ce

orientation = portrait

fullscreen = 0
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

android.api = 35
android.minapi = 21
android.ndk = 27c
android.archs = arm64-v8a, armeabi-v7a

android.permissions = android.permission.VIBRATE
