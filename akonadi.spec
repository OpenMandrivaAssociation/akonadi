# (tpg) needed for boost
%define _disable_ld_no_undefined 1

Summary:	An extensible cross-desktop storage service for PIM
Name:		akonadi
Version:	18.04.2
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
# (tpg) does not work with sqlite
Requires:	qt5-qtbase-database-plugin-mysql
Requires:	mariadb-common
# (tpg) needed for mysqld
Requires:	mariadb-server
# Needed for mysqlcheck  which is used in akonadi
Requires:	mariadb-client
# (tpg) obsolete old lang packages
Provides:	kde-l10n = 17.04.0
Obsoletes:	kde-l10n < 17.04.0
Conflicts:	kde-l10n < 17.04.0
Obsoletes:	kde-l10n-ar < 3:17.04.0
Conflicts:	kde-l10n-ar < 3:17.04.0
Provides:	kde-l10n-ar = 3:17.04.0
Obsoletes:	kde-l10n-ast < 3:17.04.0
Conflicts:	kde-l10n-ast < 3:17.04.0
Provides:	kde-l10n-ast = 3:17.04.0
Obsoletes:	kde-l10n-bg < 3:17.04.0
Conflicts:	kde-l10n-bg < 3:17.04.0
Provides:	kde-l10n-bg = 3:17.04.0
Obsoletes:	kde-l10n-bs < 3:17.04.0
Conflicts:	kde-l10n-bs < 3:17.04.0
Provides:	kde-l10n-bs = 3:17.04.0
Obsoletes:	kde-l10n-ca < 3:17.04.0
Conflicts:	kde-l10n-ca < 3:17.04.0
Provides:	kde-l10n-ca = 3:17.04.0
Obsoletes:	kde-l10n-cs < 3:17.04.0
Conflicts:	kde-l10n-cs < 3:17.04.0
Provides:	kde-l10n-cs = 3:17.04.0
Obsoletes:	kde-l10n-da < 3:17.04.0
Conflicts:	kde-l10n-da < 3:17.04.0
Provides:	kde-l10n-da = 3:17.04.0
Obsoletes:	kde-l10n-de < 3:17.04.0
Conflicts:	kde-l10n-de < 3:17.04.0
Provides:	kde-l10n-de = 3:17.04.0
Obsoletes:	kde-l10n-el < 3:17.04.0
Conflicts:	kde-l10n-el < 3:17.04.0
Provides:	kde-l10n-el = 3:17.04.0
Obsoletes:	kde-l10n-en_GB < 3:17.04.0
Conflicts:	kde-l10n-en_GB < 3:17.04.0
Provides:	kde-l10n-en_GB = 3:17.04.0
Obsoletes:	kde-l10n-en_US < 3:17.04.0
Conflicts:	kde-l10n-en_US < 3:17.04.0
Provides:	kde-l10n-en_US = 3:17.04.0
Obsoletes:	kde-l10n-eo < 3:17.04.0
Conflicts:	kde-l10n-eo < 3:17.04.0
Provides:	kde-l10n-eo = 3:17.04.0
Obsoletes:	kde-l10n-es < 3:17.04.0
Conflicts:	kde-l10n-es < 3:17.04.0
Provides:	kde-l10n-es = 3:17.04.0
Obsoletes:	kde-l10n-et < 3:17.04.0
Conflicts:	kde-l10n-et < 3:17.04.0
Provides:	kde-l10n-et = 3:17.04.0
Obsoletes:	kde-l10n-eu < 3:17.04.0
Conflicts:	kde-l10n-eu < 3:17.04.0
Provides:	kde-l10n-eu = 3:17.04.0
Obsoletes:	kde-l10n-fa < 3:17.04.0
Conflicts:	kde-l10n-fa < 3:17.04.0
Provides:	kde-l10n-fa = 3:17.04.0
Obsoletes:	kde-l10n-fi < 3:17.04.0
Conflicts:	kde-l10n-fi < 3:17.04.0
Provides:	kde-l10n-fi = 3:17.04.0
Obsoletes:	kde-l10n-fr < 3:17.04.0
Conflicts:	kde-l10n-fr < 3:17.04.0
Provides:	kde-l10n-fr = 3:17.04.0
Obsoletes:	kde-l10n-ga < 3:17.04.0
Conflicts:	kde-l10n-ga < 3:17.04.0
Provides:	kde-l10n-ga = 3:17.04.0
Obsoletes:	kde-l10n-gl < 3:17.04.0
Conflicts:	kde-l10n-gl < 3:17.04.0
Provides:	kde-l10n-gl = 3:17.04.0
Obsoletes:	kde-l10n-he < 3:17.04.0
Conflicts:	kde-l10n-he < 3:17.04.0
Provides:	kde-l10n-he = 3:17.04.0
Obsoletes:	kde-l10n-hi < 3:17.04.0
Conflicts:	kde-l10n-hi < 3:17.04.0
Provides:	kde-l10n-hi = 3:17.04.0
Obsoletes:	kde-l10n-hr < 3:17.04.0
Conflicts:	kde-l10n-hr < 3:17.04.0
Provides:	kde-l10n-hr = 3:17.04.0
Obsoletes:	kde-l10n-hu < 3:17.04.0
Conflicts:	kde-l10n-hu < 3:17.04.0
Provides:	kde-l10n-hu = 3:17.04.0
Obsoletes:	kde-l10n-ia < 3:17.04.0
Conflicts:	kde-l10n-ia < 3:17.04.0
Provides:	kde-l10n-ia = 3:17.04.0
Obsoletes:	kde-l10n-id < 3:17.04.0
Conflicts:	kde-l10n-id < 3:17.04.0
Provides:	kde-l10n-id = 3:17.04.0
Obsoletes:	kde-l10n-is < 3:17.04.0
Conflicts:	kde-l10n-is < 3:17.04.0
Provides:	kde-l10n-is = 3:17.04.0
Obsoletes:	kde-l10n-it < 3:17.04.0
Conflicts:	kde-l10n-it < 3:17.04.0
Provides:	kde-l10n-it = 3:17.04.0
Obsoletes:	kde-l10n-ja < 3:17.04.0
Conflicts:	kde-l10n-ja < 3:17.04.0
Provides:	kde-l10n-ja = 3:17.04.0
Obsoletes:	kde-l10n-kk < 3:17.04.0
Conflicts:	kde-l10n-kk < 3:17.04.0
Provides:	kde-l10n-kk = 3:17.04.0
Obsoletes:	kde-l10n-km < 3:17.04.0
Conflicts:	kde-l10n-km < 3:17.04.0
Provides:	kde-l10n-km = 3:17.04.0
Obsoletes:	kde-l10n-ko < 3:17.04.0
Conflicts:	kde-l10n-ko < 3:17.04.0
Provides:	kde-l10n-ko = 3:17.04.0
Obsoletes:	kde-l10n-lt < 3:17.04.0
Conflicts:	kde-l10n-lt < 3:17.04.0
Provides:	kde-l10n-lt = 3:17.04.0
Obsoletes:	kde-l10n-lv < 3:17.04.0
Conflicts:	kde-l10n-lv < 3:17.04.0
Provides:	kde-l10n-lv = 3:17.04.0
Obsoletes:	kde-l10n-mr < 3:17.04.0
Conflicts:	kde-l10n-mr < 3:17.04.0
Provides:	kde-l10n-mr = 3:17.04.0
Obsoletes:	kde-l10n-nb < 3:17.04.0
Conflicts:	kde-l10n-nb < 3:17.04.0
Provides:	kde-l10n-nb = 3:17.04.0
Obsoletes:	kde-l10n-nds < 3:17.04.0
Conflicts:	kde-l10n-nds < 3:17.04.0
Provides:	kde-l10n-nds = 3:17.04.0
Obsoletes:	kde-l10n-nl < 3:17.04.0
Conflicts:	kde-l10n-nl < 3:17.04.0
Provides:	kde-l10n-nl = 3:17.04.0
Obsoletes:	kde-l10n-nn < 3:17.04.0
Conflicts:	kde-l10n-nn < 3:17.04.0
Provides:	kde-l10n-nn = 3:17.04.0
Obsoletes:	kde-l10n-pa < 3:17.04.0
Conflicts:	kde-l10n-pa < 3:17.04.0
Provides:	kde-l10n-pa = 3:17.04.0
Obsoletes:	kde-l10n-pl < 3:17.04.0
Conflicts:	kde-l10n-pl < 3:17.04.0
Provides:	kde-l10n-pl = 3:17.04.0
Obsoletes:	kde-l10n-pt < 3:17.04.0
Conflicts:	kde-l10n-pt < 3:17.04.0
Provides:	kde-l10n-pt = 3:17.04.0
Obsoletes:	kde-l10n-pt_BR < 3:17.04.0
Conflicts:	kde-l10n-pt_BR < 3:17.04.0
Provides:	kde-l10n-pt_BR = 3:17.04.0
Obsoletes:	kde-l10n-ro < 3:17.04.0
Conflicts:	kde-l10n-ro < 3:17.04.0
Provides:	kde-l10n-ro = 3:17.04.0
Obsoletes:	kde-l10n-ru < 3:17.04.0
Conflicts:	kde-l10n-ru < 3:17.04.0
Provides:	kde-l10n-ru = 3:17.04.0
Obsoletes:	kde-l10n-sk < 3:17.04.0
Conflicts:	kde-l10n-sk < 3:17.04.0
Provides:	kde-l10n-sk = 3:17.04.0
Obsoletes:	kde-l10n-sl < 3:17.04.0
Conflicts:	kde-l10n-sl < 3:17.04.0
Provides:	kde-l10n-sl = 3:17.04.0
Obsoletes:	kde-l10n-sr < 3:17.04.0
Conflicts:	kde-l10n-sr < 3:17.04.0
Provides:	kde-l10n-sr = 3:17.04.0
Obsoletes:	kde-l10n-sv < 3:17.04.0
Conflicts:	kde-l10n-sv < 3:17.04.0
Provides:	kde-l10n-sv = 3:17.04.0
Obsoletes:	kde-l10n-tr < 3:17.04.0
Conflicts:	kde-l10n-tr < 3:17.04.0
Provides:	kde-l10n-tr = 3:17.04.0
Obsoletes:	kde-l10n-ug < 3:17.04.0
Conflicts:	kde-l10n-ug < 3:17.04.0
Provides:	kde-l10n-ug = 3:17.04.0
Obsoletes:	kde-l10n-uk < 3:17.04.0
Conflicts:	kde-l10n-uk < 3:17.04.0
Provides:	kde-l10n-uk = 3:17.04.0
Obsoletes:	kde-l10n-wa < 3:17.04.0
Conflicts:	kde-l10n-wa < 3:17.04.0
Provides:	kde-l10n-wa = 3:17.04.0
Obsoletes:	kde-l10n-zh_CN < 3:17.04.0
Conflicts:	kde-l10n-zh_CN < 3:17.04.0
Provides:	kde-l10n-zh_CN = 3:17.04.0
Obsoletes:	kdepimlibs-core < 3:17.04.0
Conflicts:	task-plasma < 5.9.5-9

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
%config %{_sysconfdir}/akonadi.categories
%config %{_sysconfdir}/akonadi.renamecategories

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
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir}

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi5
%find_lang akonadi_knut_resource
cat *.lang >akonadi.lang
