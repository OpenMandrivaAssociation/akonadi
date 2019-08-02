# (tpg) needed for boost
%define _disable_ld_no_undefined 1

# Use mariadb instead of sqlite
%bcond_with mariadb

Summary:	An extensible cross-desktop storage service for PIM
Name:		akonadi
Version:	19.07.90
Release:	1
Epoch:		4
License:	LGPLv2+
Group:		Networking/WWW
Url:		http://pim.kde.org/akonadi/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libxml2-utils
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	xsltproc
BuildRequires:	boost-devel
#BuildRequires:	pkgconfig(soprano)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5UiPlugin)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5DesignerPlugin)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(Backtrace)
BuildRequires:	cmake(LibXml2)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	boost-devel
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(LibXslt)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(mariadb)
%if %{with mariadb}
Requires:	mariadb-common
# (tpg) needed for mysqld
Requires:	mariadb-server
# Needed for mysqlcheck  which is used in akonadi
Requires:	mariadb-client
Requires:	qt5-qtbase-database-plugin-mysql
%else
Requires:	qt5-database-plugin-sqlite3
%endif

%description
An extensible cross-desktop storage service for PIM data and meta data
providing concurrent read, write, and query access.

%files -f akonadi.lang
%{_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_datadir}/kf5/akonadi
%{_datadir}/kf5/akonadi_knut_resource
%{_datadir}/akonadi
%{_datadir}/config.kcfg/resourcebase.kcfg
%{_libdir}/qt5/plugins/akonadi/akonadi_test_searchplugin.so
%{_datadir}/icons/*/*/*/akonadi.*

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
Obsoletes:	%{mklibname akonadiprotocolinternals 2} < 4:17.04.0

%description common
Dummy package to override old.

%files common
%doc README
%{_datadir}/qlogging-categories5/akonadi.categories
%{_datadir}/qlogging-categories5/akonadi.renamecategories

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
Requires:	akonadi = %{EVRD}
Requires:	boost-devel

%description devel
This package contains header files needed if you wish to build applications
based on %{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Akonadi
%{_libdir}/qt5/mkspecs/modules/qt_Akonadi*.pri
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kdevappwizard/templates/*

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5 \
%if ! %{with mariadb}
	-DDATABASE_BACKEND=SQLITE \
%endif
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir}

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi5
%find_lang akonadi_knut_resource
cat *.lang >akonadi.lang
