Name: gnome-globalmenu
Version: 0.7.10
Release: %mkrel 2
Summary: A globally-shared menu bar of all applications launched in desktop session

Group: Graphical desktop/GNOME
License: GPL
URL: http://code.google.com/p/gnome2-globalmenu/
Source0: http://gnome2-globalmenu.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0: gnome-globalmenu-0.7.9-fix-link.patch
Patch1: gnome-globalmenu-0.7.9-xfce-dir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: pkgconfig, gettext, scrollkeeper, intltool
BuildRequires: perl-XML-Parser, gnome-doc-utils
BuildRequires: libgnomeui2-devel
BuildRequires: gnome-panel-devel
BuildRequires: libwnck-devel
BuildRequires: libvala-devel
BuildRequires: libgnome-menu-devel
BuildRequires: libnotify-devel
BuildRequires: xfce4-panel-devel

%description
Global Menu is the globally-shared menu bar of all applications launched in
your desktop session. This project introduces document-oriented concepts into
GNOME, and improves GNOME's respect for Fitts's law. Most GTK applications work
just fine with Global Menu.

%package devel
Summary: Headers and libraries for development with gnome-globalmenu
Group: Development/GNOME and GTK+
Requires: %{name} = %{version}
Conflicts: %{name} < 0.7.10-2

%description devel
This package provides the headers and libraries required for development of
gnome-globalmenu.

%package xfce4
Summary: Applet and library for using global menu in XFCE
Group: Development/GNOME and GTK+
Requires: %name = %version

%description xfce4
Global Menu is the globally-shared menu bar of all applications launched in
your desktop session. This project introduces document-oriented concepts into
GNOME, and improves GNOME's respect for Fitts's law. Most GTK applications work
just fine with Global Menu.

This package adds xfce4 support for this functionality.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --disable-tests
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README README.GNOME README.LEGACY
%_bindir/globalmenu-settings
%_sysconfdir/gconf/schemas/gnome-globalmenu.schemas
%{_libexecdir}/GlobalMenu.PanelApplet
%{_libdir}/bonobo/servers/*
%{_libdir}/gtk-2.0/modules/libglobalmenu*.so
%{_libdir}/libglobalmenu-server.so.*
%{_mandir}/man1/*
%{_datadir}/pixmaps/globalmenu.png

%files xfce4
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README.XFCE
%{_libexecdir}/xfce4/panel-plugins/GlobalMenu.XFCEPlugin
%{_datadir}/xfce4/panel-plugins/GlobalMenu_XFCEPlugin.desktop
%{_datadir}/pixmaps/globalmenu-xfce.png

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libglobalmenu-server.so
%{_libdir}/libglobalmenu-server.la
%{_libdir}/pkgconfig/globalmenu-server.pc
%{_libdir}/gtk-2.0/modules/libglobalmenu-gnome-panel.la
%{_libdir}/gtk-2.0/modules/libglobalmenu-plugin.la
