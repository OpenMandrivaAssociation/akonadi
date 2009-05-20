%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define revision 970837
%endif

Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version: 1.1.85
Release: %mkrel 0.%revision.1
Url: http://pim.kde.org/akonadi/
License: LGPLv2+
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-build
%if %branch
Source0: http://akonadi.omat.nl/%{name}-%{version}.%revision.tar.bz2
%else
Source0: http://akonadi.omat.nl/%{name}-%{version}.tar.bz2
%endif
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: shared-mime-info >=  0.20
BuildRequires: kde4-macros
BuildRequires: libxslt-proc
BuildRequires: libxml2-utils
BuildRequires: automoc
BuildRequires: mysql-client
BuildRequires: boost-devel
BuildRequires: soprano-devel
Conflicts:     kde4-akonadi < 4.0.71-1

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

#--------------------------------------------------------------------

%package common
Summary: %name common mime and dbus calls
Group: System/Libraries
Obsoletes: akonadi
Requires: qt4-database-plugin-mysql
Requires: mysql-common

%description common
%name common mime and dbus calls.

%files common
%defattr(-,root,root)
%{_kde_bindir}/*
%{_sysconfdir}/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_kde_datadir}/dbus-1/interfaces/*.xml

#------------------------------------------------------

%define akonadiprotocolinternals_major 1
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n     %libakonadiprotocolinternals
Summary:        %name library
Group:          System/Libraries
Obsoletes:      %{_lib}akonadi_protocolinternals4 <= 4.0.70-1
Requires: %name-common

%description -n %libakonadiprotocolinternals
%name library.

%files -n %libakonadiprotocolinternals
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#---------------------------------------------------------------------

%define akonadiprivate_major 1
%define libakonadiprivate %mklibname akonadiprivate %{akonadiprivate_major}

%package -n %libakonadiprivate
Summary: %name library
Group: System/Libraries
Obsoletes:      %{_lib}akonadiprivate4 <= 4.0.70-1

%description -n %libakonadiprivate
%name library.

%files -n %libakonadiprivate
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprivate.so.%{akonadiprivate_major}*

#------------------------------------------------------

%package   devel
Summary:   Devel stuff for %name
Group:     Development/KDE and Qt
Conflicts: kdepimlibs4-devel < 4.0.70-2
Conflicts: kdepim4-devel < 2:4.0.70-2
Requires:  %libakonadiprotocolinternals = %version
Requires:  %libakonadiprivate = %version

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/pkgconfig/akonadi.pc
%{_kde_libdir}/cmake/Akonadi

#--------------------------------------------------------------------

%prep
%if %branch
%setup -q -n %name
%else
%setup -q
%endif
%build
%cmake_kde4 -DMYSQLD_EXECUTABLE=%_sbindir/mysqld -DCONFIG_INSTALL_DIR=%{_sysconfdir}
%make

%install
rm -rf %buildroot

cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
