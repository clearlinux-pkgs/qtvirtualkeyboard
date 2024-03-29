#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtvirtualkeyboard
Version  : 5.15.2
Release  : 30
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtvirtualkeyboard-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtvirtualkeyboard-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause-Clear GPL-3.0 MIT
Requires: qtvirtualkeyboard-lib = %{version}-%{release}
Requires: qtvirtualkeyboard-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Charts)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
Patch1: qtvirtualkeyboard-stable-branch.patch

%description
Qt Virtual Keyboard
Qt Virtual Keyboard is a virtual keyboard framework that consists of a C++
backend supporting custom input methods as well as a UI frontend implemented
in QML.

%package dev
Summary: dev components for the qtvirtualkeyboard package.
Group: Development
Requires: qtvirtualkeyboard-lib = %{version}-%{release}
Provides: qtvirtualkeyboard-devel = %{version}-%{release}
Requires: qtvirtualkeyboard = %{version}-%{release}

%description dev
dev components for the qtvirtualkeyboard package.


%package examples
Summary: examples components for the qtvirtualkeyboard package.
Group: Default
Requires: qtvirtualkeyboard-dev = %{version}-%{release}

%description examples
examples components for the qtvirtualkeyboard package.


%package lib
Summary: lib components for the qtvirtualkeyboard package.
Group: Libraries
Requires: qtvirtualkeyboard-license = %{version}-%{release}

%description lib
lib components for the qtvirtualkeyboard package.


%package license
Summary: license components for the qtvirtualkeyboard package.
Group: Default

%description license
license components for the qtvirtualkeyboard package.


%prep
%setup -q -n qtvirtualkeyboard-everywhere-src-5.15.2
cd %{_builddir}/qtvirtualkeyboard-everywhere-src-5.15.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1667237451
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/lipi-toolkit/3rdparty/lipi-toolkit/MIT_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/b2e28b76775b72633bc107ef13944285b4427bf8 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/lipi-toolkit/3rdparty/lipi-toolkit/license.txt %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/19cb2d123cdfd3e1e58fd4ebf85cee065bea0cf7 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/openwnn/3rdparty/openwnn/NOTICE %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/0ad70704f3dc3c6cee594f035b21168238e08b85 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/pinyin/3rdparty/pinyin/NOTICE %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/e4842b59eeb67867c51032209565509e0fc589b5 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/tcime/3rdparty/tcime/COPYING %{buildroot}/usr/share/package-licenses/qtvirtualkeyboard/c42470b2f854bca72da8965f9549c431a9475e5a || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/abstractinputpanel_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/appinputpanel_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/appinputpanel_p_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/desktopinputpanel_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/desktopinputselectioncontrol_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/enterkeyaction_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/enterkeyactionattachedtype_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/fallbackinputmethod_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/gesturerecognizer_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/handwritinggesturerecognizer_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/inputmethod_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/inputselectionhandle_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/inputview_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/plaininputmethod_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/platforminputcontext_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/qvirtualkeyboard_staticplugin_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/settings_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/shadowinputcontext_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/shifthandler_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/unipentrace_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/virtualkeyboarddebug_p.h
/usr/include/qt5/QtVirtualKeyboard/5.15.2/QtVirtualKeyboard/private/virtualkeyboardsettings_p.h
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardAbstractInputMethod
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardExtensionPlugin
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardInputContext
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardInputEngine
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardSelectionListModel
/usr/include/qt5/QtVirtualKeyboard/QVirtualKeyboardTrace
/usr/include/qt5/QtVirtualKeyboard/QtVirtualKeyboard
/usr/include/qt5/QtVirtualKeyboard/QtVirtualKeyboardDepends
/usr/include/qt5/QtVirtualKeyboard/QtVirtualKeyboardVersion
/usr/include/qt5/QtVirtualKeyboard/qtvirtualkeyboardversion.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboard_global.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardabstractinputmethod.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardextensionplugin.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardinputcontext.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardinputengine.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardselectionlistmodel.h
/usr/include/qt5/QtVirtualKeyboard/qvirtualkeyboardtrace.h
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboardConfig.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboardConfigVersion.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboard_QtVirtualKeyboardHangulPlugin.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboard_QtVirtualKeyboardOpenWnnPlugin.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboard_QtVirtualKeyboardPinyinPlugin.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboard_QtVirtualKeyboardTCImePlugin.cmake
/usr/lib64/cmake/Qt5VirtualKeyboard/Qt5VirtualKeyboard_QtVirtualKeyboardThaiPlugin.cmake
/usr/lib64/libQt5VirtualKeyboard.prl
/usr/lib64/libQt5VirtualKeyboard.so
/usr/lib64/pkgconfig/Qt5VirtualKeyboard.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_virtualkeyboard.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_virtualkeyboard_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/virtualkeyboard/virtualkeyboard.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5VirtualKeyboard.so.5
/usr/lib64/libQt5VirtualKeyboard.so.5.15
/usr/lib64/libQt5VirtualKeyboard.so.5.15.2
/usr/lib64/qt5/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
/usr/lib64/qt5/plugins/virtualkeyboard/libqtvirtualkeyboard_hangul.so
/usr/lib64/qt5/plugins/virtualkeyboard/libqtvirtualkeyboard_openwnn.so
/usr/lib64/qt5/plugins/virtualkeyboard/libqtvirtualkeyboard_pinyin.so
/usr/lib64/qt5/plugins/virtualkeyboard/libqtvirtualkeyboard_tcime.so
/usr/lib64/qt5/plugins/virtualkeyboard/libqtvirtualkeyboard_thai.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Settings/libqtquickvirtualkeyboardsettingsplugin.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Settings/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Settings/qmldir
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/libqtquickvirtualkeyboardstylesplugin.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/Styles/qmldir
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/libqtquickvirtualkeyboardplugin.so
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/VirtualKeyboard/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtvirtualkeyboard/0ad70704f3dc3c6cee594f035b21168238e08b85
/usr/share/package-licenses/qtvirtualkeyboard/19cb2d123cdfd3e1e58fd4ebf85cee065bea0cf7
/usr/share/package-licenses/qtvirtualkeyboard/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtvirtualkeyboard/b2e28b76775b72633bc107ef13944285b4427bf8
/usr/share/package-licenses/qtvirtualkeyboard/c42470b2f854bca72da8965f9549c431a9475e5a
/usr/share/package-licenses/qtvirtualkeyboard/e4842b59eeb67867c51032209565509e0fc589b5
