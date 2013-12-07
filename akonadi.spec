Summary:	An extensible cross-desktop storage service for PIM
Name:		akonadi
Version:	1.10.3
Release:	3
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
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/akonadi/src/%{name}-%{version}.tar.bz2
BuildRequires:	automoc
BuildRequires:	kde4-macros
BuildRequires:	libxml2-utils
BuildRequires:	qt4-qtdbus
BuildRequires:	shared-mime-info >= 0.20
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	mysql-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(soprano)
Requires:	qt4-database-plugin-mysql
Requires:	mysql-core
Requires:	mysql-common
# Needed for mysqlcheck  which is used in akonadi
Requires:	mysql-client

%description
An extensible cross-desktop storage service for PIM data and meta data
providing concurrent read, write, and query access.

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
%cmake_kde4 \
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	-DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make

%install
%makeinstall_std -C build
mkdir %{buildroot}%{_libdir}/qt4
mv %{buildroot}%{_libdir}/plugins %{buildroot}%{_libdir}/qt4/

