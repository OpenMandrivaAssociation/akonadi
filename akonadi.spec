Name:		akonadi
Summary:	An extensible cross-desktop storage service for PIM
Version:	1.7.90
Release:	1
Epoch:		1
Url:		http://pim.kde.org/akonadi/
License:	LGPLv2+
Group:		Networking/WWW
Source0:	ftp://ftp.kde.org/pub/kde/stable/akonadi/src/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.4.0
BuildRequires:	qt4-qtdbus
BuildRequires:	shared-mime-info >=  0.20
BuildRequires:	kde4-macros
BuildRequires:	libxslt-proc
BuildRequires:	libxml2-utils
BuildRequires:	automoc
BuildRequires:	mysql-devel
BuildRequires:	boost-devel
BuildRequires:	soprano-devel
Requires:	qt4-database-plugin-mysql
Requires:	mysql-core
Requires:	mysql-common
# Needed for mysqlcheck  which is used in akonadi
Requires:	mysql-client

%description
An extensible cross-desktop storage service for PIM data and
meta data providing concurrent read, write, and query access.

%files
%{_kde_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
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
%{name} library.

%files -n %{libakonadiprotocolinternals}
%{_kde_libdir}/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

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
%cmake_kde4 -DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld -DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make

%install
%makeinstall_std -C build

