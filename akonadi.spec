%bcond_with	qt5
# (tpg) needed for boost
%define _disable_ld_no_undefined 1

Summary:	An extensible cross-desktop storage service for PIM
Name:		akonadi
Version:	1.13.0
Release:	5
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
Source0:	ftp://ftp.kde.org/pub/kde/stable/akonadi/src/%{name}-%{version}.tar.bz2
BuildRequires:	automoc
BuildRequires:	kde4-macros
BuildRequires:	libxml2-utils
BuildRequires:	qt4-qtdbus
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(soprano)
%if %{with qt5}
BuildRequires:	cmake(ECM)
%endif
Requires:		qt4-database-plugin-mysql
%if %{mdvver} >= 201400
BuildRequires:	mariadb-devel
Requires:	mariadb-common
# (tpg) needed for mysqld
Requires:	mariadb-server
# Needed for mysqlcheck  which is used in akonadi
Requires:	mariadb-client
%else
BuildRequires:	mysql-devel
Requires:	mysql-core
Requires:	mysql-common
Requires:	mysql-client
%endif

%description
An extensible cross-desktop storage service for PIM data and meta data
providing concurrent read, write, and query access.

%files
%{_kde_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml

#------------------------------------------------------
%package -n qt4-database-plugin-sqlite3
Summary: Improved Sqlite 3.x support plugin for Qt 4.x
Group: Databases
Conflicts: akonadi < 1.12.91-1

%description -n qt4-database-plugin-sqlite3
Improved Sqlite 3.x support plugin for Qt 4.x

%files -n qt4-database-plugin-sqlite3
%{_libdir}/qt4/plugins/sqldrivers/libqsqlite3.so

#------------------------------------------------------

# Need a dummy package to override old one
%package common
Group:		Networking/WWW
Summary:	Dummy package to override old

%description common
Dummy package to override old.

%files common
%doc README

#------------------------------------------------------

%define akonadiprotocolinternals_major 1
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n %{libakonadiprotocolinternals}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libakonadiprotocolinternals}
Qt4 %{name} library.

%files -n %{libakonadiprotocolinternals}
%{_kde_libdir}/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}
%{_kde_libdir}/libakonadiprotocolinternals.so.1.13*

#------------------------------------------------------

%if %{with qt5}
%define q5akonadiprotocolinternals_major 2
%define q5libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{q5akonadiprotocolinternals_major}

%package -n %{q5libakonadiprotocolinternals}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{q5libakonadiprotocolinternals}
Qt5 %{name} library.

%files -n %{q5libakonadiprotocolinternals}
%{_kde_libdir}/libakonadiprotocolinternals.so.%{q5akonadiprotocolinternals_major}*
%{_kde_libdir}/libakonadiprotocolinternals.so.1.7*
%endif
#------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libakonadiprotocolinternals} = %{EVRD}
Requires:	akonadi-common = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/pkgconfig/akonadi.pc
%{_kde_libdir}/cmake/Akonadi
%{_kde_datadir}/dbus-1/interfaces/*.xml

#--------------------------------------------------------------------

%prep
%setup -q

%build
%global optflags %optflags -fdisable-strict-aliasing

%cmake_kde4 \
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make
cd ..
mv build build-qt4

%if %{with qt5}
%cmake_kde5 \
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir} \
	-DQT5_BUILD:BOOL=ON
%ninja -c Build
cd ..
mv build build-qt5
%endif

%install
%if %{with qt5}
ln -s build-qt5 build
%ninja_install -C build
rm build
%endif
ln -s build-qt4 build
%makeinstall_std -C build
mkdir %{buildroot}%{_libdir}/qt4
mv %{buildroot}%{_libdir}/plugins %{buildroot}%{_libdir}/qt4/
