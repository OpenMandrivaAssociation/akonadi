# (tpg) needed for boost
%define _disable_ld_no_undefined 1

Summary:	An extensible cross-desktop storage service for PIM
Name:		akonadi
Version:	16.04.0
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Networking/WWW
Url:		http://pim.kde.org/akonadi/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libxml2-utils
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(soprano)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	pkgconfig(mariadb)
# (tpg) does not work with sqlite
Requires:	qt5-qtbase-database-plugin-mysql
Requires:	mariadb-common
# (tpg) needed for mysqld
Requires:	mariadb-server
# Needed for mysqlcheck  which is used in akonadi
Requires:	mariadb-client

%description
An extensible cross-desktop storage service for PIM data and meta data
providing concurrent read, write, and query access.

%files
%{_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_datadir}/kf5/akonadi
%{_datadir}/kf5/akonadi_knut_resource
%{_datadir}/akonadi
%{_datadir}/config.kcfg/resourcebase.kcfg
%{_libdir}/qt5/plugins/akonadi/akonadi_test_searchplugin.so

#------------------------------------------------------
%package -n qt5-database-plugin-sqlite3
Summary: Improved Sqlite 3.x support plugin for Qt 5.x
Group: Databases

%description -n qt5-database-plugin-sqlite3
Improved Sqlite 3.x support plugin for Qt 5.x

%files -n qt5-database-plugin-sqlite3
%{_libdir}/qt5/plugins/sqldrivers/libqsqlite3.so

#------------------------------------------------------
%package -n qt5-designer-plugin-akonadiwidgets
Summary: Akonadi Widgets for Qt Designer
Group: Development/KDE and Qt

%description -n qt5-designer-plugin-akonadiwidgets
Akonadi Widgets for Qt Designer

%files -n qt5-designer-plugin-akonadiwidgets
%{_libdir}/qt5/plugins/designer/akonadi5widgets.so


#------------------------------------------------------

%package common
Group:		Networking/WWW
Summary:	Dummy package to override old
Obsoletes:	%{mklibname akonadiprotocolinternals 2}

%description common
Dummy package to override old.

%files common
%doc README
%config %{_sysconfdir}/akonadi.categories

#------------------------------------------------------

%libpackage KF5AkonadiAgentBase 5
%libpackage KF5AkonadiCore 5
%libpackage KF5AkonadiWidgets 5
%libpackage KF5AkonadiXml 5
%libpackage KF5AkonadiPrivate 5

#------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{mklibname KF5AkonadiAgentBase 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiCore 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiWidgets 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiXml 5} = %{EVRD}
Requires:	%{mklibname KF5AkonadiPrivate 5} = %{EVRD}
Requires:	akonadi-common = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Akonadi
%{_libdir}/qt5/mkspecs/modules/qt_Akonadi*.pri
%{_datadir}/dbus-1/interfaces/*.xml

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5 \
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir}

%build
%ninja -C build

%install
%ninja_install -C build
