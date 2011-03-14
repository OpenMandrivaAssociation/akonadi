Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version: 1.5.1
Release: %mkrel 2
Epoch: 1
Url: http://pim.kde.org/akonadi/
License: LGPLv2+
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://download.akonadi-project.org/%{name}-%{version}.tar.bz2
Patch0:        akonadi-1.3.1-fix-mysql-plugin-load.patch
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: qt4-qtdbus
BuildRequires: shared-mime-info >=  0.20
BuildRequires: kde4-macros
BuildRequires: libxslt-proc
BuildRequires: libxml2-utils
BuildRequires: automoc
BuildRequires: mysql-devel
BuildRequires: boost-devel
BuildRequires: soprano-devel
Requires: qt4-database-plugin-mysql
Requires: mysql-core
Requires: mysql-common
# Needed for mysqlcheck  which is used in akonadi
Requires: mysql-client 
Obsoletes: akonadi-common < 1:1.1.95
Conflicts: kde4-akonadi < 4.0.71-1

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

%files
%defattr(-,root,root)
%{_kde_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_libdir}/qt4/plugins/sqldrivers/libqsqlite3.so

#------------------------------------------------------

# Need a dummy package to override old one
%package common
Group: Networking/WWW
Summary: Dummy package to override old
Obsoletes: akonadi-common < 1:1.1.95

%description common
Dummy package to override old.

%files common
%doc README

#------------------------------------------------------

%define akonadiprotocolinternals_major 1
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n     %libakonadiprotocolinternals
Summary:        %name library
Group:          System/Libraries
Obsoletes:      %{_lib}akonadi_protocolinternals4 <= 4.0.70-1

%description -n %libakonadiprotocolinternals
%name library.

%files -n %libakonadiprotocolinternals
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#------------------------------------------------------

%package   devel
Summary:   Devel stuff for %name
Group:     Development/KDE and Qt
Conflicts: kdepimlibs4-devel < 4.0.70-2
Conflicts: kdepim4-devel < 2:4.0.70-2
Requires:  %libakonadiprotocolinternals = %epoch:%version
Requires: akonadi-common = %epoch:%version

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/pkgconfig/akonadi.pc
%{_kde_libdir}/cmake/Akonadi
%{_kde_datadir}/dbus-1/interfaces/*.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
#%patch0 -p1

%build
%cmake_kde4 -DMYSQLD_EXECUTABLE=%_sbindir/mysqld -DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

#We need to expand libdir into mysql-global.conf
#sed -e 's,LIBDIR,%{_libdir},g' -i  %buildroot/%_sysconfdir/akonadi/mysql-global.conf

%clean
rm -rf %{buildroot}
