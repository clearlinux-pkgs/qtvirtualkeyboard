#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtvirtualkeyboard
Version  : 5.11.0
Release  : 6
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.0/submodules/qtvirtualkeyboard-everywhere-src-5.11.0.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.0/submodules/qtvirtualkeyboard-everywhere-src-5.11.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause-Clear GPL-3.0 MIT
Requires: qtvirtualkeyboard-lib
Requires: qtvirtualkeyboard-data
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras
BuildRequires : qtdeclarative-extras

%description
Qt Virtual Keyboard
Qt Virtual Keyboard is a virtual keyboard framework that consists of a C++
backend supporting custom input methods as well as a UI frontend implemented
in QML.

%package data
Summary: data components for the qtvirtualkeyboard package.
Group: Data

%description data
data components for the qtvirtualkeyboard package.


%package dev
Summary: dev components for the qtvirtualkeyboard package.
Group: Development
Requires: qtvirtualkeyboard-lib
Requires: qtvirtualkeyboard-data
Provides: qtvirtualkeyboard-devel

%description dev
dev components for the qtvirtualkeyboard package.


%package lib
Summary: lib components for the qtvirtualkeyboard package.
Group: Libraries
Requires: qtvirtualkeyboard-data

%description lib
lib components for the qtvirtualkeyboard package.


%prep
%setup -q -n qtvirtualkeyboard-everywhere-src-5.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt5/qtvirtualkeyboard/pinyin/dict_pinyin.dat
/usr/share/qt5/qtvirtualkeyboard/tcime/dict_cangjie.dat
/usr/share/qt5/qtvirtualkeyboard/tcime/dict_phrases.dat
/usr/share/qt5/qtvirtualkeyboard/tcime/dict_zhuyin.dat

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Settings/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Settings/qmldir
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/libqtvirtualkeyboardstylesplugin.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/qmldir
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/qmldir
